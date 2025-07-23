def show_menu():
   print("1. Add books")
   print("2. Display books")
   print("3. Search book")
   print("4. Exit")
   
def add_books(lib):
    book_name = input("Enter book name: ")
    author_name = input("aUTHOR: ")
    lib.append({"book_name":book_name, "author_name":author_name})
    print("added")

def search_book(lib):
    inp = input("Enter the book you want to search: ")
    found_books = [book for book in lib if inp in book['book_name']]
    for book in found_books:
            print(f"- {book['book_name']} by {book['author_name']}")
    
def display_books(lib):
    print(lib)
    for i,book in enumerate(lib):
        print(f"{i+1}: {book.get("book_name")}")
    

def main():
    show_menu()

# try:
    library = []
    while True:

     n = int(input("Enter any number from above: "))
    
     if n == 1:
      add_books(library)
     elif n == 2:
      display_books(library)
     elif n == 3:
        search_book(library)
     elif n == 4:
        print("Done,bye")
        break
    else:
        print("Please enter a valid number.")
        
# except Exception as e:
#     print("Error:", e)
    

if __name__ == "__main__":
    main()