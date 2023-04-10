# Mercury

A chat bot who replies as you wish.

> Mercury: [god of eloquence, messages and communication](https://en.wikipedia.org/wiki/Mercury_(mythology))

## Quick start

### Install

```
git clone git@github.com:Sox-I/Mercury.git
cd Mercury
pip install -r requirements.txt
```

### Database migration

We use the default database `sqlite3`.

```
python manage.py makemigrations
python manage.py migrate
```

### Create superuser

First we’ll need to create a user who can login to the admin site. Run the following command:

```
python manage.py createsuperuser
```

Enter your desired username and press enter.

```
Username: admin
```

You will then be prompted for your desired email address:

```
Email address: admin@example.com
```

The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.

```
Password: **********
Password (again): *********
Superuser created successfully.
```

### Set up `.env` file

We will read config from `.env` file.

Create a file name `.env` in the root directory and add following config:

```
API_KEY=YOUR_MURA_API_KEY
```

### Start the server

```
python manage.py runserver
```

You will see following output on the command line:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 10, 2023 - 22:31:31
Django version 4.1.7, using settings 'mercury.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Now GL&HF! :)