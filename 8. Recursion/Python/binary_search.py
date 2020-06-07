'''
input an array
search an element from an array using binary search
'''
def binary_search(arr, s, e, k):
    if s>e:
        return -1

    mid = s+(int((e-s)/2))

    if arr[mid] == k:
        return mid

    if arr[mid] > k:
        return binary_search(arr, s, mid-1, k)
    return binary_search(arr, mid+1, e, k)

def main():
   k = 1
   arr = [1, 2, 3, 4, 5]
   n = len(arr)
   print(binary_search(arr, 0, n-1, k))

main()