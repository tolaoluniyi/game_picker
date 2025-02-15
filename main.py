from scraper.web_scraper import fetch_game_data
from analyzer.pick_generator import generate_picks
from analyzer.outcome_analyzer import analyze_outcomes
from database.db_handler import save_game_data, save_picks, get_historical_data
from utils.logger import setup_logger
from ui.app import run_ui

def main():
    logger = setup_logger()
    logger.info("Starting Game Picker Program")

    # Fetch game data
    game_data = fetch_game_data()
    if game_data.empty:
        logger.error("No game data fetched. Exiting...")
        return

    # Save game data to the database
    save_game_data(game_data)

    # Generate picks
    picks = generate_picks(game_data)
    logger.info(f"Generated Picks: {picks}")

    # Save picks to the database
    save_picks(picks)

    # Analyze outcomes (this would be run periodically or after games)
    historical_data = get_historical_data()
    analyze_outcomes(historical_data)

    # Run the user interface
    run_ui()

if __name__ == "__main__":
    main()
