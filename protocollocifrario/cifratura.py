import funzionicifratura, os, time


ex="F"
while ex!="V" :
    i=""
    sc1=""
    sc1a=""
    funzionicifratura.intestazione()
    funzionicifratura.menu()
    i=input("Effettua la tua scelta: ").upper()
    match i:
        case "1":
            os.system("cls")
            funzionicifratura.intestazione()
            sc1=input("Inserisci messaggio da decriptare: ").upper()
            os.system("cls")
            funzionicifratura.intestazione()
            print("Messaggio decriptato:",'"',funzionicifratura.decriptabase(sc1),'"')
            print("Messaggio criptato:",'"',sc1,'"')
            sca=input("Inserire qualsiasi valore per tornare al menu: ")
            if sca.isascii():
                os.system("cls")
                funzionicifratura.intestazione()
                print("Ritorno al menù...")
                time.sleep(5)
                os.system("cls")
        case "2":
            os.system("cls")
            funzionicifratura.intestazione()
            sc2=input("Inserisci messaggio da criptare: ").upper()
            os.system("cls")
            funzionicifratura.intestazione()
            print("Messaggio criptato:","'",funzionicifratura.criptabase(sc2),"'")
            print("Messaggio decriptato:","'",sc2,"'")
            sca=input("Inserire qualsiasi valore per tornare al menu: ")
            if sca.isascii():
                os.system("cls")
                funzionicifratura.intestazione()
                print("Ritorno al menù...")
                time.sleep(5)
                os.system("cls")

        case "E":
            os.system("cls")
            funzionicifratura.intestazione()
            print("Uscita in corso...")
            time.sleep(5)
            ex="V"
        case _:
            funzionicifratura.intestazione()
            print("Errore! Comando non riconosciuto\nRitorno al menù principale...")
            time.sleep(5)
            os.system("cls")