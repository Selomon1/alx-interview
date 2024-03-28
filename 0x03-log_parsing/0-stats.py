#!/usr/bin/python3
"""
Script to compute metrics from log data read from stdin.
"""

import sys
import re

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

total_size = 0
line_count = 0


def print_stats():
    """
    Prints the total file size and number of lines by status code
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line):
    """ Parse a log entry line and extract IP, status_code """
    match = re.match(r'^.*"GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$', line)
    if match:
        return int(match.group(1)), int(match.group(2))
    else:
        return None, None


try:
    for line in sys.stdin:
        code, size = parse_line(line.strip())
        if code is None:
            continue
        total_size += size
        if code is not None and code in status_codes:
            status_codes[code] += 1
            line_count += 1
        if line_count == 10:
            print_stats()
            line_count = 0
except KeyboardInterrupt:
    pass


print_stats()
