# eCommerce API

## How to run project
### 1. Clone the project
### 2. cd to project's directory
  ```
  cd Ecommerce-api
  ```
### 3. create venv
  ```
  python -m venv .venv
  ```
### 4. activate venv
  ```
  # in Windows
  .venv/scripts/activate
  # in Linux/Mac
  source .venv/bin/activate 
  ```
### 5. install requirements
  ```
  pip install -r requirements.txt
  ```
### 6. configure .env file like .env.sample
  ```
  SECRET_KEY = 'Your secret key'
  DEBUG = True 
  ALLOWED_HOSTS = 127.0.0.1, localhost, 0.0.0.0
  ```
   - You can generate the secret key using [https://djecrety.ir](url)

### 7. make migrations
  ```
  python manage.py makemigrations
  ```
### 8. migrate
  ```
  python manage.py migrate
  ```
### 9. load data for initial state
  ```
  python manage.py loaddata group.json
  ```
### 10. create superuser
  ```
  python manage.py createsuperuser
  ```
### 11. runserver
  ```
  python manage.py runserver
  ```
