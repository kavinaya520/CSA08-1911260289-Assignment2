"""Task 6: payment logic as reusable functions."""

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
STD_FAT = 3.5
STD_SNF = 8.5
STEP_SIZE = 0.1


def rate_per_litre(fat, snf):
    """Return the price per litre for the given fat and SNF, rounded to 2 decimals."""
    fat_steps = round((fat - STD_FAT) / STEP_SIZE)
    snf_steps = round((snf - STD_SNF) / STEP_SIZE)
    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    return round(rate, 2)


def payout(litres, fat, snf):
    """Return the payment for one entry, rounded to 2 decimals."""
    return round(litres * rate_per_litre(fat, snf), 2)


def ten_day_total(entries):
    """Return the total payment; entries is a list of (litres, fat, snf)."""
    total = 0.0
    for litres, fat, snf in entries:
        total += payout(litres, fat, snf)
    return round(total, 2)


def show_payout(litres, fat, snf):
    """Prints the payment but returns nothing (None)."""
    print("payment:", payout(litres, fat, snf))


if __name__ == "__main__":
    # return vs print
    amount = payout(10, 3.5, 8.5)
    print("returned value reused (amount * 2):", amount * 2)
    result = show_payout(10, 3.5, 8.5)
    print("value returned by a print-only function:", result)

    entries = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]
    print("ten-day total:", ten_day_total(entries))

    # Scope: a local variable does not change the global one
    counter = 0

    def local_demo():
        """Set a local variable with the same name as a global one."""
        counter = 99
        return counter

    print("local:", local_demo(), "| global:", counter)
