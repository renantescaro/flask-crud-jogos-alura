from entidades.jogoEntidade import Jogo

class JogoModal:
    def __init__(self):
        self.listaJogos = [Jogo(1, 'Super Mario', 'Ação', 'SNES'),Jogo(2, 'Pokemon Gold', 'RPG', 'GBA'),Jogo(3, 'Dark Souls', 'RPG', 'PC'),]

    def getTodos(self):
        return self.listaJogos

    def apagarPorId(self, id):
        jogo = self.getPorId(id)
        self.listaJogos.remove(jogo)

    def getPorId(self, id_jogo):
        for jogo in self.listaJogos:
            if int(jogo.id) == int(id_jogo):
                return jogo

    def salvar(self, jogo):
        if jogo.id == 0:
            return self.inserir(jogo)
        return self.atualizar(jogo)
            

    def inserir(self, jogo):
        self.listaJogos.append(jogo)
        return True

    def atualizar(self, jogo):
        self.apagarPorId(jogo.id)
        self.inserir(jogo)
        return True