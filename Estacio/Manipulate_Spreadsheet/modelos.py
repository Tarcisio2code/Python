class Variavel:

    def __init__(self, posicao_inicial, tamanho, codigo, descricao):
        # Modificado
        #self.posicao_inicial = posicao_inicial
        self.posicao_inicial = int(posicao_inicial) - 1
        #self.tamanho = tamanho
        self.tamanho = int(tamanho)
        self.codigo = codigo
        self.descricao = descricao
        # Alterado tipo da variavel categoria de lista para dicionaro
        # self.categoria = []
        self.categoria = {}

    def add_categoria(self, categoria):
        # categoria = dict {'categoria_tipo': tipo, 'categoria_descricao_tipo': descricao}
        # Alteração na variável categoria, a chave virá da coluna tipo e os valoes da coluna descrição
        self.categoria[categoria.get('categoria_tipo')] = categoria.get('categoria_descricao_tipo')

    def __str__(self):
        # Alteração para utilizar o fString
        #return self.codigo + " - " + self.descricao
        return f'{self.codigo} - {self.descricao}'
