from sklearn.neighbors import KNeighborsClassifier as kn
tatlilar = [[9,4], [8,5], [2,9], [1,10]]
turler = [["Bitter", "Bitter", "Sütlü", "Sütlü"]]
kn_classifier = kn(n_neighbors = 3).fit(tatlilar, turler[0])
print("Tatlı türü: ", kn_classifier.predict([[8,4]])[0])