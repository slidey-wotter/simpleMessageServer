import sanic as Sanic
from src.event_manager import EventManager
from src.message_manager import MessageManager
from src.message import Message
import json

# --- Controlador da Aplicação ---
class Router:
	"""
	Controlador que centraliza a configuração das rotas do Sanic.
	"""

	clients = set()

	def setup_routes(app):
		@app.get('/<pathname:ext=css|js>')
		async def get_file(request: Sanic.Request, pathname, ext):
			return await Sanic.file('src/www/' + pathname + '.' + ext)

		@app.get('/')
		async def get_index(request: Sanic.Request):
			return await Sanic.file('src/www/index.html')

		@app.post('/send')
		async def receive_message_http(request: Sanic.Request):
			await receive_message(request.json['text'])
			return Sanic.HTTPResponse()
		
		@app.websocket('/feed')
		async def get_feed(request: Sanic.Request, socket: Sanic.Websocket):
			Router.clients.add(socket)
			await socket.send(json.dumps(MessageManager.get_feed()))
			while True:
				text = await socket.recv()
				await receive_message(text)
		
		async def receive_message(text):
			message = Message(text)
			EventManager.notify('MessageEvent', text)
			MessageManager.receive(message)
			mark_for_discard = set()
			for client in Router.clients:
				try:
					await client.send(json.dumps(message))
				except Exception as e:
					mark_for_discard.add(client)
			for client in mark_for_discard:
				Router.clients.discard(client)