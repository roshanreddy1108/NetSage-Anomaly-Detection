import joblib, numpy as np

model = joblib.load("model.pkl")
test = np.random.rand(5,3) * 100
preds = model.predict(test)
for row, pred in zip(test, preds):
    print("Data:", row, "Anomaly" if pred == -1 else "Normal")
