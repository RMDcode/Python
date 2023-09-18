import sys

def copy(first,se):
    first=input("Input File name :")
    i=open(first,"r")
    second=input("Output file name :")
    o=open(second,"w")


    o.write(i.read())
    print("Contents copied from",first," to ",second," Successfully")


def main():
    if len(sys.argv)!=3:
        print("Usage: Python demo.txt abc.txt")
    else:
        i=sys.argv[1]
        j=sys.argv[2]
        copy(i,j)

if __name__=="__main__":
    main()