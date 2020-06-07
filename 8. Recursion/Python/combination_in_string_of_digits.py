'''
Given an input string of numbers, find all combinations of numbers that can be formed using digits in the same order.
Examples:
Input : 123 
Output :1 2 3
        1 23
        12 3
        123
'''

# method - 1
def possible_mapping(input_str, i, ouput_str, j):
    if i == len(input_str):
        print(' '.join(ouput_str[:j]))
        return

    for k in range(1, len(input_str)+1):
        if i+k <= len(input_str):
            ouput_str[j] = input_str[i:i+k] 
            possible_mapping(input_str, i+k, ouput_str, j+1)

def main():
    input_str = input()
    ouput_str = ['0'] * (len(input_str))
    possible_mapping(input_str, 0, ouput_str, 0)

main()

# method - 2
def permutations(input_str, i, output, j):
    if i == len(input_str):
        print("(", end = "")
        print(*output[:(j-1)], sep = "", end = "")
        print(")", end = "")
        return
    
    output[j] = input_str[i] 
    output[j+1] = ' '
    permutations(input_str, i+1, output, j+2)
    if i < len(input_str)-1:
        output[j] = input_str[i] 
        permutations(input_str, i+1, output, j+1)
    
if __name__ == '__main__':
    t = int(input())
    while(t):
        input_str = input()
        output = [''] * (2*len(input_str))
        permutations(input_str, 0, output, 0)
        print()
        t-=1
 
