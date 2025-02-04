import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import SMTP_SERVER, SMTP_PORT, EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER

def send_email(data):
    try:
        nom, prenom = data["nom"], data["prenom"]
        email, telephone = data["email"], data["telephone"]
        sujet, message = data["sujet"], data["message"]

        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER
        msg["Subject"] = f"📩 Nouveau message de {nom} {prenom} - {sujet}"

        body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
            <h2 style="color: #007BFF;">📬 Nouveau message reçu</h2>
            <p><strong>Nom :</strong> {nom} {prenom}</p>
            <p><strong>Email :</strong> <a href="mailto:{email}">{email}</a></p>
            <p><strong>Téléphone :</strong> {telephone}</p>
            <hr>
            <p><strong>✉️ Message :</strong></p>
            <blockquote style="background: #f9f9f9; padding: 10px; border-left: 4px solid #007BFF;">
                {message}
            </blockquote>
            <hr>
            <p style="font-size: 0.9em; color: #666;">Ce message a été envoyé via le formulaire de contact.</p>
        </body>
        </html>
        """
        msg.attach(MIMEText(body, "html"))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()

        return True
    except Exception as e:
        print(f"Erreur : {e}")
        return False
