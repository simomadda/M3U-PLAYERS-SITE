# Flask M3U Player

This project is a Flask web application that allows users to select a series and stream episodes using an integrated M3U player. 

## Project Structure

```
flask-m3u-player
├── app
│   ├── __init__.py          # Initializes the Flask application
│   ├── routes.py            # Defines the application routes
│   ├── templates             # Contains HTML templates
│   │   ├── index.html       # Main page for series selection
│   │   ├── series.html      # Displays available episodes for a series
│   │   └── player.html      # Contains the M3U player for streaming
│   └── static               # Contains static files
│       ├── css
│       │   └── styles.css   # Styles for the web application
│       └── js
│           └── player.js    # JavaScript for the M3U player functionality
├── m3u8Service.py           # Logic for managing M3U8 links
├── requirements.txt         # Lists dependencies for the application
└── README.md                # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-m3u-player
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   flask run
   ```

5. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- On the main page, select a series to view available episodes.
- Click on an episode to start streaming it using the integrated M3U player.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.