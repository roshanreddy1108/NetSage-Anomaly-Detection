from sklearn.ensemble import IsolationForest
import joblib, numpy as np

X = np.random.rand(100,3) * 100
model = IsolationForest(contamination=0.1)
model.fit(X)
joblib.dump(model, "model.pkl")
print("Model trained and saved.")
