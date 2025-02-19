from flask import request, send_from_directory
from src.event_manager import EventManager
from src.message_manager import MessageManager

# --- Controlador da Aplicação ---
class FlaskRouter:
	"""
	Controlador que centraliza a configuração das rotas do Flask.
	Separa a lógica de configuração das rotas da lógica de negócios, promovendo modularização.
	"""
	def setup_routes(app):
		@app.get('/<path:pathname>.css')
		def get_style(pathname):
			return send_from_directory('www', pathname + '.css')

		@app.get('/<path:pathname>.js')
		def get_script(pathname):
			return send_from_directory('www', pathname + '.js')

		@app.get('/')
		def get_index():
			return send_from_directory('www', 'index.html')

		@app.get('/feed')
		def get_feed():
			# NOTA: isso devia retornar not-modified as vezes
			return MessageManager.get_feed_as_json()

		@app.post('/send')
		def receive_message():
			EventManager.notify('MessageEvent', request.json['text'])
			MessageManager.receive(request.json['text'])
			return ''
