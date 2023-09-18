import os.path

def main():
    print("Enter the file name: ",end="")
    File_name=input()

    if os.path.exists(File_name):
       fobj=open(File_name,"r")     #Read mode
       if fobj:
            print("Below lines from :")

            Data = fobj.read()
            print("Data from file is:",Data)

            fobj.close()
        
       else:
            print("Unable to open File")

    else:
        print("This file isn't exist in this directory")
    
    

if __name__=="__main__":
    main()