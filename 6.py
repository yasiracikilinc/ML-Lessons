from sklearn.linear_model import LinearRegression

kullanimlar = [[2,4], [5,5], [10,8], [0,2]]
faturalar = [300, 500, 900, 150]
model = LinearRegression()
model.fit(kullanimlar,faturalar)

while True:
    klima = int(input("Klima kullanım süresini girin (saat): "))
    if klima == -1:
        break
    tv = int(input("TV kullanım süresini girin (saat): "))
    tahmin = model.predict([[klima, tv]])
    print(f"Fatura tahmini: {tahmin[0]:.2f} TL")
    if tahmin[0] > 700:
        print("Fatura tahmini yüksek! Enerji tasarrufu yapmayı düşünün.")
    elif tahmin[0] < 300:
        print("Fatura tahmini düşük! Enerji kullanımınızı kontrol altında tutuyorsunuz.")
    else:
        print("Fatura tahmini normal seviyede. Enerji kullanımınızı dengede tutmaya devam edin.")