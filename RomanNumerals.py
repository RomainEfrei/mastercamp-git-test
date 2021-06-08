def to_roman_numerals(n):
    ints = [1000, 500, 100, 50, 10, 5, 1]
    romans = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    roman_number = ""
    for i in range(len(ints)):
        count = int(n / ints[i])
        if count < 4:
            roman_number += romans[i] * count
        else:
            roman_number += (5 - count) * romans[i] + romans[i - 1]
        n -= ints[i] * count
    return roman_number

