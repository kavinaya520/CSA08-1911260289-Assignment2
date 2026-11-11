"""Task 9: test table and automated assert tests. Run: python test_calculator.py"""
from decimal import Decimal
from calculator import payout, ten_day_total, parse_number

D = Decimal
VALID = [
    ("10, 4.0, 9.0",           (10, 4.0, 9.0),   D("335.00")),
    ("10, 3.0, 8.0",           (10, 3.0, 8.0),   D("265.00")),
    ("10, 3.5, 8.5 (boundary)", (10, 3.5, 8.5),  D("300.00")),
    ("10, 2.0, 8.5 (lowest)",  (10, 2.0, 8.5),   D("240.00")),
    ("10, 7.0, 8.5 (highest)", (10, 7.0, 8.5),   D("440.00")),
]
INVALID = [
    ('"eight", 3.5, 8.5', lambda: parse_number("eight")),
    ("-5, 3.5, 8.5",      lambda: payout(-5, 3.5, 8.5)),
    ("10, 1.9, 8.5",      lambda: payout(10, 1.9, 8.5)),
    ("10, 7.1, 8.5",      lambda: payout(10, 7.1, 8.5)),
]

print(f"{'Test':<26}{'Expected':>10}{'Actual':>12}  Result")
for name, args, expected in VALID:
    actual = payout(*args)
    assert actual == expected
    print(f"{name:<26}{str(expected):>10}{str(actual):>12}  Pass")

for name, call in INVALID:
    try:
        call()
    except ValueError:
        print(f"{name:<26}{'rejected':>10}{'ValueError':>12}  Pass")
    else:
        raise AssertionError(f"{name} should be rejected")

five = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3), (15, 4.0, 9.0), (9.5, 3.8, 8.4)]
assert ten_day_total(five) == D("1713.55")
print(f"{'five-entry total':<26}{'1713.55':>10}{str(ten_day_total(five)):>12}  Pass")
print("all asserts passed")
