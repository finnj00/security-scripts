#!/usr/bin/env python

import re
import argparse

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="A simple script to parse IP addresses from a log file and print out the 5 most common IP's")

    # Add the arguments
    parser.add_argument('filename', type=str, help="The logfile to be parsed")

    # Parse the arguments
    args = parser.parse_args()

    parse_log(args.filename)

def parse_log(fileName):
    IPs = {}
    top5 = []
    # For every line in the log file
    with open(fileName) as logFile:
        for line in logFile:
            match = re.search(r'^\d+\.\d+\.\d+\.\d+', line)
            if match:
                thisIP = match.group()
                occurance = 1
                if thisIP in IPs.keys():
                    IPs[thisIP] = IPs[thisIP] + 1
                    occurance = IPs[thisIP]
                else:
                    IPs[thisIP] = 1
                if (occurance - 1, thisIP) in top5:
                    top5.remove((occurance - 1, thisIP))
                    top5.append((occurance, thisIP))
                    top5.sort()
                elif len(top5) < 5:
                    top5.append((occurance, thisIP))
                    top5.sort()
                else:
                    min, _ = top5[0]
                    if occurance > min:
                        top5.pop(0)
                        top5.append((occurance, thisIP))
                        top5.sort()
        print(top5)
if __name__ == '__main__':
    main()