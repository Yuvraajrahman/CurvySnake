import './App.css'

function App() {
  const directFile =
    'https://github.com/Yuvraajrahman/CurvySnake/raw/main/Group8%20cse423%20sping%202023%20project.py'
  const apiDownload = '/api/download'

  return (
    <div className="page">
      <header className="header">
        <div className="brand">CurvySnake</div>
        <nav className="nav">
          <a href="#download">Download</a>
          <a href="#run">How to run</a>
        </nav>
      </header>

      <main className="main">
        <section className="hero">
          <h1>Curvy Snake (Python)</h1>
          <p className="subtitle">
            A smooth, curve-based snake game built with Pygame. Download the
            script, install dependencies, and run.
          </p>

          <div id="download" className="ctaRow">
            <a
              className="button primary"
              href={directFile}
              target="_blank"
              rel="noreferrer"
            >
              Download .py (from GitHub)
            </a>
            <a className="button" href={apiDownload}>
              Download via API
            </a>
          </div>

          <div className="card">
            <h2 id="run">Run locally</h2>
            <ol className="steps">
              <li>
                Install Python 3 and Pygame:
                <div className="codeRow">
                  <code>pip install pygame</code>
                </div>
              </li>
              <li>
                Run the game:
                <div className="codeRow">
                  <code>python "Group8 cse423 sping 2023 project.py"</code>
                </div>
              </li>
            </ol>
            <p className="hint">
              Tip: At startup press <strong>1</strong>, <strong>2</strong>, or{' '}
              <strong>3</strong> to pick difficulty.
            </p>
          </div>
        </section>
      </main>

      <footer className="footer">
        <span>© {new Date().getFullYear()} CurvySnake</span>
      </footer>
    </div>
  )
}

export default App
