""" The entertainment_center.py is the executable file for a Python
program that displays in a Web browser a list of favorite movies,
including each movie's title, poster, and trailer. This file also
contains all the data stored and used for each movie identified
in this project. """

import fresh_tomatoes
import media

# List of movies begins here.
RESIDENT_EVIL = media.Movie("Resident Evil",
                            "https://upload.wikimedia.org/wikipedia/en/a/a1/"+
                            "Resident_evil_ver4.jpg",
                            "https://www.youtube.com/watch?v=lBxjZahSN7o", " ")
RESIDENT_EVIL.story_line = RESIDENT_EVIL.update_storyline()

UNDERWORLD = media.Movie("Underworld",
                         "https://upload.wikimedia.org/wikipedia/en/c/cc/"+
                         "Underworld_%282003_film%29_poster.jpg",
                         "https://www.youtube.com/watch?v=MqT-e44kIM8", " ")
UNDERWORLD.story_line = UNDERWORLD.update_storyline()

STAR_WARS = media.Movie("Star Wars",
                        "https://upload.wikimedia.org/wikipedia/en/8/87/"+
                        "StarWarsMoviePoster1977.jpg",
                        "https://www.youtube.com/watch?v=K8AD7wzsPFQ", " ")
STAR_WARS.story_line = STAR_WARS.update_storyline()

STAR_TREK = media.Movie("Star Trek",
                        "https://upload.wikimedia.org/wikipedia/en/d/df/"+
                        "Star_Trek_The_Motion_Picture_poster.png",
                        "https://www.youtube.com/watch?v=g0-7Z2lYII8", " ")
STAR_TREK.story_line = STAR_TREK.update_storyline()

WIZARD_OF_OZ = media.Movie("Wizard of Oz",
                           "https://upload.wikimedia.org/wikipedia/commons/"+
                           "c/ca/WIZARD_OF_OZ_ORIGINAL_POSTER_1939.jpg",
                           "https://www.youtube.com/watch?v=vkZcYMy85lY", " ")
WIZARD_OF_OZ.story_line = WIZARD_OF_OZ.update_storyline()

ODD_THOMAS = media.Movie("Odd Thomas",
                         "https://upload.wikimedia.org/wikipedia/en/f/ff/"+
                         "Odd_Thomas_poster_film.jpg",
                         "https://www.youtube.com/watch?v=5ybBq5AETyU", " ")
ODD_THOMAS.story_line = ODD_THOMAS.update_storyline()
# List of movies ends here.

MOVIES = [ODD_THOMAS, STAR_WARS, UNDERWORLD, STAR_TREK,
          RESIDENT_EVIL, WIZARD_OF_OZ]

# Creates an HTML page and opens in a Web browser
fresh_tomatoes.open_movies_page(MOVIES)
