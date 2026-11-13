from sklearn.neighbors import KNeighborsClassifier as kn

meyveler = [[9,9], [8,10], [2,1], [3,2]]

turler = ["Karpuz", "Karpuz", "Ceviz", "Ceviz"]

bil_bakalim_ai = kn(n_neighbors = 3)
bil_bakalim_ai.fit(meyveler, turler)

yeni_yiyecek = [[8,8]]
tahmin = bil_bakalim_ai.predict(yeni_yiyecek)[0]
print(f"Yiyecek türü: {tahmin}")


filmler = [[100, 2], [80, 5], [2, 50], [5, 40]]

kategoriler = ["Aksiyon", "Aksiyon", "Komedi", "Komedi"]

film_ai = kn(n_neighbors = 3).fit(filmler, kategoriler)

print(f"Film kategorisi: {film_ai.predict([[90, 3]])[0]}")


ogrenciler = [[90, 30], [85, 40], [40, 95], [30, 90]]
kulupler = ["Bilim Kulübü", "Bilim Kulübü", "Sanat Kulübü", "Sanat Kulübü"]

kulup_ai = kn(n_neighbors = 3).fit(ogrenciler, kulupler)
mat = int(input("Matematik notunu girin: "))
resim = int(input("Resim notunu girin: "))

yeni_ogrenci = [[mat,resim]]
tahmin = kulup_ai.predict(yeni_ogrenci)[0]

print(f"Öğrencinin katılacağı kulüp: {tahmin}")


def yildiz_gozlemevi():
    print("Yıldız Gözlemevi'ne hoş geldiniz!")

    yildizlar = [[90, 10], [95, 15], [85, 12], [10, 500], [5, 600], [8, 550],[50, 100], [55, 90], [45, 110]]
    
    turler = ["Süpernova", "Süpernova", "Süpernova", "Kızıl Cüce", "Kızıl Cüce", "Kızıl Cüce", "Mavi Dev", "Mavi Dev", "Mavi Dev"]

    uzay_ai = kn(n_neighbors = 3).fit(yildizlar, turler)

    while True:
        parlaklik = int(input("\nYıldızın parlaklığını girin (1-100)(cikmak icin 0): "))
        if parlaklik == 0:
            print("Yıldız Gözlemevi'nden çıkılıyor...")
            break
        elif parlaklik > 1 and parlaklik < 100:
                pass
        uzaklik = int(input("\nDunya'ya olan uzaklığı kac isik yilidir: "))
        yeni_yildiz = [[parlaklik, uzaklik]]
        kesif = uzay_ai.predict(yeni_yildiz)[0]

        print(f"\nYıldızın türü: {kesif.upper()}")
        if kesif == "Süpernova":
            print("Bu yıldız çok parlak ve kısa ömürlüdür. Patlamaya hazır olabilir!")
        elif kesif == "Kızıl Cüce":
           print("Bu yıldız uzun ömürlüdür ve genellikle düşük parlaklığa sahiptir.")
           pass

def akilli_depo_robotu():
    print("Akıllı Depo Robotu'na hoş geldiniz!")
    kutular = [[0.5, 20], [1.2, 30], [0.8, 15], [3.0, 50], [2.5, 45], [4.0, 60], [25.0, 150], [40.0, 200], [30.0, 180] ]
    bolumler = ["Kırtasiye ve Kitap", "Kırtasiye ve Kitap", "Kırtasiye ve Kitap","Teknoloji (Elektronik)", "Teknoloji (Elektronik)", "Teknoloji (Elektronik)", "Mobilya (Ağır Yük)", "Mobilya (Ağır Yük)", "Mobilya (Ağır Yük)"]
    depo_ai = kn(n_neighbors = 5).fit(kutular, bolumler)