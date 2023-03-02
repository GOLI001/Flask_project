from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Create your views here.
def index(request):
    if request.method=='POST':
        artist_uri = request.POST.get('uri')
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='dcb2c93f0a8a4a039a5b7a7991606c21',client_secret='73d18566ad474555ad2eacee902d98c0',))
        results = spotify.artist_top_tracks(artist_uri)
        final_result=results['tracks'][:10]
        return render(request,'base.html',{"results":final_result})
    else:
# for track in results['tracks'][:10]:
#     print('track    : ' + track['name'])
#     print('audio    : ' + track['preview_url'])
#     print('cover art: ' + track['album']['images'][0]['url'])
#     print()
      return render(request,'base.html',)
