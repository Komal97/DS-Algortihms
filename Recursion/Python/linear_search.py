'''
input a array
search an element from an array using linear search
'''
def linear_search(arr, i, n, k):
    if i == n:
        return -1
    if arr[i] == k:
        return i
    return linear_search(arr, i+1, n, k)
def main():
   k = 8
   arr = [1, 2, 3, 5, 9, 0]
   n = len(arr)
   print(linear_search(arr, 0, n, k))

main()