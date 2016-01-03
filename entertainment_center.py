# importing fresh_tomatoes functionality
import fresh_tomatoes

# imports Class made previously to facilitate this project
import media


# Adding each instance and the instance variable that go with each

holy_grail = media.Movie("Monty Python and the Holy Grail",
                         "You are a very silly person if you don't agree"
                         " this is the greatest movie ever made.",
                         "http://www.stonelibertystation.com/wp-content/uploads/2013/07/monty-python-and-the-holy-grail-poster-artwork-terry-gilliam-eric-idle-graham-chapman.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=urRkGvhXc8w",
# added another instance variable for additional comments
                         "1975 - Directed by Gilliam and Jones. Written by and starring: Chapman, Cleese, Idle, Gilliam, Jones, Palin")  # NOQA

watchmen = media.Movie("The Watchmen",
                        "Steam punk superheroes...",
                        "http://www.watchmencomicmovie.com/posters/watchmen-theatrical-poster-big.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=ONQ3Zgy195Y",
                       "2009 - Directed by Jack Snyder.")

star_wars = media.Movie("Star Wars",
                        "Cowboys in space.",
                        "http://cdn.akihabaranews.com/sites/default/files/star_wars_a_new_hope_japanese_poster.2.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=1g3_CFmnU7k",
                        "1977 - Directed by He Who Must Not Be Named.")

pulp_fiction = media.Movie("Pulp Fiction",
                           "One of my all-time favorites",
                           "https://s-media-cache-ak0.pinimg.com/236x/8a/50/82/8a5082e4da061a777a32c9ffaa6d542a.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=ewlwcEBTvcg",
                           "1994 - Directed by Quentin Tarantino.")


# creating a list of movies to be included when page is opened
movies = [holy_grail, watchmen, pulp_fiction, star_wars]

# initiates the web page
fresh_tomatoes.open_movies_page(movies)
