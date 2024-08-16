import zmq
import random
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players

def get_random_player():
    player_list = players.get_inactive_players()
    random_player = random.choice(player_list)
    return random_player['id'], random_player['full_name']

def last_5_seasons(id):
    regular_season_stats = (playercareerstats.PlayerCareerStats
                            (player_id=id).get_data_frames()[0])
    if regular_season_stats.empty:
        return {'Error:': 'This player has not played yet'}

    seasons_stats = regular_season_stats.tail(5)

    ppg_last_5 = []

    for i, v in seasons_stats.iterrows():
        ppg = round(v['PTS'] / v['GP'], 1)
        ppg_last_5.append({'season': v['SEASON_ID'], 'ppg': ppg})
    
    return ppg_last_5

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5557")

    trend_socket = context.socket(zmq.REQ)
    trend_socket.connect("tcp://localhost:5558")

    while True:
        message = socket.recv_string()

        if message == 'random_player':
            player_id, player_name = get_random_player()
            stats = last_5_seasons(player_id)
            ppg_arr = []
            for season in stats:
                ppg_arr.append(season['ppg'])
            trend_socket.send_pyobj(ppg_arr)
            trend = trend_socket.recv_string()
            print('Received trend of random player')
            result = {'player_name': player_name, 'PPG': stats, 'trend': trend}
        print('Sending random player')
        socket.send_pyobj(result)

if __name__ == "__main__":
    main()