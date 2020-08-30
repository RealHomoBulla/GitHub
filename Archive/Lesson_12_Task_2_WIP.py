'''Task 2
Library
Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []'''



class Library:
    def __init__(self, name, books, authors):
        self.name = name
        self.books = books
        self.authors = authors

    #TODO: finish this class
    def __str__(self):
        pass
    def __init__(self):
        pass

    def add_new_book(self, new_book=None):
        print('You are going to add the book.')
        if not new_book:
            new_book = self.create_new_book()
        self.books.append(new_book)
        return new_book

    def create_new_book(self, author=None):
        if not author:
            author_input = input('Author: ')
            if author_input not in str(self.authors):
                print('Seems this is a new author. Let\'s fill some information about him...')
                author = self.create_new_author()
            else:
                author = self.get_the_author(author_input)
            print(author.books)

        name = input('Name: ')
        year = int(input('Year: '))
        genre = input('Genre: ')
        new_book = Book(name, year, genre, author)
        return new_book

    def create_new_author(self):
        author_name = input('Author Name: ')
        author_country = input('Author Country: ')
        author_birthday = input('Author Birthday: ')
        author = Author(author_name, author_country, author_birthday, [])
        self.authors.append(author)
        return author

    def get_the_author(self, author_input):
        for a in range(len(self.authors)):
            if getattr(self.authors[a], 'name', 'Default') == author_input:
                return self.authors[a]

    # returns a list of all books grouped by the specified author
    def group_by_author(self, author):
        return [book for book in author.books if book in self.books]

    # returns a list of all the books grouped by the specified year
    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]




class Author:

    def __init__(self, name, country, birthday, books):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'''
Name:           {self.name}
From:           {self.country}
D.O.B.:         {self.birthday}
Bibliography: 
{self.books}
'''


class Book:
    def __init__(self, name, year, genre, author=None):
        self.name = name
        self.year = year
        self.genre = genre
        self.author = author
        self.author.books.append(self)
    def __repr__(self):
        return f'"{self.name}", {self.year}'
    def __str__(self):
        pass
    #TODO: Finish __REPR__



sir_terry_pratchett = Author('Sir Terry Pratchett', 'United Kingdom', '28 April', [])
color_of_magic = Book('Colour of Magic, The', 1983, 'Fantasy', sir_terry_pratchett)
light_fantastic = Book('Light Fantastic, The', 1986, 'Fantasy', sir_terry_pratchett)
equal_rites = Book('Equal Rites', 1987, 'Fantasy', sir_terry_pratchett)
mort = Book('Mort', 1987, 'Fantasy', sir_terry_pratchett)

mark_twain = Author('Mark Twain', 'USA', '30 November', [])
adventures_of_tom_sawyer = Book('Adventure of Tom Sawyer, The', 1876, 'Novel', mark_twain)
adventures_of_huckleberry_finn = Book('Adventures of Huckleberry Finn', 1885, 'Novel', mark_twain)
connecticut_yankee = Book('A Connecticut Yankee in King Arthur\'s Court', 1889, 'Fantasy', mark_twain)

mikhail_bulgakov = Author('Mikhail Bulgakov', 'USSR', '15 May', [])
white_guard = Book('White Guard, The', 1926, 'Novel', mikhail_bulgakov)
master_and_margarita = Book('The Master and Margarita', 1967, 'Fantasy', mikhail_bulgakov)



some_lib = Library('Odessa National Library', [color_of_magic, equal_rites, mort, adventures_of_huckleberry_finn, white_guard, master_and_margarita], [sir_terry_pratchett, mark_twain, mikhail_bulgakov])
# print(some_lib.authors[0].books)





# some_lib.add_new_book()

# print(some_lib.books)
# print(some_lib.authors)
print(some_lib.group_by_author(sir_terry_pratchett))
print(some_lib.group_by_year(1987))

print()
# print(sir_terry_pratchett.books)
# print(sir_terry_pratchett)
# print(mark_twain)
# print(mikhail_bulgakov)


# print(the_color_of_magic.author.books)




    # def add_book(self):
    #     self.books.append(self.)

