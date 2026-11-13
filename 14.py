from sklearn.tree import DecisionTreeClassifier as dt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# veriler = [[2, 100], [5, 110], [1, 90], [8, 120], [3, 105], [7, 115], [0, 95], [6, 130]]
# sonuclar = [0, 1, 0, 1, 0, 1, 0, 1]

# egitim_verileri, test_verileri, egitim_sonuclar, test_sonuclar = train_test_split(veriler, sonuclar, test_size=0.25, random_state=42)

# ai= dt().fit(egitim_verileri, egitim_sonuclar)
# ai_cevaplari = ai.predict(test_verileri)

# dogruluk_notu = accuracy_score(test_sonuclar, ai_cevaplari) * 100
# print("Doğruluk Notu: %.2f%%" % dogruluk_notu)

from sklearn.neighbors import KNeighborsClassifier as kn

konumlar = [[10,10], [12,11], [90,90], [95,85], [11,10], [88,92], [9,11], [91,89]]
bolgeler = ["A", "A", "B", "B", "A", "B", "A", "B"]

egitim_verileri, test_verileri, egitim_bolgeler, test_bolgeler = train_test_split(konumlar, bolgeler, test_size=0.25, random_state=42)
belirleyici_ai = kn(n_neighbors=3).fit(egitim_verileri, egitim_bolgeler)
ai_cevaplari = belirleyici_ai.predict(test_verileri)

basari = accuracy_score(test_bolgeler, ai_cevaplari) * 100
print("Başarı Notu: %.2f%%" % basari)