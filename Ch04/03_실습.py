class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"책 제목은 {self.title}이며 작가는 {self.author}입니다.")

class Library():
    def __init__(self):
        self.books = []

    def addBook(self, book: Book):
        if(isinstance(book, Book)):
            self.books.append(book)
        else:
            print("INCORRECT INPUT!\n", type(book))

    def bookList(self):
        print("현재 보유중인 책은 아래와 같습니다: ")
        print("==================================")
        for book in self.books:
            print(book.title)
        print("==================================")

    def show_books(self):
        for book in self.books:
            book.display_info()
    
book1 = Book("파이썬입문", "홍길동")
book2 = Book("홍길동전", "홍길동")
book3 = Book("난중일기", "이순신")
book4 = Book("셜록홈즈", "아서 코난 도일")
book1.display_info()

library1 = Library()
library1.addBook(book1)
library1.addBook(book2)
library1.addBook(book3)
library1.addBook(book4)
library1.addBook("TEST WRONG INPUT!")
library1.bookList()
print("========================")
library1.show_books()