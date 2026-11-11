# Task 4 - Expressions

    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    rate = 30.00 + fat_steps * 0.40 + snf_steps * 0.30
    payment = litres * rate

- Precedence: `**` first (right to left, so 2 ** 3 ** 2 = 512), unary minus after `**` (-2 ** 2 = -4),
  then `* / // %`, then `+ -`, then comparisons, then `not`, `and`, `or`.
- (4.2 - 3.5) / 0.1 gives 7.000000000000002, so round() is used to get 7.
- For fat 3.1 the raw value is -3.999999999999999: round() and math.floor() give -4, but int() gives -3
  (it cuts toward zero), so the rate would be 28.80 instead of 28.40. For fat 4.2 all three give 7.
- `2.0 <= fat <= 7.0` means `2.0 <= fat and fat <= 7.0`; `and`, `or`, `not` combine conditions.
- Complexity: all of these are O(1) time and O(1) space.

Unexpected results shown in output.txt: `0.1 + 0.2 == 0.3` is False, `(4.2 - 3.5) / 0.1` is not 7, `-7 // 2` is -4.
