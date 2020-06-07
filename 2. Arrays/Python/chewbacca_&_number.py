'''
input a number
create a number smaller than digit by subtracting each digit by 9
Example:
Input - 4545
Output - 4444
'''

number = input()

number = list(number)

i = 0

if number[i] == '9':
    i += 1

while(i<len(number)):
    digit = int(number[i])
    if digit >= 5:
        digit = str(9 - digit)
        number[i] = digit

    i += 1
number = ''.join(number)
print(number)