# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:17:58 2021

@author: okanr
"""

class MemberPage:

    
    def __init__(self,ID):
        
        self.ID = ID
    
    
    def add_members_favorite_bookk(self):
                        
        for i in range(int(input("Number of books to add: "))):
                
                if self.ID in backAdminPage2.memberList:
                    
                    favoritebook = input("Book Name: ")
                    
                if favoritebook not in backAdminPage3.memberFavorite[self.ID]:
                
                    if favoritebook in backAdminPage3.memberGetAllBooks[self.ID]:
                
                            backAdminPage3.memberFavorite[self.ID].append(favoritebook)
                
            
            
            
        sorunbook = input("press 'p' for previous: ")
        
        if sorunbook == "p":
                
            GirisSayfasi.problemcozum2()
                
                
        else:
                
            print("Press a valid key.")
    

            
                
    def del_favorite_bookk(self):
        
        
        for i in range(int(input("Enter the number of books you want to remove from favourites: "))):
        
            delfavoritebook = input("Book Name: ")
            
            
            if delfavoritebook in backAdminPage3.memberFavorite[self.ID]:
                
                backAdminPage3.memberFavorite[self.ID].remove(delfavoritebook)
                            
            
                        
                print("Successful.")
                        
            else:
                        
                print("There is no such book among your favorite books.")
            
        
             
        sorunbook = input("press 'p' for previous: ")
        
        if sorunbook == "p":
                
            GirisSayfasi.problemcozum2()
                
                
        else:
                
            print("Press a valid key.")
                
        
            
    def del_theAvailableBooksofMemberss(self):
        
        
        for i in range(int(input("Enter the number of books you want to return: "))):
            
            
            getBook = input("Book Name: ")
      
            if getBook in backAdminPage3.uyeninEtkinKitaplarý[self.ID]:
            
                backAdminPage3.uyeninEtkinKitaplarý[self.ID].remove(getBook)
        
                
                backAdminPage.kitaplar.append(getBook)
                print("Successful.")
                
            else:
                
                print("No such book was found in your active books.")
                
            
                 
        sorunbook = input("press 'p' for previous: ")
        
        if sorunbook == "p":
                
            GirisSayfasi.problemcozum2()
                
                
        else:
                
                print("Press a valid key.")
                
                
    def add_theAvailableBooksofMembers(self):
        
            
            
        for i in range(int(input("Enter the number of books you want to borrow: "))):
                
                getBook = input("Enter the name of the book you want to borrow from the library: ")
          
                if getBook in backAdminPage.kitaplar:
                    
                    backAdminPage3.uyeninEtkinKitaplarý[self.ID].append(getBook)
                
                    backAdminPage3.memberGetAllBooks[self.ID].append(getBook)
                        
        
                    backAdminPage.kitaplar.remove(getBook)
                    
                    print("Successful.")
                
                else:
                    
                    print("There is no such book in the library.")
            
                
                
        sorunbook = input("press 'p' for previous: ")
        
        if sorunbook == "p":
                
            GirisSayfasi.problemcozum2()
                
                
        else:
                
            print("Press a valid key.")
                
    
        
        
                
    def display_get_member_all_bookk(self):
                
        print("All the books you got: {}".format(backAdminPage3.memberGetAllBooks[self.ID]))
        
             
        sorunbook = input("press 'p' for previous: ")
        
        if sorunbook == "p":
                
            GirisSayfasi.problemcozum2()
                
                
        else:
                
            print("Press a valid key.")
        
        
    def display_favoritebookk(self):

        print("Your favorite books: {} ".format(backAdminPage3.memberFavorite[self.ID])) 
        
             
        sorunbook = input("press 'p' for previous: ")
        
        if sorunbook == "p":
                
            GirisSayfasi.problemcozum2()
                
                
        else:
                
            print("Press a valid key.")
        
    def display_availableBookss(self):
        

        print("Your current books: {} ".format(backAdminPage3.uyeninEtkinKitaplarý[self.ID])) 
         
             
        sorunbook = input("press 'p' for previous: ")
        
        if sorunbook == "p":
                
            GirisSayfasi.problemcozum2()
                
                
        else:
                
            print("Press a valid key.")
            
            
            
            
    def book_search_with_booknamee():
        
        bookSearch = input("Book Name: ")
        
        if bookSearch in backAdminPage.kitaplar:
            
            thebookcount =  backAdminPage.kitaplar.count(bookSearch)
            
            print("Currently, there are {1} copies of the book called {0} in the library.".format(bookSearch, thebookcount))
            
             
        else:
            
            print("The book does not exist in the Library.")
            
            
        sorunnnn = input("press 'p' for previous: ")
        
        if sorunnnn == "p":
                
            GirisSayfasi.problemcozum2()
            
            
        else:
            
            print("Press a valid key.")