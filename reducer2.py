#!/usr/bin/env python
"""Reducer outputs Make and year and the count."""
import sys
# [Define group level master information]

current_makeyear = None
current_count = 0


def reset():
    global current_makeyear
    global current_count
    # [Logic to reset master info for every new group]
    current_makeyear = None
    current_count = 0


# Run for end of every group
def flush():
    global current_makeyear
    global current_count
    # [Write the output]
    print(f"{current_makeyear}\t{current_count}")


def reducer(input):
    global current_makeyear
    global current_count
    # input comes from STDIN
    for line in input:
        # [parse the input we got from mapper and update the master info]
        row = line.strip().split("\t")
        makeyear = row[0]
        try:
            count = int(row[1])
        except:
            return
        # [detect key changes]
        if current_makeyear != makeyear:
            if current_makeyear != None:
                # write result to STDOUT
                flush()
            reset()
        # [update more master info after the key change handling]
        current_count += count

        current_makeyear = makeyear

    # do not forget to output the last group if needed!
    flush()


def main(input):
    reducer(input)


if __name__ == "__main__":
    input = sys.stdin
    main(input)
