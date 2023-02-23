# secure password
from passlib.context import CryptContext
#Create an object of the class CryptContext
pwd_config = CryptContext(schemes=["pbkdf2_sha256"],
                          default="pbkdf2_sha256",
                          pbkdf2_sha256__default_rounds=30000
                          )

#this function receives the unsafe password
# and returns the hashed password
def encrypt_password(user_password):
    return pwd_config.hash(user_password)

def check_password(hashed_password, user_password):
    if hashed_password == encrypt_password(user_password)[:50]:
        return True
    else:
        return False

hashed = encrypt_password("password123")
print(hashed)
