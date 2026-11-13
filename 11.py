from sklearn.ensemble import RandomForestClassifier as fr

# hayvanlar = [[15, 10], [4,16], [25,8], [3,18]]
# turler = ["kopek", "kedi", "kopek", "kedi"]

# orman_konseyi = forest(n_estimators = 100)
# orman_konseyi.fit(hayvanlar, turler)

# tahmin = orman_konseyi.predict([[5, 15]])
# print(f"Yüzlerce ağacın oylaması sonucu bir: {tahmin[0]} tahmin edildi.")

# hava_durumu = [[25, 5], [10, 40], [30, 2], [15,30]]
# durumlar = ["Gidilir", "Iptal", "Gidilir", "Iptal"]

# piknik_ai = forest(n_estimators = 9999999999999999)
# piknik_ai.fit(hava_durumu, durumlar)

# print(f"20 derece ve 10 km/s rüzgar hızında piknik yapma kararı: {piknik_ai.predict([[20, 10]])[0]}")

# oyunlar = [[90, 100], [40, 50], [95, 800], [30, 10]]
# alinir_mi = ["Al", "Alma", "Indirim bekle", "Alma"]

# oyun_ai = forest(n_estimators = 100)
# oyun_ai.fit(oyunlar, alinir_mi)

# print(f"80 TL ve 1000 MB boyutunda bir oyun için karar: {oyun_ai.predict([[80, 1000]])[0]}")

def mantar_hayatta_kalmaa_rehberi():
    print("Mantar Hayatta Kalma Rehberi")
    mantarlar = [
        [0, 0, 0], [1, 1, 1], [0, 1, 0], [1, 0, 1],
        [0, 0, 1], [1, 1, 0], [1, 0, 0], [0, 1, 1]
    ]
    sinif = ["Yenilebilir", "ÖLÜMCÜL ZEHİRLİ", "Yenilebilir", "ÖLÜMCÜL ZEHİRLİ",
             "Zehirli (Mide Bulantısı)", "Yenilebilir", "Yenilebilir", "Zehirli (Mide Bulantısı)"]

    orman_ai = fr(n_estimators=100).fit(mantarlar, sinif)
    while True:
        renk = int(input("Mantarın rengi (0: Beyaz, 1: Kırmızı): "))
        if renk == -1: break
        sekil = int(input("Mantarın şekli (0: Yuvarlak, 1: Şişkin): "))
        koku = int(input("Mantarın kokusu (0: Yok, 1: Var): "))

        analiz = orman_ai.predict([[renk, sekil, koku]])[0]

        print(f"\n AI Analizi: Bu mantar {analiz}.\n")

        if analiz == "Yenilebilir":
            print("Bu mantarı güvenle yiyebilirsiniz.")
        elif analiz == "Zehirli (Mide Bulantısı)":
            print("Bu mantar zehirli olabilir. Tüketmeyin.")
        elif analiz == "ÖLÜMCÜL ZEHİRLİ":
            print("Dikkat! Bu mantar ölümcül derecede zehirli. Kesinlikle yemeyin!")
            