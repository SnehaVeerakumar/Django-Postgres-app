# GeeksforGeeks contributed article
## Deploying Django application on Heroku with Postgres as backend.
<a href = "https://www.geeksforgeeks.org/deploying-django-app-on-heroku-with-postgres-as-backend/"> https://www.geeksforgeeks.org/deploying-django-app-on-heroku-with-postgres-as-backend/ </a>

## Project set-up

1. Clone the repository.
  ```sh
  git clone https://github.com/SnehaVeerakumar/Django-postgres-app.git
  cd Django-postgres-app/geeks
   ```
2. Install necessary python packages.
  ```sh
  pip install -r requirements.txt
   ```
3. geeks/settings.py line 29 contains host configurations to be changed.
Replace "website" with the website name to be deployed ('example.com').
  ```
   ALLOWED_HOSTS = ['<website>']
  ```  
3. geeks/settings.py line 86 contains database configurations to be changed.
Replace "name","user","password","Host" with your credentials for heroku deployment. 
  ```
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<name>', 
        'USER': '<user>', 
        'PASSWORD': '<password>',
        'HOST': '<Host>', 
        'PORT': '5432',
    }
}
   ```
### You are all set to deploy the application !

<br>
All rights reserved to <a href="https://www.geeksforgeeks.org/">@geeksforgeeks</a>


