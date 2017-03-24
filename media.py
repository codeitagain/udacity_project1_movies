""" The file media.py defines the classes used in this application
that is executed by running the file entertainment_center.py.
"""

import webbrowser

class Movie():
    """ Class Movie provides a way to store movie related info,
        including variables title, storyline, poster_image_url,
        and trailer_youtube_url. """
    
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self): 
        """Movie.show_trailer opens the given url address for
           the movie trailer."""    
        webbrowser.open(self.trailer_youtube_url)

    
