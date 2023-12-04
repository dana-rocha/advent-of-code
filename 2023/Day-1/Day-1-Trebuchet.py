# Take in input file with lines of text
# Each line has a specific calibration value
# On each line, the calibration value = first digit + last digit to form a single 2-digit number

# What is the sum of all the calibration values?

def process_data(infile):
    # function to take in file
    with open(infile) as f:
        data = f.read().split("\n")
        return data

def sum_calibration_values(calibration_data):
    results_sum = 0

    for value in calibration_data:
        digits = [char for char in value if char.isdigit()]
        results_sum += int(digits[0] + digits[-1])
    return results_sum

def main():
    data = process_data("calibration_doc.txt")
    calibration_values = sum_calibration_values(data)
    print(calibration_values)

if __name__ == '__main__':
    main()