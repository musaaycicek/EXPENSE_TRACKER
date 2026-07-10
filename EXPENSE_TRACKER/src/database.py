from sqlalchemy.orm import sessionmaker,DeclarativeBase
from sqlalchemy import create_engine
from config import settings

engine=create_engine(settings.SQLALCHEMY_DATABASE_URL)


class Base(DeclarativeBase):pass


sessionLocal=sessionmaker(bind=engine,autoflush=False)


db=sessionLocal()


def get_db(): 
 try:
    yield db
 except Exception as e:
    raise RuntimeError("Hata") from e