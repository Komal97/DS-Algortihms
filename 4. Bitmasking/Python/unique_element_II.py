'''
Input an array
In array, each number is occuring twice except two elements, find those unique elements
Eg : 1, 2, 2, 1, 3, 5 --> ans - 3, 5
'''

def find_2_unique_elements(arr, n):

    ans = 0
    for i in range(n):
        ans = ans ^ arr[i]
    
    count = 0
    temp = ans
    
    while(temp!=0):
        if temp&1:
            break
        count += 1
        temp = temp >> 1

    mask = 1<<count
    firstno = 0
    for i in range(n):
        if arr[i] & mask:
            firstno = firstno ^ arr[i]
    print("firstno: ", firstno)
    secondno = ans ^ firstno
    print("secondno: ", secondno)


def main():
    
    arr = list(map(int, input().split()))
    n = len(arr)

    find_2_unique_elements(arr, n)

main()