mappings = ['', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
def generate_mapping(input_str, i, output_str, j):
    
    if i == len(input_str):
        print(*output_str[:j])
        return

    digit = ord(input_str[i]) - ord('0')
    if digit == 0 or digit == 1:
        generate_mapping(input_str, i+1, output_str, j)
		
    if digit == 0 or digit == 1:
        generate_mapping(input_str, i+1, output_str, j)
    for k in range(len(mappings[digit])):
        output_str[j] = mappings[digit][k]
        generate_mapping(input_str, i+1, output_str, j+1)

def main():
    input_str = input()
    output_str = ['0'] * len(input_str)
    generate_mapping(input_str, 0, output_str, 0)

main()