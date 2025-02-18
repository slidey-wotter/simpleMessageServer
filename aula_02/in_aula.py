class Celular:
    def __init__(self, estrutura, tamanha_tela, cor):
        self.__estrutura = estrutura
        self.tamanha_tela = tamanha_tela
        self.cor = cor

    def altera_estrutura(self, estrutura):
        self.__estrutura = estrutura
        
class Iphone(Celular):
    def __init__(self, estrutura, tamanha_tela, cor, entrada_p_fone):
        super().__init__(estrutura, tamanha_tela, cor)
        self.entrada_fone = entrada_p_fone

iphone1 = Iphone(
    'quadrado', '7 pol', 'branco',
    entrada_p_fone=False
)

celular1 = Celular(
    estrutura='quadrada',
    tamanha_tela='6 pol',
    cor='vermelho',)


print(f'Celular 1: {celular1.cor}')
celular1.cor = 'Branco'
print(f'Celular 1: {celular1.cor}')
