/* eslint-disable no-console */
const logger = require('winston')
const app = require('./app')
const port = app.get('port')
const server = app.listen(process.env.PORT || port)

process.on('unhandledRejection', (reason, p) =>
  logger.error('Unhandled Rejection at: Promise ', p, reason)
)

server.on('listening', () => logger.info(`Feathers application started ${app.get('host')}:${port}`))
