#!/bin/sh
# UserPromptSubmit hook for Claude Code (and Codex). Points the model at the first-principles skill when the
# user asks for first-principles reasoning, or when the prompt leans on convention ("industry standard",
# "can't be done", "build vs buy"). Regex, not a model call, so it adds no latency; the model still judges
# the soft match. Prompts already running the skill, and prompts that edit the skill itself, are skipped.
prompt=$(jq -r '.prompt // empty' 2>/dev/null)
flat=$(printf '%s' "$prompt" | tr '\n' ' ')
[ -z "$flat" ] && exit 0
printf '%s' "$flat" | grep -qiE '^[[:space:]]*/first-principles|first-principles[[:space:]]+(skill|hook)|first-principles-trigger|SKILL\.md|APPLICATIONS\.md' && exit 0

emit() { jq -n --arg ctx "$1" '{hookSpecificOutput:{hookEventName:"UserPromptSubmit",additionalContext:$ctx}}'; }

if printf '%s' "$flat" | grep -qiE 'first[- ]principles?'; then
  emit 'FIRST PRINCIPLES. The user asked for first-principles reasoning. Invoke the first-principles skill and follow its steps before answering.'
  exit 0
fi

signals="(always|historically) (been )?(done|built|worked|run) (this|that|the same) way|(that'?s|it'?s) (just )?how (it'?s|it is|we'?ve|things are|everyone) (always )?(done|been|does)"
signals="$signals|industry[- ]standard|everyone (else )?(does|uses|is doing|has)|(all )?(our )?competitors (all )?(have|do|use|are doing)"
signals="$signals|(can'?t|cannot) (ever )?be done|(it'?s|that'?s|this is) (just )?impossible|never been done|nobody (has )?(ever )?(done|tried)"
signals="$signals|why (do|did|are|must|should|would) (we|they|everyone|people|users) |why (is|does) .{0,40}(cost|expensive|take so long)"
signals="$signals|build (vs\.?|versus|or) buy|rethink (this|the|our|how)"
signals="$signals|(challenge|question|stress[- ]test|sanity[- ]check) (the|this|my|our|these|that) (assumptions?|estimates?|plan|approach|numbers?|pricing|costs?)"
signals="$signals|move first|first[- ]mover|good ideas are (all )?taken|too (expensive|costly) to"
hit=$(printf '%s' "$flat" | grep -oiE "$signals" | head -n 1 | sed 's/[[:space:]]*$//')
[ -n "$hit" ] || exit 0
emit "FIRST PRINCIPLES CONSIDER. The prompt contains \"$hit\", which can mean an answer rests on convention rather than fact. If the user is asking to decide, design, estimate, price or challenge an accepted approach, invoke the first-principles skill. If it is a lookup, a bug fix or a direct instruction, ignore this block."
