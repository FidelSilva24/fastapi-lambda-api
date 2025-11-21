# FastAPI JWT Example API
A lightweight FastAPI API demonstrating secure JWT authentication and cloud deployment. Perfect for learning backend fundamentals and serverless practices.


# Project Structure
api/ \
├── main.py           # FastAPI application\
├── models.py         # Pydantic models for User and Product\
├── storage.py        # Example data (users_list, products_list)\
├── auth.py           # JWT verification functions\
├── generate_key.py   # Token creator\
├── requirements.txt  # Python dependencies\
└── README.md         # This documentation\

# Features
- FastAPI Framework – Modern, high-performance Python API.
- JWT Authentication – Protects routes with JSON Web Tokens.
- Serverless Ready – Deployable to AWS Lambda + API Gateway.
- Tested – Fully validated with Postman and curl.
- Clean Architecture – Models, storage, and API logic separated for clarity.


# Endpoints
Public:\
GET / – API health check.\
GET /products – List all products.\
Protected (JWT required):\
GET /users – List all users.\
GET /users/{id} – Retrieve a user by ID.\
Use the Authorization: Bearer <JWT> header for protected routes.\

# Installation & Local Testing
## Clone the repository:\

git clone https://github.com/FidelSilva24/fastapi-lambda-api.git \
cd fastapi-lambda-api\
python3 -m venv .venv\
source .venv/bin/activate\
pip install -r requirements.txt\
uvicorn main:app --reload\

## Test with curl:
curl -X GET http://127.0.0.1:8000/users \ \
-H "Authorization: Bearer <YOUR_JWT_TOKEN>"

# Deployment
The API was designed for serverless deployment:\
AWS Lambda: The API can be run as a Lambda function using Mangum as the adapter.\
API Gateway: Configured as a proxy to handle all HTTP requests.\
Security: JWT authentication ensures that protected routes are secure.\
Steps for deployment:\
Package your project dependencies inside a package/ folder.\
Zip the project including the dependencies.\
Upload to AWS Lambda and configure API Gateway as a trigger.
Test endpoints with a valid JWT token.
