from jose import jwt
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

if not SECRET_KEY:
    raise Exception("SECRET_KEY not found in .env file")

token = jwt.encode({"sub": "zeel"}, SECRET_KEY, algorithm=ALGORITHM)
print(token)