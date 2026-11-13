from sklearn.tree import DecisionTreeClassifier

mesaj_verileri = [[0, 0], [1, 0], [3, 2], [5, 5]]
durumlar = ["Güvenli", "Güvenli", "Şüpheli", "Tehlikeli Spam"]

model = DecisionTreeClassifier()
model.fit(mesaj_verileri, durumlar)

while True:
	link_sayisi = int(input("Mesajdaki link sayısı (çıkış için -1): "))
	if link_sayisi == -1:
		print("Programdan çıkılıyor.")
		break

	supheli_kelime_sayisi = int(input("Şüpheli kelime sayısı: "))
	tahmin = model.predict([[link_sayisi, supheli_kelime_sayisi]])
	print(f"Mesajın durumu: {tahmin[0]}")
	break