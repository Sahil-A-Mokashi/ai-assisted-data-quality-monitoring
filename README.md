# http://35.189.112.187:5000/
# Live Deployed URL


# AI-Assisted Data Quality Monitoring System

A web-based information system developed using Flask, JavaScript, SQLite and Machine Learning to analyse uploaded CSV datasets, evaluate data quality, detect anomalies, and generate interactive quality reports.

## Project Overview

1. Organisations often work with datasets collected from multiple systems. Poor data quality can lead to inaccurate reporting, incorrect business decisions and unreliable analytics.
2. In the time of AI data used for its training is of very high importance, since a model trained on a better piece of data will always work better

The AI-Assisted Data Quality Monitoring System provides a simple web-based platform where users can upload CSV datasets and automatically receive a quality assessment.

The application analyses uploaded datasets, calculates data quality metrics, predicts risk levels using a machine learning model and generates interactive reports to help users understand the overall quality of their data.

The system follows a client-server architecture where the frontend communicates with the Flask backend through REST API calls without traditional page refreshes.


## Features

The system provides a range of features to help users upload, analyse and manage datasets through a simple web interface.

- Upload CSV datasets with additional metadata such as organisation, source system and domain.
- Store datasets as either **Public** or **Private**, allowing users to control who can access their reports.
- User registration and login with password hashing for secure authentication.
- Interactive dashboard displaying dataset statistics, quality scores and predicted risk levels.
- Search, filter and sort datasets based on different criteria.
- Automatic calculation of data quality metrics including completeness, missing values and duplicate records.
- Machine learning based anomaly detection and risk prediction using a trained classification model(TODO).
- Detailed dataset report with interactive charts and AI-generated quality insights.
- REST API architecture where the frontend communicates with the backend using JavaScript Fetch API.
- Responsive interface built with Bootstrap and Chart.js for a clean user experience.


## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend programming language |
| Flask | REST API and web application framework |
| JavaScript | Dynamic frontend and API communication |
| HTML5 & CSS3 | User interface |
| Bootstrap 5 | Responsive layout and styling |
| Chart.js | Interactive charts and dashboard visualisation |
| SQLite | Database storage |
| SQLAlchemy | Object Relational Mapping (ORM) |
| Scikit-learn | Machine learning model for anomaly detection |
| Pandas | CSV processing and data analysis |
| Git & GitHub | Version control and source code management |



## System Architecture

The application follows a simple client-server architecture.

- The frontend is built using HTML, CSS, Bootstrap and JavaScript.
- JavaScript communicates with the backend using the Fetch API, allowing data to be loaded dynamically without refreshing the page.
- The backend is developed using Flask and exposes REST API endpoints for dataset management, reporting and authentication.
- Uploaded dataset information is stored in an SQLite database using SQLAlchemy.
- A machine learning model analyses(currently rule based logic) each uploaded dataset and predicts its overall risk level based on calculated quality metrics.
- Chart.js is used to display interactive visualisations on both the dashboard and dataset report pages.

### Architecture Workflow

```
            User
              │
              ▼
     HTML / Bootstrap UI
              │
      JavaScript (Fetch API)
              │
              ▼
        Flask REST API
              │
     ┌────────┴────────┐
     │                 │
     ▼                 ▼
 SQLite Database   ML Analysis Engine/ Rule based logic
     │                 │
     └────────┬────────┘
              ▼
     Dashboard & Reports
```



## Project Structure

```
ai-assisted-data-quality-monitoring/
│
├── app.py                      # Application entry point
├── database.py                 # Database configuration
├── models.py                   # SQLAlchemy models
├── requirements.txt            # Python dependencies
│
├── routes/
│   ├── auth.py                 # Login and registration
│   ├── datasets.py             # Dataset APIs
│   └── reports.py              # Report APIs
│
├── services/
│   ├── risk_engine.py           # Machine learning analysis
│   └── profiler.py      # Data quality calculations
│
├── templates/
│   ├── index.html
│   ├── upload.html
│   ├── login.html
│   ├── register.html
│   └── dataset-details.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── tests/
│
└── screenshots/
```
