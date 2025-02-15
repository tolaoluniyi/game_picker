import pandas as pd
from utils.logger import setup_logger

def parse_game_data(raw_data):
    """
    Parses raw game data into a structured format.
    """
    logger = setup_logger()
    logger.info("Parsing raw game data")

    # Example parsing logic (replace with actual logic)
    parsed_data = []
    for game in raw_data:
        parsed_game = {
            'sport': game.get('sport', 'Unknown'),
            'teams': game.get('teams', 'Unknown'),
            'time': game.get('time', 'Unknown'),
            # Add more fields as needed
        }
        parsed_data.append(parsed_game)

    return pd.DataFrame(parsed_data)
