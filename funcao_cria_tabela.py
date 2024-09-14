def criar_tabela():
	tabela = []
	prioridades = ler_prioridades("programas/prioridades.txt") #criou um array com as prioridades de cada processo

	for pid in range(1, 10):
		codigo = ler_processo(f"programas/processo0{pid}.txt")
		prioridade = prioridades[pid-1] #como pid começa em 1 e o array em 0

		pc_inicial = 0
		registradores_iniciais = [0, 0] #X e Y de uso geral

		processo = PCB(pid, "Pronto", prioridade, codigo, f"Programa{pid}", pc_inicial, registradores_iniciais)
		tabela.append(processo)

	with open("programas/quantum.txt", 'r') as arquivo:
		quantum = int(arquivo.read().strip())

	return tabela_de_processos, quantum
