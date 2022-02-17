# UCSF_Assignment_AP3
The script monitors a folder for csv files, the file is then checked for emails ending with @abc.edu, the script generates a file with the same name + YYYYMMDDHH24MISS.csv, (example: users.csv file becomes users20211018161411.csv), this file contains the records that end with @abc.edu, this new file is placed in the outgoing folder.
The original file is then archived in the Archives folder, the name is changed to name + YYYYMMDDHH24MISS.csv.

In order for the script to run correctly it needs three folder in the same folder as main.py:
* Archives
* Input
* Output

Input is where the file to process is placed.
Output is where the file with @abc.edu entries in placed.
Archives is where the original file to be processed is archived.

The script also needs values for these variables:
* MY_EMAIL
* MY_PASSWORD
* RECIPIENT_EMAIL
These values can and should be stored in environment variables.
If using gmail there are security settings that might need to be changed first in gmail settings to be able to send email.

The script can be run by running "python3 main.py" in the terminal from the same directory as main.py file, it can also be scheduled to run as a job using crontab on macOS or task scheduler on windows.
