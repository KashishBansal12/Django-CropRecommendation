from django.shortcuts import render
from joblib import load
import numpy as np
import pandas as pd
from django.contrib.auth.decorators import login_required  # <-- ADD THIS IMPORT
# We'll import the new model for storing history
from users.models import RecommendationHistory  # <-- ADD THIS IMPORT

model = load('./savedmodels/soil.pkl')
label_encoder = load('./savedmodels/label_encoder.pkl')



def predict(request):
    if request.method == 'POST':
        N = float(request.POST['N'])
        P = float(request.POST['P'])
        K = float(request.POST['K'])
        temperature = float(request.POST['temperature'])
        humidity = float(request.POST['humidity'])
        ph = float(request.POST['ph'])
        rainfall = float(request.POST['rainfall'])

        # Predict using your loaded model
        input_df = pd.DataFrame([{
                'N': N,
                'P': P,
                'K': K,
                'temperature': temperature,
                'humidity': humidity,
                'ph': ph,
                'rainfall': rainfall
            }])
        y_pred = model.predict(input_df)
        # If your model gives class names directly, this is enough
        recommended_crop = label_encoder.inverse_transform(y_pred)[0]
        # --- NEW CODE ADDITIONS START HERE ---
        # Check if the user is authenticated (logged in)
        if request.user.is_authenticated:
            # Create a new entry in the RecommendationHistory model
            RecommendationHistory.objects.create(
                user=request.user,
                nitrogen=N,
                phosphorus=P,
                potassium=K,
                temperature=temperature,
                humidity=humidity,
                ph=ph,
                rainfall=rainfall,
                recommended_crop=recommended_crop
            )
        # --- NEW CODE ADDITIONS END HERE ---

        return render(request, 'main_page.html', {'result': recommended_crop})
    return render(request, 'main_page.html')