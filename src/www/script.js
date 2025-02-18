function addLogEntry(message, type = 'message') {
    const logPanel = document.getElementById('eventLog');
    const entry = document.createElement('div');
    entry.className = `log-entry ${type}`;
    entry.textContent = `[${new Date().toLocaleTimeString()}] ${message}`;
    logPanel.insertBefore(entry, logPanel.firstChild);
}

async function sendMessage() {
    const messageInput = document.getElementById('message');
    const responseDiv = document.getElementById('response');
    
    try {
        const response = await fetch('/send', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: messageInput.value,
                funcao: 'enviarMensagem'
            })
        });
        
        const data = await response.json();
        responseDiv.innerHTML = `
            <p><strong>Status:</strong> ${response.ok ? 'Sucesso' : 'Erro'}</p>
            <p><strong>Resposta:</strong> ${JSON.stringify(data, null, 2)}</p>
        `;
        
        addLogEntry(`Mensagem enviada: ${messageInput.value}`, 'message');
        
        if (response.ok) {
            messageInput.value = '';
        } else {
            addLogEntry(`Erro: ${data.error}`, 'error');
        }
    } catch (error) {
        responseDiv.innerHTML = `<p style="color: red;">Erro: ${error.message}</p>`;
        addLogEntry(`Erro na requisição: ${error.message}`, 'error');
    }
}

function sendEmptyMessage() {
    document.getElementById('message').value = '';
    sendMessage();
}
