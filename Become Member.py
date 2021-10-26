# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:16:59 2021

@author: okanr
"""

class UyeOl:
    
    def become_member():
            
            yakut = True
                    
            while yakut:
                
                
                    member_IDDD = int(input("Enter an ID: "))
                    member_nameee = input("Enter your name and surname: ")
                    user_name = input("Enter your user name: ")
                    
                    password = input("Enter your password: ")
                    
                    repassword = input("Enter repassword: ")
                    
                    bayrak = True
                
                    while bayrak:
                
                        if password == repassword:
                    
                            print("Your password has been made.")
                    
                            bayrak = False
                    
                        elif password != repassword:
                        
                            bayrak2 = True
                        
                            while bayrak2:
                    
                                repassword = input("Passwords are not same. Please try again: ")
                            
                                if password == repassword:
                                
                                
                                    bayrak2 = False
                                
                                
                                
                                elif password != repassword:
                                
                                
                                    bayrak = True
                                    bayrak2 = False
                                    
                                    
                    flagggg = True
        
                    while flagggg:
                    
                        print("Choose a security question...")
                    
                        print("press to '1' for your most like animals.")
                        print("press to '2' for your most like colors.")
                        print("press to '3' for your most like cities.")
                    
                        presss = input("")
                        
            
                        if presss == "1":
                
                            secquestion = input("Your most like animal: ")
                            flagggg = False
                        
                        elif presss == "2":
                        
                            secquestion = input("Your most like color: ")
                            flagggg = False
                
                        elif presss == "3":
                
                            secquestion = input("Your most like city:: ")
                            flagggg = False
                                
                
                        else:
                
                            print("Press a valid key.")
                            
                            
                            
                            
                    member_age = int(input("age: "))
                    
                    backAdminPage2.trylist[member_IDDD].append(backAdminPage2(member_IDDD,member_nameee,user_name,password,repassword,secquestion,member_age))
                    print('Registration Successful.')
                    yakut = False