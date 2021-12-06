import sys
import _thread

def transformbyte(v):
    answer = 0
    for x in v:
        answer = answer * 2 + x
    return answer



def algoritm():
    opt = []
    textread = []
    textbin = []
    passwordbin = []
    val = 0
    MOD = 94
    for i in range(0,len(password)):
        x = ord(password[i]) - 33
        val = val * MOD + x

    while val > 0 :
        passwordbin.append(val % 2)
        val = val // 2

    with open(nume_fisier_intrare,"rb") as f:
        textread = f.read()

    for bit in textread :
        for i in range(7,-1,-1) :
            textbin.append((bit >> i) & 1)

    lentext = len(textbin)
    lenpass = len(passwordbin)

    rest = lenpass - lentext % lenpass

    for i in range(0,rest) :
        textbin.append(0)

    for i in range(0,lentext,lenpass):
        for j in range(0, lenpass) :
             textbin[i + j] = textbin[i + j] ^ passwordbin[j]

    for i in range(0,lentext ,8) :
        opt.append(chr(transformbyte(textbin[i:i+8])))

    with open(nume_fisier_iesire,"w") as g:
        try:
            print(*opt, sep="", file = g)
            print("ok    " +password)
            fileo.write(password)
            fileo.write('\n')
        except:
            #print("da eroare   " + password)
            pass
    return 1




opt = []
textread = []
textbin = []
passwordbin = []
val = 0
MOD = 94

nume_fisier_intrare = sys.argv[1]
nume_fisier_iesire = sys.argv[2]
fileo = open("solutii.txt",'w')


posibilitati = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
lung = len(posibilitati)
print(lung)
for nr in range(11,15):
    for a1 in range(0,lung):
        for a2 in range(0, lung):
            for a3 in range(0, lung):
                for a4 in range(0, lung):
                    for a5 in range(0, lung):
                        print(a5)
                        for a6 in range(0, lung):
                            for a7 in range(0, lung):
                                #print(a7)
                                for a8 in range(0, lung):
                                    for a9 in range(0, lung):
                                        for a10 in range(0, lung):
                                            password=""+posibilitati[a1]+posibilitati[a2]+posibilitati[a3]+posibilitati[a4]+posibilitati[a5]+posibilitati[a6]+posibilitati[a7]+posibilitati[a8]+posibilitati[a9]+posibilitati[a10]
                                            #print(password)
                                            #print(a10)
                                            for a11 in range(0, lung):
                                                password=password+posibilitati[a11]
                                                #print(a11)
                                                if nr>11:
                                                    for a12 in range(0, lung):
                                                        password=password+posibilitati[a12]
                                                        if nr >12:
                                                            for a13 in range(0, lung):
                                                                password=password+posibilitati[a13]
                                                                if nr > 13:
                                                                    for a14 in range(0,lung):
                                                                        password=password+posibilitati[a14]
                                                                        algoritm()
                                                                        password=password[:-1]
                                                                    password = password[:-1]
                                                                else:
                                                                    algoritm()
                                                                    password = password[:-1]
                                                            password = password[:-1]
                                                        else:
                                                            algoritm()
                                                            password = password[:-1]
                                                    password=password[:-1]
                                                else:
                                                    algoritm()
                                                    password = password[:-1]