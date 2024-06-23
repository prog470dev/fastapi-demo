from sqlalchemy.exc import InternalError, OperationalError
from sqlalchemy import create_engine, text

from api.models.task import Base
from api.db import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME


DB_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/?charset=utf8mb4"
)
DEMO_DB_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"
)

db_engine = create_engine(DEMO_DB_URL, echo=True)

def database_exists() -> bool:
    try:
        db_engine.connect()
        return True
    except (InternalError, OperationalError) as e:
        print(e)
        print("Database does not exist")
        return False

def create_database():
    if not database_exists():
        root = create_engine(DB_URL, echo=True)
        with root.connect() as conn:
            conn.execute(text(f"CREATE DATABASE {DB_NAME}"))
        print("Database created")
        print("run \"alembic upgrade head\"")

if __name__ == "__main__":
    create_database()
