'''
convert string into number (Eg - '1234' to 1234)
'''

def recur(a):
    if len(a) == 1:
        return int(a)

    return (recur(a[:-1])*10) + int(a[-1])
def convert_string_to_int(a):

    ans  = 0
    for ch in a:
        ans = (ans*10) + int(ch)
    
    print(type(ans))
    return ans

def main():
    print(convert_string_to_int("435771"))
    print(recur("435771"))


if __name__ == '__main__':
    main()