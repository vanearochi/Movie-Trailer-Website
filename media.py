

class Movie():
    """
    Represents a movie
    """

    #Define Movie Class variables.
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_director, wikipedia_link,
                 movie_writer, movie_cast, movie_genres, movie_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = movie_director
        self.wikipedia_url = wikipedia_link
        self.writer = movie_writer
        self.main_cast = movie_cast
        self.genres = movie_genres
        self.rating = movie_rating




