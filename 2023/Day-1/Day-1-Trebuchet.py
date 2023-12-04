# Take in input file with lines of text
# Each line has a specific calibration value
# On each line, the calibration value = first digit + last digit to form a single 2-digit number

# What is the sum of all the calibration values?

# Define a dictionary that maps
# numeric words to their corresponding digits
word_to_digit = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

# function to take in file
def process_data(infile):
    with open(infile) as f:
        data = f.read().split("\n")
        return data

# function to parse last digit and first digit to form a single 2-digit number
def get_calibration_values(calibration_data):
    
    digits = []
    current_digit = ''

    for value in calibration_data:
        for char in value:
            # check if char is in the dictionary, if it is return value
            if char.isdigit() and len(current_digit) != 2:
                current_digit += char
        digits.append(current_digit)
    return digits


# function to sum all the values and return it
def sum_calibration_values():
    pass

def main():
    data = process_data("calibration_doc.txt")
    calibration_values = print(get_calibration_values(data))

if __name__ == '__main__':
    main()