"""
Wolf-Sheep - Pandemic 
================================
Lucas Jr. Ribas - UnB

Baseado no "Wolf Sheep Predation Model"

Replicação do modelo original "Wolf Sheep Predation" encontrado no NetLogo:
    Wilensky, U. (1997). NetLogo Wolf Sheep Predation model.
    http://ccl.northwestern.edu/netlogo/models/WolfSheepPredation.
    Center for Connected Learning and Computer-Based Modeling,
    Northwestern University, Evanston, IL.
"""

import mesa

from wolf_sheep_pandemic.scheduler import RandomActivationByTypeFiltered
from wolf_sheep_pandemic.agents import Sheep, Wolf, GrassPatch


class WolfSheep(mesa.Model):
    """
    Wolf-Sheep - Pandemic
    """

    height = 20
    width = 20

    initial_sheep = 100
    initial_wolves = 50

    sheep_reproduce = 0.04
    wolf_reproduce = 0.05

    wolf_gain_from_food = 20

    grass = False
    grass_regrowth_time = 30
    sheep_gain_from_food = 4

    predator_init_doente = 1
    predator_imune = 0.1
    predator_imune_gene = 0.1

    verbose = False  # Print-monitoring

    description = (
        "Um modelo para simular a modelagem de ecossistemas de lobos e ovelhas, frente a uma doença infecciosa."
    )

    def __init__(
        self,
        width=20,
        height=20,
        initial_sheep=100,
        initial_wolves=50,
        sheep_reproduce=0.04,
        wolf_reproduce=0.05,
        wolf_gain_from_food=20,
        grass=False,
        grass_regrowth_time=30,
        sheep_gain_from_food=4,
        predator_init_doente = 1,
        predator_imune = 0.1,
        predator_imune_gene = 0.1
    ):
        """
        Descrição dos parâmetros.

        Args:
            initial_sheep: Número de ovelhas para começar
            initial_wolves: Número de lobos para começar
            sheep_reproduce: Probabilidade de cada ovelha se reproduzir a cada passo
            wolf_reproduce: Probabilidade de cada lobo se reproduzir a cada passo
            wolf_gain_from_food: Energia que um lobo ganha ao comer uma ovelha
            grass: Se as ovelhas comem grama para obter energia. Ativa a grama.
            grass_regrowth_time: quanto tempo leva para um pedaço de grama crescer novamente
                        uma vez que é comido.
            sheep_gain_from_food: Ganho de energia pela ovelha da grama, se ativado.

            predator_init_doente: Número de predadores doentes ao início da simulação
            predator_imune: Chance do Predador ser Imune
            predator_imune_gene: Chance do Predador passar o gene da imunidade aos filhos
        """
        super().__init__()
        # Set parameters
        self.width = width
        self.height = height
        self.initial_sheep = initial_sheep
        self.initial_wolves = initial_wolves
        self.sheep_reproduce = sheep_reproduce
        self.wolf_reproduce = wolf_reproduce
        self.wolf_gain_from_food = wolf_gain_from_food
        self.grass = grass
        self.grass_regrowth_time = grass_regrowth_time
        self.sheep_gain_from_food = sheep_gain_from_food

        self.predator_init_doente = predator_init_doente
        self.predator_imune = predator_imune
        self.predator_imune_gene = predator_imune_gene

        self.schedule = RandomActivationByTypeFiltered(self)
        self.grid = mesa.space.MultiGrid(self.width, self.height, torus=True)
        self.datacollector = mesa.DataCollector(
            {
                "Lobos Comuns": lambda m: m.schedule.get_type_count(
                    Wolf, lambda x: not x.doente and not x.imune
                ),
                "Ovelhas": lambda m: m.schedule.get_type_count(Sheep),
                "Grama": lambda m: m.schedule.get_type_count(
                    GrassPatch, lambda x: x.fully_grown
                ),
                "Lobos Doentes": lambda m: m.schedule.get_type_count(
                    Wolf, lambda x: x.doente
                ),
                "Lobos Imunes": lambda m: m.schedule.get_type_count(
                    Wolf, lambda x: x.imune
                ),
            }
        )

        # Create sheep:
        for i in range(self.initial_sheep):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            energy = self.random.randrange(2 * self.sheep_gain_from_food)
            
            sheep = Sheep(self.next_id(), (x, y), self, True, energy)
            self.grid.place_agent(sheep, (x, y))
            self.schedule.add(sheep)

        # Create wolves
        for i in range(self.initial_wolves):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)

            energy = self.random.randrange(2 * self.wolf_gain_from_food)

            if i < self.predator_init_doente:
                wolf = Wolf(self.next_id(), (x, y), self, True, energy, True, False)
            else:
                if self.random.random() < self.predator_imune:
                    wolf = Wolf(self.next_id(), (x, y), self, True, energy, False, True)
                else:
                    wolf = Wolf(self.next_id(), (x, y), self, True, energy, False, False)

            self.grid.place_agent(wolf, (x, y))
            self.schedule.add(wolf)

        # Create grass patches
        if self.grass:
            for agent, x, y in self.grid.coord_iter():

                fully_grown = self.random.choice([True, False])

                if fully_grown:
                    countdown = self.grass_regrowth_time
                else:
                    countdown = self.random.randrange(self.grass_regrowth_time)

                patch = GrassPatch(self.next_id(), (x, y), self, fully_grown, countdown)
                self.grid.place_agent(patch, (x, y))
                self.schedule.add(patch)

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        self.schedule.step()
        # collect data
        self.datacollector.collect(self)
        if self.verbose:
            print(
                [
                    self.schedule.time,
                    self.schedule.get_type_count(Wolf),
                    self.schedule.get_type_count(Sheep),
                    self.schedule.get_type_count(GrassPatch, lambda x: x.fully_grown),
                ]
            )

    def run_model(self, step_count=200):

        if self.verbose:
            print("Initial number wolves: ", self.schedule.get_type_count(Wolf))
            print("Initial number sheep: ", self.schedule.get_type_count(Sheep))
            print(
                "Initial number grass: ",
                self.schedule.get_type_count(GrassPatch, lambda x: x.fully_grown),
            )

        for i in range(step_count):
            self.step()

        if self.verbose:
            print("")
            print("Final number wolves: ", self.schedule.get_type_count(Wolf))
            print("Final number sheep: ", self.schedule.get_type_count(Sheep))
            print(
                "Final number grass: ",
                self.schedule.get_type_count(GrassPatch, lambda x: x.fully_grown),
            )
