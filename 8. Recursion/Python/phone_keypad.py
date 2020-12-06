'''
https://www.geeksforgeeks.org/find-possible-words-phone-digits/
'''

# generate all mappings and store in array
mappings = ['', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
def generate_mapping(input_str):
    if input_str == '':                                 # if no key pressed then 1 word which is ''(blank)
        return ['']                                     # similar to 2^0 = 1

    ch = input_str[0]                                   # extract 6
    recur_result = generate_mapping(input_str[1:])      # call on 78

    my_result = []

    str_at_ch = mappings[ord(ch)-ord('0')]              # get string at 6 from mapping
    for i in range(len(str_at_ch)):
        ch_i = str_at_ch[i]
        for recur_str in recur_result:                  # loop over all string obtained from 78
            my_result.append(ch_i + recur_str)          # append each char of 6 to strings obtained from 78

    return my_result
print(generate_mapping('678'))


# Print all mapping as soon as input is empty
# method - 1
mappings = ['', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
def generate_mapping(input_str, output_str):
    if input_str == '':
        print(output_str)
        return
    
    ch = input_str[0]                                       # extract 6
    str_at_ch = mappings[ord(ch)-ord('0')]                  # get string at 6th index
    for s in str_at_ch:                                     # append all characters of 6 in output
        generate_mapping(input_str[1:], output_str+s)

generate_mapping('678', '')

# method - 2
mappings = ['', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
def generate_mapping(input_str, i, output_str, j):
    
    if i == len(input_str):
        print(*output_str[:j])
        return

    digit = ord(input_str[i]) - ord('0')

    if digit == 0 or digit == 1:
        generate_mapping(input_str, i+1, output_str, j)
        
    for k in range(len(mappings[digit])):
        output_str[j] = mappings[digit][k]
        generate_mapping(input_str, i+1, output_str, j+1)

input_str = input()
output_str = ['0'] * len(input_str)
generate_mapping(input_str, 0, output_str, 0)







