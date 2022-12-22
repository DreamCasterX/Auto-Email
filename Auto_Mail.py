#!/usr/bin/env python3

import email.message
import smtplib

# input login info (mailbox, account & password)
# Gmail SMTP server: host=smtp.gmail.com, port=465 (SSL)
# Yahoo SMTP server: smtp.mail.yahoo.com, port: ???
# Hotmail SMTP server: host=smtp-mail.outlook.com, port=587 (no SSL)

msg = email.message.EmailMessage()
option = input("\n(1)Gmail\n" + "(2)Hotmail\n" + "\n您使用的信箱是:")
if option == "1":
    msg["From"] = str(input("信箱帳號:")) + "@gmail.com"
    server = smtplib.SMTP_SSL(host="smtp.gmail.com", port=465)
    msg["Password"] = "pofbspulyxgavbjz"
elif option == "2":
    msg["From"] = str(input("信箱帳號:")) + "@hotmail.com"
    server = smtplib.SMTP(host="smtp-mail.outlook.com", port=587)
    server.starttls()
    msg["Password"] = input("信箱密碼:")
else:
    print("\n輸入錯誤, 請重新執行")
    exit()

msg["To"] = input("收件人信箱:")
# msg["To"] = "mike.lu@hp.com"
msg["Subject"] = input("信件主旨:")

# Text format content
msg["Body"] = str(input("信件內容:"))
msg.set_content(msg["Body"])

# Html format content
# msg.add_alternative("<h3>Python Test</h3>Have a good day, my friend :)",subtype="html")

# DEBUG USE ONLY:
# --------------------------------------
# Check if return code is "250" = successfully communicated with SMTP server
# server_res = server.ehlo()
# print(f"res 1 ==> {server_res}")

# Check if return code is "220" = successfully activated TLS encryption (還沒成功過)
# smtp_tls = server.starttls()
# print(f"start tls ==> {smtp_tls}")

# Login to SMTP server
# Check if return code is "235" = successfully logged in
# smtp_login = server.login(msg["From"],msg["Password"])
# print(f"SMTP login ==> {smtp_login}")
# --------------------------------------

server.login(msg["From"], msg["Password"])
status = server.send_message(msg)
if status == {}:
    print("\n郵件發送成功!")
else:
    print("\n郵件發送失敗")
server.close()
