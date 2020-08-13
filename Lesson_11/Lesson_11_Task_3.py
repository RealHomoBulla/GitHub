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
            price = float(input('Enter price: ')) * ((100 - price_premium) / 100) # Discount from supplier applied.
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
            print(f'\nSorry, you don\'t have sufficient money to close the deal of buying {quantity} of "{new_product}"!')

    def item_search(self, identifier='', identifier_type='name'):
        i = 0
        result = []
        if not identifier:
            identifier_type = input("Enter what you will be looking for (Enter 'c' for Category, 't' for Type or 'n' for Name): ").lower()
            identifier = input('Enter what you wish to find: ').lower()
            print()
        if identifier_type == 'n':
            for item in self.inv:
                if item.name.lower() == identifier:
                    result.append(item)
                    i += 1
                    print(f'Found "{item.name}" in category "{item.category}".')
        elif identifier_type == 't':
            for item in self.inv:
                if item.type.lower() == identifier:
                    result.append(item)
                    i += 1
                    print(f'Found "{item.name}" in category "{item.type}".')
        elif identifier_type == 'c':
            for item in self.inv:
                if item.category.lower() == identifier:
                    result.append(item)
                    i += 1
                    print(f'Found "{item.name}" in category "{item.category}".')
        if i < 1:
            print(f'Sorry, "{identifier}" was not found in "{identifier_type}". Try again. ')
        return result

    def sell_product(self, sold_product='', quantity=1):   # If not specified, at least 1 item will be sold.
        products = []
        print('\nWe are going to sell now...')
        if sold_product:
            products.append(sold_product)
        if not sold_product:
            products = self.item_search()
        for item in products:
            if quantity <= 1:
                quantity = int(input(f'\nHow many "{item.name}" have you sold? '))
            if item.qty >= quantity:
                inv[item] -= quantity
                item.qty -= quantity
                self.set_inventory_info()       # Again we always have to re-assign descriptions.
                print(f'\nProduct was sold and now there is {inv[item]} of "{item.name}" in stock.')
                self.income = self.income + item.price * quantity   # and + to income
            elif item.qty < quantity:
                print(f'\nSorry, seems like you don\'t have enough "{item}" to sell.')
                decision = input('Do you wish to sell it all? [Y/N]: ').lower()
                if decision == 'y':
                    quantity = item.qty
                    self.income = self.income + item.price * item.qty
                    item.qty = 0
                    inv[item] = 0
                    self.set_inventory_info()
                    print(f'\nEverything was sold and now there is {inv[item]} "{item.name}" in stock.')
                if decision == 'n':
                    continue
            quantity = 0

    def remove_spoiled_product(self, spoiled_product='', quantity=1):   # If not specified, at least 1 item will be removed.
        products = []
        print('\nNow we are going to throw something...')
        if spoiled_product:
            products.append(spoiled_product)
        if not spoiled_product:
            products = self.item_search()
        for item in products:
            if quantity <= 1:
                quantity = int(input(f'\nHow many "{item.name}" have you spoiled and have to be thrown away? '))
            if item.qty >= quantity:
                inv[item] -= quantity
                item.qty -= quantity
                self.set_inventory_info()       # Again we always have to re-assign descriptions.
                print(f'\nProduct was spoiled and removed. Now there is {inv[item]} of "{item.name}" in stock.')
            elif item.qty < quantity:
                print(f'\nSorry, seems like you don\'t have enough "{item}" to throw away.')
                decision = input('Do you wish to throw it all away? [Y/N]: ').lower()
                if decision == 'y':
                    quantity = item.qty
                    item.qty = 0
                    inv[item] = 0
                    self.set_inventory_info()
                    print(f'\nEverything was thrown away and now there is {inv[item]} "{item.name}" in stock.')
                if decision == 'n':
                    continue
            quantity = 0

    def set_discount(self, discount_product='', percent=0):
        products = []
        print('\nWe are going to apply discount on something...')
        if discount_product:
            products.append(discount_product)
        if not discount_product:
            products = self.item_search()
        for item in products:
            if not percent:
                percent = int(input(f'\nEnter the % of discount on "{item}": '))
            if percent > 100:
                print('It is impossible to have a discount over 100%!')
                continue
            item.price = item.price * ((100 - percent) / 100)
            self.set_inventory_info()
            print(f'\nPrice of "{item}" was discounted by {percent}% and set to ${item.price}')
            percent = 0


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
metro = Store(inv, 25000)
# metro.set_inventory_info()
# Quick-check of inventory
metro.stock()
metro.get_all_products()

# Now I will demonstrate adding of items.
# Pre-created Product may be added or updated. "Lays" instance of Product was created before, quantity was 2,
# and it will be updated.
metro.add_item(lays)
# Also, "Pringles" object was created, but quantity was 0, but it will be added in same way.
# You can type quantity directly when calling the method.
metro.add_item(pringles, 50)
# Then, we can create new product using this method, no need to make instance of Product before.
nutella = metro.add_item()
# And we can simply add more to any product, without any extra input questions.
metro.add_item(nutella, 2)
# Also, if you try to go over Money limit of the store, product can't be bought and special message will be displayed.
metro.add_item(lays, 100500)

metro.get_all_products()            # Now we will check if all inventory is updated correctly.

# Same works for the selling function or removing function (if product was spoiled). You may call it without any
# argument and "search" will be conducted. Or you can directly pass product and quantity.

# Selling:
metro.sell_product()
metro.sell_product(nutella)
metro.sell_product(lays, 10)
# If you sell more than you have, you will see the message, suggesting to sell all available amount,
# but not more than you have. Same for removing
metro.sell_product(lays, 100500)

# Removing:
metro.remove_spoiled_product()
metro.remove_spoiled_product(nutella)
metro.remove_spoiled_product(lays, 10)

# Discounting:
metro.set_discount()
metro.set_discount(nutella)
metro.set_discount(lays, 10)
metro.set_discount(lays, 200)       # You can't set discount more than 100%, obviously.

# Searching
metro.item_search()                 # Searching can be started like this
metro.item_search('dairy', 'c')     # or like This

# Information
metro.get_all_products()            # Information can be received this way:
metro.get_product_info(milk)        # or this way
metro.stock()                       # or like this
metro.get_income()                  # Balance display.
