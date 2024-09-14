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

    def addProc(self, pID, prioridade, credito):
        proc = Proc(pID, prioridade, credito)
        self.processos.append(proc)
        self.processos = sorted(self.processos, key=lambda processos:processos.credito, reverse=False)

    def redistriCredito(self):
        tamanho = len(self.processos)
        temp = 0
        for i in range(tamanho):
            if self.processos[i].credito == 0:
                temp += 1
            else:
                break
        if temp == tamanho+1:
            for i in range(tamanho):
                self.processos[i].credito = self.processos[i].prioridade


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