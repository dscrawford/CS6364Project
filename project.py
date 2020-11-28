import pandas as pd
import numpy as np

# Read large datasets: https://www.kaggle.com/rohanrao/tutorial-on-reading-large-datasets
train_dtypes = {
    "row_id": "int64",
    "timestamp": "int64",
    "user_id": "int32",
    "content_id": "int16",
    "content_type_id": "boolean",
    "task_container_id": "int16",
    "user_answer": "int8",
    "answered_correctly": "int8",
    "prior_question_elapsed_time": "float32",
    "prior_question_had_explanation": "boolean"
}

train_df = pd.read_csv('train.csv', nrows=100000, dtype=train_dtypes)
questions_df = pd.read_csv('questions.csv')
lectures_df = pd.read_csv('lectures.csv')
example_test_df = pd.read_csv('example_test.csv')

train_df[