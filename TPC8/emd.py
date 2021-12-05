
import matplotlib.pyplot as plt

def getEMD(linha):
    novalinha = linha.strip("\n")
    emd = []
    campos = novalinha.split(",")
    emd.append("emd" + str(int(campos[1])+1))
    for i in range (2, len(campos)):
        emd.append(campos[i])
    return emd

def lerDataset(fnome):
    f = open(fnome, encoding="utf-8")
    bd = []
    f.readline() #tirar cabeçalho
    for linha in f:
        emd = getEMD(linha)
        bd.append(emd)
    return bd


def chaveOrd1(exame):
    return exame[1]

def listarDataset(bd):
    bd.sort(key= chaveOrd1, reverse = True)
    data=[]
    data.append("id          data          nome        apto \n")
    data.append("____________________________________________ \n")
    for emd in bd:
        if emd[11] == "true":
            a = "sim"
        elif emd[11] == "false":
            a = "não"
        data.append(emd[0] + " | " + emd[1] + " | " + emd[3] + " " + emd[2] + " | " + a + "\n")
    return(data)


def consultarDataset(bd, id):
    i = 0
    while bd[i][0] != id:
        i = i+1
    return(bd[i])

def chaveOrd7(exame):
    return exame[7]

def modalidades(bd):
    modalidades = []
    for emd in bd:
        if emd[7] not in modalidades:
            modalidades.append(emd[7])
    bd.sort(key= chaveOrd7)
    return(modalidades)

def distribPorModalidade(bd):
    distribuicao = {}
    for emd in bd:
        if emd[7] in distribuicao.keys():
            distribuicao[emd[7]] = distribuicao[emd[7]] + 1
        else:
            distribuicao[emd[7]] = 1
    return distribuicao

def distribPorClube(bd):
    dclube = {}
    for emd in bd:
        if emd[8] in dclube.keys():
            dclube[emd[8]] = dclube[emd[8]] +1
        else:
            dclube[emd[8]] = 1
    return dclube

def printdic(d):
    nk=list(d.keys())
    nv=list(d.values())
    finallist=[]
    for i in range(len(d)):
         finallist.append( str(nk[i])  +"::" + str(nv[i]) + "\n")
    return finallist

def distribPorAno(bd):
    distribuicao = {}
    for emd in bd:
        ano=str(emd[1][0:4])
        print(ano)
        if ano in distribuicao.keys():
            distribuicao[ano] = distribuicao[ano] + 1
        else:
            distribuicao[ano] = 1
    return distribuicao

def plotdist(distri,x):
    xx=distri.keys()
    yy=distri.values()
    plt.bar(xx,yy)
    plt.xlabel(x)
    plt.ylabel("Nº Ocorrências")
    plt.show()


