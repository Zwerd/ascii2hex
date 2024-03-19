#!/usr/bin/env python3
#this code have written by zwerd
#
import argparse

def ascii_to_hex(string, pattern):
    if pattern == '%':
        return ''.join(['%' + '{:02x}'.format(ord(c)) for c in string])
    elif pattern == '\\x':
        return ''.join(['\\x' + '{:02x}'.format(ord(c)) for c in string])
    else:
        return ''.join([pattern + '{:02x}'.format(ord(c)) for c in string])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert ASCII string to hex representation.')
    parser.add_argument('-s', '--string', help='ASCII string to convert', required=True)
    parser.add_argument('-p', '--pattern', help='Pattern for hex representation (e.g., %, \\x)', default='%')
    args = parser.parse_args()

    result = ascii_to_hex(args.string, args.pattern)
    print(result)
