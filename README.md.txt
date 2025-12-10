📘 Employee Attrition Predictor

A machine learning project that predicts whether an employee is likely to leave the company based on demographic, performance, satisfaction, and organizational factors.

This repository demonstrates a complete end-to-end ML workflow, including MySQL data storage, preprocessing, model training, evaluation, and visual analysis.

🚀 Project Overview

Employee attrition is a critical issue for organizations. This project builds a predictive model to estimate the probability of an employee leaving, allowing companies to take proactive decisions.

This system includes:

✔ MySQL database to store employee records

✔ Data loading via Python (database_connector.py)

✔ Data preprocessing (cleaning, encoding, scaling)

✔ Model training using Scikit-Learn & TensorFlow

✔ Visual EDA, heatmaps, and insights

✔ Model saving/loading (model_loader.py)

✔ Clean, modular file structure suitable for ML projects

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
│   ├── attrition_model.h5
│   └── scaler.pkl
│
├── visualizations/
│   └── (saved charts)
│
└── README.md

🛠 Technologies Used

Languages: Python, SQL
Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn, TensorFlow/Keras, MySQL Connector
Tools: VS Code, Jupyter Notebook, MySQL Workbench, GitHub

📊 Exploratory Data Analysis (EDA)

The project includes visual insights such as:

Line chart: Gender vs Years at Company

Bar chart: Department vs Job Satisfaction

Line chart: Job Role vs Average Monthly Income

Pie chart: Overtime Distribution

Correlation Heatmap

Attrition vs Job Satisfaction

Performance Rating vs Income

These charts help understand patterns before modeling.

🔧 Data Preprocessing

Performed in data_preprocessing.ipynb:

Handle missing values

One-hot encode categorical features

Convert Yes/No → 1/0

Standard scaling (StandardScaler)

Train–test split

Export scaled data and preprocessing objects

🤖 Model Training

Models trained in model_training.ipynb:

Logistic Regression

Random Forest Classifier

TensorFlow Sequential Neural Network

Evaluated using:

Accuracy

Precision / Recall / F1-score

Confusion Matrix

The final model and scaler are saved inside:

models/
    attrition_model.h5
    scaler.pkl

📥 Model Loading

scripts/model_loader.py allows:

Loading the trained model

Loading the scaler

Running predictions on new employee data

This enables simple integration with future UI/API systems.

🗄 Database Setup

sql/create_tables.sql contains:

Schema for employee_data table

Column definitions

Primary keys and constraints

database_connector.py handles:

Opening connection

Fetching data

Inserting new rows

Executing SQL queries

📌 How to Run the Project

1️⃣ Clone the repository
git clone https://github.com/Rizquan/EmployeeAttritionPredictor.git

2️⃣ Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   (Windows)

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set up MySQL database

Open MySQL Workbench

Run sql/create_tables.sql

5️⃣ Preprocess data

Open Jupyter Notebook:

notebooks/data_preprocessing.ipynb

6️⃣ Train the model
notebooks/model_training.ipynb

7️⃣ Make predictions

Use:

scripts/model_loader.py

🎯 Future Enhancements

Streamlit UI for real-time predictions

FastAPI/Flask deployment

Hyperparameter tuning

Automated dashboards for HR analytics

👤 Author

Mohammed Rizquan
Undergraduate in Data Science @ SLIIT
Interested in Machine Learning, AI, and Data Engineering.
