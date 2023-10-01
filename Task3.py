import schedule
from datetime import datetime
import pandas as pd
import time
import smtplib
import urllib.request
from sys import argv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def is_connected():
    try:
        urllib.request.urlopen('http://www.google.com', timeout=1)
        return True
    except urllib.error.URLError as err:
        print("Unable to establish a connection to the URL:", err)
        return False

def send_birthday_wishes(i, j, k):
    try:
        fromaddr = "dhurir163@gmail.com"
        toaddr = i
        ccaddr = "dhurir163@gmail.com"

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['cc'] = ccaddr

        subject = "Task3: Birthday Wishes Schedular "
        msg['Subject'] = subject

        body = f"""
            HI,
            {k}
            {j}
        """

        msg.attach(MIMEText(body, 'plain'))

        s=smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "wevf wmal brce nsja")

        recipients=[toaddr]+ccaddr.split(",")

        text=msg.as_string()

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
            startTime=time.time()
            separate = "-" * 20

            dataframe = pd.read_excel("C:\\Users\\Lenovo\\Desktop\\Python\\Task\\Task3.xlsx")
            column1 = "DOB"
            column2 = "Message"
            column3 = "Mail Id"

            for index, row in dataframe.iterrows():
                value1=row[column1].strftime("%Y-%m-%d")  
                print(value1)
                value2=row[column2]
                print(value2)
                value3=row[column3]
                print(value3)

                odate=datetime.strptime(value1, "%Y-%m-%d")
                fdate=odate.strftime("%d-%m-%y")
                print(fdate)
                print(separate)

                current_date=datetime.now().strftime("%d-%m-%y")
                if(current_date == fdate):
                    send_birthday_wishes(value3, value2, fdate)
        
            schedule.every().day.at("02:20")
                    
            while True:
                schedule.run_pending()
                time.sleep(1)  

            endTime = time.time()
            print("Took %s seconds to send email" % (endTime - startTime))
        else:
            print("There is no internet connection")

    except ValueError as v:
        print("Error: Invalid datatype of input", v)

    except Exception as E:
        print("Error: Invalid input", E)

if __name__ == "__main__":
    main()
