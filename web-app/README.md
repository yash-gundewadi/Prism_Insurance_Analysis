# Prism Insurance Analysis - Web App

A full-stack web application for analyzing and visualizing insurance data with ML-powered insights.

## Features

- 📊 CSV file upload and analysis
- 🤖 Machine learning predictions (when model is available)
- 🎨 Interactive frontend interface
- 🔌 RESTful backend API
- 📈 Statistical summaries and insights

## Project Structure

```
web-app/
├── frontend/              # Frontend application
│   ├── index.html        # Main HTML
│   ├── style.css         # Styling
│   └── script.js         # Client-side logic
├── backend/              # Flask API
│   ├── app.py            # Main Flask application
│   ├── utils.py          # Utility functions
│   └── model.pkl         # Pre-trained ML model (optional)
└── data/                 # Sample data
    └── sample.csv        # Example dataset
```

## Installation

### Backend Setup

1. **Navigate to the project directory:**
   ```bash
   cd web-app
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the backend server:**
   ```bash
   python backend/app.py
   ```
   The API will be available at `http://localhost:5000`

### Frontend Setup

1. **Open frontend in a browser:**
   - Simply open `frontend/index.html` in your web browser, or
   - Use a simple HTTP server:
     ```bash
     python -m http.server 8000
     ```
   - Then visit `http://localhost:8000/web-app/frontend/`

## Usage

1. Start the backend server (see Installation)
2. Open the frontend in your browser
3. Select a CSV file with insurance data
4. Click "Upload & Analyze" button
5. View the analysis results and predictions

## Sample Data

The `data/sample.csv` file contains sample insurance data with the following columns:
- `age`: Customer age
- `premium`: Insurance premium amount
- `coverage_type`: Type of coverage (Basic, Standard, Premium)
- `risk_score`: Risk assessment score (0-1)
- `claims_count`: Number of claims filed

## API Endpoints

- `GET /` - API status
- `POST /api/analyze` - Analyze CSV file
- `GET /api/health` - Health check

## Requirements

See `../requirements.txt` for backend dependencies.

## Future Enhancements

- [ ] Database integration
- [ ] Advanced ML model training
- [ ] User authentication
- [ ] Data visualization dashboard
- [ ] Real-time analytics
- [ ] Mobile app version

## Contributing

To contribute to this project, please create a new branch and submit a pull request.

## License

This project is part of the Prism Insurance Analysis initiative.
