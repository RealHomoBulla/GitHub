'''Task 3
Product Store
Write a class Product that has three attributes: (type, name, price)
Then create a class ProductStore, which will have some Products and will operate with all products in the store.
All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
Tips: Use aggregation/composition concepts while implementing the ProductStore class.
You can also implement additional classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:
add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified
by input identifiers (type or name). The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the store if available,
in other case raises an error. It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store.'''

inv = {}

class Product:
    def __init__(self, category, type, name, price):
        self.category = category
        self.type = type
        self.name = name
        self.price = price
        self.id = len(inv)+ 1
    def __repr__(self):
        return f"{self.type} {self.name}"

class Store():
    def __init__(self, inv='', money=0):
        self.inv = inv
        self.money = money
    def stock(self):
        print('We have following products in the stock:')
        for k, v in self.inv.items():
            print(f"{k}: {v}")
    def add_item(self, new_product='', quantity=0, price_premium=30):
        if not new_product and not quantity:
            category = input('Enter category: ')
            type = input('Enter type: ')
            name = input('Enter name: ')
            price = int(input('Enter price: ')) * ((100 - price_premium) / 100)
            quantity = int(input('Enter q-ty: '))
        elif not quantity:
            print(f'Okay, how many "{new_product} do we have? ')
            quantity = input('Enter q-ty: ')
        deal_cost = price * quantity
        self.money -= deal_cost
        new_product = Product(category, type, name, price)
        inv[new_product] = quantity
        print(f'''{quantity} pieces of "{new_product.name}" was bought for total ${deal_cost},
with discount of {price_premium}%.
Product "{new_product}" was successfully added to category "{new_product.category}".
Total budget: ${self.money}''')
        return new_product

    def sell_product(self, sold_product, quantity=1):
        inv[sold_product] -= quantity
        print(f'Product was sold and now there is {inv[sold_product]} in stock')
        self.money = self.money + sold_product.price * quantity
        print(f'Total $ = {self.money}')




milk = Product('Dairy', 'Milk', 'Mlekovita', 1.25)
cheese = Product('Dairy', 'Cheese', 'Komo', 3.75)
pringles = Product('Snacks', 'Chips', 'Pringles', 1.99)
lays = Product('Snacks', 'Chips', 'Lays', 1.49)

inv[milk] = 10
inv[cheese] = 27
print(inv)

metro = Store(inv, 100000)
metro.stock()

nutella = metro.add_item()
print(nutella)
print(nutella.price)
print(nutella.id)
metro.stock()
metro.sell_product(nutella, 5)
metro.stock()

















    # def __str__(self):
    #     out = '\t'.join(['Type', 'Name', 'Price', 'Q-ty'])
    #     for item in self.items.values():
    #         out += '\n' + '\t'.join([str(x) for x in [item.type, item.name, item.price, item.quantity]])
    #     return out




# inventory = Inventory()
# inventory.add_item(Product('Dairy', 'Milk', 1.25, 10))
# inventory.add_item(Product('Dairy', 'Cheese', 3.40, ))
# print(inventory)



# inventory = {'Sword': {'attack': 5, 'defence': 1,
#                        'weight': 15, 'price': 2},
#              'Armor': {'attack': 0, 'defence': 10,
#                        'weight': 25, 'price': 5}}


# class ProductStore:
#     def __init__(self, stock_items):
#         self.stock_items = stock_items
#     def add_product(self):
#         type = input("Enter type: ")
#         name = input("Enter name: ")
#         price = input("Enter price: ")
#         quantity = input("Enter quantity: ")
#         new_product = Product(type, name, price)
#         stock_items = {new_product : quantity}
#         print('Product added successfully.')
#         return stock_items
#
#     def stock(self):
#         print('We have following products in the stock:')
#         for k,v in self.stock_items:
#             print(k, v)
#
#
# milk = Product('diary', 'Mlekovita', 1.25)

    #
    # def delete_home(self):
    #     delete = input("What is the full address of the home you want to delete?: ")
    #     if delete in Allhomes.keys():
    #         del[delete]
    #         print("The home entered has been deleted.")
    #     else:
    #         print("Address not found")
    #
    #
    # def sale_status(self):
    #     update = input("What is the full address of the home you want to update?:")
    #     if update in Allhomes.keys():
    #         pass
    #     else:
    #         print("Address not found")
    #

# user=True
# while user:
#     print("1. Add to home inventory")
#     print("2. Remove home from inventory")
#     print("3. Update sale status")
#     print("4. View inventory")
#     print("5. Exit program")
#     user_wants=input("What would you like to do today?")
#     if user_wants=="1":
#         ProductStore.add_product(input)
#         print(stock_items)
#     elif user_wants=="2":
#         Home_Inventory.delete_home(input)
#     elif user_wants=="3":
#         Home_Inventory.sale_status(input)
#     elif user_wants=="4":
#         ProductStore.stock(stock_items)
#         # print(stock_items)
#     elif user_wants=="5":
#         print("\n Thank you for using home invertory.")
#         break
#     elif user_wants!="":
#         print("\n Input not understood. Please try again.")