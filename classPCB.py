class PCB:
	def __init__(self, pid, estado, prioridade, codigo, nome, pc, registradores	):
		self.pid = pid  # Identificador do processo
		self.estado = estado  # Estado do processo (Pronto, Executando, etc.)
		self.prioridade = prioridade  # Prioridade do processo
		self.tempo_cpu = 0  # Tempo de CPU utilizado em cada quantum
		self.codigo_programa = codigo  # Código do programa (lista de instruções)
		self.nome_programa = nome  # Nome do programa
		self.pc = pc  # Contador de Programa (PC)
		self.registradores = registradores if registradores else [0, 0]

	def executar(self, quantum):
		print("Exeutanto Teste-{pid}")
		for _ in range(quantum):
			instrucao = self.codigo[self.pc]

			if "=" in instrucao:
				self.processar_mov(instrucao)
			
			elif instrucao == "COM":
				self.processar_com()

			elif instrucao == "E/S":
				self.processar_es()
				self.pc += 1 #como há um break, é necessário incrementar o pc antes
				break

			elif instrucao == "SAIDA":
				self.processar_saida()
				self.pc += 1
				break

			self.pc += 1
			self.tempo_cpu +=1


	def processar_mov(self):
		registrador, valor = instrucao.split("=")
		valor = int(valor.strip())

		if registrador == "X":
			self.registradores[0] = valor  # Atribui o valor ao registrador X (índice 0)
		elif registrador == "Y":
			self.registradores[1] = valor  # Atribui o valor ao registrador Y (índice 1)


	def processar_com(self):
		#aqui deve escrever no log

	def processar_es(self):
		#escrever no log "Instrução {pid} bloquada após {self.tempo_cpu instruções}"
		self.estado = "Bloqueado"
		#mandar p fila de bloqueados

	def processar_saida(self):
		#escrever no log "Processo {pid} finalizado"
		self.estado = "Finalizado"

	def __str__(self):
        	return f"PCB(PID={self.pid}, Estado={self.estado}, Prioridade={self.prioridade}, TempoCPU={self.tempo_cpu}, PC={self.pc}, Registradores={self.registradores}, 	Nome={self.nome_programa})"	

		