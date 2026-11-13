isim = input("Ajan adın: ")

can = 100
altin = 0
guc = 10
bolum = 1
mcan = 50

while can > 0 and bolum < 4:
    print(f"\n=== {isim} - Can: {can} - Altın: {altin} - Güç: {guc} - Bölüm: {bolum}")

    if bolum == 1:
        print("HÜCREDESİN: \n1-Samanı ara, \n2-Kapıyı Tekmele, \n3- Fare deliğine bak")
        s = input("Seçim: ")

        if s == "1":
            guc += 15
            print("Hançer buldun! Gücün arttı.")
        elif s == "2":
            can -= 10
            print("Kapı açıldı ama ayağın yaralandı. Canın azaldı.")
        elif s == "3":
            altin += 10
            print("Gizli bir sandık buldun! Altın arttı.")
        else:
            print("Hatalı seçim. zaman kaybettin.")
            continue
        bolum = 2
    elif bolum == 2:
        print("\nKORİDORDASIN: \n1-Sessize geç, \n2- Nöbetçiye saldır, \n3-Nöbetçiye rüşver ver")
        s = input("Seçim: ")

        if s == "1":
            can -= 20
            print("Sessizce geçmeye çalıştın ama yakalandın. Canın azaldı.")
        elif s == "2":
            if guc >= 15:
                print("Nöbetçiyi yendin! Yoluna devam edebilirsin.")
            else:
                can -= 15
                print("Güçlü değildin ve Nöbetçi seni osman tuşladı. Zor kaçabildin.")
        elif s == "3":
            if altin >= 10:
                altin -=10
                print("Nöbetçi paranı aldı ve yoluna devam etmen için izin verdi. Ama baktın nöbetçi Fortnite Bilet pass almış.")
            else:
                can -= 25
                print("YETERLİ ALTIN YOK SENİN! diye bağırdı ve seni dövdü.")
        else:
            print("Hatalı seçim.")
            continue
        bolum = 3
    elif bolum == 3:
            print("\n EMERGENCY ACİL DURUM BOSS ÇIKTI!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            h = input("Hamlen (1-saldır, 2-savun, 3 taş at)")

            if h == "1":
                mcan -= guc
                can -= 15
                print(f"Saldırdın ve {guc} hasar verdin ama sende 15 hasar aldın.!")
            elif h == "2":
                can -= 5
                print("Savunma yaptın ve 5 hasar aldın.")
            elif h == "3":
                mcan -= 20
                print("Taş attın ve 20 hasar verdin.")
            else:
                print("Hatalı hamle! Canavar sana vurdu.")
                can -= 10

            if mcan <= 0:
                print("TEBRİKLER! BOSS'U YENDİN! ARTIK ÖZGÜRSÜN.")
                bolum = 4
    if can <= 0:
        print("MAALESEF ÖLDÜN! OYUN BİTTİ.")