'''
Input - given a number consist of 4 and 7 numbers only
Output - return index of the number in the series of 4, 7, 44, 47, 74, 77,......
Soln - if current number has 4 digits - calculate possible total number of 3, 2, 1 digits then calculate possible soln for 4 digit 
'''

num = input()
length = len(num)

if length <= 0:
    print(0)

ans = (1<<length) -2
pos = 0

for i in range(length-1, -1, -1):
    if num[i] == "7":
        ans += (1<<pos)
    pos += 1

print(ans+1)
