'''
1) XOR swapping
2) Check odd even
'''

def swapping():
    a = int(input())
    b = int(input())
    a = a^b
    b = b^a
    a = a^b
    print(a,b)

def check_odd_even():
    n = int(input())

    if n&1:
        print("Odd")
    else:
        print("Even")

check_odd_even()
swapping()
