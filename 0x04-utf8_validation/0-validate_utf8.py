#!/usr/bin/python3
"""
UTF-8 validation
"""


def validUTF8(data):
    """
    Determine if the given data set represents a valid UTF-8 encoding.
    """
    bytes_to_follow = 0

    for byte in data:
        if bytes_to_follow == 0:
            if byte >> 7:
                continue
            elif byte >> 5 == 0b110 or byte >> 5 == 0b1110:
                bytes_to_follow = 1
            elif byte >> 4 == 0b1110:
                bytes_to_follow = 2
            elif byte >> 3 == 0b11110:
                bytes_to_follow = 3

        else:
            if (byte >> 6) != 0b10:
                return False
            bytes_to_follow -= 1

    return bytes_to_follow == 0
