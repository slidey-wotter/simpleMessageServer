const Message = {
	sendMessage: async event => {
		event.preventDefault() // Evita refrescar a página

		const messageInput = document.getElementById('messageInput')

		if (!messageInput.value) {
			alert('mensagem vazia!')
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
		if (!response.ok) {
			return
		}

		Message.feed_response = true

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
