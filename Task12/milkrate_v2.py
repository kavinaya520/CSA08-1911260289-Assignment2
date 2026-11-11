"""Task 12: revised design - seasonal rate cards, two-decimal readings and bonus."""
from decimal import Decimal, ROUND_HALF_UP

STD_FAT = Decimal("3.5")
STD_SNF = Decimal("8.5")
STEP = Decimal("0.1")
BONUS_LIMIT_LITRES = Decimal("500")
BONUS_PER_LITRE = Decimal("0.50")

NORMAL = {"base": Decimal("30.00"), "fat": Decimal("0.40"), "snf": Decimal("0.30")}
SUMMER = {"base": Decimal("32.00"), "fat": Decimal("0.45"), "snf": Decimal("0.30")}   # April - June


def money(value):
    """Round a Decimal to two decimals (half up)."""
    return Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def rate_card(month):
    """Return the summer card for months 4 to 6 (April - June), otherwise the normal card."""
    return SUMMER if 4 <= month <= 6 else NORMAL


def rate_per_litre(fat, snf, month):
    """Rate for readings with two decimals (strings or numbers); steps rounded to whole steps."""
    card = rate_card(month)
    fat_steps = int(round((Decimal(str(fat)) - STD_FAT) / STEP))
    snf_steps = int(round((Decimal(str(snf)) - STD_SNF) / STEP))
    return money(card["base"] + fat_steps * card["fat"] + snf_steps * card["snf"])


def payout(litres, fat, snf, month):
    """Payment for one entry (without bonus)."""
    return money(Decimal(str(litres)) * rate_per_litre(fat, snf, month))


def bonus(total_litres):
    """Rs 0.50 per litre on all litres when the ten-day supply is MORE than 500 litres."""
    litres = Decimal(str(total_litres))
    return money(litres * BONUS_PER_LITRE) if litres > BONUS_LIMIT_LITRES else Decimal("0.00")


def ten_day_total(entries, month):
    """Sum of the payments plus the bonus; entries = [(litres, fat, snf)]."""
    total = Decimal("0")
    litres = Decimal("0")
    for l, f, s in entries:
        total += payout(l, f, s, month)
        litres += Decimal(str(l))
    return money(total + bonus(litres))


if __name__ == "__main__":
    print("Normal month (Feb), 10 L, fat 4.23, snf 8.67:", payout(10, "4.23", "8.67", 2))
    print("April-June (May), same milk               :", payout(10, "4.23", "8.67", 5))
