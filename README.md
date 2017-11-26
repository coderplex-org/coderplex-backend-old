# Coderplex Backend

**Note:** This repository uses **Python3.6** and **Django 1.11.x**

## Deploy Docker in Production

```bash
docker build -t production --build-arg build_env="production" -f Dockerfile .
docker run --name coderplex-produciton  -d -p 8000:8000 production
```

## Setup in dev

```bash
git clone git://github.com/coderplex/coderplex-backend.git
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements/requirements.txt
```

### Running in local

```bash
source venv/bin/activate # python3
python webapp/manage.py runserver # server accessible at localhost:8000
```

Check [this](API.md) for API Endpoints

## Instructions for setting things up for `local` environment

* Add environment variables for **EMAIL_HOST_USER** and **EMAIL_HOST_PASSWORD** and set those with your **email** and
  **password**

### For Testing Github Login Locally

* Create a Github OAuth App [here](https://github.com/settings/applications/new)
* Set the authorization callback url to **[http://127.0.0.1:8000/callback](http://127.0.0.1:8000/callback)**
* Open the created Oauth App from [here](https://github.com/settings/developers) and copy **client_id** and
  **client_secret**
* Now Open [Django Admin Panel](http://127.0.0.1:8000/admin)
* Create a New Social Application with **Provider** as **Github** and **client_id** and **client_secret** as copied in
  the above step.
* Now you can test the Github Login by visiting `/v1/auth/github` route

### For Testing Linkedin Login Locally

* Create a Github OAuth App [here](https://www.linkedin.com/developer/apps/new)
* Set the authorization callback url to **[http://127.0.0.1:8000/callback](http://127.0.0.1:8000/callback)**
* Open the created Oauth App from [here](https://www.linkedin.com/developer/apps) and copy **client_id** and
  **client_secret**
* Now Open [Django Admin Panel](http://127.0.0.1:8000/admin)
* Create a New Social Application with **Provider** as **LinkedIn** and **client_id** and **client_secret** as copied in
  the above step.
* Now you can test the Github Login by visiting `/v1/auth/linkedin` route

## Instructions for setting things up for `production` environment

* Follow all Instructions that are stated above
* Additionally, Set environment variables **LINKEDIN_CALLBACK_URL** and **GITHUB_CALLBACK_URL** as **base_url +
  "/callback"**
