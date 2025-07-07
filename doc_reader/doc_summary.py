from bot.logic import get_diagnosis
import os


symptom_list_path = os.path.join("bot", "symptom_list.txt")
with open(symptom_list_path, "r") as f:
    SYMPTOM_LIST = [line.strip() for line in f]

# app/doc_reader/doc_summary.py


def extract_symptoms_from_text(text):
    words = text.lower().replace("\n", " ").split()
    return [sym for sym in SYMPTOM_LIST if any(sym in word for word in words)]

def summarize_and_predict(text):
    symptoms = extract_symptoms_from_text(text)
    if not symptoms:
        return "❌ No symptoms matched in the document.", []
    
    result = get_diagnosis(symptoms)
    return result, symptoms

