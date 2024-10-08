import tabelaProcessos
import listas

# classe Rodando que guarda/exeecuta o processo
class Rodando:
    def __init__(self, pID, prioridade, credito, pc, X, Y):
        self.pID = pID
        self.prioridade = prioridade
        self.credito = credito
        self.pc = pc
        self.estado = "Pronto"
        self.X = X
        self.Y = Y
        self.over = False

    def printRodando(self):
        print(f"pID: {self.pID}, prioridade: {self.prioridade}, credito: {self.credito}, pc: {self.pc}, estado: {self.estado}, X: {self.X}, Y: {self.Y}")

# pega o valor do quantum definido em um arquivo
def getQuantum(path: str):
    quantum = open(path, "r")
    quantum = int(quantum.readline())
    return quantum

# pega os valores das prioridades de um arquivo txt em que a sua posicao de indice indica o arquivo que ele se refere
def getPrioridade(path: str):
    file = open(path)
    arqLines = []
    for line in file:
            arqLines.append(int(line[:-1]))
    return arqLines

# abre um arquivo e retorna suas linhas em uum array
def openArq(dirPath: str, fileName: str):
    file = open(f"{dirPath}/{fileName}.txt")
    arqLines = []
    for line in file:
            arqLines.append(line[:-1])
    return arqLines

# retorna a memoria(array) as instrucoes carregadas dos arquivos(nomeados de 01 a N)
def loadMem(numArq: int, dirPath: str):
    mem = []
    for i in range(1, numArq+1):
        if i < 10:
            name = "0"+str(i)
            temp = openArq(dirPath, name)
            mem.append(temp)
        else:
            temp = openArq(dirPath, str(i))
            mem.append(temp)
    return mem

def execucao():
      pass

quantum = getQuantum("./programas/quantum.txt")
prioridades = getPrioridade("./programas/prioridades.txt")
mem = loadMem(10, "./programas")
log = open("log.txt", "w", encoding="UTF-8")

tabelaPCB = tabelaProcessos.TabelaProc()
prontos = listas.ListaProntos()
bloqueados = listas.ListaBloqueados()

for i in range(len(mem)):
      tabelaPCB.addProc(i, mem[i][0])
      mem[i] = mem[i][1:]
      prontos.addProc(i, prioridades[i], prioridades[i])

for i in mem:
    print(i)
print("\n Prontos inicial:\n")
prontos.printProntos()

instrucoesTotais = 0
trocasTotais = -1 #pois o primeiro processo escalonado não é considerado como troca
procAnterior = "inicializado"

while len(prontos.listaProcessos) != 0 or bloqueados.wait1 != None or bloqueados.wait2 != None:
    if len(prontos.listaProcessos) == 0:
        novoPronto = bloqueados.moveProc()
        if novoPronto != None:
            prontos.addProc(novoPronto.pID, novoPronto.prioridade, novoPronto.credito)
            desbloqueadoPCB = tabelaPCB.findID(novoPronto.pID)
            desbloqueadoPCB.estado = "Pronto"
            tabelaPCB.atualizaProc(desbloqueadoPCB)
        continue
    tempPronto = prontos.pop()
    tempPCB = tabelaPCB.findID(tempPronto.pID)

    running = Rodando(tempPronto.pID, tempPronto.prioridade, tempPronto.credito, tempPCB.pc, tempPCB.X, tempPCB.Y)
    running.over = False

    log.write(f"Processo {tempPCB.nome} executando\n")

    if procAnterior != tempPCB.nome:
        trocasTotais += 1 #será 0 no primeiro loop

    if running.credito != 0:
        running.credito -= 1

    instructionCounter = 0
    for i in range(quantum):
        instrucoesTotais += 1
        instructionCounter += 1
        instrucao = mem[running.pID][running.pc]

        if instrucao == "COM":
            pass
        elif instrucao == "E/S":
            running.pc += 1
            running.estado = "Bloqueado"
            break
        elif instrucao == "SAIDA":
            tabelaPCB.removeProc(running.pID)
            running.over = True
            log.write("-----------------------------------\n")
            log.write(f"Processo {tempPCB.nome} finalizado\nX = {running.X}\nY = {running.Y}\n")
            log.write("-----------------------------------\n")
            break
        elif instrucao[:2] == "X=":
            running.X = int(instrucao[2:])
        elif instrucao[:2] == "Y=":
            running.Y = int(instrucao[2:])

        running.pc += 1

    procAnterior = tempPCB.nome

    if running.over == False:
        log.write(f"Interrompendo processo {tempPCB.nome} após {instructionCounter} instruções\n")

        if  running.estado == "Pronto":   
            prontos.addProc(running.pID, running.prioridade, running.credito)
        if running.estado == "Bloqueado":
            bloqueados.addProc(running.pID, running.prioridade, running.credito)
        tempPCB.pc = running.pc; tempPCB.X = running.X; tempPCB.Y = running.Y; tempPCB.estado = running.estado
        tabelaPCB.atualizaProc(tempPCB)
        
        # Processo desbloqueado
        novoPronto = bloqueados.moveProc()
        if novoPronto != None:
            prontos.addProc(novoPronto.pID, novoPronto.prioridade, novoPronto.credito)
            desbloqueadoPCB = tabelaPCB.findID(novoPronto.pID)
            desbloqueadoPCB.estado = "Pronto"
            tabelaPCB.atualizaProc(desbloqueadoPCB)

        if len(prontos.listaProcessos) == prontos.zeros and bloqueados.wait1 != None and bloqueados.wait2 != None:
            prontos.redistriCredito()
            prontos.zeros = 0


mediaTrocas = trocasTotais/10
log.write(f"Média de trocas por processo: {mediaTrocas}\n")

mediaInstrucoes = instrucoesTotais/trocasTotais
log.write(f"Média de instruções por processo: {mediaInstrucoes:.2f}\n")

log.write(f"quantum: {quantum}\n")

eff = mediaInstrucoes/quantum
log.write(f"eficiência: {eff:.2f}\n")


    
    
