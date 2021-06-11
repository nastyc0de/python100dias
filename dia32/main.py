import datetime as dt
import random
import smtplib

EMAIL = 'CORREO@GMAIL.COM'
PASSWORD = '123456'
now = dt.datetime.now()
# yr = now.year
# month = now.month
day_of_week = now.weekday()
# print(day_of_week)
dict ={}
if day_of_week == 4:
    with open('./quotes.txt', 'r') as datafile:
        all_quotes = datafile.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs='destinatario@gmail.com',
            msg=f'Subject:monday motivation\n\n{quote}'
        )
