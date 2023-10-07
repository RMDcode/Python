import os
import time
import psutil
import smtplib
import schedule
import urllib.request
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


def is_connected(url_to_check='http://www.google.com'):
    try:
        urllib.request.urlopen(url_to_check, timeout=1)
        return True
    except urllib.error.URLError as err:
        print("Unable to establish a connection to the URL:", err)
        return False

def MailSender(filename, id_mail, current_time):
    try:
        fromaddr = "dhurir163@gmail.com"
        toaddr = id_mail
        ccaddr = "dhurirohit4@gmail.com"

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Cc'] = ccaddr

        body = f"""
        Hello,

        Please find attached the log file containing information about running processes.
        Log File is created at: {current_time}

        This is an auto-generated email.

        Thank & Regards,
        Rohit Dhuri
        """

        Subject = f"Process log generated at: {current_time}"

        msg['Subject'] = Subject
        msg.attach(MIMEText(body, 'plain'))

        attachment = open(filename, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename={filename}")
        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "wevf wmal brce nsja")

        recipients = [toaddr] + ccaddr.split(",")
        text = msg.as_string()
        s.sendmail(fromaddr, recipients, text)

        s.quit()
        print("Log File successfully sent through Mail")

    except Exception as E:
        print("Unable to send mail", E)

def ProcessLog(log_dir,id_mail):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-" * 80
    timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
    log_path = os.path.join(log_dir, f"MarvellousLog_{timestamp}.log")

    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Marvellous Infosystems Process Logger: " + time.ctime() + "\n")
    f.write(separator + "\n")
    f.write("\n")

    for proc in psutil.process_iter(attrs=['name', 'pid', 'username']):
        try:
            pinfo = proc.info
            vms = proc.memory_info().vms / (1024 * 1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write(f"{element}\n")

    print(f"Log file is successfully generated at location {log_path}")

    current_time = time.ctime()
    if is_connected():
        startTime = time.time()
        MailSender(log_path, id_mail, current_time)
        endTime = time.time()

        print(f"Took {endTime - startTime} seconds to send mail")
    else:
        print("There is no internet connection")

def main():
    print("------Marvellous Infosystems------")
    print("Application name:", argv[0])

    if len(argv) != 3:
        print("Error: Invalid number of arguments")
        exit()

    if argv[1] == "-h" or argv[1] == "-H":
        print("This script is used to log records of running processes")
        exit()

    if argv[1] == "-u" or argv[1] == "-U":
        print("Usage: ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        ProcessLog(argv[1],argv[2])
    except ValueError as v:
        print("Error: Invalid datatype of input", v)

    except Exception as E:
        print("Error: Invalid input", E)

if __name__ == "__main__":
    main()
