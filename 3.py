from sklearn.linear_model import LinearRegression



izlenmeler = [[1000],[5000], [10000],[50000]]



gelirler = [10, 50, 100, 500]

youtube_gelir_modeli = LinearRegression()
youtube_gelir_modeli.fit(izlenmeler, gelirler)


tahmin = youtube_gelir_modeli.predict([[25000]])
print("25.000 izleme geliri Tahmini: ", tahmin[0], "TL")



oyun_saatleri =[[10], [20], [30], [50]]

seviyeler =[5,10,15,25]

oyun_modeli = LinearRegression()
oyun_modeli.fit(oyun_saatleri, seviyeler)

soru = int(input("Oyun içinde günlük kaç saat vakit geçirmektesiniz? "))

tahmin = oyun_modeli.predict([[soru]])

print(soru," saat oynadığında tahmini ulaşacağın seviye:", tahmin[0], "level!")


antreamanlar = [[2], [4], [6], [8]]

sayilar = [10, 20, 30, 40]

basket_modeli = LinearRegression()
basket_modeli.fit(antreamanlar, sayilar)

soru = int(input("Haftada kaç saat antrenman yapıyorsunuz? : "))
tahmin = basket_modeli.predict([[soru]])
print("Harika! Bu pazarki maçta tahmini ", tahmin[0], "sayı atacaksın!")



videolar = [[5], [10], [20], [40]]

takipciler = [100, 200, 400, 800]

medya_modeli = LinearRegression()
medya_modeli.fit(videolar, takipciler)

soru = int(input("Kanalınızda kaç video paylaşmayı düşünüyorsunuz? "))

tahmin = medya_modeli.predict([[soru]])
print("Bu videolar ile tahmini ", int(tahmin[0]), "takipçiye ulaşabilirsiniz!")

sicakliklar = [[20], [25], [30], [35], [40]]

bardak = [40, 50, 60, 70, 80]

limonata = LinearRegression()
limonata.fit(sicakliklar, bardak)
soru = int(input("Hava sıcaklığı kaç derece tahmin ediyorsunuz? "))
tahmin = limonata.predict([[soru]])
print("Tahmini ", int(tahmin[0]), " bardak limonata hazırlayabilirsiniz!")
