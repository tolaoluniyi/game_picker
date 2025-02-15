from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

# Base class for SQLAlchemy models
Base = declarative_base()

class GameData(Base):
    """
    Represents the 'game_data' table in the database.
    Stores information about upcoming games.
    """
    __tablename__ = 'game_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sport = Column(String, nullable=False)  # Type of sport (e.g., soccer, basketball)
    teams = Column(String, nullable=False)  # Teams playing (e.g., "Team A vs Team B")
    time = Column(DateTime, nullable=False)  # Date and time of the game

class Picks(Base):
    """
    Represents the 'picks' table in the database.
    Stores the generated picks for each game.
    """
    __tablename__ = 'picks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sport = Column(String, nullable=False)  # Type of sport
    teams = Column(String, nullable=False)  # Teams playing
    pick = Column(String, nullable=False)  # Predicted outcome (e.g., "Team A", "Draw")
    confidence = Column(Float, nullable=False)  # Confidence level of the pick (0 to 1)
    timestamp = Column(DateTime, nullable=False)  # When the pick was generated

class HistoricalData(Base):
    """
    Represents the 'historical_data' table in the database.
    Stores historical game outcomes for training machine learning models.
    """
    __tablename__ = 'historical_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sport = Column(String, nullable=False)  # Type of sport
    teams = Column(String, nullable=False)  # Teams playing
    outcome = Column(String, nullable=False)  # Actual outcome (e.g., "Team A", "Draw")
    feature1 = Column(Float, nullable=False)  # Example feature for ML model
    feature2 = Column(Float, nullable=False)  # Example feature for ML model
    timestamp = Column(DateTime, nullable=False)  # When the game occurred
