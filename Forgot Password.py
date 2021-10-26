# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:16:23 2021

@author: okanr
"""

class SifremiUnuttum:
    
    
    def sifremiGoster():
    
        takenID = int(input("ID: "))
        takenSecquestion = input("The answer of the security question: ")
        
        listecik8 = [i.memberID for i in backAdminPage2.trylist[takenID] if i.memberID == takenID]
        listecik9 = [i.secquestion for i in backAdminPage2.trylist[takenID] if i.secquestion == takenSecquestion]
        listecik7 = [i.password for i in backAdminPage2.trylist[takenID]]
        
        if listecik8[0] == takenID and listecik9[0] == takenSecquestion:
            
            print("Your Password: {}".format(listecik7[0]))
            