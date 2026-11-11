# Task 11 - Final Design Recommendation

- Data types: Decimal (built from strings) for money, int for step counts, strings for IDs and shifts.
- Rounding: round each payment to 2 decimals (half up) and then add the rounded payments.
- Rate revision: change the rates in one place (a rate card or rates.json), then re-run the Task 9 and
  Task 12 tests before using the new rates. Keep the old card with its start date.
- Limitations: the step rounding rule must be agreed with the co-operative, and a file or dictionary does
  not check the rate values by itself (add validation).
- Scale: with a running total the time is O(n) and the extra space is O(1). In Task 10, adding 150,000
  Decimal payments took about 0.33 s, so a district-union run of 150,000 farmers is fine on one computer.

## Rate card in a JSON file
    rates.json: {"base": 30.00, "fat": 0.40, "snf": 0.30}
Loading it at start-up costs O(t) time and space for t values (tiny). A rate change then needs only a
file edit instead of editing the program, but a bad edit can break payments, so the loaded values must
be validated.
