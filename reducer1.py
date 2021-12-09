#!/usr/bin/env python
"""Reducer outputs Make and year. Only outputs accident types."""
import sys
# [Define group level master information]

current_vin = None
make = None
year = None
count = 0


def reset():
    global current_vin
    global make
    global year
    global count
    # [Logic to reset master info for every new group]
    current_vin = None
    current_values = None
    make = None
    year = None
    count = 0


# Run for end of every group
def flush():
    global make
    global year
    global count
    # [Write the output]
    for _ in range(0, count):
        print '%s,%s' % (make, year)


def reducer(input):
    global current_vin
    global make
    global year
    global count
    # input comes from STDIN
    for line in input:
        # [parse the input we got from mapper and update the master info]
        row = line.strip().split("\t")
        vin = row[0]
        data = row[1].strip().split(",")
        # [detect key changes]
        if current_vin != vin:
            if current_vin != None:
                # write result to STDOUT
                flush()
            reset()
        # [update more master info after the key change handling]
        if data[0] == "I":
            make = data[1]
            year = data[2]

        if data[0] == "A":
            count += 1

        current_vin = vin

    # do not forget to output the last group if needed!
    flush()


def main(input):
    reducer(input)


if __name__ == "__main__":
    input = sys.stdin
    main(input)
