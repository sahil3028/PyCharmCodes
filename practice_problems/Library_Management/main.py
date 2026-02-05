import json

with open("bookData.json",'r') as file:
    data=json.load(file)

books=data.get("books",[])


def add_book():
    id1=[]
    copies=0
    ids = [int(book["id"]) for book in books]
    while True:
        try:
            id1=int(input("Enter the book id: ").strip())
            if id1 in ids:
                raise ValueError("Book id Already Exist")
            else:
                break
        except ValueError as e:
            print("Invalid ID: ")
            mainmenu = int(input("enter 0 to return to main menu "))
            if mainmenu == 0:
                return
        continue
    while True:
        try:
            copies=int(input("Enter the no of copies"))
            if copies<=0:
                raise ValueError("Copies must be more than 0")
            else:
                break
        except ValueError as e:
            print("Invalid Copies: ",e)
            continue
    title=input("Enter title")
    author=input("Enter author")
    year=input("Enter publishing year")

    book={
        "id": id1,
        "title": title,
        "author": author,
        "year": year,
        "copies": copies
    }
    books.append(book)

def borrow_book():

    # borrowVar = {book["id"]: book["copies"] for book in books}


    while True:
        count=0
        try:
            bid=int(input("Enter the id of book to borrow"))
            for borrowVar in books:
                if bid == borrowVar["id"]:
                    while True:
                        try:
                            co=int(input("Enter the copies you want: "))
                            if co>borrowVar["copies"]:
                                raise ValueError("We have only ",borrowVar["copies"]," copies left")
                            else:
                                print("Your request is successfully approved")
                                books[count]["copies"]-=borrowVar["copies"]
                                books[count]["borrowed_count"] += co
                                return

                        except ValueError as e:
                            print("copies overflowed: ",e)
                            continue

                else:
                    count+=1

            raise ValueError("Book ID is not available")
        except ValueError as e:
            print("ID not found",e)
            mainmenu = int(input("enter 0 to return to main menu "))
            if mainmenu == 0:
                return
        continue

def return_book():
    while True:
        count = 0
        try:
            bid = int(input("Enter the id of book to return"))
            for borrowVar in books:
                if bid == borrowVar["id"]:
                    while True:
                        try:
                            co = int(input("Enter the copies you want to return: "))
                            if co <=0 :
                                raise ValueError("copies should be greater than 0 ")
                            else:
                                print("Your request is successfully approved")
                                books[count]["copies"] += co
                                return

                        except ValueError as e:
                            print("copies error: ", e)
                            continue

                else:
                    count += 1

            raise ValueError("Book ID is not available")
        except ValueError as e:
            print("ID not found", e)
            mainmenu=int(input("enter 0 to return to main menu "))
            if mainmenu==0:
                return
            continue


def generate_report():
    tbook=0;tcopy=0;mostbor=[];bzero=[];mbCount=0
    for b in books:
        print(b["id"], " -- ", b["title"], " by ", b["author"], " since ", b["year"])
        tbook+=1
        tcopy+=b["copies"]
        if mbCount<b["borrowed_count"]:
            mbCount=b["borrowed_count"]
        if b["copies"] == 0:
            bzero.append(b["title"])

    print("TOtal books:",tbook)
    print("TOtal copies:",tcopy)
    for b in books:
        if b["borrowed_count"]==mbCount:
            mostbor.append(b["title"])
    print("Most borrowed books are: ", mostbor)
    print("Books with zero copies are: ",bzero)

def save_file():
    data={"books":books}
    with open("bookData.json",'w') as file:
        json.dump(data,file,indent=4)

while True:
    ch=int(input("CHOICES:\n1. Add new book\n2. View all books\n3. Borrow a book\n4. Return a book\n5. Generate report\n6. Save & Exit"))
    match ch:
        case 1:
            add_book()
        case 2:
            for b in books:
                print(b["id"]," -- ",b["title"]," by ",b["author"]," since ",b["year"])

        case 3:
            borrow_book()
        case 4:
            return_book()
        case 5:
            generate_report()
        case 6:
            print("bye bye!!")
            save_file()
            break
        case _:
            print("invalid input, Try again")