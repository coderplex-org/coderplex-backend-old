# Coderplex Backend


**Note:** This repository uses **Python3.6** and  **Django 1.11.x**

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


## APIs List

1. http://localhost:8000/books
2. http://localhost:8000/book/laravel-curiculum
3. http://localhost:8000/book/laravel-curiculum/c/chapter-1
4. http://localhost:8000/book/laravel-curiculum/c/chapter-1/introduction-to-laravel
