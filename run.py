from src.app import create_app

if __name__ == '__main__':
    # Inicia o servidor Flask em modo debug
    app = create_app()
    app.run(debug=True)
