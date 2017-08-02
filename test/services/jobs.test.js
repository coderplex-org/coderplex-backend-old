const expect = require('expect')
const faker = require('faker')
const app = require('../../src/app')

const jobTypes = ['FullTime', 'PartTime', 'Remote', 'Consulting', 'Freelance']

describe("'jobs' service", () => {
  it('registered the service', () => {
    const service = app.service('jobs')

    expect(service).toExist()
  })
  it('should create a new job', done => {
    const jobsService = app.service('jobs')
    const usersService = app.service('users')
    usersService
      .find({})
      .then(users => {
        // console.log(users)
        let technologies = []
        for (let i = 0; i < Math.floor(Math.random() * (10 - 1)); i++) {
          technologies.push(faker.name.jobType())
        }
        const job = {
          title: faker.name.title(),
          description: faker.lorem.paragraph(),
          jobType: jobTypes[Math.floor(Math.random() * (jobTypes.length - 1))],
          requiredTechnologies: technologies,
          companyDetails: {
            name: `${faker.company.companyName()} ${faker.company.companySuffix()}`,
            location: faker.address.state(),
            website: faker.internet.url(),
            email: faker.internet.email()
          },
          payScale: {
            from: faker.finance.amount(),
            to: faker.finance.amount(),
            currency: faker.finance.currencyCode()
          },
          createdBy: users.data[Math.floor(Math.random() * 2)]._id
        }
        jobsService
          .create(job)
          .then(savedJob => {
            expect(savedJob).toExist()
            expect(savedJob.title).toBe(job.title)
            expect(savedJob.createdBy).toEqual(users.data[0]._id)
            done(null)
          })
          .catch(done)
      })
      .catch(done)
  })
})
