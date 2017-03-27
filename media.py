""" The file media.py defines the class used in this application
that is executed by running the file entertainment_center.py.
"""

import urllib
import webbrowser

class Movie(object):
    """ Class Movie() provides a way to store movie related info,
        including variables title, storyline, poster_image_url,
        and trailer_youtube_url. """

    def __init__(self, video_title, poster_image, trailer_youtube, story_line):
        self.video_title = video_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.story_line = story_line

    def show_trailer(self):
        """Movie.show_trailer opens the given url address for
           the movie trailer."""
        webbrowser.open(self.trailer_youtube_url)

    def update_storyline(self):
        """Movie.update_storyline graps a storyline description provided by
        the API TheMovieDB.org."""
        search_title = self.video_title.replace(" ", "+")
        api_response = urllib.urlopen("https://api.themoviedb.org/3/search/"+
                                      "movie?api_key=0bf3188c8eacc47d41ae97"+
                                      "d1d6dd2cfc&query="+
                                      search_title)
        movie_data = api_response.read()
        api_response.close()
        if '"overview":"' in movie_data:
            #finding first position of storyline from API data
            apos = movie_data.find('"overview":"') + 12
            #finding last  position of storyline
            bpos = movie_data.find('",', apos)
            return movie_data[apos:bpos]
        else:
            return
