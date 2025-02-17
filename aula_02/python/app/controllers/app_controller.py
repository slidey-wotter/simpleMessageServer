from flask import request, jsonify

class AppController:
    def __init__(self, app, event_manager):
        self.app = app
        self.event_manager = event_manager
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/', methods=['GET'])
        def index():
            return "Bem-vindo à aula de Programação Orientada a Objetos II e Flask!"

        @self.app.route('/send', methods=['POST'])
        def send_message():
            data = request.json
            message = data.get('message', '').strip()
            if not message:
                self.event_manager.notify("ErrorEvent", "Mensagem vazia enviada")
                return jsonify({"status": "Erro", "error": "Mensagem vazia"}), 400
            self.event_manager.notify("MessageEvent", message)
            return jsonify({"status": "Mensagem processada", "message": message})
