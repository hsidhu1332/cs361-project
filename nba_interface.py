from nba_search import nba_search
from get_stats import player_stats
from get_stats import team_stats


class NBAFetchStats:
    def __init__(self):
        self.last_player_name = None
        self.last_player_stats = None
        self.last_team_name = None
        self.last_team_stats = None
        self.last_search = None

    def search(self, name=None):
        while True:
            print('Type the name of the player or team you want to search')
            print('You can also type menu to return to the menu\n')
            if name is None:
                name = input('Search: ')
                self.last_search = name
            print()
            if name == 'menu':
                return None
            results = nba_search(name)
            if results:
                if len(results) > 10:
                    while True:
                        length_choice = input('This search has more than 10 results, are you sure you want to continue? [yes/no] ')
                        if length_choice == 'yes' or length_choice == 'no':
                            break
                        else:
                            print('Unknown command, please try again.')
                    if length_choice == 'no':
                        name = None
                        continue
                print(f'Showing {len(results)} results')
                for i, result in enumerate(results, start=1):
                    print(f'{i}. {result['full_name']}')
                print()
                print('Type menu to return to the menu or back to return to search')
                print('Otherwise, type the number corresponding to the player or team to view stats\n')
                while True:
                    select_option = input('Select option: ')
                    if select_option != 'menu' and select_option !='back' and not select_option.isdigit():
                        print('Unknown command, please try again.')
                        continue
                    try:
                        if int(select_option) > len(results):
                            print('Unknown command, please try again.')
                        else:
                            break
                    except ValueError:
                        break
                if select_option == 'menu':
                    return None
                if select_option == 'back':
                    name = None
                    print()
                    continue
                else:
                    break
            else:
                print('No search results found. Try again.\n')
        option = results[int(select_option) - 1]
        if 'state' in option:
            team_name = option['full_name']
            stats = team_stats(option['id'])
            self.set_last_team(team_name, stats)
            self.team_print(team_name, stats)
        else:
            player_name = option['full_name']
            stats = player_stats(option['id'])
            self.set_last_player(player_name, stats)
            self.player_print(player_name, stats)

    def player_print(self, name, stats):
        print()
        if name.endswith('s'):
            print(f'Stats from {name}\' most recent season...\n')
        else:
            print(f'Stats from {name}\'s most recent season...\n')
        print(f'Points per Game: {round(stats['PTS'] / stats['GP'], 1)}')
        print(f'Rebounds per Game: {round(stats['REB'] / stats['GP'], 1)}')
        print(f'Assists per Game: {round(stats['AST'] / stats['GP'], 1)}')
        print(f'Steals per Game: {round(stats['STL'] / stats['GP'], 1)}')
        print(f'Blocks per Game: {round(stats['BLK'] / stats['GP'], 1)}')
        print(f'Field Goal Percentage: {round(stats['FG_PCT'] * 100, 1)}%')
        print(f'Three Point Percentage: {round(stats['FG3_PCT'] * 100, 1)}%')
        print(f'Free Throw Percentage: {round(stats['FT_PCT'] * 100, 1)}%\n')
        self.end()

    def team_print(self, name, stats):
        print()
        print(f'Stats from the {name} most recent season...\n')
        print(f'Record: {stats['WINS']} - {stats['LOSSES']}')
        print(f'Points per Game: {round(stats['PTS'] / stats['GP'], 1)}')
        print(f'Rebounds per Game: {round(stats['REB'] / stats['GP'], 1)}')
        print(f'Assists per Game: {round(stats['AST'] / stats['GP'], 1)}')
        print(f'Steals per Game: {round(stats['STL'] / stats['GP'], 1)}')
        print(f'Blocks per Game: {round(stats['BLK'] / stats['GP'], 1)}')
        print(f'Field Goal Percentage: {round(stats['FG_PCT'] * 100, 1)}%')
        print(f'Three Point Percentage: {round(stats['FG3_PCT'] * 100, 1)}%')
        print(f'Free Throw Percentage: {round(stats['FT_PCT'] * 100, 1)}%\n')
        self.end()

    def get_last_player(self):
        if self.last_player_stats is not None:
            self.player_print(self.last_player_name, self.last_player_stats)
        else:
            print('No Player has been Searched Yet!\n')

    def set_last_player(self, name, stats):
        self.last_player_name = name
        self.last_player_stats = stats

    def get_last_team(self):
        if self.last_team_stats is not None:
            self.team_print(self.last_team_name, self.last_team_stats)
        else:
            print('No Player has been Searched Yet!\n')

    def set_last_team(self, name, stats):
        self.last_team_name = name
        self.last_team_stats = stats

    def end(self):
        while True:
            print('What would you like to do?\n')
            print('1. Go back to menu')
            print('2. Back to Search Results\n')
            restart = input('Select option: ')
            if restart != '1' and restart != '2':
                print('Unknown command, please Try Again')
            elif restart == '1':
                while True:
                    confirm = input('Are you sure you want to return to the menu? You will have to search again to see your search results. [yes/no] ')
                    if confirm == 'yes' or confirm == 'no':
                        break
                    else:
                        print('Unknown command, please Try Again')
                if confirm == 'yes':
                    break
            else:
                break
        if restart == '2':
            self.search(self.last_search)

    def run(self, run_num=0):
        while True:
            if run_num == 0:
                print('Welcome! Lookup the most recent stats from NBA Players or Teams!')
                run_num += 1
            else:
                print('Lookup the most recent stats from NBA Players or Teams!')
            print('Type the number for the menu option you want to select\n')
            print('1. Search')
            print('2. View Last Player')
            print('3. View Last Team\n')
            choice = input('Select option: ')
            print()
            if choice != '1' and choice != '2' and choice != '3' and choice != 'exit':
                print('Unknown Option, Please Try Again.\n')
            if choice == '1':
                self.search()
            elif choice == '2':
                self.get_last_player()
            elif choice == '3':
                self.get_last_team()
            elif choice == 'exit':
                break


if __name__ == "__main__":
    NBAFetchStats().run()
