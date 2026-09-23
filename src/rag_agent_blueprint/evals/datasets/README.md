# Eval datasets

Folder for **fictional, hand-curated** test cases for `tool_call_eval.py`
and `judge_eval.py`. Should never contain real user traces or production
data — only examples written for this repository, in the same spirit as
`examples/`.

Expected format (to be defined during implementation):
- One file per case, or a JSONL file with one row per turn.
- Each case references a `turn_id`, a fictional transcript, and (depending
  on the eval) the expected tool or the path to a rubric under `docs/`.
