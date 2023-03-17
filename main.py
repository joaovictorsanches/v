import numpy as np

entradas = np.array([0, 1, 1, 0])
pesos = 0.1


class Neuronio:
	def __init__(self, input_x, input_y):
		self.test_list = lambda x: x if type(x) == list() else []
		self.entradas = np.array(self.test_list(input_x))
		self.pesos = np.array([input_y for i in self.entradas])
		self.ativado = None

	def run(self):
		ativacao = lambda som: True if ( som > 0 ) else False
		soma = self.entradas.dot(self.pesos)
		self.ativado = ativacao(soma)
		print('Neuronio: ', '\033[32mAtivado\033[m' if (self.ativado) else '\033[31mNão ativado\033[m')
neuronio = Neuronio(entradas, pesos)
neuronio.run()
