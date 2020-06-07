'''
multiple 2 numbers using recursion without using (*)
'''

def multiply(a, b):
    if b == 0:
        return 0
    
    if b>0:
        return a + multiply(a, b-1)
    if b<0:
        return -multiply(a, -b)


def main():
    print(multiply(-5, -3))

if __name__ == '__main__':
    main()