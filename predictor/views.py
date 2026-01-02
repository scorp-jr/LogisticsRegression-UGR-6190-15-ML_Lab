import os
import joblib
import numpy as np
from django.shortcuts import render

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "logreg_pipeline.joblib")
model = joblib.load(model_path)

def home(request):
    prediction = None

    if request.method == "POST":
        X = np.array([[
            float(request.POST["sepal_length"]),
            float(request.POST["sepal_width"]),
            float(request.POST["petal_length"]),
            float(request.POST["petal_width"]),
        ]])
        labels = ["Setosa", "Versicolor", "Virginica"]
        prediction = labels[model.predict(X)[0]]

    return render(request, "index.html", {"prediction": prediction})
