import smtplib
import datetime as dt
import random

# -- Sending quotes on Monday -- #

my_email = "tedmbangudemy@gmail.com"
app_password = ""  # fill the password for the email here
ME = "tdark237@gmail.com"


def send_email(msg):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # encryption
        connection.login(user=my_email, password=app_password)
        connection.sendmail(from_addr=my_email, to_addrs=ME, msg=f"Subject:Monday motivation \n\n{msg}")


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        # Getting the list of every single line in the file
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    send_email(msg=quote)
