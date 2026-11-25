# Bug reports for exercise2.py

Line: 13
Problem: The function `clamp` incorrectly uses `max(low, min(x, low))`. It should be `max(low, min(x, high))` to ensure the value is clamped between `low` and `high`, not between `low` and `low`. This causes values above `low` but below `high` to be incorrectly clamped to `low`.
Example: clamp(3, 1, 10) → 1 (expected: 3), clamp(15, 1, 10) → 10 (correct), clamp(0, 1, 10) → 1 (correct), but clamp(2, 1, 10) → 1 (incorrect, should be 2)
Fix: return max(low, min(x, high))
