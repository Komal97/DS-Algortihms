'''
Input a number 
Find its square root upto a precision using binary search
'''

def find_square_root(number, precision):
    start = 0
    end = number
    ans = -1
    
    while(start <= end):
        mid = int((start + end)/2)
        if mid*mid == number:
            ans = mid
            break
        elif mid*mid < number:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    
    increment = 0.1
    for i in range(precision):
        while(ans * ans <= number):
            ans = ans + increment 
        ans = ans - increment
        increment = increment/10

    return ans

def main():
    
    number = int(input())
    precision = int(input())
    print(round(find_square_root(number, precision), precision))

main()