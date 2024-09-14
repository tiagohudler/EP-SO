import tabelaProcessos
import listas

quantum = open("./programas/quantum.txt", "r")
quantum = int(quantum.readline())

class Rodando:
    def __init__(self, pID, prioridade, credito, pc, X, Y):
        self.pID = pID
        self.prioridade = prioridade
        self.credito = credito
        self.pc = pc
        self.estado = "Executando"
        self.X = X
        self.Y = Y

    def printRodando(self):
        print(f"pID: {self.pID}, prioridade: {self.prioridade}, credito: {self.credito}, pc: {self.pc}, estado: {self.estado}, X: {self.X}, Y: {self.Y}")

def openArq(fileName: str):
    file = open(f"./programas/{fileName}.txt")
    arqLines = []
    for line in file:
            arqLines.append(line[:-1])
    return arqLines

def getPrioridade():
    file = open(f"./programas/prioridades.txt")
    arqLines = []
    for line in file:
            arqLines.append(int(line[:-1]))
    return arqLines

def execucao():
      pass

prioridades = getPrioridade()
print(prioridades)

mem = []
for i in range(1,10):
      name = "0"+str(i)
      temp = openArq(name)
      mem.append(temp)
temp = openArq("10")
mem.append(temp)
# print(mem)

tabelaPCB = tabelaProcessos.TabelaProc()
prontos = listas.ListaProntos()
for i in range(len(mem)):
      tabelaPCB.addProc(i, mem[i][0])
      prontos.addProc(i, prioridades[i], prioridades[i])

# tabelaPCB.printProc()
# prontos.printProntos()

tempPronto = prontos.pop()
tempPCB = tabelaPCB.findID(tempPronto.pID)

running = Rodando(tempPronto.pID, tempPronto.prioridade, tempPronto.credito, tempPCB.pc, tempPCB.X, tempPCB.Y)
running.printRodando()
