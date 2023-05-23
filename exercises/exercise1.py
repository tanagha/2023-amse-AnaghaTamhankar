import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float,Table,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.sqlite import REAL as SQLiteReal
from sqlalchemy.orm import sessionmaker

# Create the engine and session
engine = create_engine('sqlite:///airports.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

# Create a base class for declarative models
Base = declarative_base()

class Airport(Base):
    __tablename__ = 'airports'
    column_1 = Column(Integer)
    column_2 = Column(String)
    column_3 = Column(String)
    column_4 = Column(String)
    column_5 = Column(String)
    column_6 = Column(String)
    column_7 = Column(Float)
    column_8 = Column(Float)
    column_9 = Column(Integer)
    column_10 = Column(Float)
    column_11 = Column(String)
    column_12 = Column(String)
    geo_punkt = Column(String)
    __mapper_args__ = { 'primary_key': [column_1, column_2]}
    
Base.metadata.create_all(engine)

url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"
df = pd.read_csv(url, delimiter= ";")

records = df.to_dict(orient='records')


for record in records:
    airport = Airport(**record)
    session.add(airport)
session.commit()
