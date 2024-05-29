import funzionicifratura, os, time, Color_Console
Color_Console.color(text="green", bg="black")


ex="F"
while ex!="V" :
    i=""
    sc1=""
    sc1a=""
    os.system("cls")
    funzionicifratura.intestazione()
    funzionicifratura.menu()
    i=input("Effettua la tua scelta: ").upper()
    match i:
        case "1": #####DA FINIRE -- Funzione di Decriptazione
            os.system("cls")
            funzionicifratura.intestazione()
            '''sc1=input("Inserisci messaggio da decriptare: ").upper()
            os.system("cls")
            funzionicifratura.intestazione()
            print("Messaggio decriptato:",'"',funzionicifratura.scompositore(funzionicifratura.decriptabase(sc1)),'"')
            print("Cifratura intermedia:","'",funzionicifratura.decriptabase(sc1),"'")
            print("Messaggio criptato:",'"',sc1,'"')
            sca=input("Inserire qualsiasi valore per tornare al menu: ")
            if sca.isascii():
                os.system("cls")
                funzionicifratura.intestazione()
                print("Ritorno al menù...")
                time.sleep(3)
                os.system("cls")'''
            print("Funzione WIP!")
            time.sleep(3)
        case "2":
            os.system("cls")
            funzionicifratura.intestazione()
            sc2=input("Inserisci messaggio da criptare: ").upper()
            os.system("cls")
            funzionicifratura.intestazione()
            print("Messaggio criptato:","'",funzionicifratura.convertitore(funzionicifratura.germanico(funzionicifratura.criptabase(funzionicifratura.albam(funzionicifratura.atbah(funzionicifratura.atbash(funzionicifratura.cesare(sc2,3))))))),"'")
            print("Criptazione Germanica:","'",funzionicifratura.germanico(funzionicifratura.criptabase(funzionicifratura.albam(funzionicifratura.atbah(funzionicifratura.atbash(funzionicifratura.cesare(sc2,3)))))),"'")
            print("Criptazione intermedia:","'",funzionicifratura.criptabase(funzionicifratura.albam(funzionicifratura.atbah(funzionicifratura.atbash(funzionicifratura.cesare(sc2,3))))),"'")
            print("Criptazione ALBAM:","'",funzionicifratura.albam(funzionicifratura.atbah(funzionicifratura.atbash(funzionicifratura.cesare(sc2,3)))),"'")
            print("Criptazione ATBAH:","'",funzionicifratura.atbah(funzionicifratura.atbash(funzionicifratura.cesare(sc2,3))),"'")
            print("Criptazione ATBASH:","'",funzionicifratura.atbash(funzionicifratura.cesare(sc2,3)),"'")
            print("Criptazione Cesare:","'",funzionicifratura.cesare(sc2,3),"'")
            print("Messaggio decriptato:","'",sc2,"'")
            sca=input("Inserire qualsiasi valore per tornare al menu: ")
            if sca.isascii():
                os.system("cls")
                funzionicifratura.intestazione()
                print("Ritorno al menù...")
                time.sleep(3)
                os.system("cls")
        case "E":
            os.system("cls")
            funzionicifratura.intestazione()
            print("Uscita in corso...")
            time.sleep(3)
            ex="V"
        case _:
            os.system("cls")
            funzionicifratura.intestazione()
            print("Errore! Comando non riconosciuto\nRitorno al menù principale...")
            time.sleep(3)
            os.system("cls")