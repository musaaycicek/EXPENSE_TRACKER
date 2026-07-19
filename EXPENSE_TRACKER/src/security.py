
from passlib.context import CryptContext

# Passlib kütüphanesine bcrypt algoritmasını kullanmasını söylüyoruz
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password:str) -> str:
    """
     Düz metin şifreyi alır ve bcrypt ile güvenli bir şekilde hash'ler.
    """
    return pwd_context.hash(password)


def verify_password(plain_password:str,hashed_password:str) -> bool:
    """
    Kullanıcının giriş yaparken yazdığı düz şifre ile veritabanındaki
    şifreli hali karşılaştırır. Eşleşirse True, eşleşmezse False döner.
    """
    return pwd_context.verify(plain_password, hashed_password)   





