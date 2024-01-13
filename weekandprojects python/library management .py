class Library:
  def __init__(self):
    self.noBooks = 0
    self.books = []
    
  def addBook(self, book):
    self.books.append(book)
    self.noBooks = len(self.books)

  def showInfo(self):
    print(f"The library has {self.noBooks} books. \nThe books are\v")
    for book in self.books:
      print(book)


l1 = Library()
l1.addBook("Harry Potter : Philospher stone")
l1.addBook("Harry Potter : Chamber of secrets")
l1.addBook("Harry Potter : Prisoner of azkabaan")
l1.addBook("Harry Potter : Half blood prince")
l1.addBook("Harry Potter : Order of pheonix")
l1.addBook("Harry Potter : Goblet of fire")
l1.addBook("Harry Potter : Deathly hollows")
l1.showInfo()
    
  