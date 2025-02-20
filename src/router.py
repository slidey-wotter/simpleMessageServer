import sanic as Sanic
import asyncio as AsyncIO
from src.event_manager import EventManager
from src.message_manager import MessageManager

# --- Controlador da Aplicação ---
class Router:
	"""
	Controlador que centraliza a configuração das rotas do Sanic.
	"""

	subscribers = set()

	def setup_routes(app):
		@app.get('/<pathname:ext=css|js>')
		async def get_file(request, pathname, ext):
			return await Sanic.file('src/www/' + pathname + '.' + ext)

		@app.get('/')
		async def get_index(request):
			return await Sanic.file('src/www/index.html')

		@app.post('/send')
		def receive_message(request):
			EventManager.notify('MessageEvent', request.json['text'])
			MessageManager.receive(request.json['text'])
			return Sanic.HTTPResponse()
		
		@app.websocket('/feed')
		async def get_feed(request, websocket):
			Router.subscribers.add(websocket)
			while True:
				try:
					async with AsyncIO.timeout(60):
						message = await websocket.recv()
				except AsyncIO.TimeoutError:
					Router.subscribers.discard(request.remote_addr)
					websocket.close()