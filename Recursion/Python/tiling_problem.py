def count_ways(n):
    if n == 0 or n == 1:
        return 1
    
    return count_ways(n-1) + count_ways(n-4)

def main():
    n = int(input())
    print(count_ways(n))

main()