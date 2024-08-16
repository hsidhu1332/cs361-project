from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import teamyearbyyearstats
import zmq


def player_stats(id):
    regular_season_stats = (playercareerstats.PlayerCareerStats
                            (player_id=id).get_data_frames()[0])

    if not regular_season_stats.empty:
        return regular_season_stats.iloc[-1]
    return 'Player has not played yet'


def team_stats(id):
    regular_season_stats = (teamyearbyyearstats.TeamYearByYearStats
                            (team_id=id).get_data_frames()[0])

    return regular_season_stats.iloc[-1]

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5556")

    while True:
        message = socket.recv_pyobj()

        if message['type'] == 'player':
            result = player_stats(message['id'])
            print('Sending player stats')
        elif message['type'] == 'team':
            result = team_stats(message['id'])
            print('Sending team stats')
        else:
            result = {'err': 'Error making request'}

        socket.send_pyobj(result)

if __name__ == "__main__":
    main()