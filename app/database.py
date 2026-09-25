from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os


mysql_user = os.environ.get('MYSQL_USER')
mysql_password = os.environ.get('MYSQL_PASSWORD')
mysql_host = os.environ.get('MYSQL_HOST')
mysql_db = os.environ.get('MYSQL_DATABASE')

engine = create_engine(
    f"mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
