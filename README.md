# 📊 Financial Automation & Report Generator

A Python application that automates financial data processing, generates
financial reports, and sends them via email.\
The project includes a **web interface built with Flask** that allows
users to upload a CSV file containing financial transactions and
automatically generate reports.

------------------------------------------------------------------------

# 🚀 Overview

This project demonstrates backend and automation skills using Python.

The system:

1.  Loads financial transaction data from a CSV file
2.  Processes and analyzes the data
3.  Generates financial reports
4.  Sends reports via email
5.  Provides a web interface for uploading files and triggering the
    workflow

------------------------------------------------------------------------

# ⚙️ Features

-   Upload transaction files via web interface
-   Process financial data using Pandas
-   Generate automated financial reports
-   Export reports in multiple formats:
    -   PDF
    -   Excel
-   Automatically send reports via email
-   Modular backend architecture
-   Automated testing with pytest

------------------------------------------------------------------------

# 🧱 Project Structure

    financial_automation/
    │
    ├── reports/
    │
    ├── src/
    │   ├── __init__.py
    │   ├── email_sender.py
    │   ├── loader.py
    │   ├── main.py
    │   ├── pdf_generator.py
    │   ├── processor.py
    │   └── report_generator.py
    │
    ├── tests/
    │   ├── __init__.py
    │   └── test_processor.py
    │
    ├── webapp/
    │   ├── __init__.py
    │   ├── app.py
    │   ├── uploads/
    │   ├── reports/
    │   └── templates/
    │       └── index.html
    │
    ├── .env
    ├── .gitignore
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

# 🌐 Web Application

The project includes a simple web interface built with Flask.

Users can:

-   Upload a CSV file with financial transactions
-   Provide one or more email addresses
-   Automatically generate reports
-   Send the reports via email

## Run the web application

    python webapp/app.py

Then open your browser:

    http://127.0.0.1:5000

------------------------------------------------------------------------

# 🧾 Expected CSV Format

Example:

    date,description,category,type,amount
    2024-01-01,Groceries,Food,expense,-50
    2024-01-02,Salary,Income,3000
    2024-01-03,Internet,Bills,expense,-80

------------------------------------------------------------------------

# 📄 Generated Reports

The application generates:

-   **Excel financial report**
-   **PDF financial report**

Reports are saved in:

    webapp/reports/

------------------------------------------------------------------------

# 📧 Email Automation

The system automatically sends generated reports via email.

Configuration is done through environment variables in the `.env` file.

Example:

    EMAIL_USER=your_email@gmail.com
    EMAIL_PASSWORD=your_app_password

The project uses SMTP to send emails with the generated reports
attached.

------------------------------------------------------------------------

# 🧪 Running Tests

The project includes automated tests using pytest.

Run:

    pytest

------------------------------------------------------------------------

# 🛠️ Technologies Used

-   Python
-   Flask
-   Pandas
-   OpenPyXL
-   ReportLab
-   Pytest

------------------------------------------------------------------------

# 🎯 Purpose of the Project

This project was built as a portfolio project to demonstrate skills in:

-   Backend development
-   Data processing
-   Automation
-   Report generation
-   Web integration
-   Software testing

------------------------------------------------------------------------

# 👨‍💻 Author

Romulo Araujo Correa

Backend developer / Data Analyst.

GitHub: https://github.com/RomSNM
