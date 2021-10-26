# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:12:35 2021

@author: okanr
"""

class backAdminPage:
    
    All_books = []  # All the books in the library. (Even if the members are given a book, this does not change.)
    
    kitaplar = list()  #Books currently available in the library (Books given to members are not in the list.)

    bookInformations = {} #All the books in the library are in dictionary form.(This does not change even if the members are given a book.)
    
    
        
    def __init__(self,book_ID,book_name,writer,publisher,page_count):
            
        self.book_ID = book_ID     
        self.book_name = book_name
        self.writer = writer
        self.publisher = publisher
        self.page_count = page_count
        self.add_book()
        self.add_book_information()
        
            
            
            
            
    def add_book(self):
            
        self.kitaplar.append(self.book_name)
        self.All_books.append(self.book_name)
            
            
            
    def add_book_information(self):
                
                self.bookInformations.update({
                self.book_ID: {
                'Book Name': self.book_name,        
                'Author': self.writer,
                'Publisher': self.publisher,
                'Page Count': self.page_count
                },
            })
                      
               
                print("The book informations saved.")

            
            
    def display_book_dict():
        
        print(backAdminPage.bookInformations)
        
        sorunbookss = input("press 'p' for previous: ")
        
        if sorunbookss == "p":
            
            GirisSayfasi.problemcozum()
            
            
        else:
            
            print("Press a valid key.")
        
                
            
    def del_book():
        
        
        for i in range(int(input("number of books to be deleted: "))):
            
            IDno = input("ID no of the book to be deleted: ")
        
            book = input("the name of the book to be deleted: ")
                    
            if book in backAdminPage.kitaplar:
                        
                backAdminPage.kitaplar.remove(book)
                
            if IDno in backAdminPage.bookInformations:
                
                backAdminPage.bookInformations.pop(IDno)
                
                
                
                print("The book deleted.")
                
            else:
                
                print("That book does not exist in Library already.")
            
            
        
        sorunbook = input("press 'p' for previous: ")
        
        if sorunbook == "p":
            
            GirisSayfasi.problemcozum()
            
            
        else:
            
            print("Press a valid key.")
            
            
        
    def all_thenameofbooks_and_bookcount_in_library():


        print("Number of all books in the library {}".format(len(backAdminPage.All_books)))
        print("All books in the library {}".format(backAdminPage.All_books))
        
        soruny = input("press 'p' for previous: ")
        
        if soruny == "p":
            
            GirisSayfasi.problemcozum()
            
            
        else:
            
            print("Press a valid key.")

                     
                
    def display_kitaplar():
                
        print(backAdminPage.kitaplar)
        
        sorun = input("press 'p' for previous: ")
        
        if sorun == "p":
            
            GirisSayfasi.problemcozum()
            
            
        else:
            
            print("Press a valid key.")
        
            
    def display_book_informations():
                
            
        print(backAdminPage.bookInformations)
        
        
        sorunn = input("press 'p' for previous: ")
        
        if sorunn == "p":
            
            GirisSayfasi.problemcozum()
            
            
        else:
            
            print("Press a valid key.")
            
            
    def display_all_books_length():
        
        print("Total number of books currently in the library: {}".format(len(backAdminPage.kitaplar)))
        
        sorunnnnn = input("press 'p' for previous: ")
        
        if sorunnnnn == "p":
                
            GirisSayfasi.problemcozum()
            
            
        else:
            
            print("Press a valid key.")
            
    def book_search_with_bookname():
        
        bookSearch = input("Book Name: ")
        
        if bookSearch in backAdminPage.kitaplar:
            
            thebookcount =  backAdminPage.kitaplar.count(bookSearch)
            
            print("Currently, there are {1} copies of the book called {0} in the library.".format(bookSearch, thebookcount))
            
             
        else:
            
            print("The book does not exist in the Library.")
            
            
        sorunnn = input("press 'p' for previous: ")
        
        if sorunnn == "p":
                
            GirisSayfasi.problemcozum()
            
            
        else:
            
            print("Press a valid key.")
            
    def book_search_with_bookIDnumber():
        
        
        bookIDsearch = input("Book ID no: ")
        
        if bookIDsearch in backAdminPage.bookInformations:
            
            bookIDsea = backAdminPage.bookInformations[bookIDsearch]
            
            print(bookIDsea)
            
            
        else:
            
             print("The book does not exist in the Library.")
            
            
            
            
            
        sorunn = input("press 'p' for previous: ")
        
        if sorunn == "p":
            
            GirisSayfasi.problemcozum()
            
            
        else:
            
                print("Press a valid key.")
            
        
            
    
    
    def add_object():
        
        
                
        elmas = True
                
        while elmas:
            
            zumrutpress = int(input("number of books to be added: "))
            
            j = 0
                
            while(j < zumrutpress):
                
                book_IDDD = input("Enter a book ID:")
                book_nameee = input("Enter a book name: ")
                writerrr = input("Enter an author name: ")
                publisherrr = input("Enter a publisher name: ")
                page_counttt = int(input("Enter an page count: "))  
                
                
                backAdminPage(book_IDDD,book_nameee,writerrr,publisherrr,page_counttt)
                j += 1
                
                
                
                
            elmaspress = input("press 'p' for previous: ")
                    
                
            if elmaspress == "p":
                        
                        
                elmas = False
                
            else:
                
                print("Press a valid key.")
                
                
                
backAdminPage("2","Sözler","Bediüzzman","Envar",920) 