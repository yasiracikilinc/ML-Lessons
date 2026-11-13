from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

idman_verileri = [[10, 8], [2, 3], [12, 9], [5, 5], [8, 7], [1, 2], [14, 10], [4, 4]]
mac_sonuclari = [1, 0, 1, 0, 1, 0, 1, 0]

egitim_veri, test_veri, egitim_sonuc, test_sonuc = train_test_split(idman_verileri, mac_sonuclari, test_size=0.25, random_state=42)

espor_ai = LogisticRegression().fit(egitim_veri, egitim_sonuc)
tahminler = espor_ai.predict(test_veri)

print(f"E Spor AI sinav sonucu: %{accuracy_score(test_sonuc, tahminler)* 100 }")

from sklearn.linear_model import LinearRegression as lr

ai = lr().fit([[10], [20], [30]], [100, 200, 300])
print("Dogrusal Tahmin:", ai.predict([[25]]) [0])

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression as lr

bukucu = PolynomialFeatures(degree=2)
AI_Kavisli = lr().fit(bukucu.fit_transform([[1], [2], [3]]), [2, 8, 18])

print("Kavisli Tahmin:", AI_Kavisli.predict(bukucu.transform([[4]])) [0])

from sklearn.linear_model import LogisticRegression as log
ai = log().fit([[10], [50]], [0, 1])
print("1 mi 0 mı peki sonucu", ai.predict([[40]])[0])

from sklearn.tree import DecisionTreeClassifier

ai = DecisionTreeClassifier().fit([[4, 0], [2, 1]], ["Kedi", "Kuş"])
print("Tahmin edilen hayvan:", ai.predict([[3, 0]])[0])