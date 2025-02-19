import time

class Message(dict):
	"""
	Estrutura de dados que armazena uma mensagem
	timestamp é determinado no momento de criação
	"""

	def __init__(self, text):
		dict.__init__(self, timestamp=time.time_ns(), text=text)