const mongoose = require('mongoose')

const DownloadSchema = new mongoose.Schema(
  {
    createdAt: { type: Date, default: Date.now },
    userAgent: { type: String, default: '' },
  },
  { collection: 'downloads' },
)

const Download =
  mongoose.models.Download || mongoose.model('Download', DownloadSchema)

let connectPromise = null

async function connectIfConfigured() {
  const uri = process.env.MONGODB_URI
  if (!uri) return { enabled: false, connected: false }

  if (!connectPromise) {
    connectPromise = mongoose
      .connect(uri, { serverSelectionTimeoutMS: 2000 })
      .then(() => true)
      .catch(() => false)
  }

  const connected = await connectPromise
  return { enabled: true, connected }
}

module.exports = { connectIfConfigured, Download }
