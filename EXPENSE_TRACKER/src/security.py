from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime,timedelta,timezone

#Swagger UI token mekanızmasını nereden alıcağımızı tanımlıyoruz
oath2=OAuth2PasswordBearer(tokenUrl="api/auth/login")

# Şİfrelleme motoru bcrypt
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")


def hash_password(password:str)->str:
 # Düz metin şifreyi bcrypt ile hashler
    return pwd_context.hash(password)


def verified_password(plain_password,hash_password)->bool:
 # plain_password(düz metin) kullanıcının girdiği şifre ile hash_password karşılaştırır
    return pwd_context.verify(plain_password,hash_password)


SECRET_KEY="super_gizli_anahtar"
ALGORITMA="HS256"
TOKEN_EXP_MINUTES=60


def create_access_token(data:dict)->str:
    encode=data.copy()
    exp=datetime.now(timezone.utc())+timedelta(minutes=TOKEN_EXP_MINUTES)

    encode['exp']=exp

    # jwt token kartı 
    encode_jwt=jwt.encode(encode,SECRET_KEY,ALGORITMA)

    return encode_jwt


