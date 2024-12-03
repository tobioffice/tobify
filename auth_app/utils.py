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

    subject = 'Verify Your Email Address'
    body = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Email Verification</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    </head>
    <body style="margin: 0; padding: 0; font-family: 'Inter', sans-serif; background-color: #f0f9ff;">
        <div style="max-width: 600px; margin: 40px auto; background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%); padding: 40px; border-radius: 16px; box-shadow: 0 4px 6px rgba(59, 130, 246, 0.1);">
            <div style="text-align: center; margin-bottom: 30px;">
                <h1 style="color: #1e40af; margin: 0; font-size: 28px; font-weight: 700;">Tobify</h1>
                <p style="color: #64748b; font-size: 14px; margin-top: 5px;">Professional Development Platform</p>
            </div>

            <div style="background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); border-radius: 12px; padding: 30px; margin: 20px 0;">
                #x1F44B;</h2>
                <h2 style="color: #1e3a8a; font-size: 20px; margin: 0 0 15px 0; font-weight: 600;">Welcome, {user.first_name}! &
                <p style="color: #475569; font-size: 16px; line-height: 1.6; margin: 0 0 20px 0;">
                    Thank you for joining Tobify. To ensure the security of your account, please verify your email address using the code below. This code will expire in 5 minutes.
                </p>

                <div style="background: #ffffff; border-radius: 12px; padding: 20px; text-align: center; margin: 20px 0; box-shadow: 0 2px 4px rgba(59, 130, 246, 0.05);">
                    <h2 style="background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 32px; letter-spacing: 8px; margin: 0; font-weight: 700;">{otp}</h2>
                </div>

                <p style="color: #64748b; font-size: 14px; margin: 20px 0 0 0;">
                    If you didn't request this verification, please ignore this email.
                </p>
            </div>

            <div style="text-align: center; margin-top: 30px;">
                <p style="color: #64748b; font-size: 14px; margin: 0 0 5px 0;">Need assistance? Our support team is here to help</p>
                <a href="mailto:support@tobify.com" style="color: #3b82f6; text-decoration: none; font-weight: 500;">support@tobify.com</a>
            </div>

            <div style="margin-top: 30px; text-align: center; border-top: 1px solid #e2e8f0; padding-top: 20px;">
                <p style="color: #94a3b8; font-size: 12px; margin: 0;">
                    &copy; 2024 Tobify. All rights reserved.<br>
                    Built with excellence in mind
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
