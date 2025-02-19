#!./.venv/bin/python3

from src.app import App

if __name__ == '__main__':
	# Inicia o servidor Flask em modo debug
	app = App()
	app.run(port=8080, debug=True)
