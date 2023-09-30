import smtplib
import datetime as dt
import csv
import os
import random

my_email = "tedmbangudemy@gmail.com"
app_password = "gyqwqlwobzfktjrh"  # fill the password for the email here


def send_email(address, subject, msg):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # encryption
        connection.login(user=my_email, password=app_password)
        connection.sendmail(from_addr=my_email, to_addrs=f"{address}", msg=f"Subject:{subject} \n\n{msg}")


# ----- birthday wisher start here ------- #

# Getting the date current date object
today = dt.datetime.now().date()

# Path to the folder containing letter templates
letter_folder = 'letter_templates'
# listing the files in the letter templates folder
letter_files = os.listdir(letter_folder)
# Select a random letter template
letter_to_send = random.choice(letter_files)

# Read the CSV file and check for birthdays

with open("birthdays.csv", "r") as birthday_file:
    reader = csv.DictReader(birthday_file)
    for row in reader:
        name = row['name']
        month_birth = int(row['month'])
        day_birth = int(row['day'])
        email = row['email']

        if today.month == month_birth and today.day == day_birth:
            with open(os.path.join(letter_folder, letter_to_send), "r") as letter:
                template = letter.read()
                final_letter = template.replace("[NAME]", name)
            send_email(address=email, subject="HAPPY BIRTHDAY", msg=final_letter)
