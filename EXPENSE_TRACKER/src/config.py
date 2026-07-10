

# from pydantic_settings import BaseSettings

# class Settings(BaseSettings):
#     # PostgreSQL Bağlantı Stringi Formatı:
#     # postgresql://<KULLANICI_ADI>:<SIFRE>@<HOST>:<PORT>/<VERITABANI_ADI>
    
#     SQLALCHEMY_DATABASE_URL: str = "postgresql://postgres:sifrem123@localhost:5432/expense_tracker"

# settings = Settings()

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # En sondaki veritabanı ismini 'post' yerine 'expense_tracker' yapıyoruz:
    SQLALCHEMY_DATABASE_URL: str = "postgresql://musa:sifrem123@localhost:5432/expense_tracker"

settings = Settings()