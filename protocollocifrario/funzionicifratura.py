#Cifratura Base#

def intestazione():
    print("                 DECIPHER V1")
    print("            di Marco Lo Giudice")
    print("################################################")

def menu():
    print("************************************************")
    print("* 1 per avviare il protocollo di decriptazione.*")
    print("* E per uscire dal programma.                  *")
    print("************************************************")

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