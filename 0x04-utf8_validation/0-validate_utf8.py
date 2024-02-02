#!/usr/bin/python3
"""
check if data is valid UTF-8 encoding
"""


def validUTF8(data):
    """
    check if data is valid UTF-8 encoding
    """
    continuation = 0
    UTF8_BIT_1 = 1 << 7
    UTF8_BIT_2 = 1 << 6

    for value in data:
        mask = 1 << 7
        if continuation == 0:
            while mask & value:
                continuation += 1
                mask = mask >> 1
            if continuation == 0:
                continue
            if continuation == 1 or \
                    continuation > 4:
                return False
        else:
            if not (value & UTF8_BIT_1 and not (value & UTF8_BIT_2)):
                return False
        continuation -= 1

    if continuation == 0:
        return True
    else:
        return False
