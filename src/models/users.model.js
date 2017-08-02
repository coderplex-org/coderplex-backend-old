// users-model.js - A mongoose model
//
// See http://mongoosejs.com/docs/models.html
// for more of what you can do here.
module.exports = function (app) {
  const mongooseClient = app.get('mongooseClient')
  const users = new mongooseClient.Schema({
    username: { type: String, required: true, trim: true, minLength: 3 },
    displayName: String,
    avatarUrl: { type: String, required: true },
    email: { type: String, required: true },
    bio: { type: String, minLength: 10, maxLength: 300 },
    interestedTechnologies: [{ type: String, required: true }],
    familiarTechnologies: [{ type: String }],
    mobile: { type: String },
    discordUserName: { type: String },
    socialLinks: {
      facebook: { type: String },
      github: { type: String },
      linkedin: { type: String },
      twitter: { type: String },
      codepen: { type: String },
      blog: String,
      discord: String
    },
    company: { type: String },
    profession: { type: String },
    hirable: { type: Boolean },
    projects: [{ type: mongooseClient.Schema.Types.ObjectId }],
    location: String,
    githubId: { type: String },
    linkedinId: { type: String },
    roles: [{ type: String }],
    createdAt: { type: Date, default: Date.now },
    updatedAt: { type: Date, default: Date.now }
  })

  return mongooseClient.model('users', users)
}
