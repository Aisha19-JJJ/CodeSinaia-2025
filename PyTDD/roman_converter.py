
def roman_converter(num):
    if not isinstance(num, int):
        return None
    
    if num <= 0 or num >= 4000:
        return None
    
    ROMAN_NUMS = [
        (1,"I"),
        (5,"V"),
        (10,"X"),
        (50, "L"),
        (100, "C"),
        (500, "D"),
        (1000, "M"),
    ]

    out = ''
    for value, symbols in reversed(ROMAN_NUMS):
        while num >= value:
            out += symbols 
            num -= value

    return out