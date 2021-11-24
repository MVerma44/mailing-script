from email import message
import smtplib
import imghdr
import pandas as pd
from email.message import EmailMessage
from credentials import *
from bs4 import BeautifulSoup
import ast
import json

df = pd.read_csv('personal.csv')
contact = df['Email'].to_list()
certi = df['certi'].to_list()
card = df['card'].to_list()
name = df['Name'].to_list()
memNumber = df['memNumber'].to_list()

creds = json.load(open("password.json", "rb"))

for n, c,cert, crd, number in zip(name, contact, certi, card, memNumber):
    msg = EmailMessage()
    msg['Subject'] = "Welcome Onboard at MUACM as a Platinum Member!"
    msg['From'] = "sarthakkhandelwal032000@gmail.com"

    msg.set_content(''' ''')
    html_msg = open('mail.html').read()
    soup = BeautifulSoup(html_msg, "html.parser")

    # Head Tags
    element = soup.find("h3",{"id":"Heads"})
    element.string = f"Congratulations {n}!!"

    # Membership Number
    element = soup.find("span",{"id":"memNumber"})
    element.string = number
    html_new_msg = str(soup)
    msg.add_alternative(html_new_msg, subtype='html')

    msg['To'] = c # contact[i]
    #print(msg['To'])

    # Certificate
    with open(cert , "rb") as f:
        data = f.read()
        type = imghdr.what(f.name)
        name = f.name
        #print(name)
        #print(data)
        msg.add_attachment(data, maintype="image", subtype=type, filename=name)

    # Card
    with open(crd , "rb") as f:
        data = f.read()
        type = imghdr.what(f.name)
        name = f.name
        #print(name)
        msg.add_attachment(data, maintype="image", subtype=type, filename=name)


    # with open(f"sticker.png" , "rb") as f:
    #     data = f.read()
    #     type = imghdr.what(f.name)
    #     name = f.name
    #     print(name)
    #     msg.add_attachment(data, maintype="image", subtype=type, filename=name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(creds['name'], creds["pass"])
        smtp.send_message(msg)
        print("mail_sent!")
