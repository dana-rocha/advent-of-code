import argparse

def main(infile):
    print("The elf carrying the most calories: ", most_calories(infile))
    print("How many calories are the top three elves carrying in total: ", top_three(infile))

def process_data(infile):
    with open(infile) as f:
        elves = f.read().split("\n\n")

    data = [list(map(int, elf.strip().split("\n"))) for elf in elves]
    summed_data = list(map(sum, data))
    return summed_data

def top_three(infile):
    # Day 1 Part 2
    cal_list = process_data(infile)
    return sum(sorted(cal_list, reverse=True)[:3])

def most_calories(infile):
    # Day 1 Part 1
    calorie_list = process_data(infile)
    return max(calorie_list)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='infile', required=True)
    args = parser.parse_args()
    main(args.infile)
