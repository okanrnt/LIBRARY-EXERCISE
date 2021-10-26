# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:15:46 2021

@author: okanr
"""

class GirisSayfasi:
    
    
    
    def yonlendirmeMet():
        
        
            adminID = 1
            adminUser = "admin"
            adminPassword = "1234"
            
            print("Login Page...")
            
           
            
            takenID = int(input("ID: "))
            takenUser = input("User: ")
            takenPassword = input("Password: ")
            
            listecik = [i.memberID for i in backAdminPage2.trylist[takenID] if i.memberID == takenID]
            listecik2 = [i.username for i in backAdminPage2.trylist[takenID] if i.username == takenUser]
            listecik3 = [i.password for i in backAdminPage2.trylist[takenID] if i.password == takenPassword]
            listecik4 = [i.name_surname for i in backAdminPage2.trylist[takenID]]
            
            if adminID == takenID and adminUser == takenUser and adminPassword == takenPassword:
                
                bilirim = True
        
                while bilirim:
                    
                    
                
                    print("Redirecting to admin page...")
                    print("*****Admin Page*****")
                    print("----------------------------")
                    
                    
                    print("1: Add book")
                    print("2: View book information")
                    print("3: Display only currently available books")
                    print("4: Search book by name: ")
                    print("5: Search the book by ID number: ")
                    print("6: Add member: ")
                    print("7: View member information")
                    print("8: Display member ID only")
                    print("9: Search member by ID: ")
                    print("10: Display total number of members")
                    print("11: Display the number of books currently in the library")
                    print("12: Delete book")
                    print("13: Delete member")
                    print("14: Lend a book to a member")
                    print("15: Retrieve loaned book from member")
                    print("16: Add favorite book from the books borrowed so far if the member wants")
                    print("17: Member's request delete favorite book")
                    print("18: View all the books the member has got so far")
                    print("19: View member's favorite books by ID no")
                    print("20: View member's active books")
                    print("21: Show the number and names of all the books in the library")
                    
                    print("press 'q' for logout.")
                    
                    okanýnpressi = input("Select the action you want to do: ")
                    
                    if okanýnpressi == "1":
                    
                        backAdminPage.add_object()
                        
                    elif okanýnpressi == "2":
                        
                        backAdminPage.display_book_dict()
                        
                    elif okanýnpressi == "3":
                        
                        backAdminPage.display_kitaplar()
                        
                    elif okanýnpressi == "4":
                        
                        backAdminPage.book_search_with_bookname()
                        
                    elif okanýnpressi == "5":
                        
                        backAdminPage.book_search_with_bookIDnumber()
                        
                    elif okanýnpressi == "6":
                        
                        backAdminPage2.add_member()
                        
                    
                    elif okanýnpressi == "7":
                        
                        backAdminPage2.display_all_member_dict()
                        
                    
                    elif okanýnpressi == "8":
                        
                        backAdminPage2.display_all_memberID_list()
                        
                    
                    elif okanýnpressi == "9":
                        
                        backAdminPage2.search_member_with_IDnumber()
                        
                    elif okanýnpressi == "10":
                        
                        backAdminPage2.display_all_members_length()
                        
                    elif okanýnpressi == "11":
                        
                        backAdminPage.display_all_books_length()
                        
                    elif okanýnpressi == "12":
                        
                        backAdminPage.del_book()
                    
                    elif okanýnpressi == "13":
                        
                        backAdminPage2.del_member()
                        
                    elif okanýnpressi == "14":
                        
                        backAdminPage3.add_theAvailableBooksofMembers()
                        
                    elif okanýnpressi == "15":
                        
                        backAdminPage3.del_theAvailableBooksofMembers()
                        
                    elif okanýnpressi == "16":
                        
                        backAdminPage3.add_members_favorite_book()
                        
                    elif okanýnpressi == "17":
                        
                        backAdminPage3.del_favorite_book()
                        
                    elif okanýnpressi == "18":
                        
                        backAdminPage3.display_get_member_all_book()
                        
                    elif okanýnpressi == "19":
                        
                        backAdminPage3.display_favoritebook()
                        
                    elif okanýnpressi == "20":
                        
                        backAdminPage3.display_availableBooks()
                        
                    elif okanýnpressi == "21":
                        
                        backAdminPage.all_thenameofbooks_and_bookcount_in_library()
                        
                        
                        
                        
                        
                    elif okanýnpressi == "q":
                        
                        print("Logout is doing....")
                        print("Logout is successful.")
                        
                        bilirim = False
                        
                    else:
                        
                        print("Press a valid key.")
           
            
            
            
            
            elif listecik[0] == takenID and listecik2[0] == takenUser and listecik3[0] == takenPassword:
                
                den = True
                while den:
                
                    print("Redirecting to member page...")
                    print("-------------------------------------")
                    
                    print("*****Member Page*****")
                    print("Welcome")
                    print("-------------------------------------")
                    print("1: Get book from library")
                    print("2: Return the book to the library")
                    print("3: View the books I've borrowed so far")
                    print("4: View my active books")
                    print("5: Add favorite book")
                    print("6: Delete favorite book")
                    print("7: View My Favorite Books")
                    print("8: Searching for a book in the library")
                    print("9: press 'q' for logout.")
                    
                    
                    memberpress = input("Select the action you want to do: ")
                    
                    if memberpress == "1":
                        
                        MemberPage(int(input('Your ID No: '))).add_theAvailableBooksofMembers()
                        
                    elif memberpress == "2":
                        
                        MemberPage(int(input('Your ID No: '))).del_theAvailableBooksofMemberss()
                        
                    elif memberpress == "3":
                        
                        MemberPage(int(input('Your ID No: '))).display_get_member_all_bookk()
                        
                    elif memberpress == "4":
                        
                        MemberPage(int(input('Your ID No: '))).display_availableBookss()
                        
                    elif memberpress == "5":
                        
                        MemberPage(int(input('Your ID No: '))).add_members_favorite_bookk()
                        
                    elif memberpress == "6":
                        
                        MemberPage(int(input('Your ID No: '))).del_favorite_bookk()
                        
                    elif memberpress == "7":
                        
                        MemberPage(int(input('Your ID No: '))).display_favoritebookk()
                        
                    elif memberpress == "8":
                        
                        MemberPage.book_search_with_booknamee()
                        
                    elif memberpress == "q":
                        
                        print("Logout is successful.")
                        den = False
                        
                    else:
                        
                        print("Press a valid key.")
                    
                
                
                
                
                
            elif listecik[0] != takenID or listecik2[0] != takenUser or listecik3[0] != takenPassword:
                
                print("Please check and re-enter the information.")
                    
            else:
                
                print("Please check your information and try logging in again.")
                

    def problemcozum():
        
        bilirim = True
        
        while bilirim:
            
                    bilirim = False
                

                    print("*****Admin Page*****")
                    print("----------------------------")
                    
                    print("1: Add book")
                    print("2: View book info")
                    print("3: View currently available books in the library")
                    print("4: Search book by name: ")
                    print("5: Search the book by ID number: ")
                    print("6: Add member: ")
                    print("7: View member info")
                    print("8: Display member ID only")
                    print("9: Search member by ID: ")
                    print("10: Display total number of members")
                    print("11: Display the current number of books in the library")
                    print("12: Delete book")
                    print("13: Delete member")
                    print("14: Lend a book to a member")
                    print("15: Receive the loaned book from member")
                    print("16: Add favorite book from the books borrowed so far if the member wants")
                    print("17: Member's request delete favorite book")
                    print("18: View all the books the member has borrowed so far")
                    print("19: View member's favorite books by ID no")
                    print("20: View member's active books")
                    print("21: Show the number and names of all the books in the library")
                    
                    
                    
                    print("press 'q' for logout.")
                    
                    okanýnpressi = input("Select the action you want to do: ")
                    
                    
                    
                    
                    if okanýnpressi == "1":
                    
                        backAdminPage.add_object()
                        
                    elif okanýnpressi == "2":
                        
                        backAdminPage.display_book_dict()
                        
                    elif okanýnpressi == "3":
                        
                        backAdminPage.display_kitaplar()
                        
                    elif okanýnpressi == "4":
                        
                        backAdminPage.book_search_with_bookname()
                        
                    elif okanýnpressi == "5":
                        
                        backAdminPage.book_search_with_bookIDnumber()
                        
                    elif okanýnpressi == "6":
                        
                        backAdminPage2.add_member()
                        
                    
                    elif okanýnpressi == "7":
                        
                        backAdminPage2.display_all_member_dict()
                        
                    
                    elif okanýnpressi == "8":
                        
                        backAdminPage2.display_all_memberID_list()
                        
                    
                    elif okanýnpressi == "9":
                        
                        backAdminPage2.search_member_with_IDnumber()
                        
                    elif okanýnpressi == "10":
                        
                        backAdminPage2.display_all_members_length()
                        
                    elif okanýnpressi == "11":
                        
                        backAdminPage.display_all_books_length()
                        
                    elif okanýnpressi == "12":
                        
                        backAdminPage.del_book()
                        
                    elif okanýnpressi == "13":
                        
                        backAdminPage2.del_member()
                        
                    elif okanýnpressi == "14":
                        
                        backAdminPage3.add_theAvailableBooksofMembers()
                        
                    elif okanýnpressi == "15":
                        
                        backAdminPage3.del_theAvailableBooksofMembers()
                        
                    elif okanýnpressi == "16":
                        
                        backAdminPage3.add_members_favorite_book()
                        
                    elif okanýnpressi == "17":
                        
                        backAdminPage3.del_favorite_book()
                        
                    elif okanýnpressi == "18":
                        
                        backAdminPage3.display_get_member_all_book()
                        
                    elif okanýnpressi == "19":
                        
                        backAdminPage3.display_favoritebook()
                        
                    elif okanýnpressi == "20":
                        
                        backAdminPage3.display_availableBooks()
                        
                    elif okanýnpressi == "21":
                        
                        backAdminPage.all_thenameofbooks_and_bookcount_in_library()
                        
                        
                    elif okanýnpressi == "q":
                        
                      
                        print("Logout is successful.")
                        bilirim = False
                          
                        
                    else:
                        
                        print("Press a valid key.")
                        
                        
                        

    def problemcozum2():
        
        
        den = True
        while den:
                
                    print("*****Member Page*****")
                    print("-------------------------------------")
                    
                    print("1: Get book from library")
                    print("2: Return the book to the library")
                    print("3: View the books I've borrowed so far")
                    print("4: View my active books")
                    print("5: Add favorite book")
                    print("6: Delete favorite book")
                    print("7: View My Favorite Books")
                    print("8: Searching for a book in the library")
                    print("9: press 'q' for logout.")
                    
                    
                    memberpress = input("Select the action you want to do: ")
                    
                    if memberpress == "1":
                        
                        MemberPage(int(input('Your ID No: '))).add_theAvailableBooksofMembers()
                        
                    elif memberpress == "2":
                        
                        MemberPage(int(input('Your ID No: '))).del_theAvailableBooksofMemberss()
                        
                    elif memberpress == "3":
                        
                        MemberPage(int(input('Your ID No: '))).display_get_member_all_bookk()
                        
                    elif memberpress == "4":
                        
                        MemberPage(int(input('Your ID No: '))).display_availableBookss()
                        
                    elif memberpress == "5":
                        
                        MemberPage(int(input('Your ID No: '))).add_members_favorite_bookk()
                        
                    elif memberpress == "6":
                        
                        MemberPage(int(input('Your ID No: '))).del_favorite_bookk()
                        
                    elif memberpress == "7":
                        
                        MemberPage(int(input('Your ID No: '))).display_favoritebookk()
                        
                    elif memberpress == "8":
                        
                        MemberPage.book_search_with_booknamee()
                        
                    elif memberpress == "q":
                        
                        print("Logout is successful.")
                        den = False
                        
                    else:
                        
                        print("Press a valid key.")


