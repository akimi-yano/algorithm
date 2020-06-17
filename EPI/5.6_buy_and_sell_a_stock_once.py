# 5.6 buy and sell a stock once

def max_profit(prices):
    max_profit = 0
    buy_price = float('inf')
    for price in prices:
        if price<buy_price:
            buy_price = price
        else:
            max_profit = max(max_profit,(price-buy_price))
    return max_profit

print(max_profit([2,3,5,1,4]))
print(max_profit([310,315,275,295,260,270,290,230,255,250]))

# before writing a code, stop and review my code
# when writing a code, choose a short variable name : buy_price - > buy 