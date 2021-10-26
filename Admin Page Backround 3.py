# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:15:04 2021

@author: okanr
"""

class backAdminPage3:
    
    memberFavorite = []
    memberGetAllBooks = []
    uyeninEtkinKitaplarý = []
    
    for i in range(1000):
        
        memberFavorite.append(list())
        memberGetAllBooks.append(list())
        uyeninEtkinKitaplarý.append(list())
        
        
    def add_members_favorite_book():


        a = int(input("For how many members do you want to add a favorite book?: "))
        
        j = 0
        
        while j < a:
        
            
            ID = int(input("The ID no of the member: "))
                        
            for i in range(int(input("Number of books to add: "))):
                
                if ID in backAdminPage2.memberList:
                    
                    favoritebook = input("Book Name: ")
                    
                if favoritebook not in backAdminPage3.memberFavorite[ID]:
                
                    if favoritebook in backAdminPage3.memberGetAllBooks[ID]:
                
                            backAdminPage3.memberFavorite[ID].append(favoritebook)
                
            
            j += 1
            
            
        sorunbook = input("press 'p' for previous: ")
        
        if sorunbook == "p":
                
            GirisSayfasi.problemcozum()
                
                
        else:
                
            print("Press a valid key.")
    

            
                
    def del_favorite_book():
        
        
        ID = input("Enter a ID number of the member: ")
        
        for i in range(int(input("Enter the number of books to be removed from favorites: "))):
        
            delfavoritebook = input("The Book Name: ")
            
            
            if delfavoritebook in backAdminPage3.memberFavorite[ID]:
                
                backAdminPage3.memberFavorite[ID].remove(delfavoritebook)
                            
            
                        
                print("Process is successful.")
                        
            else:
                        
                print("There is no such book among the favorite books.")
            
        
             
        sorunbook = input("press 'p' for previous: ")
        
        if sorunbook == "p":
                
            GirisSayfasi.problemcozum()
                
                
        else:
                
            print("Press a valid key.")
                
        
            
    def del_theAvailableBooksofMembers():
        
        
        ID =input("Enter the ID number of the member who wants to return the book: ")
        
        for i in range(int(input("Number of books to be returned: "))):
            
            
            getBook = input("Enter the name of the book you want to return to the library: ")
      
            if getBook in backAdminPage3.uyeninEtkinKitaplarý[ID]:
            
                backAdminPage3.uyeninEtkinKitaplarý[ID].remove(getBook)
        
                
                backAdminPage.kitaplar.append(getBook)
                print("The process is successful.")
                
            else:
                
                print("No such book has been found in active books: ")
                
            
                 
        sorunbook = input("press 'p' for previous: ")
        
        if sorunbook == "p":
                
            GirisSayfasi.problemcozum()
                
                
        else:
                
                print("Press a valid key.")
                
                
    def add_theAvailableBooksofMembers():
        
        
        b = int(input("How many members will be given books?: "))
        
        l = 0
        
        while l < b:
            
            ID =int(input("Enter the ID number of the member who wants to borrow: "))
            
            for i in range(int(input("Enter the number of books you want to borrow: "))):
                
                
                getBook = input("Enter the name of the book you want to borrow from the library: ")
          
                if getBook in backAdminPage.kitaplar:
                    
                    backAdminPage3.uyeninEtkinKitaplarý[ID].append(getBook)
                
                    backAdminPage3.memberGetAllBooks[ID].append(getBook)
                        
        
                    backAdminPage.kitaplar.remove(getBook)
                    
                    print("Process is successful.")
                
                else:
                    
                    print("There is no such book in the library.")
            
            l += 1
                
                
                
        sorunbook = input("press 'p' for previous: ")
        
        if sorunbook == "p":
                
            GirisSayfasi.problemcozum()
                
                
        else:
                
            print("Press a valid key.")
                
    
        
        
                
    def display_get_member_all_book():
        
        Idnosu = int(input("Enter the user's ID number to view all the books purchased by the member: "))
        
        print("All books bought by user ID number {}: {}".format(Idnosu,backAdminPage3.memberGetAllBooks[Idnosu]))
        
             
        sorunbook = input("press 'p' for previous: ")
        
        if sorunbook == "p":
                
            GirisSayfasi.problemcozum()
                
                
        else:
                
            print("Press a valid key.")
        
        
    def display_favoritebook():
        
        ID = int(input("Enter the member's ID: "))

        print("Favorite books of member ID number {}: {} ".format(ID,backAdminPage3.memberFavorite[ID])) 
        
             
        sorunbook = input("press 'p' for previous: ")
        
        if sorunbook == "p":
                
            GirisSayfasi.problemcozum()
                
                
        else:
                
            print("Press a valid key.")
        
    def display_availableBooks():
        
        ID = int(input("Enter the member's ID: "))

        print("Active books of member ID number {}: {} ".format(ID,backAdminPage3.uyeninEtkinKitaplarý[ID])) 
         
             
        sorunbook = input("press 'p' for previous: ")
        
        if sorunbook == "p":
                
            GirisSayfasi.problemcozum()
                
                
        else:
                
            print("Press a valid key.")