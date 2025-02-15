import requests
from bs4 import BeautifulSoup
import pandas as pd
from utils.logger import setup_logger

def fetch_game_data():
    logger = setup_logger()
    logger.info("Fetching game data from the web")

    # Replace with a real URL (e.g., ESPN's soccer schedule)
    url = "https://www.espn.com/soccer/schedule"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            logger.error(f"Failed to fetch data from the web. Status code: {response.status_code}")
            return pd.DataFrame()

        soup = BeautifulSoup(response.content, 'html.parser')
        games = []

        # Example: Scrape soccer games from ESPN
        for game in soup.find_all('tr', class_='Table__TR'):
            teams = game.find_all('span', class_='Table__Team')
            if len(teams) < 2:
                continue

            team1 = teams[0].text.strip()
            team2 = teams[1].text.strip()
            time = game.find('td', class_='date__col').text.strip() if game.find('td', class_='date__col') else "Unknown"

            game_data = {
                'sport': 'soccer',
                'teams': f"{team1} vs {team2}",
                'time': time,
            }
            games.append(game_data)

        if not games:
            logger.warning("No game data found on the webpage.")
            return pd.DataFrame()

        return pd.DataFrame(games)

    except Exception as e:
        logger.error(f"An error occurred while fetching data: {e}")
        return pd.DataFrame()
