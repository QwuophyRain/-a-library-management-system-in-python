class LibraryItem:
    def __init__(self, title, author, id):
        self.title = title
        self.author = author
        self.id = id
        self.on_loan = False

    def borrow(self):
        self.on_loan = True

    def return_item(self):
        self.on_loan = False
    def __str__(self):
        return f"{self.title} by {self.author} ({self.id})"

class Book(LibraryItem):
    def __init__(self, title, author, id, genre):
        super().__init__(title, author, id)
        self.genre = genre

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_items = []

    def borrow_item(self, item):
        if not item.on_loan and len(self.borrowed_items) < 3:
            item.borrow()
            self.borrowed_items.append(item)
            print(f"{self.name} borrowed {item}")
        else:
            if item.on_loan:
                print(f"{item} is already on loan.")
            else:
                print(f"{self.name} has reached the maximum borrowing limit.")

    def return_item(self, item):
        if item in self.borrowed_items:
            item.return_item()
            self.borrowed_items.remove(item)
            print(f"{self.name} returned {item}")
        else:
            print(f"{self.name} did not borrow {item}.")

    def __str__(self):
        return f"{self.name} ({self.member_id})"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def __str__(self):
        return f"Books: {len(self.books)}\nMembers: {len(self.members)}"


# Example usage
library = Library()

book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1234, "Fantasy")
book2 = Book("Pride and Prejudice", "Jane Austen", 5678, "Romance")

member1 = Member("Kwame Addo", 9012)
member2 = Member("Lilian Quist", 3456)

library.add_book(book1)
library.add_book(book2)
library.add_member(member1)
library.add_member(member2)

member1.borrow_item(book1)
member2.borrow_item(book2)
member1.borrow_item(book2)  # Should fail because book2 is already on loan
member2.return_item(book2)
member1.borrow_item(book2)

print(library)
