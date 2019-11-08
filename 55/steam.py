from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "http://bit.ly/2IkFe9B"

Game = namedtuple('Game', 'title link')


def get_games() -> list:
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    d = feedparser.parse(FEED_URL)

    games = []

    for i in range(len(d['entries'])):
        title = d['entries'][i]['title']
        link = d['entries'][i]['link']

        games.append(Game(title=title, link=link))

    return games

# def main():
#     print('zone in...')
#     games = get_games()
#     assert len(games) == 30
#     assert all(isinstance(game, tuple) for game in games)
#     assert all('store.steampowered.com' in game.link for game in games)
#     first_game = games[0]
#     assert first_game.title == 'Midweek Madness - RiME, 33% Off'
#     assert first_game.link == 'http://store.steampowered.com/news/31695/'
#     last_game = games[-1]
#     assert last_game.title == 'Now Available on Steam - Loco Dojo, 35% off!'
#     assert last_game.link == 'http://store.steampowered.com/news/31113/'


# if __name__ == '__main__':
#     main()
