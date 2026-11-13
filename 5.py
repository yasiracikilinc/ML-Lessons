from sklearn.linear_model import LinearRegression

# adimlar = [[2000], [4000], [6000], [10000]]
# su_miktari = [500, 1000, 1500, 2500]

# model = LinearRegression()
# model.fit(adimlar, su_miktari)

# bugun_atilan_adim = int(input("Bugün kaç adım attınız? "))
# tahmin = model.predict([[bugun_atilan_adim]])

# print(f"Vücudunuzun tahmini su ihtiyacı: {tahmin[0]:.0f} ml")

# if tahmin[0] < 1000:
#     print("Yetersiz su ihtiyacı tahmin edildi. Daha fazla su içmelisiniz!")
# elif tahmin[0] < 2000:
#     print("Biraz daha fazla su içmelisiniz. Gün içinde su içmeyi ihmal etmeyin!")
# else:
#     print("Harika gidiyorsunuz! Gün boyunca su içmeyi ihmal etmeyin ve sağlığınızı destekleyin.")

# isim = input("Adınızı girin: ")
# seviye = input("Kaçınçı seviyedesin?")
# print(isim, "hoş geldin! Senin seviyen:", seviye)



# print(f"Merhaba {isim}, hoş geldin! Senin seviye katın: {seviye}.")

# altin = int(input("altin miktarın: "))
# iksir_fiyat = int(input("iksir fiyatı: "))

# print(f"Iksir satın aldın! Altın miktarın: {altin - iksir_fiyat}, İksir fiyatı: {iksir_fiyat}.")

# hasar_carpani = 2.325432
# can_orani = 54.324049


# print(f"Can oranı: {can_orani:.0f}")
# print(f"Hasar çarpanı: {hasar_carpani:.2f}")




from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# zamanlar = [[1], [2], [3], [4], [5]]

# yükseklikler = [10,15,15,10,0]

# cevirmen = PolynomialFeatures(degree=2)
# esnek_zamanlar = cevirmen.fit_transform(zamanlar)

# top_model = LinearRegression().fit(esnek_zamanlar, yükseklikler)
# tahmin_zamani = cevirmen.transform([[6]])
# tahmin_yukseklik = top_model.predict(tahmin_zamani)
# print(f"6. saniyedeki yükseklik: {tahmin_yukseklik[0]:.0f}")
# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures


# hiz = [[30], [50], [80], [100],]

# mesafe = [5, 15, 45, 80]

# cevirmen = PolynomialFeatures(degree=2)
# t_hiz = cevirmen.fit_transform(hiz)
# model = LinearRegression().fit(t_hiz, mesafe)

# while True:
#     bugun_hiz = int(input("Bugün kaç km/s hızla gittiniz? (Çıkmak için -1 girin): "))
#     if bugun_hiz == -1:
#         print("Programdan çıkılıyor.")
#         break
#     tahmin_mesafe = model.predict(cevirmen.transform([[bugun_hiz]]))
#     print(f"Bu hızla tahmini mesafe: {tahmin_mesafe[0]:.2f} km")



saat = [[1], [2], [3], [4],]
bakteri = [2, 4, 16, 256]
cevirmen = PolynomialFeatures(degree=3)
c_saat = cevirmen.fit_transform(saat)
model = LinearRegression().fit(c_saat, bakteri)

print("---BAKLTERI COGALMA SIMULATOR---")

while True:
    istenen = int(input("Kaç saat sonra bakteri sayısını öğrenmek istiyorsunuz? (Çıkmak için -1 girin): "))
    if istenen == -1:
        print("Programdan çıkılıyor.")
        break
    elif istenen < 0:
        print("Lütfen pozitif bir sayı girin.")
        continue
    else:
        tahmin_bakteri = model.predict(cevirmen.transform([[istenen]]))
        print(f"{istenen} saat sonra tahmini bakteri sayısı: {tahmin_bakteri[0]:.0f}")
        break
