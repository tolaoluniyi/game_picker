from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from utils.config import DATABASE_URI

Base = declarative_base()

class GameData(Base):
    __tablename__ = 'game_data'
    id = Column(Integer, primary_key=True)
    sport = Column(String)
    teams = Column(String)
    time = Column(String)

class Picks(Base):
    __tablename__ = 'picks'
    id = Column(Integer, primary_key=True)
    sport = Column(String)
    teams = Column(String)
    pick = Column(String)
    confidence = Column(Float)

engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def save_game_data(game_data):
    session = Session()
    for _, row in game_data.iterrows():
        game = GameData(sport=row['sport'], teams=row['teams'], time=row['time'])
        session.add(game)
    session.commit()

def save_picks(picks):
    session = Session()
    for _, row in picks.iterrows():
        pick = Picks(sport=row['sport'], teams=row['teams'], pick=row['pick'], confidence=row['confidence'])
        session.add(pick)
    session.commit()

def get_historical_data():
    session = Session()
    return pd.read_sql(session.query(Picks).statement, session.bind)
