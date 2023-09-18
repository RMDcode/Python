import os.path

def main():
    print("Enter the file name : ",end="")
    File_name=input()

    if os.path.exists(File_name):
        print("This file is already existing")

    else:
        print("This file isn't exist in this directory")

    
if __name__=="__main__":
    main()