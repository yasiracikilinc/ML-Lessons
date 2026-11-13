from sklearn.ensemble import RandomForestClassifier

X = [[90, 85], [50, 60], [80, 40], [40, 90]]
y = ["Kabul", "Red", "Red", "Kabul"]

model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X, y)

yeni_oyuncu = [[85, 80]]
tahmin = model.predict(yeni_oyuncu)
print(tahmin[0])