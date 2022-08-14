"""
Comportamento generalizado para caminhada aleatória, uma célula da grade de cada vez.
"""

import mesa


class RandomWalker(mesa.Agent):
    """
    Classe implementando métodos random walker de forma generalizada.

    Não se destina a ser usado sozinho, mas a herdar seus métodos para vários
    outros agentes.

    """

    grid = None
    x = None
    y = None
    moore = True

    def __init__(self, unique_id, pos, model, moore=True):
        """
        grid: O objeto MultiGrid no qual o agente reside.
        x: Coordenada x atual do agente.
        y: A coordenada y atual do agente.
        moore: Se True, pode se mover em todas as 8 direções.
                Caso contrário, apenas para cima, para baixo, para a esquerda, para a direita.
        """
        super().__init__(unique_id, model)
        self.pos = pos
        self.moore = moore

    def random_move(self):
        """
        Pise uma célula em qualquer direção permitida.
        """
        # Pick the next cell from the adjacent cells.
        next_moves = self.model.grid.get_neighborhood(self.pos, self.moore, True)
        next_move = self.random.choice(next_moves)
        # Now move:
        self.model.grid.move_agent(self, next_move)
