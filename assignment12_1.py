import psutil

def ProcessDisplay():
    listprocess=[]

    for proc in psutil.process_iter(attrs=['name','pid','username']):
        try:
            pinfo = proc.info

            listprocess.append(pinfo)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listprocess  


def main():
    print("Marvellous Automation assignment on 12")

    print("Process Monitor")

    listprocess = ProcessDisplay()

    for elem in listprocess:
        print(elem)

if __name__=="__main__":
    main()