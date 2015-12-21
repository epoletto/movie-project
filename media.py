import webbrowser


# Movie() class is defined
class Movie():

    # Constructor for class, Movie() accepts four arguments
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Function show_trailer opens the the trailer for a movie in
    # the web browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
