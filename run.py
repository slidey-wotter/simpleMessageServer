#!./.venv/bin/python3

from sanic import Sanic
from src.app import App

sanic = Sanic(__name__)
App.setup(sanic)

if __name__ == '__main__':
	# Inicia o servidor Sanic em modo debug
	sanic.run(host='0.0.0.0', port=8080, debug=True)