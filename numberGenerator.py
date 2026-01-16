def generateThreeDigitNumbers():
    """Generates string numbers from 0 to 999, all padded to 3 digits."""
    threeDigitNumbers = []
    for num in range(1000):
        paddedNumber = str(num).zfill(3)
        threeDigitNumbers.append(paddedNumber)
    return threeDigitNumbers


def generateFourDigitNumbers():
    """Generates string numbers from 0 to 9999, all padded to 4 digits."""
    fourDigitNumbers = []
    for num in range(10000):
        paddedNumber = str(num).zfill(4)
        fourDigitNumbers.append(paddedNumber)
    return fourDigitNumbers


if __name__ == "__main__":
    # Demo the three digit function
    threeDigits = generateThreeDigitNumbers()
    print("Three digit numbers (first 15):")
    print(threeDigits[:15])

    # Demo the four digit function
    fourDigits = generateFourDigitNumbers()
    print("\nFour digit numbers (first 15):")
    print(fourDigits[:15])
