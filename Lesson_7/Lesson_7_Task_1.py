'''ask 1
A simple function.

Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
The function should then print “My favorite movie is named {name}”.'''


def favorite_movie(movie_name, *args):      # *args was added to exclude chances for error if args > 1
    print(f'My favourite movie is named "{movie_name}".')

# So now function can be called with input value.
movie_1 = input('What\'s your favourite movie? ')
favorite_movie(movie_1)

# Or it can utilize stored variable as well.
movie_2 = 'Pulp Fiction'
favorite_movie(movie_2)

# Also you can call this function without any variable at all.
favorite_movie('American History X')

# Somebody made a mistake and put 2 arguments, but it doesn't cause an error, thanks to *args
favorite_movie('Whiplash', '8 Mile')