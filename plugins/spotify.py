from __future__ import print_function
from __future__ import unicode_literals
import spotipy

from rtmbot.core import Plugin


class GenrePlugin(Plugin):

    def process_message(self, data):
        if 'text' in data and data['text'].startswith('genre <spotify:track:'):
            trackuri=data['text'].split(' ')[1][1:-1]
            sp = spotipy.Spotify()
            track = sp.track(trackuri)
            artist = sp.artist(track['artists'][0]['uri'])
            album = sp.album(track['album']['uri'])
            if len(artist['genres']) > 0:
                self.outputs.append([data['channel'], artist['name']+' genres are '+', '.join(artist['genres'])])
            else:
                self.outputs.append([data['channel'],'I don\'t know any genres for '+artist['name']])
