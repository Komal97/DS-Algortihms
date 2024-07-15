'''
find number of days from current day on which price is greater than current
Input: 100 80 60 70 60 75 85
Output: [0, 1, 1, 2, 1, 4, 6]
'''
#nearest left greater element
from collections import deque
def stock_span(prices, n):
    stack = deque([])
    ans = []
    for day in range(n):
        cur_price = prices[day]
        while len(stack) > 0 and cur_price > prices[stack[-1]]:
            stack.pop()
        betterday = 0 if len(stack)==0 else stack[-1]
        span = day - betterday
        ans.append(span)
        stack.append(day)
    print(ans)

if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    stock_span(prices, n)