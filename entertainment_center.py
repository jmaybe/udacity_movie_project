import fresh_tomatoes
import media



holy_grail = media.Movie("Monty Python and the Holy Grail",
                         "The greatest movie ever made",
                         "http://www.stonelibertystation.com/wp-content/uploads/2013/07/monty-python-and-the-holy-grail-poster-artwork-terry-gilliam-eric-idle-graham-chapman.jpg",
                         "https://www.youtube.com/watch?v=urRkGvhXc8w")

watchmen = media.Movie("The Watchmen",
                        "Steam punk superheroes...",
                        "http://www.watchmencomicmovie.com/posters/watchmen-theatrical-poster-big.jpg",
                        "https://www.youtube.com/watch?v=ONQ3Zgy195Y")

star_wars = media.Movie("Star Wars",
                        "Cowboys in space",
                        "http://cdn.akihabaranews.com/sites/default/files/star_wars_a_new_hope_japanese_poster.2.jpg",
                        "https://www.youtube.com/watch?v=1g3_CFmnU7k")

pulp_fiction = media.Movie("Pulp Fiction",
                           "Love it",
                           "https://s-media-cache-ak0.pinimg.com/236x/8a/50/82/8a5082e4da061a777a32c9ffaa6d542a.jpg",
                           "https://www.youtube.com/watch?v=ewlwcEBTvcg")


movies = [holy_grail, watchmen, pulp_fiction, star_wars]

fresh_tomatoes.open_movies_page(movies)
