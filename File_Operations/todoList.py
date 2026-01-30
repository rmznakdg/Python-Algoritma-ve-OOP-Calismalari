print("""
To-Do List Programına Hoşgeldiniz.
1---->Görev Ekle
2---->Görevleri Listele
3---->Görev Sil
4---->Görevi Tamamla
5---->Çıkış
""")
todoList = []
tamamlananlar = []
def görevEkle():
    görev = input("Eklemek istediğiniz görev:")
    todoList.append(görev)
    print(todoList)
    return todoList
def görevleriListele():
    m = 1
    if len(todoList) == 0:
        print("Listede henüz bir görev yok. Görev eklemek için 1'e basınız")
    while m <= len(todoList):
        for i in todoList:
            print("[{}] {}".format(m, i))
            m += 1
def göreviTamamla():
    görevleriListele()
    görev = int(input("Tamamlanmış görevin numarasını giriniz:"))
    tamamlananlar.append(todoList[görev-1])
    todoList.pop(görev-1)
    for i in tamamlananlar:
        print("[*]{}".format(i))
    for i in todoList:
        print("[ ]{}".format(i))
def görevSil():
    görevleriListele()
    hangi = int(input("Silmek istediğiniz görevin numarasını giriniz:"))
    todoList.pop(hangi-1)
    return todoList

while True:
    islem = input("Yapmak istediğiniz işlemi giriniz:")
    if islem == "1":
        görevEkle()
    elif islem == "2":
        görevleriListele()
    elif islem == "3":
        görevSil()
    elif islem == "4":
        göreviTamamla()
    elif islem == "5":
        print("Program sonlandırılıyor..")
        break