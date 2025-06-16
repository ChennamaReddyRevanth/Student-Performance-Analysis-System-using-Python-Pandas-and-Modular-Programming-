import pandas as pd
import os

DATA_FILE = 'C:\\Users\\chenn\\OneDrive\\Desktop\\student_performance\\student_data.csv'

def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    return pd.DataFrame(columns=["Student ID", "Name", "Class", "Math", "Science", "English", "Average", "Grade"])

def save_data(df):
    df.to_csv(DATA_FILE, index=False)
