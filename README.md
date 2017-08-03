# coderplex-backend

> Coderplex.org API server

## About

This project uses [Feathers](http://feathersjs.com). An open source web framework for building modern real-time applications.

## Getting Started

Getting up and running is as easy.

1. Make sure you have [NodeJS](https://nodejs.org/) and [npm](https://www.npmjs.com/) installed.
2. Clone this repo
    ```
    git clone https://github.com/coderplex/coderplex-backend.git
    ```
3. Install your dependencies

    ```
    cd path/to/coderplex-backend; npm install
    ```
4. Rename `.env.sample` to `.env`

    ```
    mv .env.sample .env
    ```
5. Get GitHub And LinkedIn OAUTH `client_id` and `client_secret` 
    - Follow [this guide for github](https://developer.github.com/apps/building-integrations/setting-up-and-registering-oauth-apps/registering-oauth-apps/) and [this guide for linkedin](https://developer.linkedin.com/docs/oauth2)
    - Use these as OAUTH redirect URL while registering
        - For Github `http://localhost:4000/auth/github/callback`
        - For LinkedIn `http://localhost:4000/auth/linkedin/callback`
    - And finally assign `client_id` and `client_secret` of each in `.env` file
6. Start your app with

    ```
    npm start
    ```

## Testing

Simply run `npm test` and all your tests in the `test/` directory will be run.

## Scaffolding

Feathers has a powerful command line interface. Here are a few things it can do:

```
$ npm install -g feathers-cli             # Install Feathers CLI

$ feathers generate service               # Generate a new Service
$ feathers generate hook                  # Generate a new Hook
$ feathers generate model                 # Generate a new Model
$ feathers help                           # Show all commands
```

## Help

For more information on all the things you can do with Feathers visit [docs.feathersjs.com](http://docs.feathersjs.com).

## License

Copyright (c) 2016

Licensed under the [MIT license](LICENSE).
