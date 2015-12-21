import fresh_tomatoes
import media

# Six objects of the class movie are created
clueless = media.Movie("Clueless",
                       "A story about a girl who tries to be a matchmaker"
                       "- loosely based on the Jane Austen novel, Emma.",
                       "https://upload.wikimedia.org/wikipedia/en/2/21/"
                       "Clueless.jpg",
                       "https://www.youtube.com/watch?v=yHDcD_xhwAo")

harry_potter = media.Movie("Harry Potter",
                           "A story of a boy who finds out he is a wizard.",
                           "https://upload.wikimedia.org/wikipedia/cy/thumb/"
                           "a/aa/Poster_Harry_Potter_and_the_Philosopher's_S"
                           "tone.jpg/200px-Poster_Harry_Potter_and_the_Philo"
                           "sopher's_Stone.jpg",
                           "https://www.youtube.com/watch?v=8nSdYGuQ6wk")

jab_we_met = media.Movie("Jab We Met",
                         "A story of a man and woman who fall in love while"
                         "traveling together.",
                         "https://upload.wikimedia.org/wikipedia/en/9/9f/"
                         "Jab_We_Met_Poster.jpg",
                         "https://www.youtube.com/watch?v=i7VGyugYCIk")

love_actually = media.Movie("Love Actually",
                            "Many stories of different kinds of love"
                            " culminating on Christmas day.",
                            "https://upload.wikimedia.org/wikipedia/en/e/eb/"
                            "Love_Actually_movie.jpg",
                            "https://www.youtube.com/watch?v=KdzH6a-XEGM")

buffy = media.Movie("Buffy the Vampire Slayer",
                    "A story of a high school girl who slays vampires.",
                    "http://static.comicvine.com/uploads/scale_small/2/29350/"
                    "874919-buffy_the_vampire_slayer_ver2.jpg",
                    "https://www.youtube.com/watch?v=5fBDiiJT4ck")

beauty_and_the_beast = media.Movie("Beauty and the Beast",
                                   "A story of a girl who learns to love a"
                                   "beast",
                                   "https://upload.wikimedia.org/wikipedia/en/"
                                   "7/7c/Beautybeastposter.jpg",
                                   "https://www.youtube.com/watch?v=tRlzmyve"
                                   "DHE")

# Creating the array movies that accepts the six Movie() objects
movies = [clueless, harry_potter, jab_we_met, love_actually, buffy,
          beauty_and_the_beast]

# Generate the html and open the page fresh_tomatoes.html to display movies
fresh_tomatoes.open_movies_page(movies)
