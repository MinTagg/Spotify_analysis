from datetime import datetime

korea = datetime.strptime('9:00:00', '%H:%M:%S')
uk = datetime.strptime('0:00:00', '%H:%M:%S')

time_difference = korea - uk

def change_to_korea_time(input_time):
    input_time = input_time[:-1]
    input_time = datetime.fromisoformat(input_time)
    return input_time + time_difference

def get_genre(artist_id, sp):
    result = sp.artist(artist_id)
    genres = result['genres']
    if genres == []:
        genres = ['Various']
    return genres