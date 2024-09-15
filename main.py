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
        self.over = False

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
# print(prioridades)

mem = []
for i in range(1,10):
      name = "0"+str(i)
      temp = openArq(name)
      mem.append(temp)
temp = openArq("10")
mem.append(temp)


tabelaPCB = tabelaProcessos.TabelaProc()
prontos = listas.ListaProntos()
for i in range(len(mem)):
      tabelaPCB.addProc(i, mem[i][0])
      mem[i] = mem[i][1:]
      prontos.addProc(i, prioridades[i], prioridades[i])
for i in mem:
    print(i)
# tabelaPCB.printProc()
prontos.printProntos()


while len(prontos.processos) != 0:
    tempPronto = prontos.pop()
    tempPCB = tabelaPCB.findID(tempPronto.pID)

    running = Rodando(tempPronto.pID, tempPronto.prioridade, tempPronto.credito, tempPCB.pc, tempPCB.X, tempPCB.Y)
    running.over = False

    running.credito -= 1
    for i in range(quantum):
        # print(mem[running.pID])
        instrucao = mem[running.pID][running.pc]
        if instrucao == "COM":
            pass
        elif instrucao == "E/S":
            pass
        elif instrucao == "SAIDA":
            tabelaPCB.removeProc(running.pID)
            running.over = True
            running.pc += 1
            running.printRodando()
            break
        elif instrucao[:2] == "X=":
            running.X = int(instrucao[2:])
        elif instrucao[:2] == "Y=":
            running.Y = int(instrucao[2:])

        running.pc += 1

    if running.over == False:
        prontos.addProc(running.pID, running.prioridade, running.credito)
        tempPCB.pc = running.pc; tempPCB.X = running.X; tempPCB.Y = running.Y
        tabelaPCB.atualizaProc(tempPCB)
        if len(prontos.processos) ==  prontos.zeros:
            prontos.redistriCredito()
            prontos.zeros = 0
    
    
