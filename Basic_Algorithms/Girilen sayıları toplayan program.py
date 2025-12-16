# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 17:18:34 2024

@author: RAMAZAN
"""

i = 1
toplam = 0
while True:
    sayı = input("{}.sayıyı giriniz:".format(i))
    if sayı == "q":
        print("Program sonlandırılıyor.")
        print("Toplam:",toplam)
        break
    else:
        i+=1
        toplam=int(sayı)+toplam
    