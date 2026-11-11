"""Task 10: float vs Decimal, rounding strategy and rate table. Run: python experiments.py"""
import os
import random
import sys
import time
from decimal import Decimal, ROUND_HALF_UP

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Task07"))
import milkrate   # noqa: E402


def rate_float(fat, snf):
    """Rate calculated with floats (same rule as milkrate.py)."""
    return 30.0 + round((fat - 3.5) / 0.1) * 0.40 + round((snf - 8.5) / 0.1) * 0.30


def make_entries(n):
    """n random entries (litres, fat, snf); the seed makes the run repeatable."""
    rng = random.Random(1911)
    return [(round(rng.uniform(5, 25), 1), round(rng.uniform(2.0, 7.0), 1),
             round(rng.uniform(7.0, 10.0), 1)) for _ in range(n)]


def total_float(entries):
    """Total using floats."""
    total = 0.0
    for litres, fat, snf in entries:
        total += litres * rate_float(fat, snf)
    return total


def total_decimal(entries):
    """Total using exact Decimal arithmetic."""
    total = Decimal("0")
    for litres, fat, snf in entries:
        total += Decimal(str(litres)) * milkrate.rate_per_litre(fat, snf)
    return total


def timed(func, *args):
    """Return (result, seconds) measured with time.perf_counter()."""
    start = time.perf_counter()
    result = func(*args)
    return result, time.perf_counter() - start


print("1. float vs Decimal totals")
print(f"{'n':>8} | {'float total':>20} | {'Decimal total':>16} | {'float s':>8} | {'Decimal s':>9}")
for n in (300, 6000, 150000):
    entries = make_entries(n)
    tf, sf = timed(total_float, entries)
    td, sd = timed(total_decimal, entries)
    print(f"{n:>8} | {tf!r:>20} | {str(td):>16} | {sf:8.4f} | {sd:9.4f}")

print("\n2. Rounding each payment vs rounding only the total (300 payments of 33.335)")
exact = [Decimal("33.335")] * 300
each = sum((x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP) for x in exact), Decimal("0"))
final = sum(exact, Decimal("0")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print("  round each payment, then add :", each)
print("  add exactly, round the total :", final)

print("\n3. Rate table (dictionary) vs recalculation, 150,000 entries, 400 distinct pairs")
fats = [round(2.0 + 0.2 * i, 1) for i in range(20)]
snfs = [round(7.0 + 0.1 * i, 1) for i in range(20)]
pairs = [(f, s) for f in fats for s in snfs]
rng = random.Random(7)
lookups = [rng.choice(pairs) for _ in range(150000)]
table = {pair: milkrate.rate_per_litre(*pair) for pair in pairs}


def with_table(keys):
    """Look up every rate in the dictionary."""
    return sum(1 for key in keys if table[key] is not None)


def recalc(keys):
    """Recalculate every rate."""
    return sum(1 for key in keys if milkrate.rate_per_litre(*key) is not None)


_, t_table = timed(with_table, lookups)
_, t_calc = timed(recalc, lookups)
print(f"  dictionary lookup : {t_table:.4f} s  = {t_table / 150000 * 1e6:.2f} microseconds per entry")
print(f"  recalculation     : {t_calc:.4f} s  = {t_calc / 150000 * 1e6:.2f} microseconds per entry")
print(f"  pairs stored in the table (k): {len(table)}")
