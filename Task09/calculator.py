"""Task 9: milk payment calculator with validation (uses Task07/milkrate.py)."""
import os
import sys
from decimal import Decimal, InvalidOperation

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Task07"))
import milkrate   # noqa: E402

MIN_FAT = Decimal("2.0")
MAX_FAT = Decimal("7.0")


def parse_number(text):
    """Convert typed text to Decimal; raise ValueError for text that is not a number."""
    try:
        value = Decimal(text.strip())
    except InvalidOperation:
        raise ValueError(f"{text!r} is not a number")
    if not value.is_finite():
        raise ValueError(f"{text!r} is not a number")
    return value


def read_number(prompt):
    """Keep asking until the clerk types a valid number (Task 5 idea)."""
    while True:
        try:
            return parse_number(input(prompt))
        except ValueError as err:
            print("Invalid:", err)


def validate_entry(litres, fat):
    """Raise ValueError if litres is negative or fat is outside 2.0 - 7.0."""
    if Decimal(str(litres)) < 0:
        raise ValueError("litres must be 0 or more")
    if not MIN_FAT <= Decimal(str(fat)) <= MAX_FAT:
        raise ValueError("fat must be between 2.0 and 7.0")


def payout(litres, fat, snf):
    """Validated payment for one entry (Decimal, 2 decimals)."""
    validate_entry(litres, fat)
    return milkrate.payout(litres, fat, snf)


def ten_day_total(entries):
    """Total of the valid entries; invalid entries are skipped."""
    total = Decimal("0")
    for litres, fat, snf in entries:
        try:
            total += payout(litres, fat, snf)
        except ValueError:
            continue
    return milkrate.money(total)


def enter_one():
    """Interactive mode: ask for one entry and print the payment."""
    litres = read_number("Litres : ")
    fat = read_number("Fat %  : ")
    snf = read_number("SNF %  : ")
    try:
        print("Rate    :", milkrate.rate_per_litre(fat, snf))
        print("Payment :", payout(litres, fat, snf))
    except ValueError as err:
        print("Rejected:", err)


if __name__ == "__main__":
    if "-i" in sys.argv:
        enter_one()
    else:
        sample = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3), (15, 4.0, 9.0), (9.5, 3.8, 8.4)]
        for litres, fat, snf in sample:
            print(f"{litres:>5} L fat {fat} snf {snf}  rate {milkrate.rate_per_litre(fat, snf):>6}"
                  f"  pay {payout(litres, fat, snf):>8}")
        print("Total:", ten_day_total(sample))
