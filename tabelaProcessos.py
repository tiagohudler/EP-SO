
class PCB:
    def __init__(self, pID, nome):
        self.pID = pID
        self.pc = 0
        self.estado = "Pronto"
        self.X = 0
        self.Y = 0
        self.nome = nome
    
    def printPCB(self):
        print(f"pID: {self.pID}, pc: {self.pc}, estado: {self.estado}, X: {self.X}, Y: {self.Y}, nome: {self.nome}")


class TabelaProc:
    listaPCB = []

    def addProc(self, pID, nome):
        pcb = PCB(pID, nome)
        self.listaPCB.append(pcb)

    def findID(self, pID):
        for i in range(len(self.listaPCB)):
            if self.listaPCB[i].pID == pID:
                return self.listaPCB[i]

    def printProc(self):
        for i in self.listaPCB:
            i.printPCB()

