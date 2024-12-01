import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables
load_dotenv()

# Get email configuration from environment variables
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = int(os.getenv('SMTP_PORT'))
sender_email = os.getenv('SENDER_EMAIL')
sender_password = os.getenv('SENDER_PASSWORD')


def send_email(user, otp):

    subject = 'Email Verification'
    body = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Email Verification</title>
    </head>
    <body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f9f9f9;">
        <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 40px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); margin-top: 20px;">
            <div style="text-align: center; margin-bottom: 30px;">
                <h1 style="color: #1DB954; margin: 0; font-size: 28px; font-weight: 700;">Tobify</h1>
                <p style="color: #666; font-size: 14px; margin-top: 5px;">Music Conversion Made Easy</p>
            </div>

            <div style="border-top: 2px solid #f0f0f0; border-bottom: 2px solid #f0f0f0; padding: 30px 0; margin: 20px 0;">
                <h2 style="color: #333; font-size: 20px; margin: 0 0 15px 0;">Hi {user.first_name}! 👋</h2>
                <p style="color: #666; font-size: 16px; line-height: 1.5; margin: 0 0 20px 0;">
                    Welcome to Tobify! Please use the verification code below to complete your registration. This code will expire in 5 minutes.
                </p>

                <div style="background-color: #f8f9fa; border-radius: 8px; padding: 20px; text-align: center; margin: 20px 0;">
                    <h2 style="color: #1DB954; font-size: 32px; letter-spacing: 5px; margin: 0;">{otp}</h2>
                </div>

                <p style="color: #666; font-size: 14px; margin: 20px 0 0 0;">
                    If you didn't request this code, you can safely ignore this email.
                </p>
            </div>

            <div style="text-align: center;">
                <p style="color: #666; font-size: 14px; margin: 0 0 5px 0;">Need help? Contact our support team</p>
                <a href="mailto:support@tobify.com" style="color: #1DB954; text-decoration: none; font-weight: 500;">support@tobify.com</a>
            </div>

            <div style="margin-top: 30px; text-align: center; border-top: 2px solid #f0f0f0; padding-top: 20px;">
                <p style="color: #999; font-size: 12px; margin: 0;">
                    2024 Tobify. All rights reserved.<br>
                    Made with ❤️ for music lovers
                </p>
            </div>
        </div>
    </body>
    </html>
    '''

    msg = MIMEMultipart()
    msg['From'] = f'Tobify <{sender_email}>'
    msg['To'] = user.email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, user.email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
