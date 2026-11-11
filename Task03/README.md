# Task 3 - Variables and Constants

Python does not enforce constants (there is no const keyword). UPPER_CASE names are a PEP 8
convention that tells other programmers not to change them.

- `x = 10` and then `x = "ten"` works because Python is dynamically typed.
- `a, b = 3, 5` then `a, b = b, a` gives a = 5 and b = 3.

| Approach | Effort to update a rate | Places to change | Time/memory |
|---|---|---|---|
| Magic numbers | high, search the whole program | every place used | O(1) |
| Named constants | low | 1 | O(1) |
| RATE_CARD dictionary | low | 1 entry | O(1) lookup |

Named constants are better for maintenance. The dictionary becomes useful when rates change by
season (see Task 12).
