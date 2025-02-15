import logging
import os

def setup_logger():
    if not os.path.exists('logs'):
        os.makedirs('logs')

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("logs/game_picker.log"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)
