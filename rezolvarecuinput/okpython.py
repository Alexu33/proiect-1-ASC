import sys

def transformbyte(v):
    answer = 0
    for x in v:
        answer = answer * 2 + x
    return answer

password = sys.argv[1]
#nume_fisier_intrare = sys.argv[2]
#nume_fisier_iesire = sys.argv[3]
passwordbin = []
textbin = []
chbin = []
opt = []
MOD = 94
val = 0

#with open(nume_fisier_intrare,"r") as f:
 #   sir = f.read()


# teste
sir="ab"

for i in range(0,len(password)):
    x=ord(password[i])-33
    val=val*MOD+x

print("valoarea este  ", val)
while val > 0 :
    passwordbin.append(val % 2)
    val = val // 2

print(val)

print(passwordbin, "                 ", len(passwordbin), "            ",password[0], "          ascii  ", val)


for i in range(0,len(sir)) :
    asci = ord(sir[i])
    chbin = []
    for j in range(0,8) :
        chbin.append(asci % 2)
        asci = asci // 2
    textbin.extend(chbin[::-1])




#print(chbin, "              ",   sir[i], "          ascii   ", ord(sir[i]))

lentext = len(textbin)
lenpass = len(passwordbin)

rest = lenpass - lentext % lenpass


print (lenpass, "    ",lentext,  "    restul este  ", rest)

for i in range(0, rest):
    textbin.append(0)

print(textbin)


print ("parola binara este", passwordbin)
print (textbin)

for i in range(0, lentext, lenpass):
    for j in range(0, lenpass):
        textbin[i + j] = textbin[i + j] ^ passwordbin[j]
print(textbin)

