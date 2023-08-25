class Loja:
    def __init__(self, nome, comissao_por_entrega):
        self.nome = nome
        self.comissao_por_entrega = comissao_por_entrega

    def __str__(self):
        return f"{self.nome}"

    def __repr__(self):
        return self.__str__()


class Pedido:
    def __init__(self, nome, valor, loja):
        self.nome = nome
        self.valor = valor
        self.loja = loja

    def __str__(self):
        return f"Pedido R$ {self.valor:.2f}"

    def __repr__(self):
        return self.__str__()


class Motoboy:
    def __init__(self, nome, valor_fixo, exclusividade):
        self.nome = nome
        self.valor_fixo = valor_fixo
        self.exclusividade = exclusividade
        self.pedidos = []

    def calcular_comissao(self):
        return sum(
            [
                pedido.loja.comissao_por_entrega * pedido.valor
                for pedido in self.pedidos
            ]
        ) + (self.valor_fixo * len(self.pedidos))

    def __str__(self):
        return f"{self.nome}"

    def __repr__(self):
        return self.__str__()
