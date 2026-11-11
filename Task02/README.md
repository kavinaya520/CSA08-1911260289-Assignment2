# Task 2 - Values and Types

| Value | Type |
|---|---|
| 10 | int |
| 10.0 | float |
| "10" | str |
| True | bool |
| [10, 8.5] | list |

`7 / 2 = 3.5`, `7 // 2 = 3`, `7 % 2 = 1`, `-7 // 2 = -4` (floor division goes toward negative infinity).

`0.1 + 0.2 == 0.3` is False because the sum is 0.30000000000000004. Floats are stored in binary
and cannot hold 0.1 exactly, so small errors add up over many payments (a few paise).

| Approach | Precision | Note |
|---|---|---|
| Integer paise (3340 for 33.40) | exact | must be converted when printing |
| round() | hides the error | does not remove it |
| Decimal | exact | a little slower |

`Decimal(float(amount))` copies the float error (total 33400.29999999999857893118278), so Decimal
must always be built from a string.

Additional question (sizes measured in output.txt): Decimal 104 bytes, int 28 bytes, float 24 bytes.
Decimal and integer paise are exact, O(1) per addition. float with rounding is O(1) and gave 33400.3
here but is not guaranteed to be exact.
