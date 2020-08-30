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
    def __init__(self, category, type, name, price, ):
        self.category = category
        self.type = type
        self.name = name
        self.price = price
    # It gives output like "Chips Lays" to save it do dics in key: value pairs for quantities support.
    def __repr__(self):
        return f"{self.type} {self.name}"



class Store():
    def __init__(self, inv='', income=0):
        self.inv = inv
        self.income = income
        self.set_inventory_info()

    def get_income(self):
        print(f'Total budget: ${self.income}')

    # This function will print the simplest inventory from a Dictionary.
    def stock(self):
        print('\nWe have following products in the stock:')
        for k, v in self.inv.items():
            print(f"\t\t* {k}: {v} pcs")

    # In my concept, Product is some info from Supplier, but for our database we need extra pieces of information,
    # like Quantity and Total Cost. Supplier gives us price only.
    # So we need a method which will be making our shop description.
    def set_item_description(self, item):
        item.description = f'''\
{'_' * 30}
Category:   {item.category}
Type:       {item.type}
Name:       {item.name}
Price:      ${item.price}
Q-ty:       {item.qty} pcs
TTL Cost:   ${item.price * item.qty}'''
        return item.description

    # This method is setting OUR description for every item.
    def set_inventory_info(self):
        for item in self.inv:
            item.qty = 0
            for k, v in self.inv.items():
                if item == k:
                    item.qty = self.inv[item]
            item.description = self.set_item_description(item)

    def get_product_info(self, product_name):
        print(product_name.description)

    # This will print any item, if quantity of that item is more than 0. So it is our Current Inventory
    def get_all_products(self):
        for item in self.inv:
            if item.qty > 0:
                print(item.description)

    # I made it possible to call this method without any variables, to add something with user input,
    # or coder may pass a product name or quantity. Also, discount from supplier can be changed.
    def add_item(self, new_product='', quantity=0, price_premium=30):
        if not new_product and not quantity:
            print('\nWhat item do you want to add?')
            category = input('Enter category: ')
            type = input('Enter type: ')
            name = input('Enter name: ')
            price = int(input('Enter price: ')) * ((100 - price_premium) / 100) # Discount from supplier applied.
            quantity = int(input('Enter q-ty: '))
            new_product = Product(category, type, name, price) # Instance of new product created.
        elif not quantity:
            print(f'\nOkay, how many "{new_product}" have we received? ')
            quantity = int(input('Enter q-ty: '))
        # Now we have to deduct from our income, to "buy" a product,
        # but first, needed to check if there is enough money to buy.
        deal_cost = new_product.price * quantity
        if self.income >= deal_cost:
            self.income -= deal_cost  # And deduct money.
            # If deal was successful, amount should be changed.
            try:
                new_product.qty = quantity + inv[new_product]  # We add previous q-ty + new q-ty and save it in attribute.
            except KeyError:
                new_product.qty = quantity  # If it is completely new item, there was no Dict value for it.
            inv[new_product] = new_product.qty  # And then we re-assign it into our dictionary value
            self.set_inventory_info()   # Save changes to the description and quantities.
            print(f'''\n\
    {quantity} pieces of "{new_product.name}" was bought for total ${deal_cost},
    with discount of {price_premium}%.
    Product "{new_product}" was successfully added / amended in the category "{new_product.category}".
    Total there is {new_product.qty} pcs of "{new_product.name}" now.''')
            return new_product      # It should be returned. You should call method like that: <nutella = self.add_item()>
        # If money balance isnot sufficient, deal will not be closed.
        elif self.income < deal_cost:
            print('Sorry, you don\'t have sufficient money to close the deal!')

    def item_search(self, identifier='', identifier_type='name'):
        i = 0
        if not identifier:
            identifier_type = input("Enter what you will be looking for ('category', 'type' or 'name'): ").lower()
            identifier = input('Enter what you wish to find: ').lower()

        if identifier_type == 'name':
            for item in self.inv:
                if item.name.lower() == identifier:
                    item.price = item.price * ((100 - percent) / 100)
                    i += 1
                    print(f'Price of "{item}" was discounted by {percent}% and set to ${item.price}')
        elif identifier_type == 'type':
            for item in self.inv:
                if item.type.lower() == identifier:
                    item.price = item.price * ((100 - percent) / 100)
                    i += 1
                    print(f'Price of "{item}" was discounted by {percent}% and set to ${item.price}')
        elif identifier_type == 'category':
            for item in self.inv:
                if item.category.lower() == identifier:
                    item.price = item.price * ((100 - percent) / 100)
                    i += 1
                    print(f'Price of "{item}" was discounted by {percent}% and set to ${item.price}')
        if i < 1:
            print(f'Sorry, "{identifier}" was not found in "{identifier_type}". Try again. ')



    def sell_product(self, sold_product='', quantity=1):   # If not specified, at least 1 item will be sold.
        if sold_product.qty >= quantity:
            inv[sold_product] -= quantity
            sold_product.qty -= quantity
            self.set_inventory_info()       # Again we always have to re-assign descriptions.
            print(f'\nProduct was sold and now there is {inv[sold_product]} of "{sold_product.name}" in stock.')
            self.income = self.income + sold_product.price * quantity   # and + to income
        elif sold_product.qty < quantity:
            print(f'Sorry, seems like you don\'t have enough {sold_product} to sell.')

    def remove_spoiled_product(self, spoiled_product, quantity=1):   # If not specified, at least 1 item will be removed.
        if spoiled_product.qty >= quantity:
            inv[spoiled_product] -= quantity
            spoiled_product.qty -= quantity
            self.set_inventory_info()       # Again we always have to re-assign descriptions.
            print(f'\nProduct was spoiled and removed. Now there is {inv[spoiled_product]} of "{spoiled_product.name}" in stock.')
        elif spoiled_product.qty < quantity:
            print(f'Sorry, seems like you don\'t have enough {spoiled_product} to sell.')

    def set_discount(self, identifier='', percent=0, identifier_type='name'):
        i = 0
        if not identifier and not percent:
            identifier_type = input("Enter what you will be looking for ('category', 'type' or 'name'): ").lower()
            identifier = input('Enter what you wish to find: ').lower()
            percent = int(input('Enter the % of discount on this product: '))
        elif not percent:
            percent = int(input('Enter the % of discount on this product: '))
        if identifier_type == 'name':
            for item in self.inv:
                if item.name.lower() == identifier:
                    item.price = item.price * ((100 - percent) / 100)
                    i += 1
                    print(f'Price of "{item}" was discounted by {percent}% and set to ${item.price}')
        elif identifier_type == 'type':
            for item in self.inv:
                if item.type.lower() == identifier:
                    item.price = item.price * ((100 - percent) / 100)
                    i += 1
                    print(f'Price of "{item}" was discounted by {percent}% and set to ${item.price}')
        elif identifier_type == 'category':
            for item in self.inv:
                if item.category.lower() == identifier:
                    item.price = item.price * ((100 - percent) / 100)
                    i += 1
                    print(f'Price of "{item}" was discounted by {percent}% and set to ${item.price}')
        if i < 1:
            print(f'Sorry, "{identifier}" was not found in "{identifier_type}". Try again. ')




# Creating class instances
milk = Product('Dairy', 'Milk', 'Mlekovita', 1.25)
cheese = Product('Dairy', 'Cheese', 'Komo', 3.75)
pringles = Product('Snacks', 'Chips', 'Pringles', 1.99)
lays = Product('Snacks', 'Chips', 'Lays', 1.49)

# Now we receive some products into our store (product_name = quantity)
inv[milk] = 10
inv[cheese] = 27
inv[lays] = 2

# Creating instance of Store Class with $2.5M)
metro = Store(inv, 2500000)
# metro.set_inventory_info()
# Quick-check of inventory
metro.stock()
metro.get_all_products()

# Now I will demonstrate adding of items.
# Pre-created Product may be added or updated. "Lays" instance of Product was created before, quantity was 2,
# and it will be updated.
metro.add_item(lays)
# Also, "Pringles" object was created, but quantity was 0, but it will be added in same way.
metro.add_item(pringles)
# Then, we can create new product using this method, no need to make instance of Product before.
nutella = metro.add_item()
# And we can simply add more to any product, without any extra input questions.
metro.add_item(nutella, 2)
# Now we will check if all inventory is updated correctly.
metro.get_all_products()



user=True
while user:
    print("1. Add to home inventory")
    print("2. Remove home from inventory")
    print("3. Update sale status")
    print("4. View inventory")
    print("5. Exit program")
    user_wants=input("What would you like to do today?")
    if user_wants=="1":
        metro.add_item()
        metro.stock()
    elif user_wants=="2":
        Home_Inventory.delete_home(input)
    elif user_wants=="3":
        Home_Inventory.sale_status(input)
    elif user_wants=="4":
        ProductStore.stock(stock_items)
        # print(stock_items)
    elif user_wants=="5":
        print("\n Thank you for using home invertory.")
        break
    elif user_wants!="":
        print("\n Input not understood. Please try again.")







# print(milk.qty)
# print(cheese.qty)
# print(milk.description)
# metro.set_discount()
# metro.get_income()

# metro.add_item()


# metro.sell_product(nutella, 10)
# print(nutella)
# print(nutella.price)
# print(nutella.id)
# metro.stock()

# metro.stock()
# print(milk)



# metro.get_product_info(milk)
# metro.get_all_products()

# metro.get_all_products()
# metro.stock()
# metro.sell_product(milk, 10)


# print(lays.description)
# print(lays.qty)
# metro.stock()
# metro.get_product_info(milk)













# float prices, discount test,


# def sell_product(self, sold_product, quantity=1):  # If not specified, at least 1 item will be sold.
#     if sold_product.qty >= quantity:
#         inv[sold_product] -= quantity
#         sold_product.qty -= quantity
#         self.set_inventory_info()  # Again we always have to re-assign descriptions.
#         print(f'\nProduct was sold and now there is {inv[sold_product]} of "{sold_product.name}" in stock.')
#         self.income = self.income + sold_product.price * quantity  # and + to income
#     elif sold_product.qty < quantity:
#         print(f'Sorry, seems like you don\'t have enough {sold_product} to sell.')
#
#
# def remove_spoiled_product(self, spoiled_product, quantity=1):  # If not specified, at least 1 item will be removed.
#     if spoiled_product.qty >= quantity:
#         inv[spoiled_product] -= quantity
#         spoiled_product.qty -= quantity
#         self.set_inventory_info()  # Again we always have to re-assign descriptions.
#         print(
#             f'\nProduct was spoiled and removed. Now there is {inv[spoiled_product]} of "{spoiled_product.name}" in stock.')
#     elif spoiled_product.qty < quantity:
#         print(f'Sorry, seems like you don\'t have enough {spoiled_product} to sell.')

# {[v for k, v in self.inv.items() if item == k]}''')



#
#     def get_product_info(self, product_name):
#         # if product_name in self.inv.items():
#         #     print(f'Here is what we have on {product_name}:')
#         for item in self.inv:
#             for k, v in self.inv.items():
#                 if k == product_name:
#                     print('_' * 30)
#                     print(f'''\
# Category:   {item.category}
# Type:       {item.type}
# Name:       {item.name}
# Price:      ${item.price}''')




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