# Mercury

A chat bot who replies as you wish.

> Mercury: [god of eloquence, messages and communication](https://en.wikipedia.org/wiki/Mercury_(mythology))

## Demo

```
curl --location --request POST 'http://127.0.0.1:8000/api/conversation/' \
--header 'Content-Type: application/json' \
--header 'Accept: */*' \
--header 'Host: 127.0.0.1:8000' \
--header 'Connection: keep-alive' \
--data-raw '{
    "message": "请介绍一下Standing Bodhisattva这个文物",
    "userId": 1
}'
```

response:
```json
{
    "data": "\n这件文物是一个不寻常的雕塑，它以中国的形式表现了印度的人物，它的体积很大，颜色鲜艳。这个人物是菩提达摩，一位佛教僧侣，据信他于520年从印度来到中国，带来了冥想佛教。从他的皱眉和闭眼，我们可以看出他正在深度冥想。他坐在雕塑的基座上，两边有便于操作的洞口，上面有一条题词，记录着日期和捐赠者：“忠实的党彦和麦太太”。",
    "conversation_id": 1,
    "result": "success"
}
```

## Quick start

### Docker

You can host the service by docker.

```shell
docker-compose up -d
```

### Install

```
git clone git@github.com:BustDot/Mercury.git
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
FILE_ID=YOUR_INDEXED_FILE_ID
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