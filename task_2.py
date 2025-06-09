class Movies:
    def __init__(self, movies):
        movies = []
        self.movies = movies

    def add_movie(self, movie):
        self.movies.append(movie) 
        
class Comedy(Movies):
    def __init__(self, movies=None):
        super().__init__(movies)

class Drama(Movies):
    def __init__(self, movies=None):
        super().__init__(movies)

comedy = Comedy()
comedy.add_movie('Большой куш')
print(comedy.movies)

drama = Drama()
drama.add_movie('Оружейный барон')
print(drama.movies)