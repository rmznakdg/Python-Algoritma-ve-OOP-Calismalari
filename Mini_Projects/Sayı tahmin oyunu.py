{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7cf65389-11e2-47f2-9098-89c78c8e6539",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Sayı tahmininizi giriniz: 50\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Daha büyük bir ssayı tahmin ediniz:\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Sayı tahmininizi giriniz: 75\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Daha büyük bir ssayı tahmin ediniz:\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Sayı tahmininizi giriniz: 88\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Daha küçük bir ssayı tahmin ediniz:\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Sayı tahmininizi giriniz: 81\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Daha büyük bir ssayı tahmin ediniz:\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Sayı tahmininizi giriniz: 84\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tebrikler\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "import time\n",
    "tahminHakkı = 5\n",
    "rastgeleSayi = random.randint(1,100)\n",
    "while True:\n",
    "    sayi = int(input(\"Sayı tahmininizi giriniz:\"))\n",
    "    if sayi > rastgeleSayi:\n",
    "        print(\"Daha küçük bir ssayı tahmin ediniz:\")\n",
    "        tahminHakkı -=1\n",
    "    elif rastgeleSayi > sayi:\n",
    "        print(\"Daha büyük bir ssayı tahmin ediniz:\")\n",
    "        tahminHakkı -=1\n",
    "    else:\n",
    "        print(\"Tebrikler\")\n",
    "        break\n",
    "    if tahminHakkı==0:\n",
    "        print(\"Kaybettiniz:\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74b35c84-721f-471e-9e65-cf405acee655",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
