# Online Book & Podcast Django Application

Welcome to the Online Book & Podcast Django Application. This application not only provides an interactive book reader through the "content" app but also features a podcast section, dashboard, reviews page, and an archive page that showcases a list of posted articles. 

## Features

- **Content App**: Features a multiple book reader online.
- **Podcast Section**: Listen to engaging podcasts.
- **Dashboard**: Get an overview of the application's content and statistics.
- **Reviews Page**: See reviews and feedback.
- **Archive Page**: Browse through a list of published articles.
- **Transcription**: Podcast transcriptions are sourced from [YouTube Transcript](https://youtube-transcript.streamlit.app/).

## Tech Stack

- **Django**: For web backend.
- **Django-Tailwind**: For frontend styling.

## Setting Up Locally

### Prerequisites

- Python 3.x
- pip
- virtualenv (optional, but recommended)

### Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Ocolus1/online-book-podcast.git
   cd online-book-podcast

## Set up a virtual environment (optional)

```
python3 -m venv venv
source venv/bin/activate  
```


## Install the required dependencies

```
pip install -r requirements.txt
```

## Run migrations

```
python manage.py migrate
```

## Start the development server


```
python manage.py runserver
```

## Accessing the Application Locally

You should now be able to access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Deployment Options

There are several ways to deploy a Django application. Here are a few popular ones:

- **Heroku**: This is a cloud platform that lets you deploy, manage, and scale apps. Django projects can be easily deployed to Heroku. [Heroku Deployment Guide for Django](https://devcenter.heroku.com/articles/deploying-python).

- **DigitalOcean's Django One-Click App**: DigitalOcean provides a simple way to deploy Django applications using their One-Click App. [Guide Here](https://www.digitalocean.com/community/tutorials/how-to-use-the-django-one-click-install-image).

- **AWS Elastic Beanstalk**: AWS's PaaS service for deploying web applications. [AWS Elastic Beanstalk Django Deployment Guide](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html).

> **Note**: Make sure you configure your `ALLOWED_HOSTS` and set `DEBUG` to `False` when deploying in a production environment.

## Contributing

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.
