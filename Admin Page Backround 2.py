# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:13:48 2021

@author: okanr
"""

class backAdminPage2:
    
    memberList = []
    memberDict = {}

    trylist = []
        
    for i in range(1000):
            
        trylist.append(list())
   
        
    
    def __init__(self, memberID,name_surname,username,password,repassword,secquestion,age):
        
        self.memberID = memberID
        self.name_surname = name_surname
        self.username = username
        self.password = password
        self.repassword =repassword
        self.secquestion = secquestion
        self.age = age
        self.add_member_list()
        self.add_member_dict()
        
        
    def add_member_list(self):
        
        self.memberList.append(self.memberID)
        
        
    def add_member_dict(self):
        
        self.memberDict.update({
            self.memberID: {
                'name surname': self.name_surname,
                'user name' : self.username,
                'password': self.password,
                'age' : self.age,
                "Security question": self.secquestion
                
                }
            })
        
        print("The member saved.")
        
        
    def display_all_memberID_list():
        
        print(backAdminPage2.memberList)
        
        
        
        
        conson = input("press 'p' for previous: ")
        
        if conson == "p":
            
            GirisSayfasi.problemcozum()
            
            
        else:
            
                print("Press a valid key.")
                
                
                
                
    def del_member():
        
        delmember = int(input("ID no of the member to be deleted: "))
        
        if delmember in backAdminPage2.memberList:
            
            backAdminPage2.memberList.remove(delmember)
            
        if delmember in backAdminPage2.memberDict:
            
             backAdminPage2.memberDict.pop(delmember)
             
             print("The member deleted.")
    
            
        else:
            print("No such member was found.")
            
            
        sýkýntýmember = input("press 'p' for previous: ")
        
        
        
        if sýkýntýmember == "p":
            
            GirisSayfasi.problemcozum()
            
            
        else:
            
                print("Press a valid key.")
                
                
    
    
    def display_all_members_length():
        
        print("total number of registered members in the library: {}".format(len(backAdminPage2.memberList)))
        
        soruncama = input("press 'p' for previous: ")
        
        if soruncama == "p":
            
            GirisSayfasi.problemcozum()
            
            
        else:
            
            print("Press a valid key.")
                
        
    def display_all_member_dict():
        
        print(backAdminPage2.memberDict)
            
             
        sýkýntý = input("press 'p' for previous: ")
        
        
        
        if sýkýntý == "p":
            
            GirisSayfasi.problemcozum()
            
            
        else:
            
                print("Press a valid key.")
                
                sýkýntý = input("press 'p' for previous: ")
                GirisSayfasi.problemcozum()
                
                
            
    def search_member_with_IDnumber():
        
        memberIDsearch = int(input("ID no of the member to be searched:: "))
        
        if memberIDsearch in backAdminPage2.memberDict:
            
            memberIDsea = backAdminPage2.memberDict[memberIDsearch]
            
            print(memberIDsea)
            
        else:
            
            print("The member does not exist in the Library.")
            
            
        sorunnnnn = input("press 'p' for previous: ")
        
        if sorunnnnn == "p":
            
            GirisSayfasi.problemcozum()
            
            
        else:
            
                print("Press a valid key.")
                
            
    def add_member():
        
        yakut = True
                
        while yakut:
            
            yakutpress = int(input("The number of the member to be added: "))
            
            o = 0
                
            while(o < yakutpress):
                
                
                
                member_IDDD = int(input("Enter an ID: "))
                
                if member_IDDD not in backAdminPage2.memberList:
                    
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
                        
                            secquestion = input(" Your most like color: ")
                            flagggg = False
                
                        elif presss == "3":
                
                            secquestion = input(" Your most like city: ")
                            flagggg = False
                                
                
                        else:
                
                            print("Press a valid key.")
                        
                        
                else:
                    
                    print("The member exist already.")
                        
                member_age = int(input("age: "))
                
                backAdminPage2.trylist[member_IDDD].append(backAdminPage2(member_IDDD,member_nameee,user_name,password,repassword,secquestion,member_age))
                
                
                o += 1
                
                
                
                
            elmaspressss = input("press 'p' for previous: ")
                    
                
            if elmaspressss == "p":
                        
                        
                yakut = False
                
            else:
                
                print("Press a valid key.")
        


