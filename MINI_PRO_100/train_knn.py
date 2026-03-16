import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(".."))
import joblib
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from preprocessing.clean_data import preprocess_data

X, y = preprocess_data("dataset/data_sensitivity.csv")

X_train, X_test, y_train, y_test = train_test_split(X, y)

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)

joblib.dump(knn, "knn_model.pkl")

print("KNN trained")