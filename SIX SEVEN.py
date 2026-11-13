
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor

ipuclari = [[150,0], [170,0], [140,1], [130,1]]
meyveler = ["Portakal","Portakal","Elma","Elma"]

dedektif = DecisionTreeClassifier().fit(ipuclari, meyveler)
tahmin = dedektif.predict([[160,0]])
print(f"Tahmin edilen meyve: {tahmin[0]}")

hayvan_ozellikleri = [[4, 1], [2, 0], [3, 1], [1, 0], [1, 1] ]
hayvan_turleri = ["Köpek", "Kedi", "Köpek", "Kedi", "Kedi"]

hayvan_dedektif = DecisionTreeClassifier().fit(hayvan_ozellikleri, hayvan_turleri)
tahmin_hayvan = hayvan_dedektif.predict([[3, 1]])
print(f"Tahmin edilen hayvan: {tahmin_hayvan[0]}") 

from sklearn.tree import DecisionTreeRegressor

ogrenciler = [[9, 5, 4], [2, 9, 3], [4, 4, 9], [8, 3, 7], [3, 8, 2], [6, 6, 8], [9, 8, 2], [5, 5, 9]]
    # y: Binalar
binalar = ["Gryffindor", "Ravenclaw", "Slytherin", "Gryffindor","Ravenclaw", "Slytherin", "Gryffindor", "Slytherin"]

sapka = DecisionTreeClassifier().fit(ogrenciler, binalar)
while True:
    print("Öğrencinin özelliklerini girin (1-10 arası değerler):")
    cesaret = int(input("Cesaret: "))
    zeka = int(input("Zeka: "))
    sadakat = int(input("Sadakat: "))
    tahmin_bina = sapka.predict([[cesaret, zeka, sadakat]])
    print(f"Öğrenci {tahmin_bina[0]} binasına yerleştirildi.")
    devam = input("Başka bir öğrenci için tahmin yapmak ister misiniz? (E/H): ")
    if devam.lower() != 'e':
        print("Programdan çıkılıyor.")
        