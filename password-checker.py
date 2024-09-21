#!/usr/bin/env python
# This script checks a single password, passed via a command line argument
import argparse

def check_password(pwd):
    validPass = True
    #Check 8 char long
    if len(pwd) < 8:
        print("Password is must be at least 8 characters long")
        validPass = False
    #Contains one upper case
    if pwd == pwd.lower():
        print("Password must contain at least one upper case letter")
        validPass = False
    #Contains one lower case
    if pwd == pwd.upper():
        print("Password must contain at least one lower case letter")
        validPass = False
    #Contains at least one digit
    containsDigit = False
    for letter in pwd:
        if letter.isDigit():
            containsDigit = True
    if not containsDigit:
        print("Password must contain at least one digit")
        validPass = False
    
    return validPass

def main():
    parser = argparse.ArgumentParser(description="A function for checking the strength of a password")
    parser.add_argument('password', type=str, help='The password to be checked')
    args = parser.parse_args()
    check_password(args.password)

if __name__ == "__main__":
    main()
