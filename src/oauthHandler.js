module.exports = function (app) {
  return function (url) {
    const config = app.get('authentication')
    const options = {
      jwt: config.jwt,
      secret: config.secret
    }

    return function (req, res, next) {
      if (req.feathers && req.feathers.payload) {
        console.log(req.feathers.payload)
        app.passport
          .createJWT(req.feathers.payload, options)
          .then(token => {
            const nextPath = req.feathers.nextPath
            console.log('nextPath', nextPath)
            console.log(`redirecting......${url}?token=${token}&next=${nextPath}`)
            res.redirect(`${url}?token=${token}&next=${nextPath}`)
          })
          .catch(error => {
            next(error)
          })
      }
    }
  }
}
