from email import message
import smtplib
import imghdr
import pandas as pd
from email.message import EmailMessage
from credientials import *

df = pd.read_csv('personal.csv')

contact = df['Email'].to_list()

certi = df['certi'].to_list()

card = df['card'].to_list()

name = df['Name'].to_list()


for i in range(len(contact)):

    msg = EmailMessage()
    msg['Subject'] = "Platinum Membership"
    msg['From'] = "vmayank.1725@gmail.com"

    msg.set_content(''' ''')
    html_msg = open('mssg.html').read()
    msg.add_alternative(html_msg, subtype='html')

    msg['To'] = contact[i]
    print(msg['To'])


    with open(f"{card[i]}" , "rb") as f:
        data = f.read()
        type = imghdr.what(f.name)
        name = f.name
        print(name)
        msg.add_attachment(data, maintype="image", subtype=type, filename=name)

    with open(f"{certi[i]}" , "rb") as f:
        data = f.read()
        type = imghdr.what(f.name)
        name = f.name
        print(name)
        msg.add_attachment(data, maintype="image", subtype=type, filename=name)

    
    # with open(f"sticker.png" , "rb") as f:
    #     data = f.read()
    #     type = imghdr.what(f.name)
    #     name = f.name
    #     print(name)
    #     msg.add_attachment(data, maintype="image", subtype=type, filename=name)


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('vmayank.1725@gmail.com', password)
        smtp.send_message(msg)

        