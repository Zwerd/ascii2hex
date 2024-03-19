#!/usr/bin/env python3
# this is zwerd code
#
import argparse

def ascii_to_hex(string, pattern):
    if pattern == '%':
        return ''.join(['%' + '{:02x}'.format(ord(c)) for c in string])
    elif pattern == '\\x':
        return ''.join(['\\x' + '{:02x}'.format(ord(c)) for c in string])
    elif pattern == '0x':
        return ''.join(['0x' + '{:02x}'.format(ord(c)) for c in string])
    else:
        return ' '.join([pattern + '{:02x}'.format(ord(c)) for c in string])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert ASCII string to hex representation.')
    parser.add_argument('-s', '--string', help='ASCII string to convert', required=True)
    parser.add_argument('-p', '--pattern', help='Pattern for hex representation (e.g., %, \\x, 0x)', default='%')
    
    # Parse arguments
    args = parser.parse_args()

    # Call function to convert ASCII string to hex representation
    result = ascii_to_hex(args.string, args.pattern)
    
    # Print the result
    print(result)
