#!/usr/bin/env python3
"""Hook-health check — LINT invariant #23.

The autoresearch never-stop loop is governed *entirely* by a Stop hook
(`.claude/stop_hook.sh`, wired in `.claude/settings.local.json`). If that hook is
unwired, missing, or shadowed/interfered-with by a rogue hook in another settings
scope, the loop discipline fails **silently** — there is no runtime signal.

This is the exact failure that let a stale global Stop hook
(`cat /tmp/v6e32_stop_hook.json 2>/dev/null || echo '{}'`) sit broken for a month:
an ephemeral experiment hook was parked in *durable global* settings, it read a
*non-durable* /tmp file, and its failure was *swallowed* into a no-op.

This script checks every Claude Code settings scope and flags:

  ERROR  — the project never-stop Stop hook is not wired, or its script is
           missing / not executable.
  ERROR  — any command hook references a script file that does not exist.
  WARN   — any *hook* command reads a /tmp/ path (non-durable: cleared on reboot;
           a hook decision must never depend on it).
  WARN   — a Stop hook is defined in a scope OTHER than this project (e.g. global
           ~/.claude): it fires for every session everywhere and can interfere
           with — or masquerade as — the loop's own hook. Ephemeral/experiment
           hooks belong in project `.claude/settings.local.json`, never global.

Exit code: 0 if no ERRORs (WARNs allowed), 1 otherwise. Import-friendly:
`check()` returns (errors, warnings) lists for the /lint skill to fold into its report.
"""
from __future__ import annotations
import json, os, re, sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PROJECT_STOP_SCRIPT = ".claude/stop_hook.sh"

SCOPES = [
    ("global",         os.path.expanduser("~/.claude/settings.json")),
    ("global-local",   os.path.expanduser("~/.claude/settings.local.json")),
    ("project",        os.path.join(PROJECT_ROOT, ".claude/settings.json")),
    ("project-local",  os.path.join(PROJECT_ROOT, ".claude/settings.local.json")),
]

_PATHLIKE = re.compile(r"(/[\w./-]+|\.claude/[\w./-]+)")
_SCRIPT_EXT = (".sh", ".py", ".js", ".ts")


def _commands(cfg: dict):
    """Yield (event, command) for every command-type hook + the statusLine."""
    for event, groups in (cfg.get("hooks") or {}).items():
        for group in groups:
            for h in group.get("hooks", []):
                if h.get("type") == "command" and h.get("command"):
                    yield event, h["command"]
    sl = cfg.get("statusLine")
    if sl and sl.get("type") == "command" and sl.get("command"):
        yield "statusLine", sl["command"]


def check():
    errors, warnings = [], []
    project_stop_wired = False
    stop_scopes = []

    for scope_name, path in SCOPES:
        if not os.path.exists(path):
            continue
        try:
            cfg = json.load(open(path))
        except (json.JSONDecodeError, OSError) as e:
            errors.append(f"[{scope_name}] {path}: unreadable/invalid JSON ({e})")
            continue

        for event, cmd in _commands(cfg):
            if event == "Stop":
                stop_scopes.append(scope_name)
                if PROJECT_STOP_SCRIPT in cmd:
                    project_stop_wired = True

            for tok in _PATHLIKE.findall(cmd):
                if tok.startswith("/tmp/") and event != "statusLine":
                    warnings.append(
                        f"[{scope_name}] {event} hook reads non-durable path {tok} "
                        f"— hook decisions must not depend on /tmp (cleared on reboot)."
                    )
                elif tok.endswith(_SCRIPT_EXT):
                    resolved = tok if tok.startswith("/") else os.path.join(PROJECT_ROOT, tok)
                    if not os.path.exists(resolved):
                        errors.append(
                            f"[{scope_name}] {event} hook references missing script: {tok}"
                        )

            # Stop hooks living outside this project affect it and can interfere.
            if event == "Stop" and scope_name.startswith("global"):
                warnings.append(
                    f"[{scope_name}] a Stop hook is defined in GLOBAL settings "
                    f"(`{cmd}`). Global Stop hooks fire in every session everywhere and "
                    f"can interfere with the never-stop loop. Move ephemeral/experiment "
                    f"hooks into project .claude/settings.local.json."
                )

    # The load-bearing invariant: the never-stop Stop hook must be wired + runnable.
    script_path = os.path.join(PROJECT_ROOT, PROJECT_STOP_SCRIPT)
    if not project_stop_wired:
        errors.append(
            "never-stop loop Stop hook is NOT wired in any settings scope "
            f"(expected a Stop hook running `{PROJECT_STOP_SCRIPT}`). The loop's "
            "retrospective gate is inactive — /start-experiment cannot enforce it."
        )
    if not os.path.exists(script_path):
        errors.append(f"never-stop hook script missing on disk: {PROJECT_STOP_SCRIPT}")
    elif not os.access(script_path, os.X_OK):
        errors.append(f"never-stop hook script not executable: {PROJECT_STOP_SCRIPT} (chmod +x)")

    return errors, warnings


def main():
    errors, warnings = check()
    print("# Hook-health check (LINT #23)\n")
    if not errors and not warnings:
        print("OK — never-stop Stop hook wired + executable; no broken refs, no /tmp reads, "
              "no rogue global Stop hooks.")
        return 0
    if errors:
        print(f"## ERRORS ({len(errors)})")
        for e in errors:
            print(f"  ✗ {e}")
        print()
    if warnings:
        print(f"## WARNINGS ({len(warnings)})")
        for w in warnings:
            print(f"  ⚠ {w}")
        print()
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
