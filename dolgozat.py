import random


def feladat1():
    szam:int=int(input("Kérek egy páros számot:"))
    while not (szam % 2 ==0):
        beker:int=input("Ez nem páros! Páros számot kérek: ")
    print(szam)




def paros():
    szam:int=int(input("Kérem az 1. páros számot:"))
    while not (szam % 2 ==0):
        print(szam)

    szam2:int=int(input("Kérem a 2. páros számot:"))
    while not (szam2 % 2==0):
        beker:int=input("Ez nem páros! Páros számot kérek:")
    print(szam2)

    szam3:int=int(input("Kérem a harmadik számot:"))
    while not szam3 % 2==0:
        print("Ez nem páros! Páros számot kérek")
    print(szam3)    
    return szam,szam2,szam3




def feladat2():
    lista=[]
    for i in range(0,13,1):
        szam:int=random.randint(-40,150)
        lista.append(szam)
    return lista   


def ketjegyuek_szama(listam):
    ketjegyuek=0
    for i in range(0,len(listam),1):
        if list[i]<= (-10) or listam[i]<=10:
            ketjegyuek_szama+=1
        i+=1


 
 
 
def paros_osszeg(listam):
    paros_szamok:int=0
    for i in range(0,len(listam),1):
        if listam[i]>1:
            paros_szamok+=listam[i]
    print(f"Pozitív számok összege:{paros_szamok}")
    return paros_osszeg





def paratlan_osszege(listam):
    paratlan_osszege:int=0
    for i in range(0,len(listam),1):
        if listam[i]%2:
            paratlan_osszege+=1
    print(f"A paratlan számok összeg: {paratlan_osszege}")
    return paratlan_osszege        






    
        


 


