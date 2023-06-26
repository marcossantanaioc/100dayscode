import smtplib
import datetime as dt
import random



EMAIL = 'giu.chemi@gmail.com'
PASSWORD = 'vkiqoqsxeyxqqbtp'

with open('quotes.txt') as f:
    quotes = [x.strip() for x in f.readlines()]
chosen_quote = random.choice(quotes)


now = dt.datetime.now()
year = now.year
month = now.month
weekday = now.weekday()

date_of_birth = dt.datetime(year=1990, month=7, day=21)

#if weekday == 0:

# with smtplib.SMTP(host='smtp.gmail.com') as connection:
#     # Put the SMTP connection in TLS (Transport Layer Security) mode.
#     # All SMTP commands that follow will be encrypted.
#     connection.starttls()
#
#     connection.login(user='marcosvssantana@gmail.com', password=PASSWORD)
#
#     connection.sendmail(from_addr='marcosvssantana@gmail.com',
#                         to_addrs='marcosvssantana@gmail.com',
#                         msg=f'Subject:100days of code test\n{chosen_quote}')

# print(date_of_birth)
# print(date_of_birth.strftime('%d-%m-%y'))