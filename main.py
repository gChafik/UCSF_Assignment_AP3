import os.path
from datetime import datetime as dt
import shutil
import time
import smtplib


MY_EMAIL = "enter from email"
MY_PASSWORD = "enter MY_EMAIL password"
RECIPIENT_EMAIL = "enter to email"

def file_name():
    for file in os.listdir("./Input/"):
        if file.endswith(".csv"):
            return file.split(".")[0]

def process_file(filename):
    d = dt.now().strftime('%Y%m%d%H%M%S')
    outputfile = f"{filename}{d}.csv"
    with open(f'./Outgoing/{outputfile}', 'a') as users_output:
        for user in users_abc:
            users_output.write(f"{user}\n")
    original_file = f"./Input/{filename}.csv"
    archive_file = f"./Archives/{filename}{d}.csv"
    shutil.move(original_file, archive_file)

def send_email():
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
    from_addr=MY_EMAIL,
    to_addrs=RECIPIENT_EMAIL,
    msg=f"Subject: File has been processed\n\n"
        f"{dt.now()}\nFile Processed: {filename}.csv\nTotal numbers of entries in file: {total_entries}\n" 
        f"Total number of entries moved: {total_moved}\n"
    )
    print('File has been processed')

while True:
    users_abc = []
    total_entries = 0
    total_moved = 0
    filename = file_name()
    if os.path.exists(f"./Input/{filename}.csv"):
        with open(f"./Input/{filename}.csv") as users_input:
            users_input_lst = users_input.readlines()
            users_abc = [user.rstrip('\n') for user in users_input_lst[1:] if user.rstrip('\n').endswith('@abc.edu')]
            process_file(filename)
            total_entries = len(users_input_lst)
            total_moved = len(users_abc)
            send_email()

    else:
        print("No file to Process")
        time.sleep(10)


