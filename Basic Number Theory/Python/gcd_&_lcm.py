'''
Input 2 numbers
1) find gcd(greatect common divisor) or hcf(highest common factor)
2) find lcm(least common multiple)
'''
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return int((a*b)/gcd(a,b))

def main():
    a = int(input())
    b = int(input())
    print(gcd(a, b))
    print(lcm(a, b))
main()