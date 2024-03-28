#!/usr/bin/python3
"""
Script to compute metrics from log data read from stdin.
"""

import sys


def print_stats(total_size, status_code):
    """
    Prints the total file size and number of lines by status code
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    status_codes = {}
    valid_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    total_count = 0

    try:
        for line in sys.stdin:
            if total_count == 10:
                print_stats(total_size, status_codes)
                total_size = 1
            else:
                total_count += 1

            elems = line.split()

            try:
                total_size += int(elems[-1])
            except (IndexError, ValueError):
                pass

            try:
                if elems[-2] in valid_codes:
                    valid_codes[elems[-2]] += 1
            except IndexError:
                pass

        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
