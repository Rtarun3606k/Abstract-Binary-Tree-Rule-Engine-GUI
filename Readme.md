### README.md

````markdown
# Rule Evaluation System

This project is a Rule Evaluation System that allows users to create, combine, and evaluate rules based on given data. The system consists of a frontend built with React and a backend built with Python.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Backend](#backend)
  - [Frontend](#frontend)
- [Running the Application](#running-the-application)
  - [Backend](#backend-1)
  - [Frontend](#frontend-1)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Node.js (v14 or higher)
- Python (v3.7 or higher)
- pip (Python package installer)
- PostgreSQL (or any other preferred database)

## Installation

### Backend

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Rtarun3606k/Abstract-Binary-Tree-Rule-Engine-GUI.git
   cd Abstract-Binary-Tree-Rule-Engine-GUI/Backend
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required Python packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   The database file will be created automatically. To view the database, you can use any SQLite viewer, such as DB Browser for SQLite.

   Download and install DB Browser for SQLite from [here](https://sqlitebrowser.org/).

### Frontend

1. **Navigate to the frontend directory:**

   ```bash
   cd ../Frontend
   ```

2. **Install the required Node.js packages:**

   ```bash
   npm install
   ```

## Running the Application

### Backend

1. **Activate the virtual environment:**

   ```bash
   source venv/bin/activate
   ```

2. **Run the Flask application:**

   ```bash
   flask run
   ```

   OR
   #for Windows

   ```bash
   python wsgi.py
   ```

   #for Linux and Mac

   ```bash
   python3 wsgi.py
   ```

   The backend server will start at `http://127.0.0.1:5000`.

### Frontend

1. **Navigate to the frontend directory:**

   ```bash
   cd Frontend
   ```

2. **Start the React application:**

   ```bash
   npm run dev
   ```

   The frontend server will start at

http

`://localhost:5173`.

## API Endpoints

- **POST /create_rule**: Create a new rule.
- **POST /combine_rules**: Combine multiple rules.
- **POST /evaluate_rule**: Evaluate
````
