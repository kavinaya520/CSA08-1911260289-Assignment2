"""Rate card of the village milk co-operative (exact Decimal version)."""
from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STD_FAT = Decimal("3.5")
STD_SNF = Decimal("8.5")
STEP = Decimal("0.1")


def money(value):
    """Round a Decimal to two decimals (half up)."""
    return Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def rate_per_litre(fat, snf):
    """Return the price per litre, rounded to two decimals."""
    # TODO 1 (completed): steps relative to 3.5% fat and 8.5% SNF, rounded to whole steps
    fat_steps = int(round((Decimal(str(fat)) - STD_FAT) / STEP))
    snf_steps = int(round((Decimal(str(snf)) - STD_SNF) / STEP))
    return money(BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE)


def payout(litres, fat, snf):
    """Return the payment amount rounded to two decimals."""
    # TODO 2 (completed): litres multiplied by the rate
    return money(Decimal(str(litres)) * rate_per_litre(fat, snf))


def ten_day_total(entries):
    """Return the total of a list of (litres, fat, snf) entries."""
    total = Decimal("0")
    for litres, fat, snf in entries:
        total += payout(litres, fat, snf)
    return money(total)


if __name__ == "__main__":
    for litres, fat, snf in [("10", "3.5", "8.5"), ("8.5", "4.2", "8.7"), ("12", "3.1", "8.3")]:
        rate = rate_per_litre(fat, snf)
        pay = payout(litres, fat, snf)
        print(f"{litres:>5} L  fat {fat}  snf {snf}  rate {rate:>6}  pay {pay:>8}")
