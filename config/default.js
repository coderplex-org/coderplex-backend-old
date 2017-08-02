if (process.env.NODE_ENV !== 'production') {
  require('dotenv').config();
}

module.exports = {
  host: 'localhost',
  port: 4000,
  public: '../public/',
  paginate: {
    default: 10,
    max: 50,
  },
  mongodb: 'mongodb://localhost:27017/coderplex_api',
  'frontend-url': 'http://localhost:3000',
  authentication: {
    secret: process.env.SECRET,
    strategies: ['jwt'],
    path: '/authentication',
    service: 'users',
    jwt: {
      header: {
        type: 'access',
      },
      audience: 'https://coderplex.org',
      subject: 'anonymous',
      issuer: 'feathers',
      algorithm: 'HS256',
      expiresIn: '1d',
    },
    github: {
      clientID: process.env.GH_CLIENT_ID,
      clientSecret: process.env.GH_CLIENT_SECRET,
    },
    linkedin: {
      clientID: process.env.LI_CLIENT_ID,
      clientSecret: process.env.LI_CLIENT_SECRET,
    },
    cookie: {
      enabled: true,
      name: 'feathers-jwt',
      httpOnly: false,
      secure: false,
    },
  },
};
