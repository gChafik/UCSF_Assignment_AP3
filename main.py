import os.path
from datetime import datetime as dt
import shutil
import time
import smtplib



filename = os.path.basename("./Input/users.csv")

def process_file():
    d = dt.now().strftime('%Y%m%d%H%M%S')
    outputfile = f"{filename.split('.')[0]}{d}.csv"
    with open(f'./outgoing/{outputfile}', 'a') as users_output:
        for user in users_abc:
            users_output.write(f"{user}\n")
    original_file = "./Input/users.csv"
    archive_file = f"./Archives/users{d}.csv"
    shutil.move(original_file, archive_file)

def send_email():
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
    from_addr=MY_EMAIL,
    to_addrs=MY_EMAIL2,
    msg=f"{dt.now()}\n Total numbers of entries in file: {total_entries}\n Total number of entries moved: {total_moved}"
    )

while True:
    users_abc = []
    total_entries = 0
    total_moved = 0
    if os.path.exists("./Input/users.csv"):
        with open("./Input/users.csv") as users_input:
            users_input_lst = users_input.readlines()
            users_abc = [user.rstrip('\n') for user in users_input_lst[1:] if user.rstrip('\n').endswith('@abc.edu')]
            process_file()
            total_entries = len(users_input_lst)
            total_moved = len(users_abc)
            send_email()

    else:
        print("No file to Process")
        time.sleep(10)


