#Cifratura Base#

def intestazione():
    print("                   CIPHER V1")
    print("              di Marco Lo Giudice")
    print("######################################################")

def menu():
    print("******************************************************")
    print("* 1 per avviare il protocollo di decriptazione. WIP! *")
    print("* 2 per avviare il protocollo di criptazione.        *")
    print("* E per uscire dal programma.                        *")
    print("******************************************************")

def decriptabase(parola):
    cifrato = ['J', '?', 'W', 'B', ':', 'Q', 'H', '.', 'Z', 'X', 'R', ';', 'N', 'T', ' ', '7', '3', '9', '1', '4', '2', '6', '0', '5', '8', 'C', 'A', 'O', 'S', '!', 'D', 'G', 'I', 'M', 'P', 'E', ',', 'F', 'U', 'L', 'Y', 'K', 'V']
    chiaro = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '!', '?', '.', ',', ';', ':', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    risultato = []
    #risultato2 = [] # Chiaro
    
    for char in parola:
        if char in chiaro:
            index = cifrato.index(char)
            risultato.append(chiaro[index])
            #risultato2.append(cifrato[index])
        else:
            risultato.append('?') 
            #risultato2.append('?')

    return ''.join(risultato)

####DEBUG_criptabase********
#ine = input().upper()######
#print(criptabase(ine))#####
####END_DEBUG***************

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

##DA FINIRE## http://www.fogazzaro.it/ISA/5AT/Crittografia.pdf
'''def criptaavanzata(risultato):
    risultato3=[]
    a=list(range(33,97))
    for n in a:
        risultato3.append(chr(n))
        indice=risultato.index()
'''


def convertitore(risultato):
    risultato4 = []
    for char in risultato:
        risultato4.append(str(ord(char)))
    return ''.join(risultato4)

def scompositore(risultato_ascii):
    risultato5 = []
    i = 0
    while i < len(risultato_ascii):
        if i + 2 < len(risultato_ascii) and risultato_ascii[i:i+3].isdigit() and 32 <= int(risultato_ascii[i:i+3]) <= 126:
            # Prova a prendere 3 cifre
            risultato5.append(chr(int(risultato_ascii[i:i+3])))
            i += 3
        elif risultato_ascii[i:i+2].isdigit():
            # Prendi 2 cifre
            risultato5.append(chr(int(risultato_ascii[i:i+2])))
            i += 2
    return ''.join(risultato5)

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