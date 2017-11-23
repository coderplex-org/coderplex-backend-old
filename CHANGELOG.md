# Changelog
All notable changes to this project will be documented in this file.

## [Pull Request [#12](https://github.com/coderplex/coderplex-backend/pull/12)]
### Added
- **Github Login** and **Linkedin Login** based on [django-allauth](https://django-allauth.readthedocs.io/en/latest/)

### Changed
- Changed **README.md** to add new API endpoints

### API EndPoints

#### Added

- `https://github.com/login/oauth/authorize`(GET)
    >    - scope  (optional)
    >    - client_id

    > returns `code`
    
    - **Example Request**:
    
      **GET `https://github.com/login/oauth/authorize?scope=user:email&client_id=97d600c69373091ac0`**          
      
- `https://www.linkedin.com/oauth/v2/authorization`(GET)
    >    - scope   (optional)
    >    - client_id
    >    - response_type
    >    - redirect_uri

    > returns `code`

    > `response_type` should take `code` as its value
    
    - **Example Request**:
    
        **GET `https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=81ps4wm9kflx&redirect_uri=http://127.0.0.1:8000/callback&scope=r_basicprofile`**

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
    
    - **Example Requests**:
    
        - **POST `http://127.0.0.1:8000/v1/auth/github`**
        
            **data** in `application/json` form
            ```json
              {
                 "code" : "f9f2d53daa483c8821a"
              }
    
            ```
            
        - **POST `http://127.0.0.1:8000/v1/auth/linkedin`**
        
            **data** in `application/json` form
            ```json
              {
                 "code" : "AQSRSzH9xn-SgYKCRjixNz6vWjdj6_Np6ef7LFPKA4L6hHzT9C-GTtiwM8uTR1eYqD1OorjgdtrpRMLgkasogSG53etnZ8H4xA9g-_LX9aZ4iGfP7QZE5sLBmog8QWZeWRrtF0l2GtnFZa0KzrTI03iv2hhNig"
              }
    
            ```