"""
Prediction de la survie d'un individu sur le Titanic
"""

import os
<<<<<<< HEAD
from dotenv import load_dotenv
import argparse
from loguru import logger

import pathlib
import pandas as pd
from sklearn.model_selection import train_test_split

from src.pipeline.build_pipeline import create_pipeline
=======
import pathlib
from dotenv import load_dotenv
from loguru import logger
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split

from src.pipeline.build_features import split_train_test, create_pipeline
>>>>>>> 2010a02e160a40b150f10aac3ab597014e4064ee
from src.models.train_evaluate import evaluate_model


# ENVIRONMENT CONFIGURATION ---------------------------

logger.add("recording.log", rotation="500 MB")
load_dotenv()

parser = argparse.ArgumentParser(description="Paramètres du random forest")
parser.add_argument(
    "--n_trees", type=int, default=20, help="Nombre d'arbres"
)
args = parser.parse_args()

<<<<<<< HEAD
URL_RAW = "https://minio.lab.sspcloud.fr/lgaliana/ensae-reproductibilite/data/raw/data.csv"
=======
URL_RAW = "https://minio.lab.sspcloud.fr/amanseur/ensae-reproductibilite/data/raw/data.csv"
>>>>>>> 2010a02e160a40b150f10aac3ab597014e4064ee

n_trees = args.n_trees
jeton_api = os.environ.get("JETON_API", "")
data_path = os.environ.get("data_path", URL_RAW)
data_train_path = os.environ.get("train_path", "data/derived/train.parquet")
data_test_path = os.environ.get("test_path", "data/derived/test.parquet")
MAX_DEPTH = None
MAX_FEATURES = "sqrt"

if jeton_api.startswith("$"):
    logger.info("API token has been configured properly")
<<<<<<< HEAD
else:
    logger.warning("API token has not been configured")


# IMPORT ET STRUCTURATION DONNEES --------------------------------
=======
    # print("API token has been configured properly")
else:
    logger.warning("API token has not been configured")
    # print("API token has not been configured")


# IMPORT ET EXPLORATION DONNEES --------------------------------
>>>>>>> 2010a02e160a40b150f10aac3ab597014e4064ee

p = pathlib.Path("data/derived/")
p.mkdir(parents=True, exist_ok=True)

TrainingData = pd.read_csv(data_path)

y = TrainingData["Survived"]
X = TrainingData.drop("Survived", axis="columns")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1
)
<<<<<<< HEAD
pd.concat([X_train, y_train], axis = 1).to_parquet(data_train_path)
pd.concat([X_test, y_test], axis = 1).to_parquet(data_test_path)


=======
pd.concat([X_train, y_train], axis=1).to_parquet(data_train_path)
pd.concat([X_test, y_test], axis=1).to_parquet(data_test_path)


# SPLIT TRAIN/TEST --------------------------------

X_train, X_test, y_train, y_test = split_train_test(TrainingData, test_size=0.1)

>>>>>>> 2010a02e160a40b150f10aac3ab597014e4064ee

# PIPELINE ----------------------------


# Create the pipeline
pipe = create_pipeline(
    n_trees, max_depth=MAX_DEPTH, max_features=MAX_FEATURES
)


# ESTIMATION ET EVALUATION ----------------------

pipe.fit(X_train, y_train)


# Evaluate the model
score, matrix = evaluate_model(pipe, X_test, y_test)

logger.success(f"{score:.1%} de bonnes réponses sur les données de test pour validation")
logger.debug(20 * "-")
<<<<<<< HEAD
logger.info("Matrice de confusion")
logger.debug(matrix)
=======
logger.info("matrice de confusion")
logger.debug(matrix)

# print(f"{score:.1%} de bonnes réponses sur les données de test pour validation")
# print(20 * "-")
# print("matrice de confusion")
# print(matrix)
>>>>>>> 2010a02e160a40b150f10aac3ab597014e4064ee
