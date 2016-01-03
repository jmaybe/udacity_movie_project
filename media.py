# imports module (or functionality) of webbrowser
import webbrowser

# creating a class that will be used in another program
class Movie():
    
    # This is the constructor that provides the foundation for the instances and
    # their variables to come
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_comments):

        # These are instance variables. They can be whatever we want them to be, but
        # must match in number and order when creating the Instance.
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.comments = movie_comments

    # This is the Instance Method
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
