from collections import deque

class MessageManager:
  """
  Classe estática que armazena as mensagens mais recentes em um buffer circular
  """

  __buffer = deque()

  def receive(message):
    MessageManager.__buffer.append(message) # Adiciona ao final
    if len(MessageManager.__buffer) > 100:
      MessageManager.__buffer.popleft() # Remove do início

  def get_feed():
    return MessageManager.__buffer
