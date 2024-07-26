from nba_search import nba_search
from get_stats import player_stats
from get_stats import team_stats


class NBAFetchStats:
    def __init__(self):
        self.last_player_name = None
        self.last_player_stats = None
        self.last_team_name = None
        self.last_team_stats = None

    def search(self):
        name = input('Search: ')
        print()
        results = nba_search(name)
        if results:
            print(f'Showing {len(results)} results')
            for i, result in enumerate(results, start=1):
                print(f'{i}. {result['full_name']}')

            select_option = int(input('Select a result by number to display stats: ')) - 1
            option = results[select_option]

            if 'state' in option:
                team_name = option['full_name']
                stats = team_stats(option['id'])
                self.team_print(team_name, stats)
            else:
                player_name = option['full_name']
                stats = player_stats(option['id'])
                self.player_print(player_name, stats)
                self.set_last_player(player_name, stats)

    def player_print(self, name, stats):
        print(f'Fetching stats from the {name} most recent season...')
        print()
        print(f'Points per Game: {round(stats['PTS'] / stats['GP'], 1)}')
        print(f'Rebounds per Game: {round(stats['REB'] / stats['GP'], 1)}')
        print(f'Assists per Game: {round(stats['AST'] / stats['GP'], 1)}')
        print(f'Steals per Game: {round(stats['STL'] / stats['GP'], 1)}')
        print(f'Blocks per Game: {round(stats['BLK'] / stats['GP'], 1)}')
        print(f'Field Goal Percentage: {round(stats['FG_PCT'] * 100, 1)}%')
        print(f'Three Point Percentage: {round(stats['FG3_PCT'] * 100, 1)}%')
        print(f'Free Throw Percentage: {round(stats['FT_PCT'] * 100, 1)}%')
        print()

    def team_print(self, name, stats):
        print(f'Fetching stats from the {name} most recent season...')
        print()
        print(f'Record: {stats['WINS']} - {stats['LOSSES']}')
        print(f'Points per Game: {round(stats['PTS'] / stats['GP'], 1)}')
        print(f'Rebounds per Game: {round(stats['REB'] / stats['GP'], 1)}')
        print(f'Assists per Game: {round(stats['AST'] / stats['GP'], 1)}')
        print(f'Steals per Game: {round(stats['STL'] / stats['GP'], 1)}')
        print(f'Blocks per Game: {round(stats['BLK'] / stats['GP'], 1)}')
        print(f'Field Goal Percentage: {round(stats['FG_PCT'] * 100, 1)}%')
        print(f'Three Point Percentage: {round(stats['FG3_PCT'] * 100, 1)}%')
        print(f'Free Throw Percentage: {round(stats['FT_PCT'] * 100, 1)}%')
        print()

    def get_last_player(self):
        if self.last_player_stats is not None:
            self.player_print(self.last_player_name, self.last_player_stats)
        else:
            print('No Player has been Searched Yet!')

    def set_last_player(self, name, stats):
        self.last_player_name = name
        self.last_player_stats = stats

    def run(self):
        print('Welcome! Lookup the most recent stats from NBA Players or Teams!')
        print('Type the number for the menu option you want to select')
        print('1. Search')
        print('2. View Last Player')
        print('3. View Last Team')
        choice = int(input('Select option: '))
        print()
        if choice == 1:
            self.search()


if __name__ == "__main__":
    NBAFetchStats().run()
