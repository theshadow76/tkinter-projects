import smtplib
from email.message import EmailMessage

while True:
    msg = EmailMessage()
    msg.set_content('This is my message')

    msg['Subject'] = 'hackeado!'
    msg['From'] = "vigopaul05@gmail.com"
    msg['To'] = "06.alexandre.portner@lafase.cl"

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("vigopaul05@gmail.com", "ztrduxmunhapfhap")
    server.send_message(msg)
server.quit()