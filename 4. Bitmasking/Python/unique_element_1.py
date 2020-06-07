'''
Input an array
In array, each number is occuring twice except one, find that unique element
Eg : 1, 2, 2, 1, 3, 3, 5 --> ans - 5
'''

def main():
    arr = list(map(int, input().split()))
    n = len(arr)

    ans = arr[0] ^ arr[1]

    for i in range(2, n):
        ans = ans ^ arr[i]
    print(ans)

main()