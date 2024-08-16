from nba_api.stats.static import players
from nba_api.stats.static import teams
import zmq


def nba_search(name):
    player_list = players.get_active_players()
    team_list = teams._get_teams()
    results = []
    for player in player_list:
        if name.lower() in player['full_name'].lower():
            results.append(player)
    for team in team_list:
        if name.lower() in team['full_name'].lower():
            results.append(team)
    return results

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        message = socket.recv_string()

        results = nba_search(message)
        print('Sending search results')
        socket.send_pyobj(results)

if __name__ == "__main__":
    main()