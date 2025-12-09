import mysql.connector
import pandas as pd
from mysql.connector import Error

class DatabaseConnector:
    def __init__(self, host="localhost", user="root", password="root", database="employee_attrition"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    
    def connect(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return connection
        except Error as e:
            print("❌ Error connecting to MySQL:", e)
            return None

    def fetch_employee_data(self):
        connection = self.connect()
        if connection is None:
            return None
        
        query = "SELECT * FROM employees"
        df = pd.read_sql(query, connection)
        connection.close()
        return df

    def insert_prediction(self, employee_id, prediction, probability):
        connection = self.connect()
        if connection is None:
            return
        
        cursor = connection.cursor()
        query = """
            INSERT INTO predictions_log (employee_id, predicted_attrition, prediction_probability)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (employee_id, prediction, probability))
        connection.commit()
        cursor.close()
        connection.close()
