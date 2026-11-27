from sklearn.ensemble import RandomForestClassifier as rdc
oyuncular = [
    [25, 9, 8], [10, 4, 3], [30, 2, 2], [18, 8, 9],
    [12, 5, 4], [28, 9, 10], [8, 3, 2], [22, 7, 8],
    [24, 8, 9], [15, 7, 8], [29, 3, 4], [14, 3, 2],
    [20, 9, 8], [27, 4, 3], [11, 6, 5], [19, 8, 8],
    [32, 9, 9], [9, 2, 1], [26, 2, 3], [17, 9, 9],
    [13, 4, 4], [21, 7, 7], [23, 8, 7], [16, 5, 4]
]

kararlar = [
    "Kaptan Olur", "Olamaz", "Olamaz (Çok Sinirli)", "Kaptan Olur",
    "Olamaz", "Kaptan Olur", "Olamaz", "Kaptan Olur",
    "Kaptan Olur", "Kaptan Olur", "Olamaz (Çok Sinirli)", "Olamaz",
    "Kaptan Olur", "Olamaz (Çok Sinirli)", "Olamaz", "Kaptan Olur",
    "Kaptan Olur", "Olamaz", "Olamaz (Çok Sinirli)", "Kaptan Olur",
    "Olamaz", "Kaptan Olur", "Kaptan Olur", "Olamaz"
]

konsey_ai = rdc(n_estimators=100, random_state=42).fit(oyuncular, kararlar)

print("--- E-SPOR KAPTANLIK SEÇMELERİ ---")

while True:
    skor = int(input("\nOyuncunun maç başı ortalama skoru kaç?: "))
    iletisim = int(input("\nOyuncunun iletişim becerisi kaç?: "))
    sogukkanli = int(input("\nOyuncunun soğukkanlılığı kaç?: "))

    sonuc = konsey_ai.predict([[skor, iletisim, sogukkanli]])[0]

    print(f"\n100 Ağacın Ortak Kararı: {sonuc.upper()}")

    devam = input("\nBaşka bir oyuncu için tahmin yapmak ister misiniz? (E/H): ").strip().lower()

    if devam != "e":
        print("\nTahmin programından çıkılıyor...")
        break