const express = require('express')
const { connectIfConfigured, Download } = require('./db')

const app = express()

app.get('/api/health', async (_req, res) => {
  const mongo = await connectIfConfigured()
  res.json({ ok: true, mongo })
})

app.get('/api/download', async (req, res) => {
  const mongo = await connectIfConfigured()

  if (mongo.enabled && mongo.connected) {
    try {
      await Download.create({ userAgent: req.get('user-agent') || '' })
    } catch {
      // non-blocking
    }
  }

  // The file itself is served as a static asset by the React app build.
  res.redirect(302, '/curvy-snake.py')
})

// Local dev convenience (Vercel will handle the serverless runtime)
if (require.main === module) {
  const port = process.env.PORT || 3001
  app.listen(port, () => {
    // eslint-disable-next-line no-console
    console.log(`API listening on http://localhost:${port}`)
  })
}

module.exports = app
