class BookStore:
    No_of_books=0

    def __init__(self,name,author):
        self.BookName=name
        self.BookAuthor=author
        BookStore.No_of_books=BookStore.No_of_books + 1

    def Display(self):
        print("Name of the book:",self.BookName)
        print("Author of the book:",self.BookAuthor)
        print("Number of the books in the store:",BookStore.No_of_books)
        print("<-------------------------------------------------------->")

def main():
    obj1 = BookStore("Linux System Programming", "Robert Love")
    obj1.Display()

    obj2 = BookStore("C-Programming", "Dennis Ritchie")
    obj2.Display()

if __name__ == "__main__":
    main()
