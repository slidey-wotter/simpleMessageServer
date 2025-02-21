let web_socket = {}
const create_socket = () => {
	web_socket = new WebSocket('ws://' + document.location.host + '/feed')
	// web_socket.onopen = event => console.log("WebSocket open: ", event)
	web_socket.onclose = event => create_socket()
	web_socket.onerror = event => console.log("WebSocket error: ", event)
	web_socket.onmessage = event => {
		const message = JSON.parse(event.data)
		console.log("Message: ", message)
		const messageFeed = document.getElementById('messageFeed')
		// NOTA: isso é irresponsável e a resposta devia ter um campo chamado "type"
		if (message.text && message.timestamp) {
			messageFeed.appendChild(Message.buildMessage(message))
		} else {
			Message.buildFeed(messageFeed, message)
		}
	}
}

create_socket()

const Message = {
	sendMessage: async event => {
		event.preventDefault() // Evita refrescar a página

		const messageInput = document.getElementById('messageInput')

		if (!messageInput.value) {
			alert('mensagem vazia!')
			return
		}

		if (messageInput.value.length >= 50) {
			alert('somente mensagens de até 50 caracteres são aceitas')
			return
		}

		const text = messageInput.value
		messageInput.value = ''

		web_socket.send(text)
	},

	buildFeed: (element, data) => {
		element.replaceChildren()
		for(const message of data) {
			element.appendChild(Message.buildMessage(message))
		}
	},

	buildMessage: message => {
		const p = document.createElement('p')
		p.textContent = '[' + (new Date(message.timestamp / 1000000)).toLocaleTimeString() + ']: ' + message.text
		return p
	}
}