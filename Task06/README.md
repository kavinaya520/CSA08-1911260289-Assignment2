# Task 6 - Functions

Functions: `rate_per_litre(fat, snf)`, `payout(litres, fat, snf)` and `ten_day_total(entries)`,
each with a docstring. The Decimal version of these functions is in Task07/milkrate.py.

- Each function has parameters and returns a value.
- `return` gives the value back so it can be reused; `print` only shows it on the screen.
- Variables inside a function are local; variables outside, like BASE_RATE, are global.
- Functions can read constants but should not change them, otherwise one function could change the
  rates for all the others.

| Style | Reuse | Repeated logic | Maintainability |
|---|---|---|---|
| One long script | none | high | poor |
| Functions | high | none | good |
| lambda | fine for a one-line calculation, no docstring | none | hard to read if long |

Function call overhead is small and the total time stays O(n), so functions are better.
