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
import hashlib

def findDup(path):
    flag = os.path.isabs(path)
    
    if flag == False:
        path = os.path.abspath(path)
    
    exists = os.path.isdir(path)

    dups = {}

    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            print("Current folder is : "+dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]

        return dups
    else:
        print("Invalid Path")


def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()


def DeleteFiles(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    
    icnt = 0
    iFound = 0

    if len(results) > 0:
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt >= 2:
                    os.remove(subresult)
                    iFound+=1
            icnt = 0
        
        print("Number of duplicate files found and deleted : ",iFound)
        
    else:
        print("No duplicate files found.")



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

        Please find attached the log file containing information about Duplicate files.
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

def ProcessLog(dict1,wait_time,id_mail):
    log_dir = "C:\\Users\\Lenovo\\Desktop\\Python\\assignment_13\\Apps"

    listprocess = []
    print("Waiting time is :",wait_time)
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-" * 80
    timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
    log_path = os.path.join(log_dir, f"DuplicateFilesLog_{timestamp}.log")

    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Duplicate files logger: " + time.ctime() + "\n")
    f.write(separator + "\n")
    f.write("\n")

    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    
    if len(results) > 0:
        print("Duplicates Found:")
        print("The following files are duplicate")
        for result in results:
            for subresult in result:
                listprocess.append(subresult)
    else:
        print("No duplicate files found.")
    for element in listprocess:
        f.write(f"{element}\n")

    print(f"Log file is successfully generated at location {log_path}")

    try:
        while True:
            time.sleep(int(wait_time))
        
            current_time = time.ctime()
            if is_connected():
                startTime = time.time()
                MailSender(log_path, id_mail, current_time)
                endTime = time.time()

                print(f"Took {endTime - startTime} seconds to send mail")
            else:
                print("There is no internet connection")

    except KeyboardInterrupt:
            scheduler.shutdown()
            print("Scheduler stopped.")
    
def main():
    print("------Marvellous Infosystems------")
    print("Application name:", argv[0])
    print("Absolute path of directory contains duplicate files :",argv[1])
    print("Time interval of script in minutes :",argv[2])
    print("Mail ID of the receiver :",argv[3])


    if len(argv) != 4:
        print("Error: Invalid number of arguments")
        exit()

    if argv[1] == "-h" or argv[1] == "-H":
        print("This script is used to log records of running processes")
        exit()

    if argv[1] == "-u" or argv[1] == "-U":
        print("Usage: ApplicationName AbsolutePath_of_Directory Waiting_minutes Mail_ID")
        exit()

    wait_time = int(argv[2]) * 60


    try:
        arr = {}
        arr=findDup(argv[1])
        ProcessLog(arr,wait_time,argv[3])
        DeleteFiles(arr)

    except ValueError as v:
        print("Error: Invalid datatype of input", v)

    except Exception as E:
        print("Error: Invalid input", E)

if __name__ == "__main__":
    main()
