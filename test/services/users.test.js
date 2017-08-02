const expect = require('expect')
const faker = require('faker')
const app = require('../../src/app')

describe("'users' service", () => {
  it('registered the service', () => {
    const service = app.service('users')
    expect(service).toExist()
  })
  it('should register new user', done => {
    const service = app.service('users')
    const technologies = []
    for (let i = 0; i < Math.floor(Math.random() * (10 - 1)); i++) {
      technologies.push(faker.name.jobType())
    }
    const user = {
      username: faker.internet.userName(),
      displayName: faker.name.firstName(),
      avatarUrl: faker.internet.avatar(),
      email: faker.internet.email(),
      bio: faker.lorem.paragraph(),
      mobile: faker.phone.phoneNumber(),
      roles: ['user'],
      company: `${faker.company.companyName()} ${faker.company.companySuffix()}`,
      blog: faker.internet.url(),
      hirable: true,
      location: faker.address.state(),
      interestedTechnologies: technologies
    }
    service
      .create(user)
      .then(savedUser => {
        expect(savedUser).toExist()
        expect(savedUser.username).toBe(user.username)
        done(null)
      })
      .catch(done)
  })
})
