import json
from src.message import Message

class MessageManager:
  """
  Classe estática que armazena as mensagens mais recentes em um buffer circular
  """

  __buffer = []

  def receive(text):
    MessageManager.__buffer.append(Message(text)) # Adiciona ao final
    if len(MessageManager.__buffer) > 20:
      MessageManager.__buffer.pop(0) # Remove do início

  def get_feed():
    return MessageManager.__buffer