# Task 1 - Understand the Problem and Identify the Data

## Inputs
| Input | Type | Reason |
|---|---|---|
| Farmer ID | string | may contain letters or leading zeros |
| Litres | float | can be fractional |
| Fat % | Decimal | exact decimal value needed |
| SNF % | Decimal | exact decimal value needed |
| Shift | string | "Morning" or "Evening" |

## Outputs
Rate per litre, payment per entry and the ten-day total (all Decimal, 2 decimals).
Step counts are int. A bool (valid or not) is used internally for validation.

## Named constants
BASE_RATE = 30.00, FAT_STEP_VALUE = 0.40, SNF_STEP_VALUE = 0.30, STD_FAT = 3.5, STD_SNF = 8.5,
MIN_FAT = 2.0, MAX_FAT = 7.0

## Validation rules
- Litres must be 0 or more
- 2.0 <= fat <= 7.0

## Assumptions
- Two entries a day (morning and evening), so 20 entries in ten days.
- Fat and SNF steps are rounded to the nearest 0.1.
- Money is rounded to 2 decimals.

## Additional question: separate variables vs list of records
| Aspect | Separate variables (litres1, fat1, ...) | List of tuples |
|---|---|---|
| Names needed for 300 farmers | about 900 variable names | 1 list |
| Loop | cannot be used in a loop | one loop |
| Time | O(n) | O(n) |
| Space | O(n) | O(n) |

Both take O(n) time and O(n) space, but the list is easier to scale.
