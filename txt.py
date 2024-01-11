from osztaly import osztaly
def feladat():
    f=open("stadionok.txt","r",encoding="utf-8")
    f.readline()
    f_sorok_lista=f.readline()
    f.close()
    osztaly.lista=[]
    for i in range(0,len(f_sorok_lista),1):
        aktelem=f_sorok_lista[i]
        sor_lista=aktelem.strip().split("!")
        osztalyom=osztaly(int(sor_lista[0]),int(sor_lista[1]))
        osztaly.lista.append(osztalyom)
        return osztalyom   
        







