[![Build Status](https://travis-ci.org/Tawakalt/bucketlist.svg?branch=travis)](https://travis-ci.org/Tawakalt/bucketlist)
# Bucket List API

A bucketlist is a list of things you'd like to do, experience or achieve.

### Technologies
- Python3
- Django
- Djangorestframework

### Setup
- Clone repo `git clone https://github.com/Tawakalt/bucketlist.git`
- Create a virtual environent using python3 and activate it
- create a `.env` to have your app configurations like this

      SECRET_KEY ='your secret key'
      DATABASE_URL="postgres://localhost/<database-name>"

Activate your .env file by typing `source .env` in the commandline

- Install requirements.txt `pip install -r requirements.txt`

### Database
- Run `python3 manage.py migrate` to run the database migrations

### Create SuperUser
- Run `python3 manage.py createsuperuser`

### Starting application
- Start the application with `python3 manage.py runserver`
- Navigate to `http://localhost:8000/` or `http://127.0.0.1:8000/` to use the API

### Testing
- Run the tests with `python3 manage.py test`.

### API Endpoints
Bucketlist:

| Endpoints	| Methods	|Description|
| ------------- | ------------- | -----|
|/get-token/   | POST | Sign in a user |
|/bucketlists/	   |GET	  | Get all bucketlists|
|/bucketlists/	   |POST  | Add a bucketlist |
|/bucketlists/:id  |GET	  | Get a single bucketlist |
|/bucketlists/:id  |PUT	  | Update a single bucketlist |
|/bucketlists/:id  |DELETE| Delete a single bucketlist |


Authentication:
- Get token from the /get-token route
- Put token generated in the header with key `Authorization` in format:
`Token <auth token>`
e.g: 
```
Token 3c11a65f887c31d537397a9326e102e852ec8140hhhhhhhhhhhhhh
```