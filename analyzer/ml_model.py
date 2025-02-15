import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from utils.logger import setup_logger

def train_model(historical_data):
    """
    Trains an XGBoost model using historical data.
    """
    logger = setup_logger()
    logger.info("Training XGBoost model")

    # Prepare features and target
    X = historical_data[['feature1', 'feature2']]  # Replace with actual features
    y = historical_data['outcome']  # Replace with actual target

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = xgb.XGBClassifier(
        objective='binary:logistic',  # Use 'multi:softmax' for multi-class
        n_estimators=100,
        learning_rate=0.1,
        max_depth=5
    )
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    logger.info(f"Model accuracy: {accuracy * 100:.2f}%")

    return model

def predict_outcome(model, game_data):
    """
    Predicts outcomes for new games using the trained model.
    """
    logger = setup_logger()
    logger.info("Predicting outcomes for new games")

    # Predict outcomes
    predictions = model.predict(game_data[['feature1', 'feature2']])
    return predictions
