ciclu="94 32 136 175 91 91 233 67 209 186 188 65 17 94 182 183 210 135 163 117 120 130 34 189 109 111 165 15 70 234 241 4 69 122 218 223 74 30 141 213 226 8 138 245 181 190 148 61 27 171 196 17 21 235 107 125 40 122 55 87 136 34 43"
fisier = open("sirbin.txt",'w')

"""
nr = [int(x) for x in ciclu.split(' ')]
print(nr)
#print(nr)
complet=""
for x in nr:
    #print(x)
    aux=""
    while x>0:
        c=x%2
        x=x//2
        aux=chr(c+48)+aux
    lun = len(aux)
    while lun<8:
        aux="0"+aux
        lun+=1
    #print(s, "     ", aux)
    complet=complet+aux

fisier.write(complet)
print (len(complet))

l=1
s=complet[0]

while l<=251:
    p1=0
    p2=l
    ok=1
    while p1<l:
        if s[p1]!=complet[p2]:
            ok=0
        p1+=1
        p2+=1
    if ok==1:
        print("ok   ",s)
    s=s+complet[l]
    l+=1
"""



codposibil="0101111000100000100010001010111101011011010110111110100101000011110100011011101"
valoare=441758202249721423135866

def strtoint(y):
    val=0

    for i in range(0, len(y)):
        x = ord(y[i]) - 33
        val = val * 94 + x
        print("valoarea la pozitia  ",i,"     este   ",val)
    if val<valoare:
        print("este mai mica     ",y)
    else:
        if val>valoare:
            print("este mai mare     ", y)
        else:
            print("sunt egale   ", y)
    print(val)
    print(valoare)
    return 1

# abcdefghijklmnopqrstuvwxyz

test1="x8fdAmVVskZe"
strtoint(test1)







