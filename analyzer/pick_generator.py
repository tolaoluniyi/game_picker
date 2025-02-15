import pandas as pd
import numpy as np
import xgboost as xgb
from database.db_handler import get_historical_data
from utils.logger import setup_logger

def generate_picks(game_data):
    logger = setup_logger()
    logger.info("Generating intelligent picks using XGBoost")

    # Load historical data for training
    historical_data = get_historical_data()
    if historical_data.empty:
        logger.warning("No historical data found. Using random picks.")
        return generate_random_picks(game_data)

    # Prepare features and target
    X = historical_data[['feature1', 'feature2']]  # Replace with actual features
    y = historical_data['outcome']  # Replace with actual target

    # Train an XGBoost model
    model = xgb.XGBClassifier(
        objective='binary:logistic',  # Use 'multi:softmax' for multi-class
        n_estimators=100,
        learning_rate=0.1,
        max_depth=5
    )
    model.fit(X, y)

    # Predict outcomes for new games
    game_data['predicted_outcome'] = model.predict(game_data[['feature1', 'feature2']])
    picks = game_data[['sport', 'teams', 'predicted_outcome']]

    return picks

def generate_random_picks(game_data):
    picks = []
    for _, game in game_data.iterrows():
        pick = {
            'sport': game['sport'],
            'teams': game['teams'],
            'pick': np.random.choice(['Team A', 'Team B', 'Draw']),
            'confidence': np.random.randint(1, 10)
        }
        picks.append(pick)
    return pd.DataFrame(picks)
