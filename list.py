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
print(lista)'''

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
print(dbfelett,dbalatt)