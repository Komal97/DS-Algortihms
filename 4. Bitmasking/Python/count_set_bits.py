'''
Input a number
Find minimum number of bits require to change a to b
'''

# method - 1, check for rightmost bit , if 1 count ++ 
# complexity = o(no. of bits)
def count_set_bits(n):

    count = 0
    while(n):
        count+=(n&1)
        n = n>>1
    return count

# method - 2
# complexity = o(no. of set bits)
def count_set_bits_2(n):
    count = 0
    while(n):
        count += 1
        n = n&(n-1)
    return count

def main():
    a = int(input())
    b = int(input())

    c = a ^ b
    print(count_set_bits(c))
    print(count_set_bits_2(c))
main()