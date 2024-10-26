# Rule Evaluation System

A Rule Evaluation System that enables users to create, combine, and evaluate rules based on given data. This system includes a frontend built with React and a backend built with Python.

---

## Table of Contents

- [Video Overview](#video-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Running the Application](#running-the-application)
  - [Backend](#backend)
  - [Frontend](#frontend)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Video Overview

_Coming soon!_ – This video will give an in-depth walkthrough of the Rule Evaluation System, showcasing its features and demonstrating how to create, combine, and evaluate rules.

---

## Prerequisites

To run this project, you’ll need the following installed:

- **Node.js** (v14 or higher)
- **Python** (v3.7 or higher)
- **pip** (Python package installer)
- **PostgreSQL** (or any other preferred database)

---

## Installation

### Backend Setup

1. **Clone the Repository:**

   ```bash
   
   git clone https://github.com/Rtarun3606k/Abstract-Binary-Tree-Rule-Engine-GUI.git
   cd Abstract-Binary-Tree-Rule-Engine-GUI/Backend
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux and macOS
   ```

   ```bash
   venv\Scripts\activate  # For Windows
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database:**
   The database file will be generated automatically. You can view it using an SQLite viewer such as [DB Browser for SQLite](https://sqlitebrowser.org/).

### Frontend Setup

1. **Navigate to the Frontend Directory:**

   ```bash
   cd ../Frontend
   ```

2. **Install Node.js Packages:**

   ```bash
   npm install
   ```

---

## Running the Application

### Backend

1. **Activate the Virtual Environment:**

   ```bash
   source venv/bin/activate  # For Linux and macOS
   ```

   ```bash
   venv\Scripts\activate  # For Windows
   ```

2. **Run the Flask Application:**

   ```bash
   flask run
   ```

   Alternatively, you can start the server using the `wsgi.py` script:

   ```bash
   python wsgi.py  # For Windows
   python3 wsgi.py  # For Linux and macOS
   ```

   The backend server will start at `http://127.0.0.1:5000`.

### Frontend

1. **Navigate to the Frontend Directory:**

   ```bash
   cd Frontend
   ```

2. **Start the React Application:**

   ```bash
   npm run dev
   ```

   The frontend server will start at `http://localhost:5173`.

---

## API Endpoints

- **POST /create_rule**: Create a new rule by defining conditions and assigning a rule name.
- **POST /combine_rules**: Combine multiple rules to create a compound rule with a specified name.
- **POST /evaluate_rule**: Evaluate a rule against a dataset to determine if the rule conditions are met.

---

## Usage

This system is designed to handle rule-based evaluations for various data conditions. Through the API endpoints, you can:

1. **Create Rules**: Define rules using conditions and variables relevant to your data.
2. **Combine Rules**: Merge multiple rules to form complex logical expressions.
3. **Evaluate Rules**: Test rules against datasets to check if specified conditions are met.

For more details, watch the [video overview](#video-overview) (coming soon!) to see the system in action.

---

## Contributing

Contributions are welcome! Please fork this repository, create a branch for your feature or bug fix, and submit a pull request with a clear description of your changes.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
