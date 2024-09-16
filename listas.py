class Processo:
    def __init__(self, pID, prioridade, credito):
        self.pID = pID
        self.prioridade = prioridade
        self.credito = credito

    def printProc(self):
        print(f"pID: {self.pID}, prioridade: {self.prioridade}, credito: {self.credito}")
    
    def setCredito(self, credito):
        self.credito = credito


class ListaProntos:
    def __init__(self):
        self.listaProcessos = []
        self.zeros = 0

    def addProc(self, pID, prioridade, credito):
        proc = Processo(pID, prioridade, credito)
        self.listaProcessos.append(proc)
        self.listaProcessos = sorted(self.listaProcessos, key=lambda listaProcessos:listaProcessos.credito, reverse=False)
        if credito == 0:
            self.zeros += 1

    def redistriCredito(self):
        tamanho = len(self.listaProcessos)
        
        for i in range(tamanho):
            self.listaProcessos[i].credito = self.listaProcessos[i].prioridade
        
        self.listaProcessos = sorted(self.listaProcessos, key=lambda listaProcessos:listaProcessos.credito, reverse=False)


    def printProntos(self):
        for i in self.listaProcessos:
            i.printProc()

    def pop(self):
        return self.listaProcessos.pop()

class ListaBloqueados:
    def __init__(self):
        self.wait3 = None
        self.wait2 = None
        self.wait1 = None

    def addProc(self, pID, prioridade, credito):
        proc = Processo(pID, prioridade, credito)
        self.wait3 = proc

    def moveProc(self):
        
        pronto = self.wait1
        self.wait1 = None
        
        self.wait1 = self.wait2
        self.wait2 = None
        
        self.wait2 = self.wait3
        self.wait3 = None
        
        return pronto