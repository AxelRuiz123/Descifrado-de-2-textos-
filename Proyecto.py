#--------------------------Proyecto final disenio y analisis de algoritmos--------------------------
#---------------------------Creación de diccionarios e histogramas---------------------------

#---------------------------Diccionario e histograma en frances (francais.txt)---------------------------
alfabeto = "abcdefghijklmnopqrstuvwxyz"

arch_fr=open("francais.txt","r")
texto_fr = arch_fr.read()
texto2_fr = ""
texto2_fr = texto_fr.lower()
arch_fr.close()

for c in texto_fr:
    if c == "ã" or c == "à":
        texto2_fr += "a"
    elif c == "è" or c == "é" or c == "ê":
        texto2_fr += "e"
    elif c == "ì" or c == "í" or c == "î":
        texto2_fr += "i"
    elif c == "ò":
        texto2_fr += "o"
    elif c == "ù":
        texto2_fr += "u"

datos_fr = texto2_fr.split()

dic_fr=[]

for d in datos_fr:
    if not (d in dic_fr):
        dic_fr.append(d)
dic_fr.sort()

diccio_fr = open("dic_fr.txt", 'w')
cad_fr = ''
for p in dic_fr:
    cad_fr += p+" "
diccio_fr.write(cad_fr)
diccio_fr.close()

histo_fr = {}
for c in alfabeto:
    histo_fr[c] = 0

for c in texto_fr:
    if c in alfabeto:
        histo_fr[c] += 1

arch2_fr = open("histo_frances.csv","w")
for e in histo_fr.keys():
    arch2_fr.write(e+","+str(histo_fr[e])+"\n")
arch2_fr.close()

#---------------------------Diccionario e histograma en ingles (words.txt)---------------------------
arch_en=open("words.txt","r")
texto_en = arch_en.read()
texto2_en = ""
texto2_en = texto_en.lower()
arch_en.close()

datos_en = texto2_en.split()

dic_en=[]
for d in datos_en:
    if not (d in dic_en):
        dic_en.append(d)
dic_en.sort()

diccio_en = open("dic_en.txt", 'w')
cad_en = ''
for p in dic_en:
    cad_en += p+" "
diccio_en.write(cad_en)
diccio_en.close()

histo_en = {}
for c in alfabeto:
    histo_en[c] = 0

for c in texto_en:
    if c in alfabeto:
        histo_en[c] += 1


arch2_en = open("histo_ingles.csv","w")
for e in histo_en.keys():
    arch2_en.write(e+","+str(histo_en[e])+"\n")
arch2_en.close()

#---------------------------Diccionario e histograma en italiano (italian.txt)------------------------------------
arch_it=open("italian.txt","r")
texto_it = arch_it.read()
texto2_it = ""
texto2_it = texto_it.lower()
arch_it.close()


for c in texto_it:
    if c == "ã" or c == "à":
        texto2_it += "a"
    elif c == "è" or c == "é" or c == "ê":
        texto2_it += "e"
    elif c == "ì" or c == "í" or c == "î":
        texto2_it += "i"
    elif c == "ò":
        texto2_it += "o"
    elif c == "ù":
        texto2_it += "u"

datos_it = texto2_it.split()

dic_it=[]

for d in datos_it:
    if not (d in dic_it):
        dic_it.append(d)
dic_it.sort()

diccio_it = open("dic_it.txt", 'w')
cad_it = ''
for p in dic_it:
    cad_it += p+" "
diccio_it.write(cad_it)
diccio_it.close()

histo_it = {}
for c in alfabeto:
    histo_it[c] = 0

for c in texto_it:
    if c in alfabeto:
        histo_it[c] += 1

arch2 = open("histo_italiano.csv","w")
for e in histo_it.keys():
    arch2.write(e+","+str(histo_it[e])+"\n")
arch2.close()

#---------------------------Diccionario e histograma de los textos de proyecto (Proy14)------------------------
arch=open("Proy14.txt","r")
texto = arch.read()
texto2 = ""
texto2 = texto.lower()
arch.close()
textos = texto2.split("\n")

#-----------------------------Ambos textos---------------------------------------
datos = texto2.split()
dic=[]
for d in datos:
    if not (d in dic):
        dic.append(d)
dic.sort()

histo = {}
for c in alfabeto:
    histo[c] = 0

for c in texto:
    if c in alfabeto:
        histo[c] += 1

arch2 = open("histo_proyecto.csv","w")
for e in histo.keys():
    arch2.write(e+","+str(histo[e])+"\n")
arch2.close()

#-------------------------------Para el texto 1---------------------------------------
datos_txt1 = textos[0].split()
del datos_txt1[0:2]
txt_1 = ''.join(datos_txt1)

dic1=[]
for d in datos_txt1:
    if not (d in dic1):
        dic1.append(d)
dic1.sort()

histo_1 = {}
for c in alfabeto:
    histo_1[c] = 0

for c in txt_1:
    if c in alfabeto:
        histo_1[c] += 1

arch2_1 = open("histo_texto1.csv","w")
for e in histo_1.keys():
    arch2_1.write(e+","+str(histo_1[e])+"\n")
arch2_1.close()

print ('\n',datos_txt1)
#------------------------------------Para el texto 2--------------------------------------------------------
datos_txt2 = textos[2].split()
del datos_txt2[0:2]
txt_2 = ''.join(datos_txt2)

dic2=[]
for d in datos_txt2:
    if not (d in dic2):
        dic1.append(d)
dic2.sort()

histo_2 = {}
for c in alfabeto:
    histo_2[c] = 0

for c in txt_2:
    if c in alfabeto:
        histo_2[c] += 1

arch2_2 = open("histo_texto2.csv","w")
for e in histo_2.keys():
    arch2_2.write(e+","+str(histo_2[e])+"\n")
arch2_2.close()

print ('\n',datos_txt2)

#---------------------------------------Descifrando los textos------------------------------------------------
"""     Ahora obtendremos a que idioma pertenece el primer texto, por lo que primero compararemos
palabras con ayuda denuestro histograma al suponer que w = e, ya que es la letra que mas se repite y 
por ende obtener las demas                """

#Palabra wuawiaowi
print("Palabra: wuawiaowi")
c=0
for p in dic_it:
    if len(p) == 9:
        if p[0] == p[7] and p[2] == p[5]:
            if p[4] == p[-1] and p[3] == p[7]:
                c+=1
                if c < 1:
                    print("  - Italiano: ",c)
                else:
                    print("  - Italiano: ",p)
            
c=0
for p in dic_fr:
    if len(p) == 9:
        if p[0] == p[7] and p[2] == p[5]:
            if p[4] == p[-1] and p[3] == p[7]:
                c+=1
                if c == 0:
                    print("  - Frances: ",c)
                else:
                    print("  - Frances: ",p)

c=0
for p in dic_en:
    if len(p) == 9:
        if p[0] == p[7] and p[2] == p[5]:
            if p[4] == p[-1] and p[3] == p[7]:
                c+=1
                if c == 0:
                    print("  - Ingles: ",c)
                else:
                    print("  - Ingles: ",p)
"""Al realizar la comparacion podemos ver que solamente el frances tiene una palabra que cumple esas 
caracteristicas siendo esta 'encercler', por lo que: w=e, u=a, a=c, i=r, o=l """

# Palabra aquxiypduyux
print("Palabra: aquxiypduyux")
c=0
for p in dic_it:
    if len(p) == 12:
        if p[2] == p[8] and p[3] == p[-1]:
            if p[5] == p[9]:
                c+=1
                if c == 0:
                    print("  - Italiano: ",c)
                else:
                    print("  - Italiano: ",p)

c=0
for p in dic_fr:
    if len(p) == 12:
        if p[2] == p[8] and p[3] == p[-1]:
            if p[5] == p[9]:
                c+=1
                if c == 0:
                    print("  - Frances: ",c)
                else:
                    print("  - Frances: ",p)

c=0
for p in dic_en:
    if len(p) == 12:
        if p[2] == p[8] and p[3] == p[-1]:
            if p[5] == p[9]:
                c+=1
                if c == 0:
                    print("  - Ingles: ",c)
                else:
                    print("  - Ingles: ",p)
""" Para comprobar si efectivamente el idioma el frances volvemos a realizar otra prueba y de nuva cuenta
vuelve a ser el unico con un resultado con la palabra 'contraignant' por lo que ahora enlistaremos las letras
que conocemos
"""
#--------------------------La letras que conocemos hasta el momento son:
"""    
          w=e,  u=a,     a=c,   i=r,    o=l,    q=o,    x=t,    y=a,    p=i,    d=g
"""

"""Ahora mismo biscaremos las demas letras del frances mediante palabras"""

#Palabra iwfxw --------------------------
print("Palabra: iwfxw")
for p in dic_fr:
    if len(p) == 5:
        if p[0] == "r" and p[3] == "t":
            if p[1] == p[-1]:
                print("  - ",p)
""" f=s ya que 'n' tiene un valor ya asignado"""

#Palabra iwrwiw
print("Palabra: iwrwiw")
for p in dic_fr:
    if len(p) == 6:
        if p[0] == p[4] and p[1] == p[3]:
            if p[3] == p[-1] and p[0] == "r":
                print("  - ",p)

#Palabra flihyaw
print("Palabra: flihyaw")
for p in dic_fr:
    if len(p) == 7:
        if p[0] == "s" and p[2] == "r" and p[4] == "a" and p[5] == "c" and p[6] == "e":
            if p[0] == "s" or p[0] == "n":
                print("  - ",p)
"""Como tenemos una sola palabra como resultado entonces: l=u, h=f"""

#Palabra kqmwuuw
print("Palabra: kqmwuuw")
for p in dic_fr:
    if len(p) == 7:
        if p[1] == "o" and p[3] == p[-1] and p[-1] == "e":
            if p[4] == p[5] and p[5] == "n":
                print("  - ",p)
"""Como a = c entonces k = m """

#Palabra vlyiyuxypuw
print("Palabra: vlyiyuxypuw")
for p in dic_fr:
    if len(p) == 11:
        if p[1] == "u" and p[2] == p[4] and p[4] ==  "a" and p[3] == "r":
            if p[5] == p[9] and p[9] == "n":
                print("  - ",p)

#Palabra abyffwux
print("Palabra: abyffwux")
for p in dic_fr:
    if len(p) == 8:
        if p[0] == "c" and p[2] == "a" and p[3] == p[4] and p[4] == "s":
            if p[5] == "e" and p[6] == "n" and p[-1] == "t":
                print("  - ",p)

#Palabra cyua
print("Palabra: cyua")
for p in dic_fr:
    if len(p) == 4:
        if p[1] == "a" and p[2] == "n" and p[-1] == "c":
            print("  - ",p)

#Palabra jwkp
print("Palabra: jwkp")
for p in dic_fr:
    if len(p) == 4:
        if p[1] == "e" and p[2] == "m" and p[-1] == "i":
             print("  - ",p)

#Palabra diqlrwf
print("Palabra: diqlrwf")
for p in dic_fr:
    if len(p) == 7:
        if p[1] == "r" and p[2] == "o" and p[3] == "u" and p[4] == "p" and p[5] == "e" and p[-1] == "s" :
             print("  - ",p)

#Palabra spsiw
print("Palabra: spsiw")
for p in dic_fr:
    if len(p) == 5:
        if p[0] == p[2] and p[1] == "i" and p[3] == "r" and p[-1] == "e" :
             print("  - ",p)

#Palabra wzawoowuxw
print("Palabra: wzawoowuxw")
for p in dic_fr:
    if len(p) == 10:
        if p[0] == p[3] and p[3] == p[6] and p[6] == p[-1] and p[-1] == "e" :
            if p[2] == "c" and p[4] == p[5] and p[5] == "l" and p[7] == "n" and p[8] == "t":
             print("  - ",p)

#Palabra tlfvl'y
print("Palabra: tlfvl'y")
for p in dic_fr:
    if len(p) >= 6 and len(p) <= 7:
        if p[1] == p[4] and p[4] == "u" and p[2] == "s" and p[3] == "q" and p[-1] == "a" :
            print("  - ",p)

#Despues de buscar las letras podemos decir que quedan en este orden:
"""
    a=c     b=h     c=b     d=g     e=k*     f=s     g=w*     h=f     i=r     j=d     
    k=m     l=u     m=y     n=z*    o=l      p=i     q=o      r=p     s=v     t=j
    u=n     v=q     w=e     x=t     y=a      z=x

Donde * son letras que no aparecian por ende les asignamos otra letra que no se usa 
"""
#Ahora creamos una funcion para poder descifrar el primer texto
def descifrado_1(msg):   
    char_y="chbgkswfrdmuyzliopvjnqetax.:' "    
    char_x="abcdefghijklmnopqrstuvwxyz.:' " 
    msg_cifrado = ""
    for x in msg:
        for n in range(len(char_x)):
            if x == char_x[n]:
                msg_cifrado+=char_y[n]
    return msg_cifrado
msg = textos[0]
msg_cifrado = descifrado_1(msg)

#Imprimir el texto cifrado y descifrado
print("Mensaje cifrado:",msg[8:])
print("Mensaje descifrado:",msg_cifrado[8:])

#----------------------------------------------------------Texto 2----------------------------------------------------------

"""Ahora repetiremos los mismos pasos con el segundo texto"""
# Palabra nvxxhnn
print("Palabra: nvxxhnn")
c=0
for p in dic_it:
    if len(p) == 7:
        if p[0] == p[5] and p[5] == p[-1]:
            if p[2] == p[3]:
                c+=1
                if c == 0:
                    print("  - Italiano: ",c)
                else:
                    print("  - Italiano: ",p)
            
c=0
for p in dic_fr:
    if len(p) == 7:
        if p[0] == p[5] and p[5] == p[-1]:
            if p[2] == p[3]:
                c+=1
                if c == 0:
                    print("  - Frances: ",c)
                else:
                    print("  - Frances: ",p)


c=0
for p in dic_en:
    if len(p) == 7:
        if p[0] == p[5] and p[5] == p[-1]:
            if p[2] == p[3]:
                c+=1
                if c == 0:
                    print("  - Ingles: ",c)
                else:
                    print("  - Ingles: ",p)
""" Ya que solo el ingles tiene resultados que coincidan podemos decir que el segundo texto se encuentra en 
ese idioma (Ingles)"""

#Palabra phlpbh
print("Palabra: phlpbh")
for p in dic_en:
    if len(p) == 6:
        if p[1] == p[-1] and p[-1] == "e" and p[0] == p[3]:
            print("  - ",p)
""" No puede ser teethe ya que p[1] y p[2] se repiten, y tambien testae ya que sabemos que s = n"""

#Palabra rcppumhnn
print("Palabra: rcppumhnn")
for p in dic_en:
    if len(p) == 9:
        if p[2] == p[3] and p[6] == "e" and p[7] == p[-1] and p[-1] == "s":
            if p[3] == "a" or p[3] == "p":
                print("  - ",p)
"""Con lo anterior podemos inferir que p = p ya que no hay otra opcion al igual que m = n y u = i, c = a debido  que ya tenemos la 
letra 'e' e igualmente no se repite c para que pueda ser 'i' ademas de ser r = h por descarte ya que obtuvimos 's' anteriormente, y 
regresando al caso anterior l = o y b = l por ser people la unica opcion """

#Palabra srlvyrsn
print("Palabra: srlvyrsn")
for p in dic_en:
    if len(p) == 8:
        if p[0] == p[6] and p[1] == p[5] and p[5] == "h" and p[2] == "o":
            if p[3] == "u" and p[-1] == "s":
                print("  - ",p)
"""Teniendo una sola opcion para esta palabra podemos obtener que s = t, y = g"""

#Palabra palqvxs
print("Palabra: palqvxs")
for p in dic_en:
    if len(p) == 7:
        if p[0] == "p" and p[2] == "o" and p[4] == "u" and p[5] == "c" and p[6] == "t":
            print("  - ",p)
"""Al solo existir un resultado tenemos que a = r, y q = d"""

#Palabra frcs
print("Palabra: frcs")
for p in dic_en:
    if len(p) == 4:
        if p[1] == "h" and p[2] == "a" and p[-1] == "t":
            print("  - ",p)
"""Como ya tenemos 'c' y 't', ademas de que esta ultima se repite, podemos deducior que f = w """

#Palabra srhz
print("Palabra: srhz")
for p in dic_en:
    if len(p) == 4:
        if p[0] == "t" and p[1] == "h" and p[2] == "e":
            print("  - ",p)
"Al ya conocer a 'e' y 'n', 'z' solo podria ser 'm' o 'y'"

#Palabra dla
print("Palabra: dla")
for p in dic_en:
    if len(p) == 3:
        if p[1] == "o" and p[-1] == "r":
            print("  - ",p)
"""Con esto tenemos que d = f ya que 'n' fue asignado con anterioridad"""

#Palabra ghxlzhn
print("Palabra: ghxlzhn")
for p in dic_en:
    if len(p) == 7:
        if p[1] == p[5] and p[5] == "e" and p[2] == "c" and p[3] == "o" and p[-1] == "s":
            if p[4] == "m" or p[4] == "y":
             print("  - ",p)
"""Despues de obtener los resultamos podemos decir que z = m y g = b"""

#Palabra srumj
print("Palabra: srumj")
for p in dic_en:
    if len(p) == 5:
        if p[0] == "t" and p[1] == "h" and p[2] == "i" and p[3] == "n":
            print("  - ",p)
"""Al ya tener los valores de 'e', 'g' y 's' podemos inferir que j = k"""

#Palabra umkhms
print("Palabra: umkhms")
for p in dic_en:
    if len(p) == 6:
        if p[1] == p[4] and p[4] == "n" and p[0] == "i" and p[3] == "e" and p[-1] == "t":
            print("  - ",p)
"""Por descarte podemos decir que k = v"""

#Palabra umkhms
print("Palabra: umkhms")
for p in dic_en:
    if len(p) == 6:
        if p[0] == "i" and p[1] == p[4] == "n" and p[3] == "e" and p[-1] == "t":
            print("  - ",p)
#rcazlmt
print("Palabra: rcazlmt")
for p in dic_en:
    if len(p) == 7:
        if p[0] == "h" and p[1] == "a" and p[2] == "r" and p[3] == "m" and p[4] == "o" and p[5] == "n":
            print("  - ",p)
"""Por lo que t=y y esta es la ultima letra ya que las otras no aparecen en el texto"""
def descifrado_2(msg_2):   
    char_y="rlafjwbeqkvonsxpdhtyiuzcgm,.:' "    
    char_x="abcdefghijklmnopqrstuvwxyz,.:' " 
    msg_cifrado_2 = ""
    for x in msg_2:
        for n in range(len(char_x)):
            if x == char_x[n]:
                msg_cifrado_2+=char_y[n]
    return msg_cifrado_2
msg_2 = textos[2]
msg_cifrado_2 = descifrado_2(msg_2)
#Imprimiendo el mensaje cifrado y descifrado
print("Mensaje cifrado:",msg_2[8:])
print("Mensaje descifrado:",msg_cifrado_2[8:])

"""Finalmente imprimiremos los resultados despues de desciifrar ambos textos:"""
print("\nTexto 1:\n",msg_cifrado[8:],"\n")
print("Texto 2:\n",msg_cifrado_2[8:],"")