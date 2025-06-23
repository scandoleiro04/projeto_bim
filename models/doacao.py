class Doacao:
    def __init__(self, id, restauranteId, alimento, quantidade, perecivel):
        self.id = id
        self.restauranteId = restauranteId
        self.alimento = alimento
        self.quantidade = quantidade
        self.perecivel = perecivel
        self.ongId = None
