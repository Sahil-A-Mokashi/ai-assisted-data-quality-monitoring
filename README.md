# http://35.189.112.187
**Live Deployed URL**
## https://github.com/Sahil-A-Mokashi/ai-assisted-data-quality-monitoring
**github link**
# AI-Assisted Data Quality Monitoring System
# Assignment Cover Sheet

**Student Name:** Sahil Aslam Mokashi

**Student Number:** 20102281

**Programme:** MSc Information Systems with Computing

**Lecturer Name:** Paul Laird

**Module Title:** Programming for Information Systems (B9IS123)

**Assignment Title:** AI-Assisted Data Quality Monitoring System

---

### Student Declaration

By submitting this assignment, I confirm that:

- This assignment is entirely my own work.
- Any external sources used have been appropriately referenced.
- I have followed the Generative AI guidance provided in the assignment brief.
- I understand the College regulations regarding academic integrity.
- I understand that all submitted work may be checked for similarities with other submissions.

---


# AI-Assisted Data Quality Monitoring System

A web-based information system developed using Flask, JavaScript, SQLite and Rule Based/Machine Learning to analyse uploaded CSV datasets, evaluate data quality, detect anomalies, and generate interactive quality reports.

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

## Project Links

| Component | Description | URL |
|-----------|-------------|-----|
| Frontend Application | User Interface | http://35.189.112.187 |
| Backend REST API | Flask API Service | http://35.189.112.187/datasets |
| Backend Dataset Reports | Dataset Analysis Interface | http://35.189.112.187/dataset/1 |
| Dashboard | Dashboard Interface | http://35.189.112.187 |
| Upload Module | Dataset Upload Interface | http://35.189.112.187/upload |
| Authentication | Login & Registration | http://35.189.112.187/login |
| Source Code | GitHub Repository | https://github.com/Sahil-A-Mokashi/ai-assisted-data-quality-monitoring |



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


## Installation

### Prerequisites

Before running the project, make sure the following software is installed:

- Python 3.11 or later
- Git
- pip (Python package manager)

### Clone the Repository

```bash
git clone https://github.com/Sahil-A-Mokashi/ai-assisted-data-quality-monitoring.git

cd ai-assisted-data-quality-monitoring
```

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Once the server starts, open the application in your browser.

```
http://127.0.0.1:5000
```

## Using the Application

After launching the application, users can perform the following tasks:

1. Register a new account or log in using an existing account.
2. Upload a CSV dataset along with metadata such as organisation, source system and domain.
3. Choose whether the dataset should be public or private.
4. View uploaded datasets from the dashboard.
5. Search, filter and sort datasets using the available controls.
6. Open the dataset report to view quality metrics, AI predictions and interactive charts.
7. Review recommendations generated from the data quality analysis.

## REST API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Dashboard page |
| GET | `/dashboard` | Dashboard statistics |
| GET | `/datasets` | Retrieve all datasets |
| POST | `/datasets` | Upload a new dataset |
| GET | `/reports/<id>` | Retrieve dataset report |
| GET | `/login` | Login page |
| POST | `/login` | User login |
| GET | `/register` | Registration page |
| POST | `/register` | Create a new user |
| GET | `/logout` | Log out current user |


## Machine Learning Workflow

The application includes a simple machine learning workflow that evaluates the quality of uploaded datasets and predicts an overall risk level.

### Data Processing

When a CSV file is uploaded:

- The file is read using the Pandas library.
- Basic data quality metrics are calculated.
- Missing values, duplicate rows, total rows and total columns are identified.
- A quality score is calculated based on these metrics.

### AI Analysis [this will be implemented as part of applied reseach methods module]

The calculated metrics are passed to a trained machine learning model built using Scikit-learn.

The model predicts one of three possible risk levels:

- Low Risk
- Medium Risk
- High Risk

The prediction is then stored in the database and displayed throughout the application.

### Report Generation

For every uploaded dataset, the system automatically generates a report containing:

- Overall quality score
- Data quality breakdown
- AI predicted risk level
- Data quality metrics
- Interactive charts
- Suggested future improvements

This allows users to quickly understand the quality of their datasets without manually analysing the data.


## Testing

Testing was carried out throughout the development process to verify that the main features of the application worked correctly.

### Functional Testing

The following functionality was manually tested:

- User registration
- User login and logout
- Dataset upload
- Public and private dataset visibility
- Dataset search
- Dataset filtering
- Dataset sorting
- Dataset report generation
- Dashboard statistics
- Access control for private datasets

### Unit Testing

Unit tests were created to verify important backend functionality, including:

- Dataset creation
- Dataset retrieval
- Data quality calculations
- Report generation
- Authentication logic

Tests are available in the **tests/** directory.

### Integration Testing

Integration testing was performed to ensure that the frontend and backend communicate correctly through the REST API.

The following interactions were verified:

- Uploading datasets through the web interface
- Loading dashboard statistics using Fetch API
- Displaying dataset reports
- Retrieving AI analysis results
- User authentication and session handling

Overall, testing confirmed that the system behaves as expected and that the main workflows operate correctly.


## Future Improvements

Although the application meets the current project requirements, there are several enhancements that could be implemented in the future.

- Deploy the application using Docker and automate deployments with GitHub Actions.
- Replace the SQLite database with Cloud SQL for improved scalability.
- Store uploaded datasets in cloud storage instead of the local file system.
- Create a Ml Moel and later Improve the machine learning model by training it on larger and more diverse datasets.
- Add email verification, password reset and multi-factor authentication.
- Introduce role-based access control with separate Administrator and Standard User accounts.
- Generate downloadable PDF reports containing quality metrics and AI analysis.
- Provide historical quality tracking to compare dataset quality over time.
- Integrate real-time notifications when high-risk datasets are uploaded.
- Add interactive dashboards with additional charts and business intelligence visualisations.


## Acknowledgements

The following technologies and resources were used during the development of this project.

### Software and Libraries

- Python
- Flask
- SQLAlchemy
- SQLite
- JavaScript
- Bootstrap 5
- Chart.js
- Pandas
- NumPy
- Scikit-learn
- Git and GitHub

### Development Tools

- PyCharm
- Visual Studio Code
- Google Chrome Developer Tools
- Google Cloud Platform (GCP)

### AI Assistance

Generative AI tools were used during the development process to assist with:

- Brainstorming ideas
- Debugging code
- Improving documentation with tables and structure charts
- Explaining programming concepts
- Refining user interface layouts, dataset details.html and output.html page generated by AI along with its bootstrap/css content.
- js and bootstrap content was implemented with the help of ai for syntax, logic flow improvement, simpifying processess, Boiler/generic code was generated, then based upon that code i implemented what i actually wanted to for my project, example ai generates a user module, as i dont need a full fledged user handling, i would see how that was implemented and then based upon that write a smaller one thats follows the pattern. similar pattern i then use for a other module by comapring the requirements i have for that against how this was built.

All generated suggestions were reviewed, modified and integrated by the author before being included in the final solution.
link - https://claude.ai/share/b5e36da2-8946-4c02-8f7c-4ea44eb088bb


## Conclusion

The AI-Assisted Data Quality Monitoring System demonstrates the development of a modern web-based information system using a client-server architecture.

The project combines data storage, REST APIs, authentication, machine learning and interactive data visualisation to provide an easy-to-use platform for analysing dataset quality.

Throughout the project, emphasis was placed on clean architecture, API-driven communication, responsive user interface design and practical software engineering principles. The completed application satisfies the functional requirements of the assignment while providing a strong foundation for future enhancements and real world deployment.

## Deployment

The application has been successfully deployed on a Google Cloud Platform (GCP) Virtual Machine.

### Deployment Environment

- Platform: Google Cloud Platform (GCP)
- Compute Service: Compute Engine Virtual Machine
- Operating System: Ubuntu Linux
- Backend: Flask
- Database: SQLite
- Version Control: GitHub

The application can be accessed through the deployed server using the assigned public IP address.

### Deployment Process

The deployment process consists of the following steps:

1. Clone the GitHub repository onto the virtual machine.
2. Create and activate a Python virtual environment.
3. Install all required project dependencies.
4. Start the Flask application.
5. Access the application through the virtual machine's public IP address.

### Screenshots
Screenshots were added in the test folder that show the use of postman for testing all the backend api's once they started working in local machine in development process





