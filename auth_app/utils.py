

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(user, otp):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465

    sender_email = 'tobixdev@gmail.com'
    sender_password = 'ahbnxwrbwzgaogqa'
    subject = 'Email Verification'
    body = f'''<div style="font-family: Helvetica,Arial,sans-serif;min-width:1000px;overflow:auto;line-height:2">
   <div style="margin:50px auto;width:70%;padding:20px 0">
     <div style="border-bottom:1px solid #eee">
       <a href="" style="font-size:1.4em;color: #00466a;text-decoration:none;font-weight:600">Tobix Dev.</a>
     </div>
     <p style="font-size:1.1em">Hi, {user.first_name}</p>
     <p>Welcome. Use the following OTP to complete your Sign Up procedures. OTP is valid for 5 minutes</p>
     <h2 style="background: #00466a;margin: 0 auto;width: max-content;padding: 0 10px;color: #fff;border-radius: 4px;">{otp}</h2>
     <p style="font-size:0.9em;">Regards,<br />Tobix Dev</p>
     <hr style="border:none;border-top:1px solid #eee" />
     <div style="float:right;padding:8px 0;color:#aaa;font-size:0.8em;line-height:1;font-weight:300">
       <p>Tobix Inc</p>
     </div>
   </div>
 </div>
 '''

    msg = MIMEMultipart()
    msg['From'] = 'Tobix Dev. <tobi@tobix.dev>'
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


class User:
    def __init__(self) -> None:
        self.first_name = 'tobi'
        self.email = 'xhaalez1@gmail.com'


user1 = User()

send_email(user1, 123456)
# print(user.first_name)
