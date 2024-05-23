import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from core.config import get_api_settings
# from sendgrid import SendGridAPIClient
from utils.base_utils import get_frontend_url

# from sendgrid.helpers.mail import Mail


settings = get_api_settings()


def send_email(email_data: str):
    to_email = email_data.email

    msg = MIMEMultipart()
    msg["From"] = settings.FROM_EMAIL
    msg["To"] = to_email
    msg["Subject"] = email_data.subject

    msg.attach(MIMEText(email_data.message, "plain"))

    server = smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT)
    server.starttls()
    server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
    text = msg.as_string()
    server.sendmail(settings.FROM_EMAIL, to_email, text)
    server.quit()


def send_sendgrid_email(email_data: str):
    # message = Mail(
    #     from_email=settings.FROM_EMAIL,
    #     to_emails=email_data.email,
    #     subject=email_data.subject,
    #     html_content=email_data.message,
    # )

    try:
        pass
        # sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        # response = sg.send(message)

    except Exception as e:
        print(e)


def case_activation(incident_id: str, email: str, subject: str):
    try:
        url = get_frontend_url()

        email_payload = SmsPayload(
            id=incident_id,
            email=email,
            subject=subject,
            message=f"""
                <html>
                <head>
                    <meta charset="UTF-8">
                    <title>TrusTool Team</title>
                </head>
                <body>
                    <p style="color: #000000; font-size: 14px;"><u><b>Antwoord niet op deze email. Die komt niet bij de vertrouwenspersoon.</b></u></p>
                    <p style="color: #000000; font-size: 14px;"><u><b>Dit is een automatisch gegenereerd systeembericht.</b></u></p>
                    <p style="color: #000000; font-size: 14px;">Geachte melder,</p>
                    <p style="color: #000000; font-size: 14px;">De vertrouwenspersoon heeft jouw melding geregistreerd.</p>
                    <p style="color: #000000; font-size: 14px;">Het registratienummer is: {incident_id}</p>
                    <p style="color: #000000; font-size: 14px;">Wanneer je de melding zou willen bekijken, dan is dat mogelijk via: <a href="{url}" style="color: #0000FF; text-decoration: none;">Klik hier</a></p>
                    <p style="color: #000000; font-size: 14px;">Je kunt inloggen met jouw e-mailadres en het registratienummer (zie hierboven) waarna je als extra
                        veiligheidsstap een verificatiecode per e-mail ontvangt. Voer deze in, daarna ben je ingelogd in jouw
                        meldingsdossier. Log uit om het portaal te verlaten.</p>
                    <p>----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------</p>
                    <p style="color: #000000; font-size: 14px;"><u><b>Do not reply to this email. This does not reach the confidential counsellor.</b></u></p>
                    <p style="color: #000000; font-size: 14px;"><u><b>This is an automatically generated system message.</b></u></p>
                    <p style="color: #000000; font-size: 14px;">Dear reporter,</p>
                    <p style="color: #000000; font-size: 14px;">The Confidential Counsellor has registered your report.</p>
                    <p style="color: #000000; font-size: 14px;">The registration number is: {incident_id}</p>
                    <p style="color: #000000; font-size: 14px;">You can check your report here: <a href="{url}" style="color: #0000FF; text-decoration: none;">Click Here</a></p>
                    <p style="color: #000000; font-size: 14px;">Log in with your registration number (see above) and your email address. For security reasons you
                        will receive a verification code by email. After entering this code you are logged in. To leave the
                        portal log out.</p>
                    <p style="color: #000000; font-size: 14px;">Best regards,</p>
                    <p style="color: #000000; font-size: 14px;">TrusTool Team</p>
                </body>
                </html>
            """,
        )

        send_sendgrid_email(email_payload)
    except Exception as ex:
        # logging.error(ex)
        return "SendEmailException()"


def case_registartion(email: str):
    try:
        email_payload = SmsPayload(
            email=email,
            subject="Nieuwe melding/New notification",
            message=f"""
                <html>
                <head>
                    <meta charset="UTF-8">
                    <title>TrusTool Team</title>
                </head>
                <body>
                    <div style="text-align: center">
                        <img src="https://trustool.s3.eu-central-1.amazonaws.com/Logo-TrusTool-small.jpg" alt="TrusTool Image"><br/>
                        <p style="color: #000000; font-size: 14px;">Vertrouwenspersoon, Confidential Counsellor,</p><br/>
                        <p style="color: #000000; font-size: 14px;">Er is een nieuwe melding in het TrusTool portaal.</p>
                        <p style="color: #000000; font-size: 14px;">There is a new notification in the TrusTool portal.</p>
                    </div>
                 </body>
                </html>
            """,
        )

        send_sendgrid_email(email_payload)
    except Exception as ex:
        # logging.error(ex)
        return "SendEmailException()"
