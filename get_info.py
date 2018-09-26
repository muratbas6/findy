import spotipy.util as util
import spotipy

scope = 'user-read-currently-playing'

username = "fotntys10iaawb4qd2nexvz50"


def set_token():
    token = util.prompt_for_user_token(username, scope, client_id='2f8e6614eca44359abf5bdf519f09165',
                                       client_secret='5132ee50f6f340779365cc70c16394dc', redirect_uri='http://127.0.0.1:8000/main/')
    return token


sp = spotipy.Spotify(auth=set_token())


def get_current_song_info():
    results = sp.currently_playing()
    content = results.get("item")
    song_name = content['name']
    artist = content['artists'][0]['name']
    return artist, song_name
