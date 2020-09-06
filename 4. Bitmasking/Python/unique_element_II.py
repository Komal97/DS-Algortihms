'''
https://practice.geeksforgeeks.org/problems/finding-the-numbers/0
IYou are given an array A containing 2*N+2 positive numbers, out of which 2*N numbers exist in pairs whereas the other two number occur exactly once and are distinct. 
You need to find the other two numbers and print them in ascending order.
Input :
2
2
1 2 3 2 1 4
1
2 1 3 2

Output :
3 4
1 3
'''

def find_numbers(arr, n):
    
    number = 0
    for num in arr:
        number ^= num                   # find xor of all elements
        
    rsbm = (number&-number)             # find rightmost set bit mask
    
    first_num = 0
    for num in arr:
        if (num&rsbm)!=0:               # xoring all element with rightmost set bit
            first_num ^= num
    
    second_num = first_num ^ number     # second num = xor ans ^ first num
    
    if first_num > second_num:
        print(second_num, first_num)
    else:
        print(first_num, second_num)
        
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        find_numbers(arr, n)
        t -= 1