'''
My food delivery startup wants to give out some gift cards to customers.

I also want to know what kind of food they could order for each gift card amount so I can prepare food ahead of time.

(the menu and gift card amounts are provided below)


Constraints/Hints:
- customers must use 100% of the gift card value
- a customer must be allowed order many of the same menu item
- there are combinations to be found for every gift card, none of these are trick values

Goal:
Print the first combination of food that you find which adds up to the gift card amount.

Example:
The $5 gift card has two possible answers:
['coffee', 'coffee', 'toast']
['cheese', 'cheese', 'cheese', 'cheese']


The output format is up to you, but here are some examples:

$5, 4 items
cheese, cheese, cheese, cheese

$99, 15 items:
{'coffee': 1, 'curry': 11, 'sandwich': 1, 'toast': 2}




'''

primary_menu = {
    'curry': 7.85,
    'sandwich': 6.85,
    'soup': 3.45,
    'egg': 3.20,
    'toast': 2.20,
    'soda': 2.05,
    'coffee': 1.40,
    'cheese': 1.25,
}

gift_cards = [5.00, 14.00, 19.00, 25.00, 33.00, 45.00, 49.00, 99.00, 114.00, 199.00]
'''
                    5.00   

toast 2.20
 5.00
-2.20
 2.80
 
 toast cheese ciffee soda ...
 
 
 1 initialize an answer array with None [None]
 2 iterate through the gift_cards call recursion
 3 recursion - input: remaing_amount, [], idx, primary_menu
   basecase 
  - if remianig_amount == 0.00 -> append to answer if the element at the idx in answer array is None and  return
  - if remianig_amount > 0.00 -> return
    recursive calls
  - loop through the dictionary and if the amount is less than or equal to remaining -> call helper(remaing_amount - value of primary_menu, arr + [key of primary_menu], idx, primary_menu
  
 
 [['cheese','toast'],['cheese','toast']]
'''

# gift_cards = [5.00]
        
# This solution works
# def combination_items(primary_menu, gift_cards):
#     items = []
#     def helper(remaining, arr, idx, primary_menu):
#         if remaining == 0.00 and answer[idx] is None:
#             answer[idx] = arr
#             return
#         if remaining < 0.00 or answer[idx] is not None:
#             return
        
#         for item, price in primary_menu.items():
#             if price <= remaining:
#                 helper(round(remaining - price,2), arr + [item], idx, primary_menu)
    
    
#     answer = [None for _ in range(len(gift_cards))]
    
#     for i, price in enumerate(gift_cards):
#         helper(price, [], i, primary_menu)
#         print(price, answer[i])
    
#     return answer

# This solution works -optimization by changing it bottom up approach (we can round up to 2 or multiply by 100 and cast to int)
from functools import lru_cache
def combination_items(primary_menu, gift_cards):
    @lru_cache(None)
    def helper(remaining):
        nonlocal i, primary_menu
        if remaining == 0.00:
            return []

        for item, price in primary_menu.items():
            if price <= remaining:
                ans = helper(round(remaining - price, 2))
                if ans is not None:
                    return [item] + ans
        return None
    
    answer = []
    for i, price in enumerate(gift_cards):
        answer.append(helper(price))
        print((i, price), answer[-1])

    return answer

print(combination_items(primary_menu, gift_cards))

'''
primary_menu = {
    'sandwich': 6.85,
    'toast': 2.20,
    'curry': 7.85,
    'egg': 3.20,
    'cheese': 1.25,
    'coffee': 1.40,
    'soup': 3.45,
    'soda': 2.05,
}

gift_cards = [5.00]


answer = [['toast','coffee', 'coffee']]
helper(5.00, [], 0, primary_menu)
helper(2.80, ['toast'], 0, primary_menu)
helper(0.60, ['toast', 'toast'], 0, primary_menu) / helper(1.55, ['toast', 'cheese'], 0, primary_menu) / helper(1.40, ['toast','coffee'], 0, primary_menu)
helper(0.00, ['toast','coffee', 'coffee'], 0, primary_menu)

2.80
1.25
1.55

2.80
1.40
1.40
'''


'''
Refactor your first algorithm to examine many matching combinations for each gift card to find the 
combination with the fewest total number of items purchased.

For example, the $5 gift card list should return ['coffee', 'coffee', 'toast'] instead of 
['cheese', 'cheese', 'cheese', 'cheese']

$5, 3 items: {'coffee': 2, 'toast': 1}
$14, 4 items: {'curry': 1, 'soda': 3}
$19, 4 items: {'cheese': 1, 'curry': 2, 'soda': 1}
$25, 4 items: {'curry': 1, 'sandwich': 2, 'soup': 1}
$33, 6 items: {'coffee': 1, 'curry': 2, 'sandwich': 2, 'toast': 1}
$45, 8 items: {'cheese': 1, 'curry': 4, 'sandwich': 1, 'soda': 1, 'soup': 1}
$49, 8 items: {'curry': 1, 'sandwich': 5, 'soup': 2}
$99, 15 items: {'coffee': 1, 'curry': 11, 'sandwich': 1, 'toast': 2}
$114, 16 items: {'curry': 14, 'soda': 2}
$199, 28 items: {'cheese': 3, 'curry': 24, 'sandwich': 1}
'''

from functools import lru_cache
def combination_items_ch2(primary_menu, gift_cards):
    
    @lru_cache(None)
    def helper(remaining):
        nonlocal i, primary_menu
        if remaining == 0.00:
            return []
        best_ans = None
        for item, price in primary_menu.items():
            if price <= remaining:
                sub_ans = helper(round(remaining - price, 2))
                if sub_ans is not None and (best_ans is None or len(best_ans) > len(sub_ans) + 1):
                    best_ans = sub_ans + [item]
        return best_ans
    
    answer = []
    for i, price in enumerate(gift_cards):
        answer.append(helper(price))
        print((i, price), answer[-1])
    return answer

print(combination_items_ch2(primary_menu, gift_cards))

