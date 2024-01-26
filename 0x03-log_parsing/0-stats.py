#!/usr/bin/python3
""" log parsing project"""
import sys

def print_stats(total_size, status_codes):
    """print statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def parse_line(line, status_codes):
    """parse each line and update status codes"""
    try:
        parts = line.split()
        size = int(parts[-1])
        code = int(parts[-2])

        if code in status_codes:
            status_codes[code] += 1
        else:
            status_codes[code] = 1

        return size

    except Exception:
        return 0

def main():
    """Main function"""
    total_size = 0
    status_codes = {}
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            size = parse_line(line, status_codes)
            total_size += size

            if count == 10:
                print_stats(total_size, status_codes)
                count = 0

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()
