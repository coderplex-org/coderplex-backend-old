const authentication = require('feathers-authentication')
const jwt = require('feathers-authentication-jwt')

const oauth2 = require('feathers-authentication-oauth2')
const GithubStrategy = require('passport-github')
const LinkedinStrategy = require('passport-linkedin-oauth2').Strategy
const oauthHandler = require('./oauthHandler')

const logger = require('./hooks/logger')

module.exports = function () {
  const app = this
  const config = app.get('authentication')

  // Set up authentication with the secret
  app.configure(authentication(config))
  app.configure(jwt())

  app.configure(
    oauth2(
      Object.assign(
        {
          name: 'github',
          Strategy: GithubStrategy,
          scope: ['user:email'],
          handler: oauthHandler(app)(app.get('frontend-url'))
        },
        config.github
      )
    )
  )

  app.configure(
    oauth2(
      Object.assign(
        {
          name: 'linkedin',
          Strategy: LinkedinStrategy,
          scope: ['r_basicprofile', 'r_emailaddress'],
          handler: oauthHandler(app)(app.get('frontend-url'))
        },
        config.linkedin
      )
    )
  )

  // The `authentication` service is used to create a JWT.
  // The before `create` hook registers strategies that can be used
  // to create a new valid JWT (e.g. local or oauth2)
  app.service('authentication').hooks({
    before: {
      create: [authentication.hooks.authenticate(config.strategies), logger()],
      remove: [authentication.hooks.authenticate('jwt')]
    }
  })
}
