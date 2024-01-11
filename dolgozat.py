import random


def feladat1():
    szam:int=int(input("Kérek egy páros számot:"))
    while not (szam % 2 ==0):
        beker:int=input("Ez nem páros! Páros számot kérek: ")
    print(szam)




def paros():
    szam:int=int(input("Kérem az 1. páros szmot:"))
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




Lista=[]
def feladat2():
    for i in range(0,13,1):
        lista=random.random(-40,150)




        
