from sklearn.preprocessing import PolynomialFeatures as pf
from sklearn.linear_model import LinearRegression as lr

km_verisi = [[1], [5], [10], [10], [15], [20], [25], [30], [35], [40]]
yorgunluk = [2, 5, 10, 18, 30, 45, 70, 90, 100]

poly_ko = pf(degree=3)

t_km = poly_ko.fit_transform(km_verisi)

spor_ai = lr().fit(t_km, yorgunluk)

print("Olimpiyat antranörü simülatörü")
soru_km = int(input("Koşu mesafesi (km): "))
tahmin_yorgunluk = spor_ai.predict(poly_ko.transform([[soru_km]]))[0]
if tahmin_yorgunluk > 100:
    tahmin_yorgunluk = 100

print(f"\nDurum Raporu: ")
print(f"{soru_km} km koştuğunuzda tahmini yorgunluk oranınız: %{tahmin_yorgunluk:.1f}")
