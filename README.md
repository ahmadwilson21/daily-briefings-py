# Daily Briefings Service (Python)

Sends you a customized email every morning, with information of interest such as the upcoming weather forecast.

## Setup

Fork this repo and clone it onto your local computer (for example to your Desktop), then navigate there from the command-line:

```sh
cd ~/Desktop/final-project-py
```

Create and activate a new Anaconda virtual environment, perhaps named "briefings-env":

```sh
conda create -n final-env python=3.7
conda activate final-env
```

Then, from within the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```



```sh
# .env example

APP_ENV="development" # or set to "production" on Heroku server

GOOGLE_SHEET_ID = "abcd123"



SENDGRID_API_KEY=""
MY_EMAIL_ADDRESS="me@example.com"

MY_NAME="John Snow"

```

> IMPORTANT: remember to save the ".env" file :-D

## Usage

## WEb App Usage
Run the app:

On Mac:
```py
$ FLASK_APP=web_app flask run
```
From within the virtual environment, ensure you can run each of the following files and see them produce their desired results of: printing today's weather forecast, and sending an example email, respectively.

```sh
python -m app.weather_service # note the module-syntax invocation
#> TODAY'S WEATHER FORECAST IS ...
```

```sh
python -m app.email_service # note the module-syntax invocation
#> SENDING EMAIL TO ...
```

> NOTE: the Sendgrid emails might first start showing up in spam, until you designate them as coming from a trusted source (i.e. "Looks Safe")
>
> ![](https://user-images.githubusercontent.com/1328807/77856232-c7a0ff80-71c3-11ea-9dce-7a32b88701c6.png)

As long as each of those scripts works by itself, you can send the daily briefing email:

```sh
python -m app.daily_briefing # note the module-syntax invocation
```

![](https://user-images.githubusercontent.com/1328807/77860069-173ef580-71db-11ea-83c6-5897bb9f4f51.png)
