# Task 10 - Expectation vs Execution

experiments.py output is saved in output.txt (the times depend on the computer, the totals do not).

## 1. float vs Decimal
| n | float total | Decimal total | float time | Decimal time |
|---|---|---|---|---|
| 300 | 152056.72 | 152056.720 | 0.0001 s | 0.0008 s |
| 6,000 | 3087077.7200000053 | 3087077.720 | 0.0012 s | 0.0133 s |
| 150,000 | 76516787.26999982 | 76516787.270 | 0.0304 s | 0.3333 s |

float totals pick up tiny errors as n grows; Decimal stays exact. Decimal was about 10 times slower
in this run, but 150,000 payments still took about a third of a second.

## 2. Rounding strategy
300 payments of 33.335: rounding each payment first (33.34 each) gives 10002.00, rounding only the
final total gives 10000.50. A farmer is paid a whole-paise amount, so each payment is rounded first.

## 3. Rate table
With k = 400 distinct (fat, SNF) pairs stored in a dictionary, a lookup took about 0.07 microseconds
per entry, while recalculating the rate took about 1.90 microseconds per entry. Lookup is O(1) per
entry; the extra space is O(k).
