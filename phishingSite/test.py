import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendmails(name, mail):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "epitauto@gmail.com"  # Enter your address
    receiver_email = mail  # Utiliser le paramètre 'mail' pour l'adresse du destinataire
    password = "ajip dzed tnyd relc"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Alerte Sécurité Microsoft"
    message["From"] = sender_email
    message["To"] = receiver_email

    html = """\
    <html>
      <body>
        <p>Bonjour {name},<br><br>
           Nous avons détecté une activité suspecte sur votre compte, veuillez cliquer sur le bouton suivant pour récupérer votre compte :
           <br><br>
           <a href="http://127.0.0.1:8000/microsoft/login?email_campagne_id=5" style="background-color: #007bff; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border: none; border-radius: 5px;">Update Account</a>
           <br><br>
           Merci,<br>
           L'équipe sécurité Microsoft
        </p>
      </body>
    </html>
    """.format(name=name)

    part2 = MIMEText(html, "html")
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


# Exemple d'appel de la fonction
sendmails("Raphael", "raphael13410@gmail.com")