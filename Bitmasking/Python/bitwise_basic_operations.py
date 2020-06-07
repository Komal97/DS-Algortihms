'''
Bitwise basic operation
1) Get ith bit
2) Set ith bit
3) Clear ith bit
'''

def get_ith_bit(n, i):
    mask = 1<<i
    print("1") if n&mask else print("0")        

def set_ith_bit(n, i):
    mask = 1<<i
    print(n|mask)

def clear_ith_bit(n, i):
    mask = ~(1<<i)
    print(n&mask)

def main():
    n = int(input())
    i = int(input())
    get_ith_bit(n, i)
    set_ith_bit(n, i)
    clear_ith_bit(n, i)

main()