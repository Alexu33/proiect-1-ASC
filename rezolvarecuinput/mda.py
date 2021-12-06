def xor(str1,str2):
    return int(str1)^int(str2)

def decriptare():
    filebin = open(input,"rb")
    outfile = open(output,"w")

    byte = filebin.read(1)

    i=0

    while i<l:
        s=int.from_bytes(byte,"little")
        #print(int(s),end=" ")
        k = xor(s, ord(password[i]))
        #print (password[i], "   ", ord(password[i]),  "    ", int(s), "    xor=    ", int(k))
        print(int(k),end=" ")
        i += 1

        #outfile.write(chr(s))
        byte=filebin.read(1)
    return 0


ciclu ="94 32 136 175 91 91 233 67 209 186 188 65 17 94 182 183 210 135 163 117 120 130 34 189 109 111 165 15 70 234 241 4 69 122 218 223 74 30 141 213 226 8 138 245 181 190 148 61 27 171 196 17 21 235 107 125 40 122 55 87 136 34 43 214 214 250 80 244 110 175 16 68 87 173 173 244 161 232 221"
#input="outputtestareteorie"
#password="fgsadjfgsfdghdfsgrestagsdafaewfsdaffasdgafdafsd"
#output="teoriefinal.txt"

input = "out"
output = "hahaha.txt"
password="In primavara anului 1916, ca sublocotenent proaspat, intaia data concentrat, luasem parte, cu un regiment de in- fanterie din capitala"

l=len(password)


#decriptare()

try:
    decriptare()
    print("decriptare efectuata cu succes")
except:
    print("decriptare esuata")
    pass

