# def main to call txt file
# helper function to loop through txt file and count # of calories
import argparse
import sys

def main(infile):
    print(most_calories(infile))

def process_data(infile):
    with open(infile) as f:
        elves = f.read().split("\n\n")

    return [list(map(int, elf.strip().split("\n"))) for elf in elves]

def most_calories(infile):
    current_max = 0
    calorie_list = process_data(infile)

    for elf in calorie_list:
        if sum(elf) >= current_max:
            current_max = sum(elf)
    return current_max

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='infile', required=True)
    args = parser.parse_args()
    main(args.infile)
