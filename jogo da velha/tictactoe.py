#JOGO DA VELHA NO TERMINAL
#MEU PRIMEIRO PROJETO PYTHON

#PARA JOGAR, BASTA DIGITAR O NUMERO DO QUADRADO Q VOCE VAI JOGAR.

#0 | 1 | 2
#—————————
#3 | 4 | 5
#—————————
#6 | 7 | 8

#sua jogada(X): 4

#0 | 1 | 2
#—————————
#3 | X | 5
#—————————
#6 | 7 | 8

#sua jogada(O): 5

#0 | 1 | 2
#—————————
#3 | X | O
#—————————
#6 | 7 | 8

#sua jogada(X):
	
#divirta-se (ou tente se divertir)


class Jogo:
	def __init__(self):
		self.table = ["0","1","2",
		"3","4","5",
		"6","7","8"]
	#end
	
	def desenhar_o_tabuleiro(self):
		print(f"\n{self.table[0]} | {self.table[1]} | {self.table[2]}")
		print("—————————")
		print(f"{self.table[3]} | {self.table[4]} | {self.table[5]}")
		print("—————————")
		print(f"{self.table[6]} | {self.table[7]} | {self.table[8]}")
		
	#end
	
	
	
	def XO(self, num, opcao):
		
		self.table[num] = opcao
	#end
	
	def checkwin(self):
		if self.table[0] == self.table[1] == self.table[2]: # X X X
			   
			return True
		if self.table[3] == self.table[4] == self.table[5]: # 0 1 2
		       # X X X
		       # 6 7 8
			return True
		if self.table[6] == self.table[7] == self.table[8]: # 0 1 2
		       # 3 4 5
		       # X X X
			return True
		if self.table[0] == self.table[3] == self.table[6]: # X
		       # X
		       # X
			return True
		if self.table[1] == self.table[4] == self.table[7]: # 0 X 2
		       # 3 X 5
		       # 6 X 8
			return True
		if self.table[2] == self.table[5] == self.table[8]: # 0 1 X
		       # 3 4 X
		       # 6 7 X
			return True
		if self.table[3] == self.table[4] == self.table[5]: # 0 1 2
		       # X X X
		       # 6 7 8
			return True
		if self.table[6] == self.table[7] == self.table[8]: # 0 1 2
		       # 3 4 5
		       # X X X
			return True
		if self.table[0] == self.table[4] == self.table[8]:
			return True
		if self.table[2] == self.table[4] == self.table[6]:
			return True
		else:
			return False


	def ojogo(self):
		while True:
			
			self.desenhar_o_tabuleiro()
			if self.checkwin():
				print("temos um vencedor! Encerrando o jogo")
				break
			
			jogada = int(input(f"\nsua jogada(X): "))
			
			if(self.table[jogada] == "O"):
				print("Jogou errado, perdeu a vez")
			else:
				self.XO(jogada, "X")
			
			
			self.desenhar_o_tabuleiro()
			if self.checkwin():
				print("temos um vencedor! Encerrando o jogo")
				break
			
			jogada = int(input("\nsua jogada(O): "))
			
			if(self.table[jogada] == "X"):
				print("Jogou errado, perdeu a vez")
			else:
				self.XO(jogada, "O")
			
			
		#end
	#end
#end


jogo = Jogo()


jogo.ojogo()
