#!/usr/bin/python3
"""module for UTF-8 validation"""


def validUTF8(data):
    """Establishes if given data represents valid UTF_8 encoding
    Args: data: list of int
    Returns: True if valid UTF-8, otherwise False
    """
    # num of bytes in UTF-8 set
    num_bytes = 0
    # mask to check if first significant bit is set or not
    mask_1 = 1 << 7
    #mask to check if second significant bit is set or not
    mask_2 = 1 << 6

    for num in data:
        # gets significany bit in byte if starting byte
        mask = 1 << 7
        if num_bytes == 0:
            while mask & num:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
            
        else:
            # if part of UTF-8 character, look at the two significant bits
            if not ((num & mask_1) and not (num & mask_2)):
                return False
        num_bytes -= 1
    return num_bytes == 0

