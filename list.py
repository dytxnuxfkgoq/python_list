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