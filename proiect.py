import sys
import os

# verifica daca exista fisierul de input
def Check(file):
    try:
        file=open(input, "r")
        return 1
    except:
        return 0

def xor(str1,str2):
    return int(str1)^int(str2)



#verifica nr argumente
if(len(sys.argv)!=5):
    print("Numar invalid de parametri\n Formatul este: python3 proiect.py <encrypt/decrypt> <input> <output> <parola>")
    sys.exit()

metoda = sys.argv[1]
input = sys.argv[2]
extensie =  os.path.splitext(input)[1]
output = sys.argv[3]
parola = sys.argv[4]

#verificari
if (metoda != "encrypt" and metoda != "decrypt"):
    print("metoda invalida\n Formatul este: python3 proiect.py <encrypt/decrypt> <input> <output> <parola>")
    sys.exit()
if (metoda=="encrypt"):
    if (extensie != ".txt"):
        print("fisier input invalid\n Formatul este: python3 proiect.py <encrypt/decrypt> <input> <output> <parola>")
        sys.exit()
if(Check(input) == 0):
    print("fisierul nu exista")
    sys.exit()


if (len(parola)<10 or len(parola)>15):
    print("parola invalida, numarul de caractere nu este corect")
    sys.exit()


def criptare():
    ok=1
    lungime=len(parola)
    i=0
    files=open(input,'r')
    filesout=open(output,'wb')

    while ok:
        try:
            char = ord(files.read(1))
        except:
            break
        rez = xor(char,ord(parola[i]))
        filesout.write(rez.to_bytes(1,byteorder='little'))
        i += 1
        if(i==lungime):
            i=0
        if not char:
           ok = 0
    return 0

def decriptare():
    filebin = open(input,"rb")
    outfile = open(output,"w")
    byte = filebin.read(1)

    lungime = len(parola)
    i=0

    while byte:
        s=int.from_bytes(byte,"little")
        s = xor(s, ord(parola[i]))
        i += 1
        if(i==lungime):
            i=0

        outfile.write(chr(s))
        byte=filebin.read(1)
    return 0

if metoda=="encrypt":
    try:
        criptare()
        print("criptare efectuata cu succes")
    except:
        print("criptare esuata")
else:
    try:
        decriptare()
        print("decriptare efectuata cu succes")
    except:
        print("decriptare esuata")