# Cipher & Decipher V1
Criptatore e Decriptatore in Python.
> [!IMPORTANT]  
> Il programma non presenta la funzione dechiper in quanto è ancora in fase di scviluppo.

> [!NOTE]  
> La presente documentazione, il programma e qualsiasi cosa ad esso correlato sono stati creati per scopi didattici, pertanto non si ritiene sicuro per un utilizzo professionale.

> [!TIP]
> Non eseguire il programma come amministratore in quanto non necessario.
## Programma [cifratura.py]
```
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
```
1. Intestazione e Inizializzazione:
-L'import delle librerie e delle funzioni necessarie, inclusa la libreria funzionicifratura.
-L'impostazione dell'interfaccia a colori tramite la libreria Color_Console.
-L'impostazione di un loop while che gestisce l'esecuzione del programma fino a quando l'utente sceglie di uscire.
2. Menu Principale:
-La visualizzazione del menu principale che offre opzioni all'utente per eseguire operazioni come cifratura e decriptazione.
3.Selezione dell'Operazione:
-L'utente inserisce un input per selezionare un'operazione, come cifratura (scelta "2") o decriptazione (scelta "1").
-Il programma esegue l'operazione corrispondente in base alla scelta dell'utente.
3. Cifratura:
-Viene richiesto all'utente di inserire un messaggio da cifrare.
-Il messaggio viene cifrato utilizzando una serie di funzioni di cifratura concatenate, tra cui cesare, atbash, atbah, albam, criptabase, e germanico.
-Viene visualizzato il messaggio cifrato e le diverse fasi di cifratura intermedie.
4. Decriptazione:
- La funzione di decriptazione è in fase di sviluppo e non è completamente implementata. Viene visualizzato un messaggio "Work In Progress" (WIP) per segnalare che la funzione è in corso di lavoro.
5. Uscita dal Programma:
- Se l'utente sceglie di uscire (scelta "E"), il programma termina l'esecuzione.
6. Gestione degli Errori:
- Se l'utente inserisce un comando non riconosciuto, viene visualizzato un messaggio di errore e il programma ritorna al menu principale.
7. Feedback all'Utente:
- Diverse stampe a schermo forniscono informazioni all'utente, come il risultato delle operazioni di cifratura/decriptazione e messaggi di ritorno al menu principale.
## Funzioni Cifratura [funzionicifratura.py]
### Intestazione [def intestazione()]
```
def intestazione():
    print("                   CIPHER V1")
    print("              di Marco Lo Giudice")
    print("######################################################")
```
Stampa l'intestazione del programma.
### Menù di scelta [def menu()]
```
def menu():
    print("******************************************************")
    print("* 1 per avviare il protocollo di decriptazione. WIP! *")
    print("* 2 per avviare il protocollo di criptazione.        *")
    print("* E per uscire dal programma.                        *")
    print("******************************************************")
```
Stampa il testo del menù di scelta iniziale del programma
### Protocollo base di criptazione [def criptabase(parola)]
```
def criptabase(parola):
    cifrato = ['J', '?', 'W', 'B', ':', 'Q', 'H', '.', 'Z', 'X', 'R', ';', 'N', 'T', ' ', '7', '3', '9', '1', '4', '2', '6', '0', '5', '8', 'C', 'A', 'O', 'S', '!', 'D', 'G', 'I', 'M', 'P', 'E', ',', 'F', 'U', 'L', 'Y', 'K', 'V']
    chiaro = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '!', '?', '.', ',', ';', ':', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    #risultato = []
    risultato2 = [] # Chiaro
    
    for char in parola:
        if char in cifrato:
            index = chiaro.index(char)
            risultato2.append(cifrato[index])
            #risultato2.append(cifrato[index])
        else:
            risultato2.append('?') 
            #risultato2.append('?')

    return ''.join(risultato2)
```
- Se il carattere è presente nella lista `chiaro`, viene determinato l'indice corrispondente in `chiaro`.
- Il carattere corrispondente dalla lista `cifrato` viene aggiunto alla lista `risultato2`.
- Se il carattere non è presente nella lista `chiaro`, viene aggiunto il carattere `?` alla lista `risultato2`.
#### Tabella alfabeto in chiaro e cifrato
| Alfabeto chiaro | Alfabeto Cifrato |
| - | - |
| A | J |
| B | ? |
| C | W |
| D | B |
| E | : |
| F | Q |
| G | H |
| H | . |
| I | Z |
| J | X |
| K | R |
| L | ; |
| M | N |
| N | T |
| O |  |
| P | 7 |
| Q | 3 |
| R | 9 |
| S | 1 |
| T | 4 |
| U | 2 |
| V | 6 |
| W | 0 |
| X | 5 |
| Y | 8 |
| Z | C |
|  | A |
| ! | O |
| ? | S |
| . | ! |
| , | D |
| ; | G |
| : | I |
| 0 | M |
| 1 | P |
| 2 | E |
| 3 | , |
| 4 | F |
| 5 | U |
| 6 | L |
| 7 | Y |
| 8 | K |
| 9 | V |
### Protocollo di conversione in ASCII [def convertitore(risultato)]
```
def convertitore(risultato):
    risultato4 = []
    for char in risultato:
        risultato4.append(str(ord(char)))
    return ''.join(risultato4)
```
- Per ogni carattere, viene utilizzata la funzione `ord(char)` per ottenere il suo valore ASCII decimale come una stringa.
- Il valore ASCII decimale viene aggiunto alla lista `risultato4`
### Protocollo di conversione ATBASH [def atbash(parola)]
```
def atbash(parola):
    chiaro = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cifrato = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
    
    risultato = []
    for char in parola.upper():
        if char in chiaro:
            index = chiaro.index(char)
            risultato.append(cifrato[index])
        else:
            risultato.append(char)
    
    return ''.join(risultato)
```
- Se il carattere è presente nell'alfabeto normale `chiaro`, viene determinato l'indice corrispondente.
- Viene quindi aggiunto il carattere corrispondente dall'alfabeto cifrato di Atbash `cifrato` alla lista `risultato`.
- Se il carattere non è presente nell'alfabeto normale, viene aggiunto direttamente alla lista risultato.
### Protocollo di conversione ALBAM [def albam(parola)]
```
def albam(parola):
    chiaro = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cifrato = 'NOPQRSTUVWXYZABCDEFGHIJKLM'
    
    risultato = []
    for char in parola.upper():
        if char in chiaro:
            index = chiaro.index(char)
            risultato.append(cifrato[index])
        else:
            risultato.append(char)
    
    return ''.join(risultato)
```
- Se il carattere è presente nell'alfabeto normale `chiaro`, viene determinato l'indice corrispondente.
- Viene quindi aggiunto il carattere corrispondente dall'alfabeto cifrato alla lista `risultato`.
- Se il carattere non è presente nell'alfabeto normale, viene aggiunto direttamente alla lista `risultato`.
### Protocollo di conversione ATBAH [def atbah(parola)]
```
def atbah(parola):
    chiaro = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cifrato = 'TSRQPONMLKJIHGFEDCBAUVWXYZ'
    
    risultato = []
    for char in parola.upper():
        if char in chiaro:
            index = chiaro.index(char)
            risultato.append(cifrato[index])
        else:
            risultato.append(char)
    
    return ''.join(risultato)
```
- Se il carattere è presente nell'alfabeto normale `chiaro`, viene determinato l'indice corrispondente.
- Viene quindi aggiunto il carattere corrispondente dall'alfabeto cifrato secondo il metodo Atbah alla lista `risultato`.
- Se il carattere non è presente nell'alfabeto normale, viene aggiunto direttamente alla lista `risultato`.
### Protocollo di Cesare [def cesare(parola, shift)]
```
def cesare(parola, shift):
    chiaro = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    risultato = []

    for char in parola.upper():
        if char in chiaro:
            index = (chiaro.index(char) + shift) % 26
            risultato.append(chiaro[index])
        else:
            risultato.append(char)

    return ''.join(risultato)
```
- Se il carattere è una lettera presente nell'alfabeto `chiaro`, ne viene trovato l'indice.
- Viene quindi calcolato il nuovo indice sommando il valore di shift al suo indice corrente e applicando l'operazione modulo 26 per gestire il wrap-around dell'alfabeto.
- Il carattere corrispondente a questo nuovo indice nell'alfabeto viene aggiunto alla lista `risultato`.
- Se il carattere non è una lettera, viene aggiunto direttamente alla lista `risultato`.
### Protocollo Germanico [def cesare(parola, shift)]
```
def germanico(parola):
    cifrato = ['J', '?', 'W', 'B', ':', 'Q', 'H', '.', 'Z', 'X', 'R', ';', 'N', 'T', ' ', '7', '3', '9', '1', '4', '2', '6', '0', '5', '8', 'C', 'A', 'O', 'S', '!', 'D', 'G', 'I', 'M', 'P', 'E', ',', 'F', 'U', 'L', 'Y', 'K', 'V']
    chiaro = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '!', '?', '.', ',', ';', ':', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    risultato = []

    for char in parola:
        if char in chiaro:
            index = cifrato.index(char)
            risultato.append(chiaro[index])
        else:
            risultato.append(char)

    return ''.join(risultato)
```
- Se il carattere è presente nella lista `chiaro`, viene determinato l'indice corrispondente nella lista `cifrato`.
- Viene quindi aggiunto il carattere corrispondente dalla lista `chiaro` alla lista `risultato`.
- Se il carattere non è presente nella lista `chiaro`, viene aggiunto direttamente alla lista `risultato`.
## Problemi noti
> [!CAUTION]
> La funzione dechiper non funziona in quanto work in progress (WIP).

> [!WARNING]
> Alcuni sistemi rilevano il file eseguibile (`cifratura.exe`) non sicuro.
### Risoluzione eseguibile non sicuro
![Risoluzione.](https://cdn.discordapp.com/attachments/1012823427574403135/1249019522417950851/cunnutuwindows.PNG?ex=6665c793&is=66647613&hm=05597d961b602c2bd381d8c01462c3c2021126ae3c853608e4325da4887df5c2&)

La schermata che ci appare è la seguente, pertanto premiamo `Ulteriori informazioni`.

![Risoluzione pt.2.](https://cdn.discordapp.com/attachments/1012823427574403135/1249019522137198674/cunnutuwindows2.PNG?ex=6665c793&is=66647613&hm=91fcfebb166536ecb9e2efbdd7d5ee7229fd612e711731cfaa5813387e8aba80&)

Ci apparirà il pulsante `Esegui comunque`, lo premiamo e il programma ci si avvierà.
