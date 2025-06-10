from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv("key.env")

def send_alert_email(subject: str, message: str):
    sender_email = os.getenv("GMAIL_USER")
    app_password = os.getenv("GMAIL_PASS")
    receiver_email = "ericlinlin950521@gmail.com"  # 也可換成其他人

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("✅ 郵件已成功寄出！")
    except Exception as e:
        print("❌ 郵件寄送失敗：", e)
if __name__ == "__main__":
    send_alert_email(
        subject="⚠️ 刀具異常警告",
        message="目前刀具 RMS 偏高，預測磨耗異常，請盡速檢查。"
    )