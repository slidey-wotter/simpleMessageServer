import sanic as Sanic
from src.event_manager import EventManager
from src.message_manager import MessageManager

# --- Controlador da Aplicação ---
class Router:
	"""
	Controlador que centraliza a configuração das rotas do Sanic.
	"""

	def setup_routes(app):
		@app.get('/<pathname:ext=css|js>')
		async def get_file(request, pathname, ext):
			return await Sanic.file('src/www/' + pathname + '.' + ext)

		@app.get('/')
		async def get_index(request):
			return await Sanic.file('src/www/index.html')

		@app.get('/feed')
		async def get_feed(request):
			# NOTA: isso devia retornar not-modified as vezes
			return Sanic.json(MessageManager.get_feed())

		@app.post('/send')
		async def receive_message(request):
			EventManager.notify('MessageEvent', request.json['text'])
			MessageManager.receive(request.json['text'])
			return Sanic.HTTPResponse()
