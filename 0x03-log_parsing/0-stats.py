#!/usr/bin/python3
"""
Script to compute metrics from log data read from stdin.
"""

import sys

def print_stats(total_sizes, status_codes):
    """
    Prints the total file size and number of lines by status code
    """
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    status_code = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    lines_read = 0

    try:
        for line in sys.stdin:
            lines_read += 1
            try:
                parts = line.split()
                if len(parts) >= 10:
                    file_size = int(parts[-1])
                    total_size += file_size
                    status_code = parts[-2]
                    if status_code in status_codes:
                        status_codes[status_code] += 1
                        if lines_read % 10 == 0:
                            print_stats(total_size, status_codes)
            except KeyboardInterrupt:
                print_stats(total_size, status_codes)
                raise
            except Exception as e:
                pass
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
