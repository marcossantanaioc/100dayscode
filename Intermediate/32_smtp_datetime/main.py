##################### Extra Hard Starting Project ######################
import pandas as pd
import random
import smtplib
import datetime as dt

EMAIL = 'blablabla@mail.com'
PASSWORD = 'XXXXXXXXXXXXXXXXXX'

# 1. Update the birthdays.csv
birthdays = pd.read_csv('birthdays.csv')

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day

current_birthdays = birthdays[(birthdays['month'] == month) & (birthdays['day'] == day)]
if not current_birthdays.empty:
    target_email = current_birthdays.email.item()
    name = current_birthdays.name.item()
    print(target_email)

    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
    # actual name from birthdays.csv
    letters = [f'letter_templates/letter_{x}.txt' for x in range(1, 4)]
    chosen_letter = random.choice(letters)
    with open(chosen_letter, 'r') as f:
        all_lines = [line.replace("[NAME]", name) for line in f.readlines()]
        message_to_send = ''.join(all_lines)
    # 4. Send the letter generated in step 3 to that person's email address.

    with smtplib.SMTP(host='smtp.mymailprovider.com') as connection:
        # Put the SMTP connection in TLS (Transport Layer Security) mode.
        # All SMTP commands that follow will be encrypted.
        connection.starttls()

        connection.login(user='MYMAIL@MAIL.COM', password=PASSWORD)

        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=f'Subject:Happy birthday {name}\n{message_to_send}')
