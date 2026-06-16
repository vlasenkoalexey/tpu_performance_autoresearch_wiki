#!/usr/bin/env bash
set -uo pipefail

# Codex Stop hook for the autoresearch never-stop loop.
#
# Compatibility policy:
# - Prefer `.codex/.loop_active.json` when present.
# - Fall back to `.claude/.loop_active.json` so the current Claude-oriented
#   start-experiment marker can still gate Codex sessions.
# - Allow stop immediately when neither marker exists.

INPUT=$(cat)

MARKER=""
if [ -f ".codex/.loop_active.json" ]; then
  MARKER=".codex/.loop_active.json"
elif [ -f ".claude/.loop_active.json" ]; then
  MARKER=".claude/.loop_active.json"
else
  exit 0
fi

json_field() {
  HOOK_INPUT="$INPUT" python3 - "$1" "$2" <<'PY' 2>/dev/null
import json
import os
import sys

source, key = sys.argv[1], sys.argv[2]
try:
    if source == "-":
        raw = os.environ.get("HOOK_INPUT", "")
        data = json.loads(raw) if raw else {}
    else:
        with open(source) as f:
            data = json.load(f)
    value = data.get(key, "")
    print(value if value is not None else "")
except Exception:
    print("")
PY
}

CURRENT_SESSION=$(printf '%s' "$INPUT" | json_field - session_id)
LOOP_SESSION=$(json_field "$MARKER" session_id)
LOOP_MODEL=$(json_field "$MARKER" model)
LOOP_LANE=$(json_field "$MARKER" lane)

# If both the hook input and marker carry session IDs, a mismatch means this is
# a stale marker from a previous session. Clean it up and allow the stop.
if [ -n "$CURRENT_SESSION" ] && [ -n "$LOOP_SESSION" ] && [ "$CURRENT_SESSION" != "$LOOP_SESSION" ]; then
  rm -f "$MARKER"
  exit 0
fi

if [ -n "$LOOP_MODEL" ] && [ -n "$LOOP_LANE" ]; then
  PATTERN="*${LOOP_MODEL}*${LOOP_LANE}*retrospective*.md"
else
  PATTERN="*retrospective*.md"
fi

RECENT_RETROSPECTIVES=$(find wiki/analyses/ \
  -name "$PATTERN" -mmin -360 2>/dev/null | wc -l)

if [ "$RECENT_RETROSPECTIVES" -ge 1 ]; then
  exit 0
fi

python3 - "$LOOP_MODEL" "$LOOP_LANE" "$PATTERN" <<'PY'
import json
import sys

model, lane, pattern = sys.argv[1], sys.argv[2], sys.argv[3]
reason = (
    "DO NOT STOP. The autoresearch never-stop marker is active"
    f" for model='{model}' lane='{lane}', and there is no recent lane-specific"
    f" retrospective in wiki/analyses/ matching {pattern!r} from the last 6 hours.\n\n"
    "Before concluding the lane is exhausted, run the create-retrospective skill "
    f"for {model} {lane}. Then read its recommended next directions and dispatch "
    "the top viable experiment. To override, remove .codex/.loop_active.json and "
    ".claude/.loop_active.json, then stop again."
)
print(json.dumps({"decision": "block", "reason": reason}))
PY
