import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import joblib


def train_and_save_scam_detector(
        data_csv_path: str,
        model_output_path: str,
        test_size: float = 0.2,
        random_state: int = 42
) -> None:
    """
    Train a scam token detection model and save the pipeline to disk.

    Args:
        data_csv_path (str): Path to the labeled CSV with 'name', 'url', and 'is_scam'.
        model_output_path (str): File path to save the trained model pipeline.
        test_size (float): Proportion of data to use for testing.
        random_state (int): Random seed for reproducibility.
    """
    # 1. Load the labeled dataset

    # 2. Prepare the text feature by combining name and URL slug

    # 3. Define features and target

    # 4. Split into training and test sets

    # 5. Create a pipeline with TF-IDF vectorizer and RandomForest classifier

    # 6. Train the model

    # 7. Save the trained pipeline

    pass


if __name__ == "__main__":
    DATA_PATH = "data/Crypto_final_labeled.csv"
    MODEL_PATH = "scam_token_detector.pkl"
    train_and_save_scam_detector(
        data_csv_path=DATA_PATH,
        model_output_path=MODEL_PATH,
        test_size=0.2,
        random_state=42
    )
