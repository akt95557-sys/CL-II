import pandas as pd
from sklearn.naive_bayes import CategoricalNB

# 1. Load Dataset (Colab upload or Jupyter local path)
try:
    from google.colab import files
    df = pd.read_csv(list(files.upload().keys())[0])
except ImportError:
    df = pd.read_csv("heart.csv")

# 2. Extract key features & binarize continuous values
X = df[["age", "sex", "cp", "chol"]].copy()
X["age"] = (X["age"] > 50).astype(int)
X["chol"] = (X["chol"] > 240).astype(int)
y = (df["target"] > 0).astype(int)

# 3. Construct Bayesian Model & Train
model = CategoricalNB()
model.fit(X, y)

# 4. Predict Diagnosis for Sample Patient [Age>50, Male, High ChestPain, High Chol]
patient = [[1, 1, 2, 1]]
probs = model.predict_proba(patient)[0]

print("No Disease Prob :", round(probs[0], 4))
print("Disease Prob    :", round(probs[1], 4))
print("Diagnosis       :", "Heart Disease" if model.predict(patient)[0] == 1 else "Normal")