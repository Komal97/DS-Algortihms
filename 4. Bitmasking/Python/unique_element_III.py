'''
Input an array
In array, each number is occuring thrice except one element, find that unique element
Eg : 1, 2, 2, 2, 1, 1, 1, 3 --> ans - 3
'''

def find_3_unique_elements(arr, n):
    
    cnt = [0 for _ in range(64)]
    
    for i in range(n):
        j = 0
        val = arr[i]
        while(val):
            cnt[j] += (val&1)
            val = val>>1
            j += 1

    p = 1
    ans = 0    
    for i in range(64):
        cnt[i] %= 3
        ans += (p*cnt[i])
        p = p<<1
    print(ans)

def main():
    
    arr = list(map(int, input().split()))
    n = len(arr)
    find_3_unique_elements(arr, n)

main()