'''
input an array
search an element from an array using binary search
'''
global count
def tower_of_hanoi(n, src, dest, helper):
    if n == 0:
        return

    tower_of_hanoi(n-1, src, helper, dest)
    print("move disk", n, "from rod", src, "to rod", dest)
    tower_of_hanoi(n-1, helper, dest, src)

def main():
   
    n = int(input())
    tower_of_hanoi(n, '1', '3', '2')
    print("total moves: ", (1<<n)-1)
        

main()