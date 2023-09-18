import sys

def compare(first,second):
    first=input("Input File name :")
    i=open(first,"r")
    second=input("Output file name :")
    o=open(second,"r")

    content1 = i.read()
    content2 = o.read()

    if content1 == content2:
        print("Success: Both files have the same contents.")
    else:
        print("Failure: Files have different contents.")

def main():
    if len(sys.argv)!=3:
        print("Usage: Python demo.txt abc.txt")
    else:
        i=sys.argv[1]
        j=sys.argv[2]
        compare(i,j)

if __name__=="__main__":
    main()