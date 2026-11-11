# Task 12 - Day-4 Design Challenge

## A. Impact analysis
- New: the analyser gives fat and SNF with two decimals; April to June (months 4-6) use base 32.00 and
  fat step 0.45; a bonus of Rs 0.50 per litre applies when the ten-day supply is more than 500 litres.
- Must change: the constants (they become two rate cards), `rate_per_litre` (needs the month),
  `ten_day_total` (needs the bonus) and the tests.
- Two-decimal readings: steps are still rounded to whole steps, so 4.23 and 4.24 both give 7 steps and
  pay the same, while 4.25 gives 8 steps. The step counts are made with Decimal to avoid float errors.

## B. Evaluation of the original design
Fixed named constants cannot hold two rate cards. The old rate function would pay 33.40 per litre for
4.23 fat and 8.67 SNF in May, but the correct summer rate is 35.75 (a loss of 2.35 per litre). The
module structure and the function names are still good and are kept.

## C. Revised design
milkrate_v2.py: two rate cards (NORMAL, SUMMER) in dictionaries, `rate_card(month)` chooses the card,
a separate `bonus(total_litres)` function, Decimal everywhere, half-up rounding to 2 decimals.
Assumption: the bonus is paid on all litres once the ten-day total is above 500 litres.

## D. Defence and tests
test_v2.py (output_tests.txt) checks both seasons, with and without bonus, and exactly 500 litres.
Decision: modify the design (not rewrite). Trade-off: Decimal is slower than float but exact, and a
dictionary is slightly slower than constants but handles any number of seasons.
