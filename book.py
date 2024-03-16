from library import Library

class Book:
    def __init__(self, title, year, status):
        self.title = title
        self.year = year
        self.status = status
        self.dispo = True
        
    def emprunter(self):
        if self.dispo:
            self.dispo = False
            print(f"Le livre {self.title} a été emprunté avec succés")
        else:
            print("Désolé, ce livre  n' est pas disponible")
            
    def retourner(self):
        self.dispo = Trueprint(f"Le livre {self.title} a été retourné avec succés")
        

#instanciation de la classe librairie
my_library = Library()

#instanciation de la classe livre
book_1 = Book("alice et la diligence", 1951, "disponible")
book_2 = Book("Harry potter et le Fantome", 2000, "disponible")

my_library.add_book(book_1)
my_library.add_book(book_2)
my_library.search_book("Harry")
my_library.print_book()


        
        