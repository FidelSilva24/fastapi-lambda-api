import jwt

SECRET_KEY = "SECRET KEY"
ALGORITHM = "HS256"

token = jwt.encode({"user": "admin"}, SECRET_KEY, algorithm=ALGORITHM)
print(token)


#This script can generate your token based in your secret key to access