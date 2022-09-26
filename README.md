# Emphasoft test assigment
## To_Do

Create CRUD app with token-authentication

## How to start 

Clone this repository, add .env file in a root with this env. variables:
- DATABASE_URL - MongoDB Connection String
- MONGO_DB - MongoDB Database Name
- SECRET_KEY - Secret Key for encoding and decoding JWT Token (i used openssl to generate one)
- ALGORITHM - Encoding and decoding algorithm (i used "HS256")
- ACCESS_TOKEN_EXPIRE_MINUTES - 30 minutes

Then install all the packages from requirements.txt using
'''
pip install requirements.txt
'''
Then run main.py file
The service will be hosted at http://127.0.0.1:8000