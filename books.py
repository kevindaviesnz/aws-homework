from books import Author, BookItem, BookStore

try:
    
    book_author = Author(name="hello", author_id="AAAA-1111")
    print(book_author.__dict__)

    book = BookItem(name="my book", author=book_author, year_published=3000)
    print(book.__dict__)

    book_store = BookStore(name="my bookstore", bookShelf=[1])
    print(book_store.__dict__)

except ValueError as ve:
    print(ve)
    
