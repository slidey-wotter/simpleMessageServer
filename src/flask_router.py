from flask import request, jsonify, send_from_directory
from src.event_manager import EventManager

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
			print('stub!')
			return jsonify([
				{"timestamp": 1739985287065979421, "text": "mensagem1"},
				{"timestamp": 1739985376845628687, "text": "mensagem2"}
			])

		@app.post('/send')
		def receive_message():
			print('stub!')
			EventManager.notify('MessageEvent', request.json['message'])
			return ''
