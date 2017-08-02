const path = require('path')
const favicon = require('serve-favicon')
const compress = require('compression')
const cors = require('cors')
const helmet = require('helmet')
const bodyParser = require('body-parser')

const feathers = require('feathers')
const configuration = require('feathers-configuration')
const hooks = require('feathers-hooks')
const rest = require('feathers-rest')
const socketio = require('feathers-socketio')

const handler = require('feathers-errors/handler')
const notFound = require('feathers-errors/not-found')

const middleware = require('./middleware')
const services = require('./services')
const appHooks = require('./app.hooks')

const mongodb = require('./mongodb')

const authentication = require('./authentication')

const app = feathers()

// Load app configuration
app.configure(configuration(path.join(__dirname, '..')))
// Enable CORS, security, compression, favicon and body parsing
app.use(cors())
app.use(helmet())
app.use(compress())
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }))
app.use(favicon(path.join(app.get('public'), 'favicon.ico')))
// Host the public folder
app.use('/', feathers.static(app.get('public')))
// Configure other middleware (see `middleware/index.js`)
app.configure(middleware)

// Set up Plugins and providers
app.configure(hooks())
app.configure(mongodb)
app.configure(rest())
app.configure(socketio())

app.use(function (req, res, next) {
  console.log('*path*', req.path)
  console.log('**query**', req.query.next)
  if ((req.path === '/auth/github' || req.path === '/auth/linkedin') && req.query.next) {
    app.set('nextPath', req.query.next)
  } else if (req.path !== '/auth/github/callback' || req.path !== '/auth/linkedin/callback') {
    app.set('nextPath', '/profile')
  }
  if (req.path === '/auth/github/callback' || req.path === '/auth/linkedin/callback') {
    console.log('**nextPath**', app.get('nextPath'))
    req.feathers.nextPath = app.get('nextPath')
  }
  next()
})

app.configure(authentication)

// Set up our services (see `services/index.js`)
app.configure(services)
// Configure a middleware for 404s and the error handler
app.use(notFound())
app.use(handler())

app.hooks(appHooks)

module.exports = app
