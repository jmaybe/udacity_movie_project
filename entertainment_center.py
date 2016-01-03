# importing fresh_tomatoes functionality
# fresh_tomatoes executes the actual visual presentation of our code.
import fresh_tomatoes

""" Imports class media.py made previously to facilitate this project
by importing this module we are able to employ the class .movie and its
constuctor that gives us the ability to add our specific instance variables for
each movie
"""

import media


""" Adding each instance (media.x) and the instance variables (self.x)
that go with each. One can change the order up for the instances, but not the
instance variables (Technically, you can change the order, but it would not
make any sense as the order is predicated on the constructor that was created
in media.py) Each instance variable from the constructor is listed as a comment.

"""
holy_grail = media.Movie("Monty Python and the Holy Grail",  # movie_title
                         "You are a very silly person if you don't agree this is the greatest movie ever made.",  # NOQA  (also movie_storyline)
                         "http://www.stonelibertystation.com/wp-content/uploads/2013/07/monty-python-and-the-holy-grail-poster-artwork-terry-gilliam-eric-idle-graham-chapman.jpg",  # NOQA (also movie_poster)
                         "https://www.youtube.com/watch?v=urRkGvhXc8w",  # movie_trailer
                         "1975 - Directed by Gilliam and Jones",  # movie_comments
                         "Fresh Tomato score: 97%")  # movie_rating

watchmen = media.Movie("The Watchmen",  # movie_title
                        "Steam punk superheroes...",  # movie_storyline
                        "http://www.watchmencomicmovie.com/posters/watchmen-theatrical-poster-big.jpg",  # NOQA (also movie_poster)
                        "https://www.youtube.com/watch?v=ONQ3Zgy195Y",  # movie_trailer
                       "2009 - Directed by Jack Snyder.",  # movie_comments
                       "Fresh Tomato Score: 92%")  # movie_rating

star_wars = media.Movie("Star Wars",  # movie_title
                        "Cowboys in space.",  # movie_storyline
                        "http://cdn.akihabaranews.com/sites/default/files/star_wars_a_new_hope_japanese_poster.2.jpg",  # NOQA (also movie_poster)
                        "https://www.youtube.com/watch?v=1g3_CFmnU7k",  # movie_trailer
                        "1977 - Directed by He-who-must-not-be-named.",  # movie_comments
                        "Fresh Tomato score: (1977) 100% | (2015) 95%")  # movie_rating

pulp_fiction = media.Movie("Pulp Fiction",  # movie_title
                           "One of my all-time favorites",  # movie_storyline
                           "https://s-media-cache-ak0.pinimg.com/236x/8a/50/82/8a5082e4da061a777a32c9ffaa6d542a.jpg",  # NOQA (movie_poster)
                           "https://www.youtube.com/watch?v=ewlwcEBTvcg",  # movie_trailer
                           "1994 - Directed by Quentin Tarantino.",  # movie_comments
                           "Fresh Tomato score: 93%")  # movie_rating


"""Here we are creating a list of movies to streamline our opening them in a
later statement. By making a list of objects it will be possible to change the
listed items here rather than in our later statment.
"""

movies = [holy_grail, watchmen, pulp_fiction, star_wars]

# initiates the web page
fresh_tomatoes.open_movies_page(movies)
