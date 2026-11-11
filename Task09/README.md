# Task 9 - Implementation and Testing

calculator.py uses the rate function from Task07/milkrate.py, validates every entry (litres 0 or more,
fat 2.0 - 7.0) and uses `read_number()` (Task 5 idea) to check typed values. Run `python calculator.py`
for the sample table or `python calculator.py -i` to type one entry.

test_calculator.py prints the test table (saved in output_tests.txt) and uses assert for every case.

| Test | Input (litres, fat, SNF) | Expected | Result |
|---|---|---|---|
| 1 | 10, 4.0, 9.0 | 335.00 | Pass |
| 2 | 10, 3.0, 8.0 | 265.00 | Pass |
| 3 | 10, 3.5, 8.5 (boundary) | 300.00 | Pass |
| 4 | 10, 2.0, 8.5 (lowest fat) | 240.00 | Pass |
| 5 | 10, 7.0, 8.5 (highest fat) | 440.00 | Pass |
| 6 | "eight", 3.5, 8.5 | rejected (ValueError) | Pass |
| 7 | -5, 3.5, 8.5 | rejected (ValueError) | Pass |
| 8 | 10, 1.9, 8.5 | rejected (ValueError) | Pass |
| 9 | 10, 7.1, 8.5 | rejected (ValueError) | Pass |
| 10 | five entries | 1713.55 | Pass |

Manual vs automated testing: manual testing means typing inputs and reading the output each time, which
is slow and easy to forget. Automated tests (functions plus assert) run all cases in one command, in
well under a second, so they can be re-run after every change.
