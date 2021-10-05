import smtplib
import imghdr
import pandas as pd
from email.message import EmailMessage

df = pd.read_csv('Details.csv')

contact = df['Email'].to_list()

file = df['Name'].to_list()

print(file)
print(contact)

for i in range(len(contact)):

    msg = EmailMessage()
    msg['Subject'] = "Subject"
    msg['From'] = "Sender's email address"

    msg.set_content('''Content of the mail''')

    msg['To'] = contact[i]
    print(msg['To'])

    with open(f"{file[i]}.jpg" , "rb") as f:  # For image attachment
        data = f.read()
        type = imghdr.what(f.name)
        name = f.name
        print(name)

        msg.add_attachment(data, maintype="image", subtype=type, filename=name)


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('Sender's email address', 'password')
        smtp.send_message(msg)

