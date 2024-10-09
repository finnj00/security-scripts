#!/usr/bin/env python

import re
import argparse
from collections import defaultdict

def scan_login(filename):
    failedAttempts = defaultdict(int)
    with open(filename) as logs:
        for line in logs:
            match = re.search(r'Failed password for (invalid user )?(.*)from (\d+.\d+.\d+.\d+) port (\d+)', line)
            if match:
                failedAttempts[match.group(3)] += 1
            pass
        for ip in failedAttempts.keys():
            print(f'{ip} failed to login {failedAttempts[ip]} times')

def main():
    parser = argparse.ArgumentParser(description='Script to check log files and  report any suspicious login attempts (more than 10 failed)')
    parser.add_argument('filename', type=str, help='Name of login log file')
    args = parser.parse_args()
    scan_login(args.filename)

if __name__ == "__main__":
    main()