'''Task 2
Creating a dictionary.

Create a function called make_country, which takes in a country’s name and capital as parameters.
Then create a dictionary from those parameters, with ‘name’ and ‘capital’ as keys.
Make the function print out the values of the dictionary to make sure that it works as intended.'''

print()

def make_country(country_name, capital_name, *args):
    if str(country_name).isalpha() and str(capital_name).isalpha():
        country_dict = {'name' : country_name.capitalize(), 'capital' : capital_name.capitalize()}
        print(country_dict)
        print(f'The capital of {country_name.capitalize()} is {capital_name.capitalize()}.\n')
    else:
        print('Sorry, only alphabetical letters are used for naming of countries and their capitals on planet Earth.')
        print(f'Country {country_name} with capital {capital_name} can\'t be added to database.\n')

# It can also be called with variables,
name_of_country = 'canada'
capital_of_country = 'ottawa'
make_country(name_of_country, capital_of_country)

# Or with any strings.
make_country('PoLaNd', 'WaRsAw')

# And it can also handle errors with extra arguments. Only first two will be used in this case.
make_country('Ukraine', 'Kyiv', 'Dnipro')

# Also, it doesn't take incorrect input, giving an extra message.
make_country('Betelgeuse-42', '2932482784')
make_country(3242, 234235)