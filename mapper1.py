#!/usr/bin/env python
"""Mapper outputs VIN as a key and incident type, make, and year as values"""
import sys


# input comes from STDIN (standard input)
def mapper(input):
    for line in input:
        row = str(line).strip().split(",")
        # Data
        vin_number = row[2]
        incident_type = row[1]
        make = row[3]
        year = row[5]
        # Return
        key = vin_number
        value = f"{incident_type},{make},{year}"
        print(f"{key}\t{value}")


def main(input):
    mapper(input)


if __name__ == "__main__":
    input = sys.stdin
    main(input)
