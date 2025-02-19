# --- Observadores (Observers) ---

from time import gmtime, strftime
# O uso de strftime é para usar UTC (Coordinated Universal Time) ao invés do tempo local da máquina
# Com máquinas no mundo todo, UTC é preferido

class Logger:
    """
    Observador que registra (log) os dados recebidos.
    Demonstra o padrão Observer: reage a notificações de eventos.
    """
    def __init__(self, pathname):
      self.__logfile = open(file=pathname, mode='a', encoding='utf-8')

    def __del__(self):
      self.__logfile.close()

    def log(self, data):
      self.__logfile.write(strftime("[%Y/%m/%d %H:%M:%S]: " + data + "\n", gmtime()))
      self.__logfile.flush() # Força o arquivo a ser escrito

    def message(self, data):
      self.log('[M] ' + data)

    def error(self, data):
      self.log('[E] ' + data)
