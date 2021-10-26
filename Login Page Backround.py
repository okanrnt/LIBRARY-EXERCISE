# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:18:37 2021

@author: okanr
"""

class Library:
    
    
    print("Select the action you want to do.")
    print("'1:' Login, '2': I want to become a member, '3:' Forgot Password, 'q': Sign out'")
    
    userpressing = input("Choose: ")
    
    
    if userpressing == "1":
        
        GirisSayfasi.yonlendirmeMet()
        
       
    elif userpressing == "2":
        
        UyeOl.become_member()
        
    elif userpressing == "3":
        
        SifremiUnuttum.sifremiGoster()
        
    elif userpressing == "q":
        
        print("Logout doing...")
        print("Logout is successful.")
        
    else:
        
        print("Press a valid key.")