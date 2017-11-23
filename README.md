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


API endpoints
=============

Basic Authentication
--------------------

- `https://github.com/login/oauth/authorize`(GET)
    >    - scope  (optional)
    >    - client_id

    > returns `code`

- `https://www.linkedin.com/oauth/v2/authorization`(GET)
    >    - scope   (optional)
    >    - client_id
    >    - response_type
    >    - redirect_uri

    > returns `code`

    > `response_type` should take `code` as its value

- `/v1/auth/<social>` (POST)
    > social can be replaced by `github` or `linkedin`
    >    - code

    > returns
     
     ```json
        {
            "token": "",
            "user": {
                "pk": ,
                "username": "",
                "first_name": "",
                "last_name": "",
                "avatar": ""
            }
         }
    ```   

Other APIs
-----------

- `/book/<slug>` (GET)
    > returns
    - `/v1/auth/<social>` (POST)
    > social can be replaced by `github` or `linkedin`
    >    - code

    > returns
     
     ```json
        {
            "id": "",
            "title": "",
            "slug": "",
            "image": "",
            "description": "",
            "chapters": [],
            "updated_by": {
                    "first_name": "",
                    "last_name": ""
             },
            "created_by": {
                "first_name": "",
                "last_name": ""
             }
         }
    ```   
 
    

- `/books` (GET)
    > returns list of books