class Proc:
    def __init__(self, pID, prioridade, credito):
        self.pID = pID
        self.prioridade = prioridade
        self.credito = credito

    def printProc(self):
        print(f"pID: {self.pID}, prioridade: {self.prioridade}, credito: {self.credito}")
    
    def setCredito(self, credito):
        self.credito= credito


class ListaProntos:
    def __init__(self):
        self.processos = []
        self.zeros = 0

    def addProc(self, pID, prioridade, credito):
        proc = Proc(pID, prioridade, credito)
        self.processos.append(proc)
        self.processos = sorted(self.processos, key=lambda processos:processos.credito, reverse=False)
        if credito == 0:
            self.zeros += 1

    def redistriCredito(self):
        tamanho = len(self.processos)
        
        for i in range(tamanho):
            self.processos[i].credito = self.processos[i].prioridade
        
        self.processos = sorted(self.processos, key=lambda processos:processos.credito, reverse=False)


    def printProntos(self):
        for i in self.processos:
            i.printProc()

    def pop(self):
        return self.processos.pop()

class ListaBloqueado:
    def __init__(self):
        self.processos = []

    def addProc(self, pID, prioridade, credito):
        proc = Proc(pID, prioridade, credito)
        self.processos.append(proc)
        self.processos = sorted(self.processos, key=lambda processos:processos.credito, reverse=False)