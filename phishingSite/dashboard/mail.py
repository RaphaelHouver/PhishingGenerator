import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def sendmailsMicrosoft(name, mail):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "noreplymicrosoftalertlogin@gmail.com"  # Enter your address
    receiver_email = mail  # Utiliser le paramètre 'mail' pour l'adresse du destinataire
    password = os.getenv('PHISHING_MAIL_PWD_MICROSOFT')
    print(password)

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
           <a href="http://127.0.0.1:8000/info/microsoft/login?email_campagne_id=5" style="background-color: #007bff; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border: none; border-radius: 5px;">Update Account</a>
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

def sendmailsDigipost(name, mail):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "noreplydigiposte@gmail.com"  # Enter your address
    receiver_email = mail  # Utiliser le paramètre 'mail' pour l'adresse du destinataire
    password = os.getenv('PHISHING_MAIL_PWD_DIGIPOSTE')

    message = MIMEMultipart("alternative")
    message["Subject"] = "Un nouveau document dans votre coffre Digiposte"
    message["From"] = sender_email
    message["To"] = receiver_email

    html = """\
    <html>
      <body>
        <p>Bonjour {name},<br><br>
            Vous avez reçu de nouveau(x) document(s) dans <span style="background-color: #fcf03a;">Digiposte</span> :
            <br><br>
            <strong>Bulletin de paie</strong> de la part de NEWEN.
            <br><br>
            Pour les consulter, connectez-vous dès à présent au site <span style="background-color: #fcf03a;">Digiposte</span>. 
            <br><br>
            <a href="http://127.0.0.1:8000/info/microsoft/login?email_campagne_id=5" style="background-color: #2b15fa; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border: none; border-radius: 5px;">CONSULTER MES DOCUMENTS</a>
            <br><br>
            Nous vous remercions de votre confiance.<br>
            L'équipe Digiposte
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