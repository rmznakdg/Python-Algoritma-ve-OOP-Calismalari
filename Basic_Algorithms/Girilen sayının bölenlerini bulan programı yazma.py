x = int(input("Bir sayı giriniz:"))
bölenler = []
for i in range(1,x):
    if x % i == 0:
        bölenler.append(i)
print(x,"sayısının bölenleri:",bölenler) 
