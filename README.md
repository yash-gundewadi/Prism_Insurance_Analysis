# Prism Insurance Analysis

A comprehensive insurance data analysis project combining Power BI dashboards and a full-stack web application for insights and predictions.

## 📁 Project Structure

```
Prism_Insurance_Analysis/
│
├── powerbi/                     # Power BI Dashboards (Friend's work)
│   └── Insurance Project.pbix   # Power BI project file
│
├── web-app/                     # Full-stack Web Application
│   ├── frontend/                # React/HTML/CSS/JS frontend
│   │   ├── index.html
│   │   ├── style.css
│   │   └── script.js
│   │
│   ├── backend/                 # Flask Python backend
│   │   ├── app.py              # Main Flask application
│   │   ├── utils.py            # Utility functions
│   │   └── model.pkl           # ML model (optional)
│   │
│   ├── data/                    # Sample datasets
│   │   └── sample.csv
│   │
│   └── README.md                # Web app documentation
│
├── README.md                    # This file
├── requirements.txt             # Python dependencies
└── .gitignore                   # Git ignore rules
```

## 🎯 Overview

### Power BI Component
- Interactive dashboards for insurance data visualization
- Created and maintained by project collaborators
- Located in `powerbi/` directory

### Web Application Component
A complete full-stack application for insurance analysis:

**Frontend:**
- Modern HTML/CSS interface
- File upload functionality
- Real-time analysis display
- Responsive design

**Backend:**
- Flask REST API
- CSV data processing
- Machine learning predictions
- Statistical analysis
- CORS enabled for cross-origin requests

## 🚀 Quick Start

### 1. Activate Virtual Environment

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start Backend Server

Open a terminal and run:
```bash
python web-app/backend/app.py
```

The API will start on: `http://localhost:5000`

Keep this terminal running!

### 4. Start Frontend Server

Open a **new terminal** and run:
```bash
python -m http.server 8000
```

Then visit: `http://localhost:8000/web-app/frontend/`

### 5. Use the Application

Once loaded, you'll see **two main tabs:**

#### 📊 Dashboard Tab
- View embedded Power BI report
- Interactive insurance analytics dashboard
- Real-time visualizations

#### 🔍 Analyze Data Tab
- Upload CSV files with insurance data
- View statistical analysis
- Get ML predictions
- Download results

## 📊 Features

- ✅ Embedded Power BI Dashboard - View insurance analytics and KPIs
- ✅ CSV File Upload - Import insurance data for analysis
- ✅ Statistical Analysis - Get insights from uploaded datasets
- ✅ Machine Learning Predictions - ML-powered forecasting
- ✅ RESTful API - Backend API for data processing
- ✅ Responsive Web Interface - Works on desktop and mobile
- ✅ Real-time Results - Instant analysis feedback

## 🔌 API Endpoints

- `GET /` - API status check
- `POST /api/analyze` - Analyze uploaded CSV file
- `GET /api/health` - Health check with model status

## 📋 Technology Stack

**Frontend:**
- HTML5, CSS3, JavaScript
- Responsive design with modern UI

**Backend:**
- Flask 3.0.0
- pandas 2.1.0+
- scikit-learn 1.4.0+
- NumPy 1.26.0+

**Integration:**
- Power BI Embedded
- CORS enabled

## 🗂️ Sample Data Format

The application accepts CSV files with insurance data:

```csv
age,premium,coverage_type,risk_score,claims_count
25,500,Basic,0.3,0
35,750,Standard,0.5,1
45,1200,Premium,0.7,2
```

Sample data available in `web-app/data/sample.csv`

## 🤝 Contributing

This is a collaborative project:

- **Power BI**: Handled by project collaborators
- **Web App**: Your contribution area

To add features:

1. Create a feature branch
2. Make your changes
3. Submit a pull request

## 📝 Documentation

- Web app details: See `web-app/README.md`
- API documentation: Check `web-app/backend/app.py` docstrings
- Dependencies: See `requirements.txt`

## 🔐 Security

- CORS enabled for development
- Input validation on file uploads
- Error handling for malformed data
- Environment variables support via `.env`

## ⚙️ Future Enhancements

- [ ] Database integration (PostgreSQL)
- [ ] Advanced ML model training
- [ ] User authentication system
- [ ] Data visualization dashboard
- [ ] Mobile application
- [ ] Real-time analytics streaming
- [ ] Docker containerization

