from flask import request, jsonify, send_from_directory

# --- Controlador da Aplicação ---
class AppController:
    """
    Controlador que centraliza a configuração das rotas do Flask.
    Separa a lógica de configuração das rotas da lógica de negócios, promovendo modularização.
    """
    def setup_routes(app, event_manager):
        @app.route('/', methods=['GET'])
        def index():
            return send_from_directory('static', 'index.html')

        @app.route('/send', methods=['POST'])
        def send_message():
            # Extrai o JSON da requisição
            data = request.json
            message = data.get('message', '').strip()
            if not message:
                # Se a mensagem estiver vazia, dispara um evento de erro
                event_manager.notify("ErrorEvent", "Mensagem vazia enviada")
                return jsonify({"status": "Erro", "error": "Mensagem vazia"}), 400
            # Dispara o evento de mensagem com o conteúdo recebido
            event_manager.notify("MessageEvent", message)
            return jsonify({"status": "Mensagem processada", "message": message})
