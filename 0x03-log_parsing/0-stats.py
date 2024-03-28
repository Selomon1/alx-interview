#!/usr/bin/python3
"""
Script to compute metrics from log data read from stdin.
"""

import sys
import signal
import re


def signal_handler(sig, frame):
    """ Signal handler for keyboard inturruption """
    print_stats(total_size, status_codes)


def print_stats(total_size, status_codes):
    """
    Prints the total file size and number of lines by status code
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

signal.signal(signal.SIGINT, signal_handler)

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def parse_line(line):
    """ Parse a log entry line and extract IP, status_code """
    match = re.match(r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[.*\] \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d+)$", line)
    if match:
        return int(match.group(2)), int(match.group(3))
    else:
        return None, None

try:
    for line in sys.stdin:
        code, size = parse_line(line.strip())
        if code is None:
            continue
        total_size += size
        status_codes[code] += 1
        line_count += 1
        if line_count == 10:
            print_stats(total_size, status_codes)
            line_count = 0
except KeyboardInterrupt:
    pass

print_stats(total_size, status_codes)
