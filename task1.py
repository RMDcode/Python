import pandas as pd
import os
import time
import psutil
import smtplib
import schedule
import urllib.request
from sys import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def is_connected():
    try:
        urllib.request.urlopen('http://www.google.com', timeout=1)
        return True
    except urllib.error.URLError as err:
        print("Unable to establish a connection to the URL:", err)
        return False

def MailSender(i,time):
    try:
        fromaddr = "dhurir163@gmail.com"
        toaddr = i
        ccaddr = "dhurir163@gmail.com"

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['cc'] = ccaddr


        subject = "Task1"
        msg['Subject'] = subject

        body = """
            Hello........
        """

        msg.attach(MIMEText(body, 'plain'))

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "wevf wmal brce nsja")

        recipients = [toaddr] + ccaddr.split(",")

        text = msg.as_string()

        s.sendmail(fromaddr, recipients, text)
        s.quit()

        print("Email sent successfully")

    except Exception as E:
        print("Unable to send email", E)

def main():
    print("------Marvellous Infosystems------")
    print("Application name:", argv[0])

    try:
        if is_connected():
            startTime = time.time()
            dataframe = pd.read_excel("C:\\Users\\Lenovo\\Desktop\\Python\\Task\\Task1.xlsx")
            df = pd.DataFrame(dataframe)

            for i in range(len(df)):  
                for j in range(len(df.columns)): 
                    cell_value = df.iloc[i, j]
                    print(cell_value)
                    MailSender(cell_value,time.ctime())
            endTime = time.time()
            print("Took %s seconds to send email" % (endTime - startTime))
        else:
            print("There is no internet connection")

    except ValueError as v:
        print("Error: Invalid datatype of input", v)

    except Exception as E:
        print("Error: Invalid input", E)

if __name__=="__main__":
    main()