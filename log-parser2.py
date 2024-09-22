#!/usr/bin/env python
import re
import argparse

def parse_log(filename):
    with open(filename) as logs:
        for log in logs:
            match = re.search(r'GET[^"]*', log)
            if match:
                print(match.group())

def main():
    parser = argparse.ArgumentParser(description="Log parser to identify the URLs being accessed in logs")
    parser.add_argument('filename', help="The filename of the logs to be parsed")
    args = parser.parse_args()
    parse_log(args.filename)

if __name__ == "__main__":
    main()