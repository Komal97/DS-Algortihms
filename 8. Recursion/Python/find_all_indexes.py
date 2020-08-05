'''
find all occurences of an element in an array recursively
return an array containing all indexes
Input: 
3
[2, 3, 6, 9, 8, 3, 2, 6, 2, 9]
Output:
[1, 5]
'''

def findAllIndexes(arr, i, data, found_so_far):
    
    if i == len(arr):                                               # create an array of size found so far count while returning from base case
        return [0]*found_so_far
    
    if arr[i] == data:                                              # if data match, then inc i and count
        found_arr = findAllIndexes(arr, i+1, data, found_so_far+1)
        found_arr[found_so_far] = i                                 # while returning fill index from last in array
    else:                                                           # else inc i only
        found_arr = findAllIndexes(arr, i+1, data, found_so_far)
    return found_arr

arr = [2, 3, 6, 9, 8, 3, 2, 6, 2, 9]
found_arr = findAllIndexes(arr, 0, 2, 0)
print(found_arr)