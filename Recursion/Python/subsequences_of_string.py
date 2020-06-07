'''
input a string
print all subsequences
'''

def print_subsequences(input_str, output_str):
    if input_str == "":
        print(output_str)
        return 
    
    print_subsequences(input_str[1:], output_str)
    print_subsequences(input_str[1:], output_str + input_str[0])

def main():
    input_str = input()
    output_str = ""
    print_subsequences(input_str, output_str)
        
main()