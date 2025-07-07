

import joblib
import numpy as np
import os
import pandas as pd
from datetime import datetime
symptom_summary_path = os.path.join("bot", "symptom_list.txt")
with open(symptom_summary_path, "r") as f:
    SYMPTOM_LIST = [line.strip() for line in f]

# Define paths
model_path = os.path.join("datasets", "disease_model.pkl")
encoder_path = os.path.join("datasets", "label_encoder.pkl")
precautions_path = os.path.join("datasets", "symptom_precaution.csv")

# ✅ Load model and encoder using joblib
model = joblib.load(model_path)
label_encoder = joblib.load(encoder_path)

# ✅ Load precautions
precaution_df = pd.read_csv(precautions_path)
precaution_map = {
    row["Disease"]: [row["Precaution_1"], row["Precaution_2"], row["Precaution_3"], row["Precaution_4"]]
    for _, row in precaution_df.iterrows()
}

def extract_known_symptoms(user_text):
    """
    Match user input against known symptoms using partial matching.
    """
    user_text = user_text.lower()
    detected = [sym for sym in SYMPTOM_LIST if sym.replace("_", " ") in user_text or sym in user_text]
    return detected


def get_precautions(disease_name):
    """Return list of precautions for the predicted disease."""
    return precaution_map.get(disease_name, [])

def get_diagnosis(symptom_input_raw):
    # Accepts either list or string input
    if isinstance(symptom_input_raw, list):
        user_text = " ".join(symptom_input_raw)
    else:
        user_text = symptom_input_raw

    filtered = extract_known_symptoms(user_text)

    if not filtered:
        return "❌ No valid symptoms provided. Please enter known symptoms like headache, nausea, cough, etc."

    input_vector = [1 if symptom in filtered else 0 for symptom in SYMPTOM_LIST]
    input_np = np.array(input_vector).reshape(1, -1)

    prediction_encoded = model.predict(input_np)[0]
    prediction_label = label_encoder.inverse_transform([prediction_encoded])[0]

    result = f"""
📅 Prediction Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🧍 Symptoms Entered: {', '.join(filtered)}
🤖 Predicted Disease: **{prediction_label}**
"""

    precautions = get_precautions(prediction_label)
    if precautions:
        result += "\n💡 Precautions:\n" + "\n".join([f"  {i+1}. {p}" for i, p in enumerate(precautions)])

    return result.strip()

