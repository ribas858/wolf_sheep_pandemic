from typing import Type, Callable

import mesa


class RandomActivationByTypeFiltered(mesa.time.RandomActivationByType):
    """
    Um agendador que substitui o método get_type_count para permitir a filtragem
    de agentes por uma função antes de contar.

    Exemplo:
    >>> scheduler = RandomActivationByTypeFiltered(model)
    >>> scheduler.get_type_count(AgentA, lambda agent: agent.some_attribute > 10)
    """

    def get_type_count(
        self,
        type_class: Type[mesa.Agent],
        filter_func: Callable[[mesa.Agent], bool] = None,
        
    ) -> int:
        """
        Retorna o número atual de agentes de determinado tipo na fila que atendem à função de filtro.
        """
        count = 0
        for agent in self.agents_by_type[type_class].values():
            if filter_func is None or filter_func(agent):
                count += 1
        return count
