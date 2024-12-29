<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <h1>Real Time Lyrics Project</h1>
    <p>This project listens to music and displays real-time lyrics!</p>
  </header>
  
  <section id="about">
    <h2>About the Project</h2>
    <p>
      The Real Time Lyrics project listens to the audio being played on your system and matches it to available lyrics in real-time. It uses libraries like `sounddevice` to record audio and fetches lyrics dynamically.
    </p>
  </section>

  <section id="directory-structure">
    <h2>Directory Structure</h2>
    <pre>
      <code>
        Real-Time-Lyrics/
        ├── main.py              # Main Python script to run the project
        ├── requirements.txt     # List of dependencies
        ├── README.md            # Project documentation
        ├── index.html           # Web interface for the project
        ├── style.css            # Basic styling for the HTML page
      </code>
    </pre>
  </section>

  <section id="requirements">
    <h2>Requirements</h2>
    <p>This project requires the following Python libraries:</p>
    <ul>
      <li><strong>sounddevice</strong> - To record audio from your microphone.</li>
      <li><strong>lyricsgenius</strong> - To fetch lyrics dynamically.</li>
      <li><strong>requests</strong> - To make HTTP requests for lyrics fetching.</li>
      <li><strong>pyttsx3</strong> - For text-to-speech functionality (optional).</li>
    </ul>
    <p>You can install all the required dependencies using:</p>
    <pre><code>pip install -r requirements.txt</code></pre>
  </section>

  <section id="installation">
    <h2>Installation and Setup</h2>
    <ol>
      <li>Clone the repository:</li>
      <pre><code>git clone https://github.com/Gautamgrove/RealTimeLyrics.git</code></pre>
      <li>Navigate to the project directory:</li>
      <pre><code>cd Real-Time-Lyrics</code></pre>
      <li>Install the required dependencies:</li>
      <pre><code>pip install -r requirements.txt</code></pre>
      <li>Run the project:</li>
      <pre><code>python main.py</code></pre>
    </ol>
  </section>

  <section id="usage">
    <h2>How to Use</h2>
    <ol>
      <li>Start the script `main.py` from the terminal.</li>
      <li>The application will listen to your system's audio and fetch lyrics for the currently playing song.</li>
      <li>The lyrics will be displayed in real-time.</li>
    </ol>
  </section>

  <section id="contributing">
    <h2>Contributing</h2>
    <p>If you'd like to contribute to this project, follow these steps:</p>
    <ul>
      <li>Fork the repository</li>
      <li>Clone your fork:</li>
      <pre><code>git clone https://github.com/Gautamgrove/RealTimeLyrics.git</code></pre>
      <li>Make your changes and create a pull request.</li>
    </ul>
  </section>

  <section id="license">
    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
  </section>

  <footer>
    <p>&copy; 2024 Real Time Lyrics Project. All rights reserved.</p>
  </footer>
</body>
</html>
