'''
input a number
print number in words
Eg: 2048 -> two zero four eight
'''
def convert_to_words(n):
    string = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    if n <= 0:
        return 

    convert_to_words(int(n/10))
    print(string[n%10], end = " ")

def main():
    n = 204809
    convert_to_words(n)

main()