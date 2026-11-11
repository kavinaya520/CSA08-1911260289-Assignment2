"""Task 5: read clerk entries and convert types safely."""


def to_float_try(text):
    """Convert text to float using try/except ValueError. Return None if invalid."""
    try:
        return float(text)
    except ValueError:
        return None


def to_float_checked(text, strip=False):
    """Validate with string methods first, then convert. Return None if invalid."""
    cleaned = text.strip() if strip else text
    if cleaned.replace(".", "", 1).isdigit():
        return float(cleaned)
    return None


def read_entry():
    """Read one entry from the clerk (input() always returns a string)."""
    farmer_id = input("Farmer ID : ").strip()
    litres = to_float_try(input("Litres    : "))
    fat = to_float_try(input("Fat %     : "))
    snf = to_float_try(input("SNF %     : "))
    return farmer_id, litres, fat, snf


if __name__ == "__main__":
    print("input() returns a str, so we convert it")
    print("int('12') =", int("12"), "| float('3.5') =", float("3.5"))

    print("\nWhat happens with bad text")
    for bad in ("8,5", "eight"):
        try:
            float(bad)
        except ValueError as err:
            print(f"  float({bad!r}) -> ValueError: {err}")

    print("\nHandling invalid input")
    print(f"{'text':>10} | {'try/except':>10} | {'str check':>9} | {'check+strip':>11}")
    for text in ("8.5", " 8.5 ", "8,5", "eight"):
        print(f"{text!r:>10} | {str(to_float_try(text)):>10} | {str(to_float_checked(text)):>9}"
              f" | {str(to_float_checked(text, strip=True)):>11}")

    print("\nFormatted output with f-strings")
    amount = 33.4
    print(f"[{amount:8.2f}]")
