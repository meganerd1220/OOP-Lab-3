class Book:
    def __init__(self):
        book_id = ""
        book_title = ""
        author_id = ""
        publisher = ""
        edition_no = ""
        year_of_publication = ""

    def create_a_book(self):
        self.book_id = input("Enter the book ID: ")
        self.book_title = input("Enter the book title: ")
        self.author_id = input("Enter the author ID: ")
        self.publisher = input("Enter the publisher: ")
        self.edition_no = input("Enter the edition number: ")

    def display_book(self):
        print("Book ID: ", self.book_id)
        print("Title: ", self.book_title)
        print("Author ID: ", self.author_id)
        print("Publisher: ", self.publisher)
        print("Edition number: ", self.edition_no)


class Author:
    def __init__(self):
        author_id = ""
        author_name = ""
        affiliation = ""
        country = ""
        author_phone = ""
        author_email = ""

    def create_author(self):
        self.author_id = input("Enter the author ID: ")
        self.author_name = input("Enter the author name: ")
        self.affiliation = input("Enter the author's affiliation: ")
        self.country = input("Enter the author's country: ")
        self.author_phone = input("Enter the author's phone number: ")
        self.author_email = input("Enter the author's email address: ")

    def display_author(self):
        print("Author ID: ", self.author_id)
        print("Author Name: ", self.author_name)
        print("Affiliation: ", self.affiliation)
        print("Country: ", self.country)
        print("Phone number: ", self.author_phone)
        print("Email: ", self.author_email)


class User:
    def __init__(self):
        user_id = ""
        user_name = ""
        password = ""
        address = ""
        user_phone = ""
        user_email = ""

    def create_user(self):
        self.user_id = input("Enter the user ID: ")
        self.user_name = input("Enter the name of the user: ")
        self.password = input("Enter the password for the user's account: ")
        self.address = input("Enter the user's address: ")
        self.user_phone = input("Enter the user's phone number: ")
        self.user_email = input("Enter the user's email address: ")

    def display_user(self):
        print("User ID: ", self.user_id)
        print("User name: ", self.user_name)
        print("Password: ", self.password)
        print("Address: ", self.address)
        print("Phone number: ", self.user_phone)
        print("Email: ", self.user_email)


class LendingBooks:
    def __init__(self):
        lend_id = ""
        book_id = ""
        user_id = ""
        date_of_lend = ""
        date_of_return = ""

    def create_a_lend(self):
        self.lend_id = input("Enter the lend ID: ")
        self.book_id = input("Enter the ID of the lending book: ")
        self.user_id = input("Enter the user ID of the person checking out the book: ")
        self.date_of_lend = input("Enter the date the lend started: ")
        self.date_of_return = input("Enter the date the book is due: ")

    def display_lend(self):
        print("Lend ID: ", self.lend_id)
        print("Book ID: ", self.book_id)
        print("User ID: ", self.user_id)
        print("Lend Date: ", self.date_of_lend)
        print("Return date: ", self.date_of_return)


a_count = 1
b_count = 1
u_count = 1
l_count = 1
while 1:
    print("1. Add a Book")
    print("2. Add an Author")
    print("3. Add a User")
    print("4. Create a Lending Book")
    print("5. Display all the books")
    print("6. Display all the Authors")
    print("7. Display all the Users")
    print("8. Display all the books that are given out for lending")
    print("9. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        mybook = "book" + str(b_count)
        mybook = Book()
        mybook.create_a_book()
        mybook.display_book()
        b_count += 1
    if choice == '2':
        author = "author" + str(a_count)
        author = Author()
        author.create_author()
        author.display_author()
        a_count += 1
    if choice == '3':
        user = "user" + str(u_count)
        user = User()
        user.create_user()
        user.display_user()
        u_count += 1
    if choice == '4':
        lend = "lend" + str(l_count)
        lend = LendingBooks()
        lend.create_a_lend()
        lend.display_lend()
        l_count += 1
    if choice == '5':
        for i in range(1, b_count + 1):
            mybook = "book" + str(i)
            mybook = Book()
            mybook.display_book()
    if choice == '6':
        for i in range(1, a_count):
            myauthor = "author" + str(i)
            myauthor = Author()
            myauthor.display_author()
    if choice == '7':
        for i in range(1, u_count):
            myuser = "user" + str(i)
            myuser = User()
            myuser.display_user()
    if choice == '8':
        for i in range(1, l_count):
            mylend = "lend" + str(i)
            mylend = LendingBooks()
            mylend.display_lend()
    if choice == '9':
        break
