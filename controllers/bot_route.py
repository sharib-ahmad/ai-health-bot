from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from bot.logic import get_diagnosis
from models.model import db, User, SymptomLog
from models.forms import SymptomForm
from flask import session
from flask import jsonify
from datetime import datetime
import os

bot_bp = Blueprint("bot_bp", __name__, template_folder="../templates")

@bot_bp.route("/chat", methods=["GET", "POST"])
@login_required
def chat():
    form = SymptomForm()
    chat_history = session.get("chat_history", [])
    chat_index = session.get("chat_index", len(chat_history) - 1)

    if form.validate_on_submit():
        # Get symptom input and split into list
        symptoms_raw = form.symptoms.data
        symptoms = [s.strip().lower() for s in symptoms_raw.split(",") if s.strip()]

        # Generate AI response
        response = get_diagnosis(symptoms)

        # Save to database
        symptom_log = SymptomLog(user_id=current_user.id, symptoms=symptoms_raw, response=response)
        db.session.add(symptom_log)
        db.session.commit()
        # Log to session history
        chat_history.append({
            "input": ", ".join(symptoms),  # Store as string for display
            "response": response,
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

        session["chat_history"] = chat_history
        session["chat_index"] = len(chat_history) - 1
        return redirect(url_for("bot_bp.chat"))

    # Get current chat message
    current_chat = chat_history[chat_index] if chat_history and 0 <= chat_index < len(chat_history) else None

    return render_template("chatbot.html", form=form, chat=current_chat, index=chat_index, total=len(chat_history))



@bot_bp.route("/chat/prev")
def prev_chat():
    if "chat_index" in session and session["chat_index"] > 0:
        session["chat_index"] -= 1
    return redirect(url_for("bot_bp.chat"))

@bot_bp.route("/chat/next")
def next_chat():
    if "chat_index" in session and session["chat_index"] < len(session.get("chat_history", [])) - 1:
        session["chat_index"] += 1
    return redirect(url_for("bot_bp.chat"))

@bot_bp.route("/chat/clear")
def clear_chat():
    session.pop("chat_history", None)
    session.pop("chat_index", None)
    return redirect(url_for("bot_bp.chat"))

@bot_bp.route("/api/chat/get", methods=["GET"])
@login_required
def get_current_chat():
    chat_history = session.get("chat_history", [])
    chat_index = session.get("chat_index", len(chat_history) - 1)

    if chat_history and 0 <= chat_index < len(chat_history):
        current_chat = chat_history[chat_index]
    else:
        current_chat = {}

    return jsonify({
        "chat": current_chat,
        "index": chat_index,
        "total": len(chat_history),
        "is_last": chat_index == len(chat_history) - 1
    })

@bot_bp.route("/api/chat/nav/<string:direction>", methods=["POST"])
@login_required
def nav_chat(direction):
    chat_history = session.get("chat_history", [])
    chat_index = session.get("chat_index", len(chat_history) - 1)

    if direction == "prev" and chat_index > 0:
        chat_index -= 1
    elif direction == "next" and chat_index < len(chat_history) - 1:
        chat_index += 1

    session["chat_index"] = chat_index

    return jsonify({"success": True})

@bot_bp.route("/api/chat/clear", methods=["POST"])
@login_required
def api_clear_chat():
    session.pop("chat_history", None)
    session.pop("chat_index", None)
    return jsonify({"success": True})

@bot_bp.route("/")
def index():
    return render_template("index.html")