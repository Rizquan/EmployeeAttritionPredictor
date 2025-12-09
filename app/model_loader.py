import numpy as np
import pandas as pd
import tensorflow as tf
from database_connector import DatabaseConnector

class AttritionModel:
    def __init__(self, model_path="model/model.h5"):
        self.model = tf.keras.models.load_model(model_path)
        self.db = DatabaseConnector()

    def preprocess_input(self, data_dict):
        """
        data_dict: {
            "age": 35,
            "gender": "Male",
            "department": "Sales",
            ...
        }
        Convert into model-ready format (must match training pipeline).
        """
        df = pd.DataFrame([data_dict])

        # IMPORTANT:
        # Encode exactly the same way you did during training.
        # Example:
        df['gender'] = df['gender'].map({"Male": 0, "Female": 1})
        df['overtime'] = df['overtime'].map({"Yes": 1, "No": 0})

        # For one-hot encoding of department/job_role
        df = pd.get_dummies(df)

        # Align columns to match training feature columns
        model_features = np.load("model/feature_columns.npy", allow_pickle=True)
        df = df.reindex(columns=model_features, fill_value=0)

        return df.values

    def predict(self, employee_id, data_dict):
        processed = self.preprocess_input(data_dict)
        probability = float(self.model.predict(processed)[0][0])
        prediction = "Yes" if probability > 0.5 else "No"

        # Save prediction in DB
        self.db.insert_prediction(employee_id, prediction, probability)

        return {
            "employee_id": employee_id,
            "prediction": prediction,
            "probability": probability
        }
