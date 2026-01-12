import httpx
from fastapi import HTTPException
from schemas.contact_schema import ContactForm
from config import settings

async def sendContactEmail(form: ContactForm):
    """
    Send email using Brevo API (replaces SMTP)
    Free tier: 300 emails/day
    No SMTP authentication issues on production servers
    """
    try:
        # Brevo SMTP API endpoint
        url = "https://api.brevo.com/v3/smtp/email"
        
        # API headers
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "api-key": settings.BREVO_API_KEY
        }
        
        # Email payload (Brevo format)
        payload = {
            "sender": {
                "name": "Noork Enterprises",
                "email": settings.SENDER_EMAIL
            },
            "to": [
                {
                    "email": settings.RECIPIENT_EMAIL,
                    "name": "Admin"
                }
            ],
            "subject": f"New Contact Form Submission from {form.name}",
            "htmlContent": f"""
            <html>
                <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                    <div style="max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
                        <h2 style="color: #2c3e50;">New Contact Form Submission</h2>
                        
                        <p><strong>Name:</strong> {form.name}</p>
                        <p><strong>Email:</strong> <a href="mailto:{form.email}">{form.email}</a></p>
                        
                        <h3 style="color: #34495e; margin-top: 20px;">Message:</h3>
                        <p style="background-color: #ecf0f1; padding: 15px; border-radius: 5px;">
                            {form.message.replace(chr(10), '<br>')}
                        </p>
                        
                        <hr style="border: none; border-top: 1px solid #ddd; margin: 20px 0;">
                        <p style="font-size: 12px; color: #7f8c8d;">
                            This email was sent from your contact form.
                        </p>
                    </div>
                </body>
            </html>
            """,
            "replyTo": {
                "email": form.email,
                "name": form.name
            }
        }
        
        # Make async request to Brevo API
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(url, json=payload, headers=headers)
        
        # Handle response
        if response.status_code not in [200, 201]:
            print(f"Brevo API Error: {response.status_code} - {response.text}")
            raise HTTPException(
                status_code=500,
                detail=f"Failed to send email. Please try again later."
            )
        
        return {"message": "Email sent successfully", "status": "success"}
    
    except httpx.RequestError as e:
        print(f"Network Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Network error while sending email"
        )
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to send email: {str(e)}"
        )

# import smtplib
# from fastapi import HTTPException
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from schemas.contact_schema import ContactForm
# from config import settings

# async def sendContactEmail(form: ContactForm):
#     try:
#         # Create email message
#         msg = MIMEMultipart()
#         msg['From'] = settings.EMAIL_ADDRESS
#         msg['To'] = settings.RECIPIENT_EMAIL
#         msg['Subject'] = f"New Contact Form Submission from {form.name}"

#         # Email body
#         body = f"""
#         New message from: {form.name}
#         Email: {form.email}
#         Message: {form.message}
#         """
#         msg.attach(MIMEText(body, 'plain'))

#         # Connect to Gmail's SMTP server
#         with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
#             server.login(settings.EMAIL_ADDRESS, settings.EMAIL_PASSWORD)
#             server.send_message(msg)

#         return {"message": "Email sent successfully"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")