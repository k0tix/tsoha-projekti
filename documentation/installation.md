# Installation and running

## Prerequisites
* SQLite3
* Python 3.6

Clone repository: 
```
git clone https://github.com/k0tix/tsoha2019.git
cd tsoha2019
```

Initialize python venv:
```
python3 -m venv venv
source venv/bin/activate
```

Install requirements:
```
pip install -r requirements.txt
```

Run application:
```
python3 run.py
```

## Heroku
Make sure you have heroku-cli installed

Clone the repo
```
git clone https://github.com/k0tix/tsoha2019.git
cd tsoha2019
```

Create a new heroku project:
```
heroku create some-creative-name-here
git remote add heroku https://git.heroku.com/some-creative-name-here.git
```

Add a Postgres database with the command: 
```
heroku addons:add heroku-postgresql:hobby-dev
```

Push the project to heroku:
```
git push heroku master
```