from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Prediction(Base):
    __tablename__ = 'predictions'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    surname = Column(String(50), index=True)
    personality_type = Column(String(50), index=True)

class PredictionDetails(Base):
    __tablename__ = 'prediction_details'
    
    id = Column(Integer, primary_key=True, index=True)
    personality_type = Column(String(50), index=True)
    
    for i in range(1, 61):
        locals()[f'q{i}'] = Column(Integer)