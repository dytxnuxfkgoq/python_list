import random

"""list = []
for i in range(1,51):
    x = random.randint(0,100)
    list.append(x)
print(list)
print(list[:24])
print(list.count(0))

def alma_van_e():
    return "alma" in gyumolcsok

gyumolcsok = []
for x in range(5):
    gyum = input("gyümölcs")"""


tantargyak = ["angol","tesi","matek","tori","biosz"]
for i in tantargyak:
    print(i)

for index in range(len(tantargyak)):
    print(index, tantargyak[index])

for index,tantargy in enumerate(tantargyak):
    print(index)

tantargyak.sort() #tantargyak.sort(reverse=True)
print(tantargyak)

tantargyak.reverse() #csak megforditja
print(tantargyak)

x = tantargyak.count("matek")
print(x)

i = tantargyak.index("matek")
print("index =",i)

tantargyak.append("magyar")
print(tantargyak)

tantargyak.insert(0,"Hálózat")
print(tantargyak)

hobbi=['krunker','kódolás','hálózat','app inventor']
tantargyak.extend(hobbi)
print(tantargyak)
uj = hobbi.copy()
print(uj)
uj.pop(3)
print(uj)
uj.remove("kódolás")
print(uj)

import random


'''lista=[]
nevek=['Zoli','Kata','Olga','Jani','Laci','Dani']
jegyek=[2,1,4,3,5,2]
list=['Z0li',4,'Peti',6]
print(nevek)
print(','.join(nevek))
print(nevek[1:3])
print(nevek[3:])
print(nevek[:4])
print(nevek[-3])
print(nevek[-3:])

honapok=['jan','feb','mar','apr','may','june','july','august','september','october','november','december']
print(honapok[0:6])
print(honapok[9:])
print(honapok[5:8])
print(honapok[-1])


for i in range(20):
    x=random.randint(1,30)
    lista.append(x)
print(lista)

szamok=[]
for i in range(20):
    x=random.randint(1,50)
    szamok.append(x)
print(szamok)

szam = None
szamlista = []
while szam!=0:
    szam=int(input("Szám:"))
    if szam!=0:
        szamlista.append(szam)
print(szamlista)

szo=None
szolista=[]
while szo!="":
    szo=input("Szó:")
    if szo!="":
        szolista.append(szo)
print(szolista)
szolista[0]="hétfő"
print(szolista)

lista=["vasárnap","kedd","szerda","csütörtök"]
lista[1:3]="alma","körte"
print(lista)
lista.insert(1,'csirke')
print(lista)

list = []
felett = 0
alatt = 0
x = 0
for i in range(20):
    if x>50:
        felett+=1
    elif x<50:
        alatt+=1
    x=random.randint(1,100)
    list.append(x)
print(list)
print(felett,alatt)

dbfelett = 0
dbalatt = 0
szamos=[1,55,43,6,36,4]
for szam in szamos:
    if szam>50:
        dbfelett+=1
    else:
        dbalatt+=1
print(szamos)
print(dbfelett,dbalatt)'''

list = []
for i in range(50):
    if i%2==0:
        x = random.randint(50,100)
        list.append(x)
    elif i%2!=0:
        y = random.randint(1,51)
        list.append(y)
print(list)

"""feladat(1)
def kerulet(a,b,c):
    kerulet = a+b+c
    return kerulet
print(kerulet(7,9,4))

def terulet(a):
    return(a*a)
print(terulet(5))

def string(txt):
    return len(txt)

def negyzet(n):
    return (n**2)
print(negyzet(5))

def koszont():
    print("üdv a fedélzeten")
koszont()

def feladat(a):
    print()
    print(f"{a}. feladat:")
feladat(3)

def szamjegy(a):
    if 0 < szam < 10:
        return "egyszamjegyu"
    else:
        return "nem egyszamjegyu"

def negyzet(szam):
    return szam**2

def negyzet_elj(szam):
    print(szam**2)

def hossz(t):
    return len(t)

def paros(szam):
    if szam%2==0:
        return "páros"
    else:
        return "páratlan"

def feladat(i):
    print(f"{i}. feladat: ")

def szamok(szam1,szam2):
    if szam1>szam2:
        return szam1
    else:
        return szam2

feladat(1)
szam = 5
print(szam,szamjegy(szam))
print(szam,negyzet(szam))

feladat(2)
negyzet_elj(szam)
x=2*negyzet(szam)
print(x)
txt=input("szöveg:")
print(f"A szöveg hossza: {hossz(txt)}")

feladat(3)
print(szam,paros(szam))
for x in range(1,51):
    print(x,paros(x))

feladat(4)
szam1=int(input("Kérek egy számot:"))
szam2=int(input("Kérek egy másik számot"))
print(szamok(szam1,szam2))

szo1 = input("Kérek egy szót:")
szo2 = input("Kérek még egy szót:")
hossz = len(szo1)
hossz1 = len(szo2)
if hossz>hossz1:
    print(szo1)
else:
    print(szo2)

for i in range(1,11):
    print()
    for x in range(1,11):
        print(ix,end=" ")"""

import random
for i in range(1,6):
    def kerulet(a, b, c):
        if a + b > c and a + c > b and c + b > a:
            return "szerkeszthető"
        else:
            return "nem szerkeszthető"

        a = random.randint(1, 20)
        b = random.randint(1, 20)
        c = random.randint(1, 20)

        print("A", a, b, c, "oldalú háromszög", kerulet(a, b, c))
