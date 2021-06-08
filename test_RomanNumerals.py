from RomanNumerals import to_roman_numerals


def test_basic_numerals():
    output = to_roman_numerals(1)
    assert output == 'I'


def test_complex_numerals():
    output = to_roman_numerals(1246)
    assert output == 'MCCXLVI'
