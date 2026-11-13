from sklearn.linear_model import LinearRegression as lr

teslimat_verileri = [[2, 3, 0], [5, 8, 2], [1, 1, 0], [10, 9, 5], [3, 5, 1], [7, 7, 0], [4, 2, 4], [8, 10, 3], [2, 9, 5], [6, 4, 0]]
sureler = [15, 45, 10, 85, 25, 50, 35, 75, 40, 40]
kurye_ai = lr().fit(teslimat_verileri, sureler)

print("Akıllı Yemek Teslimat Sistemi")
while True:
    mesafe = float(input("\nTeslimat mesafesi (km) ne kadar?(çıkış için -1): "))
    if mesafe == -1:
        print("Programdan çıkılıyor.")
        break

    siparis_sayisi = int(input("Sipariş sayısı: "))
    trafik_durumu = int(input("Trafik durumu (0: Hafif, 1: Orta, 2: Yoğun): "))

    tahmin_sure = kurye_ai.predict([[mesafe, siparis_sayisi, trafik_durumu]])
    print(f"Tahmini teslimat süresi: {tahmin_sure[0]:.2f} dakika")
    break