'''
Given a number find all the possible mappings of the characters in sorted order.
Examples:
Input: 123
Output: ABC AW LC
'''
mapping = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def create_mapping(input_str, i, output_str, j):
    if i == len(input_str):
        print(''.join(output_str[:j]), end = " ")
        return

    # take one digit at a time
    first_digit = ord(input_str[i]) - ord('0')
    output_str[j] = mapping[first_digit]
    create_mapping(input_str, i + 1, output_str, j + 1)
    #print("output_str 1 : ", output_str)
    if i+1 <len(input_str):
        second_digit = ord(input_str[i+1]) - ord('0')
        number = first_digit * 10 + second_digit
        if number <= 26:
            output_str[j] = mapping[number]
            create_mapping(input_str, i + 2, output_str, j + 1)

    #print("output_str 2 : ", output_str)

def main():
    input_str = input()
    output_str = ['0'] * len(input_str)
    create_mapping(input_str, 0, output_str, 0)

main()