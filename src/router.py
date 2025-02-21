import json
from threading import Lock
import sanic as Sanic
from src.event_manager import EventManager
from src.message_manager import MessageManager
from src.message import Message

# --- Controlador da Aplicação ---
class Router:
	"""
	Controlador que centraliza a configuração das rotas do Sanic.
	"""

	__clients = set()
	__message_lock = Lock()

	def setup_routes(app):
		@app.get('/<pathname:ext=css|js>')
		async def get_file(request: Sanic.Request, pathname, ext):
			return await Sanic.file('src/www/' + pathname + '.' + ext)

		@app.get('/')
		async def get_index(request: Sanic.Request):
			return await Sanic.file('src/www/index.html')

		@app.post('/send') # esse método é deprecado
		async def receive_message_http(request: Sanic.Request):
			await receive_message(request.json['text'])
			return Sanic.HTTPResponse()
		
		@app.websocket('/feed')
		async def get_feed(request: Sanic.Request, socket: Sanic.Websocket):
			with Router.__message_lock:
				Router.__clients.add(socket)
			await socket.send(json.dumps(MessageManager.get_feed()))
			while True:
				text = await socket.recv()
				await receive_message(text)

		async def receive_message(text):
			with Router.__message_lock:
				message = Message(text)
				EventManager.notify('MessageEvent', text)
				MessageManager.receive(message)
				mark_for_discard = set()
				for client in Router.__clients:
					try:
						await client.send(json.dumps(message))
					except:
						mark_for_discard.add(client)
				for client in mark_for_discard:
					Router.__clients.discard(client)