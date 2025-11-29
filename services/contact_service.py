import smtplib
from fastapi import HTTPException
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from schemas.contact_schema import ContactForm
from config import settings

async def sendContactEmail(form: ContactForm):
    try:
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = settings.EMAIL_ADDRESS
        msg['To'] = settings.RECIPIENT_EMAIL
        msg['Subject'] = f"New Contact Form Submission from {form.name}"

        # Email body
        body = f"""
        New message from: {form.name}
        Email: {form.email}
        Message: {form.message}
        """
        msg.attach(MIMEText(body, 'plain'))
        print("📩 Attempting SMTP connection...")

        # Connect to Gmail's SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(settings.EMAIL_ADDRESS, settings.EMAIL_PASSWORD)
            server.send_message(msg)

        return {"message": "Email sent successfully"}
    except Exception as e:

        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")
