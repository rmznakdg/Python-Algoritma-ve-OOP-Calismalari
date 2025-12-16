number1 = int(input("Bir sayı giriniz."))
işlem = input("Yapmak istediğiniz işlemin sembolünü seçiniz: (*,+,-,/)")
number2 = int(input("Bir sayı daha giriniz:"))

if işlem == "*":
    print("{} * {} = {}".format(number1,number2,number2*number1))
elif işlem == "/":
    print("{} / {} = {}".format(number1,number2,number1/number2))
elif işlem == "+":
    print("{} + {} = {}".format(number1,number2,number1+number2))
elif işlem == "-":
    print("{} - {} = {}".format(number1,number2,number1-number2))
else: print("Lütfen geçerli bir işlem giriniz!")
