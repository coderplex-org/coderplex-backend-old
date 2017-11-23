# Coderplex Backend


**Note:** This repository uses **Python3.6** and  **Django 1.11.x**


### Deploy Docker in Production

```
docker build -t production --build-arg build_env="production" -f Dockerfile .
docker run --name coderplex-produciton  -d -p 8000:8000 production
```

### Setup in dev

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