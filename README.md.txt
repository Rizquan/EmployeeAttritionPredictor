📘 Employee Attrition Predictor

A machine learning project that predicts whether an employee is likely to leave the company based on demographic, performance, satisfaction, and organizational factors.

This is a complete end-to-end ML workflow including MySQL integration, data preprocessing, model training, evaluation, and visualization.

🚀 Project Overview

Employee attrition is a major concern for HR departments. This project builds a predictive model to estimate the likelihood of an employee leaving, helping companies take proactive action.

This system includes:

✔ MySQL database to store employee data

✔ Data loading via Python (database_connector.py)

✔ Preprocessing: encoding, scaling, cleaning

✔ Model training using TensorFlow / Scikit-Learn

✔ Visual EDA & correlation analysis

✔ Model saving and loading (model_loader.py)

✔ Organized file structure suitable for professional ML projects

📂 Project Structure
EmployeeAttritionPredictor/
│
├── data/
│   └── sample_data.csv
│
├── sql/
│   └── create_tables.sql
│
├── scripts/
│   ├── database_connector.py
│   └── model_loader.py
│
├── notebooks/
│   ├── data_preprocessing.ipynb
│   └── model_training.ipynb
│
├── models/
│   └── attrition_model.pkl
│
└── README.md

🛠 Technologies Used
Languages

Python

SQL

Libraries

Pandas

NumPy

Matplotlib

Seaborn

Scikit-Learn

TensorFlow / Keras

MySQL Connector

Tools

VS Code / Jupyter Notebook

MySQL Workbench

GitHub for version control

📊 Exploratory Data Analysis

The project includes several visual insights such as:

Gender vs Years at Company (Line Chart)

Job Role vs Average Monthly Income (Line Chart)

Department vs Job Satisfaction (Bar Chart)

Overtime Distribution (Pie Chart)

Correlation Heatmap

Attrition vs Job Satisfaction

Performance Rating vs Income

These help understand patterns before model training.

🔧 Data Preprocessing Steps

The preprocessing notebook includes:

Handling missing values

One-hot encoding:

gender, department, job_role

Binary conversion:

overtime, attrition (Yes/No → 1/0)

Feature scaling using StandardScaler

Train-test split

Exporting cleaned data for model training

🤖 Model Training

The model is trained to predict attrition (1 = Yes, 0 = No):

Models used:

Logistic Regression

Random Forest Classifier

TensorFlow Sequential Neural Network

Each model is evaluated using:

Accuracy

Precision

Recall

F1-Score

Confusion Matrix

The best-performing model is saved into:

models/attrition_model.pkl

📥 Loading the Model

model_loader.py helps load any saved ML model to use for predictions:

For testing new employee data

For deploying in a future UI / API

For integration into dashboards

This ensures modularity and clean separation of concerns.

🗄 Database Setup

The MySQL schema is created using:

sql/create_tables.sql


database_connector.py handles:

Database connection

Data fetch

Data insertion

Query execution

This makes the project production-friendly.

📌 How to Run the Project

Clone the repository

git clone https://github.com/Rizquan/EmployeeAttritionPredictor.git


Create a virtual environment

python -m venv venv
source venv/bin/activate  (or)  venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Set up the MySQL database

Run the SQL file in Workbench

Import data and preprocess

Open data_preprocessing.ipynb

Train the model

Open model_training.ipynb

Make predictions

Use model_loader.py

🎯 Future Improvements

Streamlit-based interactive UI

API deployment using FastAPI/Flask

AutoML hyperparameter tuning

Dashboard to view attrition trends

👤 Author

Mohammed Rizquan
Data Science undergraduate @ SLIIT
Passionate about AI, machine learning, and data engineering.

🌟 Final Opinion for You as a Year 2 Student

This project is perfect for GitHub WITHOUT a UI:

✔ Clean structure
✔ Database + ML integration
✔ Visualizations
✔ Well-documented notebooks
✔ Model saving/loading
✔ Looks professional and industry-ready
