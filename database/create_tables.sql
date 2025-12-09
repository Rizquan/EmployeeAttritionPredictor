CREATE DATABASE IF NOT EXISTS employee_attrition;
USE employee_attrition;

-- Main table to store employee data
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    age INT NOT NULL,
    gender VARCHAR(20),
    department VARCHAR(100),
    job_role VARCHAR(100),
    monthly_income INT,
    years_at_company INT,
    job_satisfaction INT,
    performance_rating INT,
    overtime VARCHAR(10),
    attrition VARCHAR(10)       -- Yes / No (Label for prediction)
);

-- Table to store predictions for audit logs
CREATE TABLE IF NOT EXISTS predictions_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    predicted_attrition VARCHAR(10),
    prediction_probability FLOAT,
    prediction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);
