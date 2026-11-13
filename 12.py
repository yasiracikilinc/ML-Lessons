
from sklearn.model_selection import LogisticRegression as lr

def anti_cheat():

    oyuncular = [ [30, 5, 4], [95, 0, 20], [45, 6, 5], [98, 0, 25], [20, 8, 3], [100, 0, 30], [55, 4, 6], [90, 1, 18] ]

    ban_durumu = [0, 1, 0, 1, 0, 1, 0, 1]
    vanguard_anticheat = lr().fit(oyuncular, ban_durumu)

    while True:
        print("\nOyuncu bilgilerini giriniz: (oyun_suresi, hile_sayisi, ban_sayisi)")
        hs = input("Hile sayısı: ")
        if hs.lower() == "exit":
            print("Programdan çıkılıyor...")
            break

        while hs.isdigit() == False:
            print("Hile sayısı bir sayı olmalıdır.")
            hs = input("Hile sayısı: ")
            if hs.lower() == "exit":
                print("Programdan çıkılıyor...")
                return

        else:
            hs = int(hs)

            titreme = input("Oyun süresi: ")
            while titreme.isdigit() == False:
                print("Oyun süresi bir sayı olmalıdır.")
                titreme = input("Oyun süresi: ")
                if titreme.lower() == "exit":
                    print("Programdan çıkılıyor...")
                    return
                elif titreme.isdigit() == True:
                    titreme = int(titreme)
                    break
                tiklama = input("Ban sayısı: ")
                while tiklama.isdigit() == False:
                    print("Ban sayısı bir sayı olmalıdır.")
                    tiklama = input("Ban sayısı: ")
                    if tiklama.lower() == "exit":
                        print("Programdan çıkılıyor...")
                        return
                    elif tiklama.isdigit() == True:
                        tiklama = int(tiklama)
                        break
                LogisticRegression = vanguard_anticheat.predict([[titreme, hs, tiklama]])
                lr = LogisticRegression[0]
                if lr == 1:
                    print("Bu oyuncu banlanmıştır.")
                else:
                    print("Bu oyuncu banlanmamıştır.")

                    sklearn.model = vanguard_anticheat.predict([[titreme, hs, tiklama]])
                    lr = sklearn.model[0]