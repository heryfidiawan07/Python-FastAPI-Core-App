from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def Verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def Hash(password):
    return pwd_context.hash(password)