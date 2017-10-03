# elsociobot
Just a Telegram bot for "academic purposes". Don't take this seriously, it's more a useful joke than a serious bot.

## Prerequisites
There are few things you need have installed to get the bot running:

* **Python 3.x.x**

Then install requirements:

```
python -m pip install -r requirements.txt
```

Set the token on your system for the bot:

``` sh
# On Unix systems
export TELEGRAM_TOKEN='PUT-YOUR-TOKEN-HERE'

# On Windows systems
SET TELEGRAM_TOKEN='PUT-YOUR-TOKEN-HERE'
```

## Usage
The bot usage is easy, just run:

```sh
python bot.py
```

# Built-in bot commands
There are *"helpful"* commands set on the bot.

If you want to **"madrear"** someone:

```
/madrear <name>
```

## Deploying
Install [Heroku Toolbelt](https://toolbelt.heroku.com/), then go inside the folder:

```
cd elsociobot
```

Login to Heroku from console:

```
heroku login
```

Create a new app:

```
heroku create
```

Install python (buildpack):

```
heroku buildpacks:set heroku/python # set python buildpack
```

Push code to Heroku app:

```
git push heroku master
```

Set the TELEGRAM_TOKEN variable:

```
heroku config:set TELEGRAM_TOKEN=123456789:AAABBBCCCDDDEEEFFFGGGHHHIIIJJJKKKLL
```

Start the party!

```
heroku ps:scale bot=1 # start bot dyno
```

If you want to check the logs:

```
heroku logs --tail
```

If you want to stop the bot:

```
heroku ps:stop bot #stop bot dyno
```
