from sklearn.tree import DecisionTreeClassifier as tree

kart_verileri = [[150, 0], [170, 0], [140, 1], [130, 1]]

durumlar = ["GÜVENLİ ", "GÜVENLİ ", "TEHLİKELİ", "TEHLİKELİ"]   
banka_ai = tree().fit(kart_verileri, durumlar)
print("Banka güvenlik simülatörü")
tutar = int(input("Kart tutarı: "))
kart_tipi = int(input("Kart tipi (0: Kredi, 1: Banka): "))
tahmin_durum = banka_ai.predict([[tutar, kart_tipi]])[0]
print(f"\nDurum Raporu: ")
print(f"{tutar} TL tutarında {kart_tipi} tipindeki kartınızın durumu: {tahmin_durum}")
