function addLogEntry(message, type = 'message') {
    const logPanel = document.getElementById('logPanel');
    const entry = document.createElement('div');
    const now = new Date();
    entry.className = 'log-entry ' + type;
    entry.textContent = '[' + now.toLocaleTimeString() + '] ' + message;
    logPanel.insertBefore(entry, logPanel.firstChild);
}

async function sendMessage(message) {
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

        addLogEntry('Mensagem enviada: ' + messageInput.value, 'message');
        messageInput.value = '';

        const data = await response.json();
        responseDiv.innerHTML =
            '<p><strong>Status:</strong> ' + response.status + '</p>' +
            '<p><strong>Resposta:</strong> ' + JSON.stringify(data, null, 2) + '</p>';

        if (!response.ok) {
            addLogEntry('Erro: ' + data.error, 'error');
        }
    } catch (error) {
        responseDiv.innerHTML = '<p style="color: red;">Erro: ' + error.message + '</p>';
        addLogEntry('Erro na requisição: ' + error.message, 'error');
    }
}

function sendEmptyMessage() {
	const messageInput = document.getElementById('messageInput');
	messageInput.value = '';
	sendMessage();
}
