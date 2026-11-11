"""Task 3: named constants, dynamic typing and multiple assignment."""

# Rate card constants (UPPER_CASE by PEP 8 convention)
BASE_RATE = 30.00        # Rs per litre at standard fat and SNF
FAT_STEP_VALUE = 0.40    # Rs per litre for every 0.1% fat
SNF_STEP_VALUE = 0.30    # Rs per litre for every 0.1% SNF
STD_FAT = 3.5            # % fat baseline
STD_SNF = 8.5            # % SNF baseline
STEP_SIZE = 0.1          # size of one step in percent
MIN_FAT = 2.0
MAX_FAT = 7.0

# Dictionary version of the rate card (alternative design)
RATE_CARD = {"base": 30.00, "fat": 0.40, "snf": 0.30}

if __name__ == "__main__":
    # Python does not stop us from changing a constant
    print("BASE_RATE before:", BASE_RATE)
    BASE_RATE = 31.00
    print("BASE_RATE after reassigning:", BASE_RATE, "(allowed, the UPPER_CASE name is only a warning)")

    # Dynamic typing
    x = 10
    print(x, type(x))
    x = "ten"
    print(x, type(x))

    # Multiple assignment and swap
    a, b = 3, 5
    print("before:", a, b)
    a, b = b, a
    print("after :", a, b)
