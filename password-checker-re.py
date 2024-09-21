#!/usr/bin/env python

import argparse
import re

def check_password(filename):
    # Valid pass list is structured as such:
    # 1 means at passes this category, 0 means it fails
    # In order, at least 8 digits, contains lower, contains upper, contains digit
    # Example entry would be 1100, meaning it needs an upper case letter and a digit
    validPassList = []
    with open(filename) as passwords:
        for line in passwords:
            checks = []
            score = ''
            line = line.strip()
            lengthMatch = len(line) >= 8
            checks.append(lengthMatch)
            lowerCaseMatch = re.search(r'[a-z]', line)
            checks.append(lowerCaseMatch)
            upperCaseMatch = re.search(r'[A-Z]', line)
            checks.append(upperCaseMatch)
            digitMatch = re.search(r'[0-9]', line)
            checks.append(digitMatch)         
            for check in checks:
                score = score + str(int(bool(check)))
            validPassList.append(score)
    return validPassList

def main():
    parser = argparse.ArgumentParser(description="A password checker that uses regular expressions for password checking")
    parser.add_argument('filename', help='The filename containing passwords to be checked')
    args = parser.parse_args()
    print(check_password(args.filename))

if __name__ == "__main__":
    main()