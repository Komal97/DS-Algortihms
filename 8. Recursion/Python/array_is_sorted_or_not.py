'''
input an array
check whether this is sorted or not
'''

def isSorted(arr, n):
    # if there is only one element then it is true
    if n==1:
        return True

    # check first and second element, if it true then check for remaining smaller array
    if arr[0]<arr[1] and isSorted(arr[1:], n-1):
        return True
    
    # if no condition match, then return False
    return False

def main():
    arr = [1, 2, 3, 4, 5, 8, 9, 11]
    n = len(arr)
    print(isSorted(arr, n))

if __name__ == '__main__':
    main()