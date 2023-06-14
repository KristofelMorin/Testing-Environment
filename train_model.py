from sklearn import model_selection, datasets, linear_model
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib
import pickle
import numpy as np
import pandas as pd

dataset = datasets.load_wine()
X = dataset.data; y = dataset.target
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

filename = "X_train.joblib"
joblib.dump(model, filename)

loaded_model = joblib.load(filename)
result = loaded_model.score(X_test, y_test)
print(result)