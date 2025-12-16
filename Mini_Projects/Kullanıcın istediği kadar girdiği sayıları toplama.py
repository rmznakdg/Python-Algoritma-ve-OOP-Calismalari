# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 14:07:18 2024

@author: RAMAZAN
"""
i = 1
toplam = 0
while True:
    girilensayi = input("{}. sayıyı giriniz:".format(i))
    if girilensayi == 'q':
        print(toplam)
        print("Program sonlandırılıyor..")
        break
    else:  
        toplam = toplam + int(girilensayi)
        i+=1