'''
Input a string
Print its subsequences i.e a, b, c, ab, ac, bc, abc, ' '
'''
def print_subseq(string, no):

    i = 0
    while(no):
        print(string[i], end = "") if no&1 else print("", end = "")
        no = no>>1 
        i += 1


def main():
    string = input()
    total_subseq_count = 1<<(len(string))

    for i in range(total_subseq_count):
        print_subseq(string, i)
        print()

main()