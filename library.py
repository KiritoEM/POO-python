class Library:
    def __init__(self):
        self.book = []
        
    def add_book(self,book):
        self.book.append(book)
        print(f"Livre {book.title} a été ajouté")
    
    
    def print_book(self):
        print("Liste des livres diponibles dans la bibliothèque")
        
        for book in self.book:
            if book.dispo:
                print(f"Titre: {book.title}, Année: {book.year}, Disponibilité: {book.dispo}")
    
    def search_book(self, title):
        for book in self.book:
            if title.lower() in book.title.lower():
                print(f"Livre {title} trouvé dans la bibliothèque")
                return book
        print("Livre non trouvé")
        return None
                
    def emprunter_book(self, title):
        book = self.search_book(title)
        if (book):
            book.emprunter()
        