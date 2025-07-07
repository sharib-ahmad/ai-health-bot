# 🤖 AI Health Assistant Bot

A full-stack Flask web application that predicts diseases based on symptoms entered by the user. The prediction is powered by a trained **Random Forest** classifier using a real dataset from Kaggle. The app supports login/registration, secure session handling, aesthetic design, and a clean backend using Flask extensions like `Flask-WTF`, `Flask-Login`, and `Flask-SQLAlchemy`.

---

## 📚 Table of Contents

- [Features](#features)
- [Machine Learning](#machine-learning)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Dataset Info](#dataset-info)
- [Sample Usage](#sample-usage)
- [Dependencies](#dependencies)
- [Author](#author)


---

## 🚀 Features

- 🔐 User registration and login using **Flask-Login**
- 🧠 Disease prediction using trained **Random Forest Classifier**
- 📝 Symptom input using **Flask-WTF** form validation
- 📋 SQLite3 database with **Flask-SQLAlchemy**
- 💾 Session management using cookies
- 🎨 Clean and aesthetic UI using custom CSS and Bootstrap
- 📂 Structured code using Blueprints and MVC pattern
- 🧾 Symptom list stored in `bot/symptoms_list.txt`

---

## 🧠 Machine Learning

The ML model is trained using a cleaned version of the Kaggle dataset:
📦 [`itachi9604/disease-symptom-description-dataset`](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset)

- **Algorithm used:** Random Forest Classifier
- **Libraries:** scikit-learn, pandas, joblib
- **Steps:**
  - Data loaded and cleaned
  - Label encoding applied to diseases
  - Model trained and tested
  - Model serialized using `joblib` to `model.pkl`
  - Symptoms stored in `symptoms_list.txt` for the UI

Notebook: notebook/training_pipeline.ipynb


---

## 🗂️ Project Structure

```text
ai-health-bot/
├── app.py                    # Main Flask app entry
├── .gitignore
├── README.md
├── dataset/
│   └── disease_symptom.csv   # Cleaned dataset from Kaggle
├── notebook/
│   └── training_pipeline.ipynb
├── bot/
│   ├── logic.py              # Prediction logic
│   └── symptoms_list.txt     # Unique symptoms list
├── static/
│   ├── favicon/bot.png
│   ├── css/styles.css
│   └── screenshots/          # (Optional) Screenshots
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── summary.html
│   └── auth/
│       ├── login.html
│       └── register.html
├── controllers/
│   ├── user_routes.py
│   └── prediction_routes.py
├── models/
│   └── user_model.py
└── instance/
    └── app.db                # SQLite3 database

---

## ⚙️ Setup Instructions

# 1. Clone the repo
git clone https://github.com/sharib-ahmad/ai-health-bot.git
cd ai-health-bot

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set environment variables (optional)
export FLASK_APP=app.py
export FLASK_ENV=development

# 5. Run the app
python app.py

---

## 📁 Dataset Info
Dataset Source:
🔗 Kaggle - Disease Symptom Description

Used File:

bash
Copy
Edit

dataset/dataset.csv
Symptom_1, Symptom_2, ..., Symptom_17, Disease

---

## 🧪 Sample Usage

Go to /register → Create a new user

Login at /login

Enter symptoms (comma-separated) like:

fever, cough, fatigue

Click Predict to view the disease result

View the disease summary or recommendation (optional)

You can logout via the top nav

---

## 📌 Dependencies
nginx
Copy
Edit
Flask
Flask-WTF
Flask-Login
Flask-SQLAlchemy
scikit-learn
joblib
pandas
numpy

pip freeze > requirements.txt

---

## 🙋 Author
👨‍💻 Sharib Ahmad

📫sharibahmad6716@gmail.com      ---> personal gmail
📫24f2001786@ds.study.iitm.ac.in --->college gmail/aicte


🎓 B.S. Student | AI, ML & Data Scientist Enthusiast

---
