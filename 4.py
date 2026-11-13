from sklearn.linear_model import LinearRegression


veriler = [[2,5], [4,6], [5,8], [8,8]]


notlar = [40, 65, 80, 95]

model = LinearRegression()
model.fit(veriler, notlar)

tahmin = model.predict([[3,7]])
print("Sınav tahmini: ", tahmin[0])



oyuncu_bilgisi = [[10, 50], [20, 40], [30, 20], [40, 10]]

hiz = [5, 12, 15, 35]

model = LinearRegression()
model.fit(oyuncu_bilgisi, hiz)

tahmin = model.predict([[25, 30]])

print("Karakter hızı: ", tahmin[0])



veri= [[50,40], [70,60], [90, 80], [30, 90]]

kazanma = [45, 65, 95, 40]

savas_modeli = LinearRegression()
savas_modeli.fit(veri, kazanma)

print("AI SAVAŞ ÖNGÖRÜ 3.0")
print("Çıkmak için güç değerine 0 girin")

while True:
    guc = int(input("Güç değerini giriniz: "))
    if guc == 0:
        print("Çıkış yapılıyor...")
        break
    else:
        tahmin = savas_modeli.predict([[guc, 50]])
        print("Tahmini kazanma yüzdesi: ", tahmin[0], "%")

    while True:
        hiz = int(input("Hız değerini giriniz: "))

        if hiz < 1 or hiz > 100:
            print("Hız değeri 1 ile 100 arasında olmalıdır. Lütfen tekrar deneyin.")
        else:
            break
    tahmin = savas_modeli.predict([[guc, hiz]])
    sans = int(tahmin[0])
    print("Tahmini kazanma yüzdesi: ", sans, "%")

    if sans >= 80:
        print("Tebrikler! Yüksek bir kazanma şansınız var!")
    elif sans >= 50:
        print("Orta seviyede bir kazanma şansınız var. Dikkatli olun!")
    else:
        print("Düşük bir kazanma şansınız var. Stratejinizi gözden geçirin!")


