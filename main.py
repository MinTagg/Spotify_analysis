import spotipy
import spotipy.util as util
import json
from account import *
from datetime import datetime
from utils import *

korea = datetime.strptime('9:00:00', '%H:%M:%S')
uk = datetime.strptime('0:00:00', '%H:%M:%S')

time_difference = korea - uk

token = util.prompt_for_user_token(username='ohht10004@gmail.com',
                                   scope=scopes,
                                   client_id=id,
                                   client_secret=pw,
                                   redirect_uri=uri)

if token:
    sp = spotipy.Spotify(auth=token)
    result = sp.current_user_recently_played()

saving = []

for instance in result['items']:
    temp = []
    temp.append({'Played_Time' : change_to_korea_time(instance['played_at']),
                 'Song_name' : instance['track']['name'],
                 'Artist' : instance['track']['artists'][0]['name'],
                 'Length' : instance['track']['duration_ms']//1000},
                 #노래 장르 검색하는 방법 찾기 -> 노래에 대한 장르는 없고, 가수의 장르를 검색해야할듯
                 )