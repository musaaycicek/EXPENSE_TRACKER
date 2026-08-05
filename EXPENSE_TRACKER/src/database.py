from sqlalchemy.orm import sessionmaker,DeclarativeBase
from sqlalchemy import create_engine
from config import settings

engine=create_engine(settings.SQLALCHEMY_DATABASE_URL)


class Base(DeclarativeBase):pass


sessionLocal=sessionmaker(bind=engine,autoflush=False)





def get_db(): 
 db=sessionLocal()
 try:
    yield db
 except Exception as e:
    raise RuntimeError(f"Hata:{e}") from e
 finally:
   db.close()