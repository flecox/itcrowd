"""
Code obtained from: https://stackoverflow.com/questions/33486183/convert-from-numbers-to-roman-notation
and fixed.
"""

ROMAN_CONVERSION = [
    [1000, 'M'],
    [900, 'CM'],
    [500, 'D'],
    [400, 'CD'],
    [100, 'C'],
    [90, 'XC'],
    [50, 'L'],
    [40, 'XL'],
    [10, 'X'],
    [9, 'IX'],
    [5, 'V'],
    [4, 'IV'],
    [1, 'I'],
]


def to_roman(num):
    result = ''
    for denom, roman_digit in ROMAN_CONVERSION:
        result += roman_digit * int((num / denom))
        num %= denom
    return result
