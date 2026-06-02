#!/bin/bash
# Stop hook for the autoresearch never-stop loop. Project-shared, opt-in
# via /start-experiment Step 9a (writes the marker file). Without the
# marker, this script exits 0 immediately — non-autoresearch sessions in
# this project are unaffected.
#
# The hook receives a JSON blob on stdin from Claude Code:
#   { "session_id", "transcript_path", "hook_event_name", "stop_hook_active", "cwd" }
#
# Wire-up (one-time per checkout):
#   .claude/settings.local.json -> hooks.Stop[*].hooks[*] = {
#     "type": "command", "command": ".claude/stop_hook.sh"
#   }
#
# Decision tree (cascades to allow):
#   1. No marker → allow (no active never-stop loop)
#   2. Marker exists, session mismatch → cleanup + allow (zombie from crashed session)
#   3. Marker exists, session matches, recent retrospective in wiki/analyses/ → allow
#      (agent did its homework; respect the genuine exhaustion signal)
#   4. Marker exists, session matches, NO recent retrospective → BLOCK with
#      reason that forces /create-retrospective first

INPUT=$(cat)
MARKER=".claude/.loop_active.json"

# Layer 1: no marker → no active loop → allow stop
[ -f "$MARKER" ] || exit 0

# Read session_id + model + lane from inputs
CURRENT_SESSION=$(echo "$INPUT" \
  | python3 -c 'import json,sys; print(json.load(sys.stdin).get("session_id",""))' 2>/dev/null)
LOOP_SESSION=$(python3 -c \
  'import json; print(json.load(open(".claude/.loop_active.json")).get("session_id",""))' 2>/dev/null)
LOOP_MODEL=$(python3 -c \
  'import json; print(json.load(open(".claude/.loop_active.json")).get("model",""))' 2>/dev/null)
LOOP_LANE=$(python3 -c \
  'import json; print(json.load(open(".claude/.loop_active.json")).get("lane",""))' 2>/dev/null)

# Layer 2: session mismatch → cleanup orphan marker + allow stop
if [ "$CURRENT_SESSION" != "$LOOP_SESSION" ]; then
  rm -f "$MARKER"
  exit 0
fi

# Layer 3: recent retrospective for THIS (model, lane) exists → agent ran
# the homework, allow. 360 minutes = 6 hours. Tune here if needed.
#
# Filter by *${MODEL}*${LANE}* pattern when model+lane are present in the
# marker. Cross-lane retrospectives don't satisfy the gate — exhaustion on
# JAX needs a JAX-specific retrospective. Falls back to any *retrospective*
# if model+lane are absent from marker (backward compat for markers written
# by older /start-experiment versions before this lane-filter update).
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

# Layer 4: BLOCK with retrospective-first prompt (heredoc with var expansion
# so MODEL + LANE show up in the message the agent reads)
cat <<JSON
{
  "decision": "block",
  "reason": "DO NOT STOP. The never-stop loop marker is active for this session (you opted in via /start-experiment) on model='${LOOP_MODEL}' lane='${LOOP_LANE}', and there is NO recent retrospective in wiki/analyses/ matching the pattern *${LOOP_MODEL}*${LOOP_LANE}*retrospective*.md (last 6 hours). Cross-lane retrospectives don't count — exhaustion on this lane requires a lane-specific retrospective.\n\nBefore concluding the lane is exhausted, you MUST first invoke /create-retrospective ${LOOP_MODEL} ${LOOP_LANE}. The skill reads every experiment on this lane plus sibling-lane retrospectives, identifies coverage gaps from the topic taxonomy and Pallas catalog, surfaces premature-exhaustion signals (single-axis-probe vs kernel-port imbalance, frontier-stuck duration), and proposes ranked next directions.\n\nMost 'I'm exhausted' conclusions are wrong. The canonical case: 2026-05-21 gemma4-jax was declared exhausted; tokamax CE landed +4.18 pp a week later because a retrospective would have surfaced kernel work as the unexplored axis.\n\nAfter the retrospective runs:\n  1. Read its 'Recommended next directions' table (ranked by gain × confidence / effort).\n  2. Pick the top-ranked direction and dispatch it as the next experiment.\n  3. If STILL exhausted after acting on the retrospective's recommendations — re-attempt to stop. This hook will detect the lane-specific retrospective file and ALLOW the stop. You will have done genuine due diligence.\n\nDo NOT write 'recommend pausing' or 'all options exhausted' to wiki/log.md or any per-lane log. File a next-step experiment instead.\n\nTo stop without running a retrospective (override): the user can manually rm .claude/.loop_active.json and then ask you to stop. Otherwise, run the retrospective."
}
JSON
