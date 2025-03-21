import logging

from pandas import DataFrame
import pandas
import os
from sklearn.linear_model import SGDClassifier

_logger = logging.getLogger(__name__)
    
def load_winequality_data(data_dir: str = "data") -> DataFrame:
    _logger.info("Loading wine quality dataset")
    red_wines_path = os.path.join(data_dir, "winequality-red.csv")
    white_wines_path = os.path.join(data_dir, "winequality-white.csv")
    red_wines = pandas.read_csv(red_wines_path, sep=";")
    red_wines["is_red"] = 1
    white_wines = pandas.read_csv(white_wines_path, sep=";")
    white_wines["is_red"] = 0
    all_wines = pandas.concat([red_wines, white_wines])
    if _logger.isEnabledFor(logging.DEBUG):
        _logger.debug(f"Wine quality dataset statistics:\n{all_wines.describe().to_string()}")
    return all_wines


def train_model(winequality_data: DataFrame) -> SGDClassifier:
    X_train = winequality_data.drop(columns=["is_red"])
    y_train = winequality_data["is_red"]
    
    estimator_params = {}
    model = SGDClassifier(random_state=42, **estimator_params)
    model.fit(X_train, y_train)

    return model