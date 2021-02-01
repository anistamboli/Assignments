#Add remove or search book on book records system


rec={'b1':"as",'b3':"dw",'b4':"sasa",'12':"cdsv"}

def addBk():
    bookId= input("Enter book id to add : ")
    if bookId in rec:
        print("Book already exists")
    else:
        bookName= input("Enter book name to add : ")
        rec[bookId]=bookName


def removeBk():
    bookId=input("Enter book id to remove book : ")
    if bookId in rec:
        rec.pop(bookId)
        print("book removed successfully...")
    else:
        print("Book not found!!!")


def search():
    bookId= input("Enter id of book to search: ")
    if bookId in rec:
        print(bookId," is a book naming : ", rec[bookId])
    else:
        print("Book not found!!!")


addBk()
removeBk()
search()
