# 🤖 AI Health Assistant Bot

A full-stack Flask web application that predicts diseases based on symptoms entered by the user. The prediction is powered by a trained **Random Forest** classifier using a real dataset from Kaggle. The app supports login/registration, secure session handling, aesthetic design, and a clean backend using Flask extensions like `Flask-WTF`, `Flask-Login`, and `Flask-SQLAlchemy`.

---

## 📚 Table of Contents

- [🚀 Features](#-features)
- [🧠 Machine Learning](#-machine-learning)
- [🗂️ Project Structure](#️-project-structure)
- [⚙️ Setup Instructions](#️-setup-instructions)
- [📁 Dataset Info](#-dataset-info)
- [🧪 Sample Usage](#-sample-usage)
- [📌 Dependencies](#-dependencies)
- [🖼️ Screenshots](#-screenshots)
- [🙋 Author](#-author)
- [📌 License](#-license)

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

Notebook:

---

## 🗂️ Project Structure

```text
ai-health-bot/
├── app.py                    # Main Flask app entry
├── .gitignore
├── README.md
├── dataset/
|   ├── *.pkl
│   └── *.csv  
├── notebook/
│   └── training_pipeline.ipynb
├── bot/
│   ├── logic.py              # Prediction logic
│   └── symptoms_list.txt     # Unique symptoms list
├── static/
│   ├── favicon/bot.png
│   └── css/styles.css
│   
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── summary.html
│   └── auth/
│       ├── login.html
│       └── register.html
├── controllers/
│   ├── auth_routes.py
│   └── chatbot_routes.py
├── models/
|   ├── form.py
│   └── user_model.py
└── instance/
    └── app.db                # SQLite3 database
