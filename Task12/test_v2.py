"""Task 12: tests for normal and summer rates, with and without bonus."""
from decimal import Decimal
from milkrate_v2 import rate_per_litre, payout, bonus, ten_day_total, rate_card, SUMMER, NORMAL

D = Decimal


def ten(litres_each):
    """Ten entries of the same milk (fat 4.23, snf 8.67)."""
    return [(litres_each, "4.23", "8.67")] * 10


rows = [
    ("Feb, 4.23 fat 8.67 snf, rate",  rate_per_litre("4.23", "8.67", 2),  D("33.40")),
    ("May, 4.23 fat 8.67 snf, rate",  rate_per_litre("4.23", "8.67", 5),  D("35.75")),
    ("May, 480 L (no bonus)",         ten_day_total(ten(48), 5),          D("17160.00")),
    ("May, 540 L (with bonus)",       ten_day_total(ten(54), 5),          D("19575.00")),
    ("Feb, 540 L (with bonus)",       ten_day_total(ten(54), 2),          D("18306.00")),
    ("bonus, exactly 500 L",          bonus(500),                         D("0.00")),
    ("bonus, 540 L",                  bonus(540),                         D("270.00")),
    ("4.23 and 4.24 pay the same",    payout(10, "4.24", "8.67", 5),      payout(10, "4.23", "8.67", 5)),
]

print(f"{'Test':<32}{'Expected':>10}{'Actual':>10}  Result")
for name, actual, expected in rows:
    assert actual == expected, name
    print(f"{name:<32}{str(expected):>10}{str(actual):>10}  Pass")

assert rate_card(4) is SUMMER and rate_card(6) is SUMMER
assert rate_card(3) is NORMAL and rate_card(7) is NORMAL
print("rate_card: months 4-6 use SUMMER, other months use NORMAL: Pass")
print("all asserts passed")
