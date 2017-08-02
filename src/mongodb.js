const mongoose = require('mongoose')

module.exports = function () {
  const app = this

  mongoose.connect(process.env.MONGO_URL || app.get('mongodb'))
  mongoose.Promise = global.Promise

  app.set('mongooseClient', mongoose)
}
