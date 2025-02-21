class MessageManager:
  """
  Classe estática que armazena as mensagens mais recentes em um buffer circular
  """

  __buffer = []

  def receive(message):
    MessageManager.__buffer.append(message) # Adiciona ao final
    if len(MessageManager.__buffer) > 100:
      MessageManager.__buffer.pop(0) # Remove do início

  def get_feed():
    return MessageManager.__buffer