'''
Niharika Agrawal
CSC 161
HW 8
'''

#define my book class
class Book:
    def __init__(self, title, author, publication_year, isbn):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn

    #define the four accessor classes for my data
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.publication_year

    def get_isbn(self):
        return self.isbn

    #return book data in a pretty format
    def to_str(self):
        return f"{self.title} by {self.author} ({self.publication_year})"

    #is the book published in the last 10 years?
    def is_published_recently(self, current_year):
        if self.publication_year <= (current_year - 10):
            return False
        else:
            return True

#define class to enter data for a book manually
def enter_book_data():
    title = input("Title: ")
    author = input("Author: ")
    publication_year = int(input("Publication Year: "))
    isbn = input("ISBN: ")

    new_book = Book(title, author, publication_year, isbn)
    return new_book

#define main class with all example tests
def main():
    #book 1
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "978-3-16-148410-0")
    '''
    print(book1.to_str())
    print(book1.is_published_recently(2023))
    print(book1.get_isbn())
    print(book1.get_year())
    '''

    #book 2
    book2 = Book("The Last Wish", "Andrzej Sapkowski", 1993, "0-575-07192-1")
    '''
    print(book2.to_str())
    print(book2.is_published_recently(2023))
    print(book2.get_title())
    print(book2.get_author())
    '''

    #book 3
    book3 = enter_book_data()
    print(book3.to_str())

main()
