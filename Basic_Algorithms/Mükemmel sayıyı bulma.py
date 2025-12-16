def mukemmel_sayi_mi(sayi):
    toplam = 0
    for i in range(1, sayi // 2 + 1):  # Bir sayının bölenleri en fazla sayının yarısına kadar gider
        if sayi % i == 0:
            toplam += i
    return toplam == sayi

print("1 ile 1000 arasındaki mükemmel sayılar:")
for i in range(1, 1000):
    if mukemmel_sayi_mi(i):
        print(i)