import requests
from bs4 import BeautifulSoup
import pandas as pd
from utils.logger import setup_logger

def fetch_game_data():
    logger = setup_logger()
    logger.info("Fetching game data from the web")

    # Example URL (replace with actual URLs)
    url = "http://example.com/games"
    response = requests.get(url)
    if response.status_code != 200:
        logger.error("Failed to fetch data from the web")
        return pd.DataFrame()

    soup = BeautifulSoup(response.content, 'html.parser')
    games = []
    for game in soup.find_all('div', class_='game'):
        game_data = {
            'sport': game.find('span', class_='sport').text,
            'teams': game.find('span', class_='teams').text,
            'time': game.find('span', class_='time').text,
            # Add more fields as needed
        }
        games.append(game_data)

    return pd.DataFrame(games)
