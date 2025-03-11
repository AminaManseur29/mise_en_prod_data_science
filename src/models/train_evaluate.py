<<<<<<< HEAD
from loguru import logger
from sklearn.metrics import confusion_matrix

@logger.catch
=======
from sklearn.metrics import confusion_matrix

>>>>>>> 2010a02e160a40b150f10aac3ab597014e4064ee
def evaluate_model(pipe, X_test, y_test):
    """
    Evaluate the model by calculating the score and confusion matrix.

    Args:
        pipe (sklearn.pipeline.Pipeline): The trained pipeline object.
        X_test (pandas.DataFrame): The test data.
        y_test (pandas.Series): The true labels for the test data.

    Returns:
        tuple: A tuple containing the score and confusion matrix.
    """
    score = pipe.score(X_test, y_test)
    matrix = confusion_matrix(y_test, pipe.predict(X_test))
    return score, matrix
<<<<<<< HEAD
=======

>>>>>>> 2010a02e160a40b150f10aac3ab597014e4064ee
