'''Task 2
Create a function which takes as input two dicts with structure mentioned below,
then computes and returns the total price of stock.'''

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

def total_stock_price(stock, prices):
    for item in stock:
        if stock[item] > 0:
            print(f"Total Price of {item.capitalize()} stock is {str(stock[item] * prices[item])} UAH")
        else:
            print(f'Total Price of {item.capitalize()}s is unavailable because current amount is Zero (0).')

total_stock_price(stock, prices)
