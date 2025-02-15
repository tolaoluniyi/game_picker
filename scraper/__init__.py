
# This file makes the scraper directory a Python package.
# It can be left empty or used to expose specific functions/classes.
from .web_scraper import fetch_game_data
from .data_parser import parse_game_data

__all__ = ['fetch_game_data', 'parse_game_data']
