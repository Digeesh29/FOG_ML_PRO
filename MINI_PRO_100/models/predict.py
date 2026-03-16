import joblib
import os

BASE_DIR = os.path.dirname(__file__)

rf_path = os.path.join(BASE_DIR, "rf_model.pkl")
knn_path = os.path.join(BASE_DIR, "knn_model.pkl")

rf = joblib.load(rf_path)
knn = joblib.load(knn_path)


def classify_data(data):

    rf_pred = rf.predict(data)[0]

    knn_pred = knn.predict(data)[0]

    print("RF Prediction:", rf_pred)
    print("KNN Prediction:", knn_pred)

    if rf_pred == knn_pred:
        return rf_pred
    else:
        return rf_pred