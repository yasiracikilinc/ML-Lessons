
from sklearn.linear_model import LogisticRegression

hastalar = [[25, 120, 0], [65, 280, 1], [30, 150, 0], [70, 260, 0],
            [45, 200, 1], [80, 300, 1], [35, 130, 0], [55, 240, 1]]
kriz = [0, 1, 0, 1, 0, 1, 0, 1]

model = LogisticRegression()
model.fit(hastalar, kriz)

print("Kalp krizi tahmin sistemi")
yas = int(input("Hastanın yaşını girin: "))
kolesterol = int(input("Kolesterol seviyesini girin: "))
sigara_iciyor = int(input("Sigara içiyor mu? (Hayır: 0, Evet: 1): "))

if sigara_iciyor not in (0, 1):
    print("Hata: Sigara değeri yalnızca 0 veya 1 olmalıdır.")
else:
    yeni_hasta = [[yas, kolesterol, sigara_iciyor]]
    tahmin = model.predict(yeni_hasta)[0]

    print(f"\nSonuç: {tahmin}")
    if tahmin == 1:
        print("Acil kontrol zamanı! Kalp krizi riskiniz yüksek görünüyor. Bir doktora en kısa sürede danışın.")
    else:
        print("Harika haber! Sağlıklı yaşam yolunda ilerleyin: dengeli beslenin, hareket edin ve sigaradan uzak durun.")

# Örnek profil: 60 yaş, 250 kolesterol, sigara içiyor
print(model.predict([[60, 250, 1]])[0])
