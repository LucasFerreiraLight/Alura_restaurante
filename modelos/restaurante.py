from modelos.avaliacao import Avaliacao

class Restaurante:
    '''Representa um restaurante e suas características'''
    restaurantes = []
    _avaliacao = []

    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False #_ativo significa que é um atributo protegido
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    

    """Retorna uma representação em string do restaurante."""
    def __str__(self): # self é a referencia do objeto que está chamando!
        return f'{self.nome} | {self.categoria} | {self.ativo}'


    """Exibe uma lista formatada de todos os restaurantes."""
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo}')


    '''Alterar o estado'''
    def alternar_estado(self):
        self._ativo = not self._ativo

    
    
    '''Mudar a propriedade da string, para mostrar o emogi'''
    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'
    
    
    
    '''Adicionar a avaliação a lista'''
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    
    """Calcula e retorna a média das avaliações do restaurante."""
    @property #Com essa annotion, nós somos capazes de ler essas
    def media_avaliacoes(self):
        if not self._avaliacao: 
            return '-'
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media