# UCSF_Assignment_AP3
The script monitors a folder for csv files, the file is then chekced for emails ending with @abc.edu, the script generates a file with the same name + YYYYMMDDHH24MISS.csv, (example: users.csv file becomes users20211018161411.csv), this file contains the records that end with @abc.edu, this new file is placed in the outgoing folder.
The original file is then archived in the Archives folder, the name is changed to name + YYYYMMDDHH24MISS.csv.

The script is a continuously running while loop, in order for the script to run correctly it needs three folder in the same folder as main.py:
* Archives
* Input
* Output

Input is where the file to process is placed.
Output is the file with @abc.edu entries in placed.
Archives is where the original file to be processed is archived.

The script also needs values for these variables:
* MY_EMAIL
* MY_PASSWORD
* RECIPIENT_EMAIL
These values can and should be stored in environment variables
If using gmail there are security settings that might need to be changed first to be able to send email.
