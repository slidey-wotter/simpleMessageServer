const Message = {
	addLogEntry: (message, type = 'message') => {
	    const logPanel = document.getElementById('logPanel');
	    const entry = document.createElement('div');
	    const now = new Date();
	    entry.className = 'log-entry ' + type;
	    entry.textContent = '[' + now.toLocaleTimeString() + '] ' + message;
	    logPanel.insertBefore(entry, logPanel.firstChild);
	},

	sendMessage: async () => {
	    const messageInput = document.getElementById('messageInput');
	    const responseDiv = document.getElementById('response');

	    try {
	        const response = await fetch('/send', {
	            method: 'POST',
	            headers: {
	                'Content-Type': 'application/json'
	            },
	            body: JSON.stringify({
	                message: messageInput.value
	            })
	        });

	        Message.addLogEntry('Mensagem enviada: "' + messageInput.value + '"', 'message');
	        messageInput.value = '';

	        const data = await response.json();
	        responseDiv.innerHTML =
	            '<p><strong>Status:</strong> ' + response.status + '</p>' +
	            '<p><strong>Resposta:</strong> ' + JSON.stringify(data, null, 2) + '</p>';

	        if (!response.ok) {
	            Message.addLogEntry('Erro: ' + data.error, 'error');
	        }
	    } catch (error) {
	        responseDiv.innerHTML = '<p style="color: red;">Erro: ' + error.message + '</p>';
	        Message.addLogEntry('Erro na requisição: ' + error.message, 'error');
	    }
	},

	sendEmptyMessage: () => {
		const messageInput = document.getElementById('messageInput');
		messageInput.value = '';
		Message.sendMessage();
	}
}

Object.freeze(Message); // Por segurança
