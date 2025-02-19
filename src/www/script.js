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

		await fetch('/send', {
			method: "POST",
			headers: {
				'content-type': 'application/json'
			},
			body: JSON.stringify({'text': text})
		})
	},

	requestFeed: async () => {
		if (Message.feed_response != undefined && !Message.feed_response) {
			return // Somente iremos requisitar se houve resposta
		}

		Message.feed_response = false

		const response = await fetch('/feed')

		Message.feed_response = true
		
		if (!response.ok) {
			return
		}

		const data = await response.json()
		const messageFeed = document.getElementById('messageFeed')

		Message.buildFeed(messageFeed, data)
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

Message.requestFeed()
setInterval(Message.requestFeed, 500)
// Essa não é a forma correta de se fazer isso, mas é a mais simples
