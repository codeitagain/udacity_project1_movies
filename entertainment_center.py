""" The entertainment_center.py is the executable file for a Python
program that displays in a Web browser a list of favorite movies,
including each movie's title, poster, and trailer. This file also
contains all the data stored and used for each movie identified
in this project. """

import fresh_tomatoes
import media

# List of movies begins here.
resident_evil_1 = media.Movie("Resident Evil",
                        "A deadly virus may be released upon the world if an elite military team is unable to break into the secret complex of an evil corporation set out to achieve world domination.",
                        "https://upload.wikimedia.org/wikipedia/en/a/a1/Resident_evil_ver4.jpg",
                        "https://www.youtube.com/watch?v=lBxjZahSN7o")

underworld = media.Movie("Underworld",
                         "A beautiful vampire warrior, is entrenched in a war between the vampire and werewolf races.",
                         "https://upload.wikimedia.org/wikipedia/en/c/cc/Underworld_%282003_film%29_poster.jpg",
                         "https://www.youtube.com/watch?v=MqT-e44kIM8")

star_wars = media.Movie("Star Wars",
                        "Star Wars is a 1977 American epic space opera film written and directed by George Lucas.",
                        "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                        "https://www.youtube.com/watch?v=K8AD7wzsPFQ")

star_trek = media.Movie("Star Trek",
                        "Storyline",
                        "https://upload.wikimedia.org/wikipedia/en/d/df/Star_Trek_The_Motion_Picture_poster.png",
                        "https://www.youtube.com/watch?v=g0-7Z2lYII8")

wizard_of_oz = media.Movie("Wizard of Oz",
                           "A tornado wisks Dorothy and her dog, Toto, to the magical land of Oz.",
                           "https://upload.wikimedia.org/wikipedia/commons/c/ca/WIZARD_OF_OZ_ORIGINAL_POSTER_1939.jpg",
                           "https://www.youtube.com/watch?v=vkZcYMy85lY")

terminator = media.Movie("Terminator",
                         "In the not too distant future, artificial intelligence has taken over the world and only a small human resistence remains.  Disguised as a human, a cyborg assassin known as a Terminator travels from 2029 to 1984 to kill the mother of the future resistence leader. ",
                         "https://upload.wikimedia.org/wikipedia/en/7/70/Terminator1984movieposter.jpg",
                         "https://www.youtube.com/watch?v=QIcomuI1j7I")
# List of movies ends here.

movies = [terminator, star_wars, underworld, star_trek,
          resident_evil_1, wizard_of_oz]

fresh_tomatoes.open_movies_page(movies)     # Creates an HTML page
                                            # and opens in a Web browser

