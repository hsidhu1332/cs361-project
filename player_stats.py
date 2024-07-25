from nba_api.stats.endpoints import playercareerstats


def player_stats(id):
    recent_season_stats = playercareerstats.PlayerCareerStats(player_id=id).get_data_frames()[0]

    if not recent_season_stats.empty:
        return recent_season_stats.iloc[-1]
    return 'Player has not played yet'
