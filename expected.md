# Data Quality Monitor

**Module:** B9IS123 - Programming for Information Systems  
**Student:** Sahil Aslam Mokashi - 20102281  
**Lecturer:** Paul Laird  
**Dublin Business School - 2025/2026**

---

## What This Is

An information system for a small data analytics consultancy that receives CSV datasets from clients and needs to assess their quality before using them in reporting or analytics pipelines.

Users upload a CSV dataset through the web interface. The system automatically profiles it, calculates a quality score, predicts a risk level, and stores everything for review. Datasets and their quality reports can be searched, filtered, updated, and deleted through the frontend without any page refresh.

---

## System Architecture


Frontend (HTML + Vanilla JS + Fetch API)
↓
Flask REST API (Python)
↓
SQLite Database (via SQLAlchemy)
↓
Pandas Profiling + Rule-Based Risk Engine
↓
Google Cloud Storage (CSV file storage)


No page refresh. All interactions go through REST API calls.

---

## Features

- Upload CSV datasets with metadata (name, organisation, source system, domain)
- Automatic data profiling on upload (missing values, duplicates, outliers, invalid emails, schema issues)
- Quality score calculated from profiling results
- AI assisted risk prediction (Low / Medium / High) based on quality score
- Email address validation via external API during profiling
- Full CRUD operations on datasets and reviews
- Search by name, organisation, source system
- Filter by risk level, status, upload date
- Sort by quality score, upload date, name
- Review workflow (Approved / Rejected / Under Review)
- Quality report per dataset
- CSV files stored in Google Cloud Storage

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, Vanilla JavaScript, Fetch API |
| Backend | Python 3.11, Flask, Flask-SQLAlchemy |
| Database | SQLite |
| File Storage | Google Cloud Storage |
| Data Processing | Pandas |
| Email Validation | Abstract API |
| Testing | Pytest |

---

## Database Tables

- **dataset** - stores metadata for each uploaded CSV
- **quality_metrics** - stores profiling results linked to each dataset
- **review** - stores reviewer comments and status per dataset

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/datasets` | List all datasets |
| GET | `/datasets/<id>` | Get one dataset |
| POST | `/datasets` | Upload new dataset |
| PUT | `/datasets/<id>` | Update dataset |
| DELETE | `/datasets/<id>` | Delete dataset |
| POST | `/analyse` | Run profiling and risk prediction |
| GET | `/metrics/<dataset_id>` | Get quality metrics |
| GET | `/dashboard` | Dashboard summary statistics |
| GET | `/report/<dataset_id>` | Full quality report |
| GET | `/reviews/<dataset_id>` | Get reviews for a dataset |
| POST | `/reviews` | Add a review |
| PUT | `/reviews/<id>` | Update a review |

---

## Validation

The backend validates all inputs and returns appropriate HTTP status codes:

- `400` - missing required fields, wrong file type, empty file
- `404` - dataset or resource not found
- `409` - duplicate dataset name
- `500` - server error with description

---

## Running Locally

```bash
# 1. Clone the repo
git clone https://github.com/Sahil-A-Mokashi/data-quality-monitor
cd data-quality-monitor

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set environment variables
cp .env.example .env
# Fill in your GCP credentials and Abstract API key

# 5. Run
python app.py
```

Open `http://localhost:5000` in your browser.

---

## Testing

```bash
pytest tests/ -v
```

Tests cover:
- CRUD operations for datasets
- Quality score calculation
- API validation (bad input returns 400)
- Full upload to report integration test

---


## Project Structure
data-quality-monitor/
├── app.py                  # Flask application entry point
├── models.py               # SQLAlchemy database models
├── routes/
│   ├── datasets.py         # Dataset CRUD endpoints
│   ├── analysis.py         # Profiling and risk endpoints
│   └── reports.py          # Dashboard and report endpoints
├── services/
│   ├── profiler.py         # Pandas profiling logic
│   ├── risk_engine.py      # Quality score and risk prediction
│   ├── gcs_service.py      # Google Cloud Storage integration
│   └── email_validator.py  # Abstract API email validation
├── frontend/
│   ├── index.html          # Dashboard
│   ├── upload.html         # Upload page
│   ├── dataset.html        # Dataset detail page
│   └── js/
│       ├── dashboard.js
│       ├── upload.js
│       └── dataset.js
├── tests/
│   ├── test_datasets.py
│   ├── test_profiler.py
│   └── test_integration.py
├── requirements.txt
├── .env.example
├── ATTRIBUTIONS.md         # All external resources and AI assistance acknowledged
└── README.md

---

## Relationship to Research Methods Assignment

My Research Methods CA1 investigates machine learning based detection of data quality anomalies in cloud data lakes. This programming assignment builds the information system that wraps that research the frontend, REST API, database, profiling pipeline, and cloud storage that would surround an ML model in a real deployment. The ML model itself is simulated here using a rule based risk engine, designed to be replaced with a trained model from the research project later.

---

## Submission

- **Submission date:** 13 July 2026
- **GitHub:** https://github.com/Sahil-A-Mokashi/data-quality-monitor
- **Module:** B9IS123 - Programming for Information Systems
