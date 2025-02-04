from flask import render_template, request, jsonify
from app import app
from app.email_sender import send_email

@app.route("/")
def index():
    return render_template("index.html")  # Affiche la page HTML du formulaire

@app.route("/send-email", methods=["POST"])
def send_email_route():
    data = request.json
    if send_email(data):
        return jsonify({"message": "Email envoyé avec succès !"})
    return jsonify({"message": "Erreur lors de l'envoi"}), 500
