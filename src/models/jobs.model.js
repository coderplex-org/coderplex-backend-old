// jobs-model.js - A mongoose model
//
// See http://mongoosejs.com/docs/models.html
// for more of what you can do here.
module.exports = function (app) {
  const mongooseClient = app.get('mongooseClient')
  const jobs = new mongooseClient.Schema({
    title: { type: String, required: true, trim: true },
    description: { type: String, required: true },
    payScale: { type: String, required: true },
    jobType: { type: String, required: true },
    requiredTechnologies: [{ type: String }],
    companyDetails: {
      name: { type: String, required: true },
      location: { type: String, required: true },
      website: { type: String, required: true },
      email: { type: String, required: true }
    },
    createdBy: { type: mongooseClient.Schema.Types.ObjectId, required: true },
    createdAt: { type: Date, default: Date.now },
    updatedAt: { type: Date, default: Date.now }
  })

  return mongooseClient.model('jobs', jobs)
}
