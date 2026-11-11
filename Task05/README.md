# Task 5 - Input and Type Conversion

- input() returns a string because the keyboard gives only text.
- `int("12")` and `float("3.5")` convert text to numbers; `"8,5"` and `"eight"` raise ValueError.
- try/except converts and handles bad input in one step. String checks (like isdigit) validate
  before converting.
- `print(f"{amount:8.2f}")` prints 33.4 as `   33.40`.

| Text | try/except float() | string check | string check + strip() |
|---|---|---|---|
| "8.5" | 8.5 | 8.5 | 8.5 |
| " 8.5 " | 8.5 | rejected | 8.5 |
| "8,5" | rejected | rejected | rejected |
| "eight" | rejected | rejected | rejected |

Both take O(L) time for a string of length L, which is almost constant. try/except is shorter.
