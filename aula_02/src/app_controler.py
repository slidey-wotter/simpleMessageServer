from flask import request, jsonify, send_from_directory

# --- Controlador da Aplicação ---
class AppController:
    """
    Controlador que centraliza a configuração das rotas do Flask.
    Separa a lógica de configuração das rotas da lógica de negócios, promovendo modularização.
    """
    def __init__(self, app, event_manager):
        self.app = app
        self.event_manager = event_manager
        self.setup_routes()  # Configura as rotas assim que a instância é criada

    def setup_routes(self):
        @self.app.route('/', methods=['GET'])
        def index():
            return send_from_directory('src/static', 'index.html')

        @self.app.route('/send', methods=['POST'])
        def send_message():
            # Extrai o JSON da requisição
            data = request.json
            message = data.get('message', '').strip()
            if not message:
                # Se a mensagem estiver vazia, dispara um evento de erro
                self.event_manager.notify("ErrorEvent", "Mensagem vazia enviada")
                return jsonify({"status": "Erro", "error": "Mensagem vazia"}), 400
            # Dispara o evento de mensagem com o conteúdo recebido
            self.event_manager.notify("MessageEvent", message)
            return jsonify({"status": "Mensagem processada", "message": message})
        