from sqlalchemy import create_engine

from api.models.task import Base
from api.db import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

DB_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"
)

db_engine = create_engine(DB_URL, echo=True)

def reset_database():
    Base.metadata.drop_all(bind=db_engine)
    Base.metadata.create_all(bind=db_engine)

if __name__ == "__main__":
    reset_database()
