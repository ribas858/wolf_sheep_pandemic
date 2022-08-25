import mesa
from wolf_sheep_pandemic.random_walk import RandomWalker


class Sheep(RandomWalker):
    """
    Uma ovelha que anda, se reproduz (assexuadamente) e é comida.

    O init é o mesmo do RandomWalker.
    """

    energy = None

    def __init__(self, unique_id, pos, model, moore, energy=None):
        super().__init__(unique_id, pos, model, moore=moore)
        self.energy = energy

    def step(self):
        """
        Um passo de modelo. Mova-se, depois coma grama e se reproduza.
        """
        self.random_move()
        living = True

        if self.model.grass:
            # Reduce energy
            self.energy -= 1

            # If there is grass available, eat it
            this_cell = self.model.grid.get_cell_list_contents([self.pos])
            grass_patch = [obj for obj in this_cell if isinstance(obj, GrassPatch)][0]
            if grass_patch.fully_grown:
                self.energy += self.model.sheep_gain_from_food
                grass_patch.fully_grown = False

            # Death
            if self.energy < 0:
                self.model.grid.remove_agent(self)
                self.model.schedule.remove(self)
                living = False

        if living and self.random.random() < self.model.sheep_reproduce:
            # Create a new sheep:
            if self.model.grass:
                self.energy /= 2
            lamb = Sheep(
                self.model.next_id(), self.pos, self.model, self.moore, self.energy
            )
            self.model.grid.place_agent(lamb, self.pos)
            self.model.schedule.add(lamb)


class Wolf(RandomWalker):
    """
    Um lobo que anda, se reproduz (assexuadamente) e come ovelhas. Caso doente, infecta outros lobos.
    """

    energy = None
    doente = None
    imune = None

    def __init__(self, unique_id, pos, model, moore, energy=None, doente=None, imune=None):
        super().__init__(unique_id, pos, model, moore=moore)
        self.energy = energy
        self.doente = doente
        self.imune = imune

    def step(self):
        self.random_move()

        if self.doente:
                this_cell = self.model.grid.get_cell_list_contents([self.pos])
                pos_x = self.pos[0]
                pos_y = self.pos[1]

                this_cell += self.area_lobos(self.pos, this_cell)

                # self.print_thiscell(this_cell) # Exibe a lista de lobos na area de alcance do lobo infectado.

                wolfs = [obj for obj in this_cell if isinstance(obj, Wolf) and not obj.doente ]
                
                if len(wolfs) > 0:
                    wolf_contamina = self.random.choice(wolfs)
                    if not wolf_contamina.doente:
                        wolf_contamina.contamina()
            
        self.energy -= 1

        # Se o Lobo não estiver doente, e a ovelha estiver presente, coma a ovelha
        if not self.doente:
            x, y = self.pos
            this_cell = self.model.grid.get_cell_list_contents([self.pos])
            sheep = [obj for obj in this_cell if isinstance(obj, Sheep)]
            if len(sheep) > 0:
                sheep_to_eat = self.random.choice(sheep)
                self.energy += self.model.wolf_gain_from_food
                # Mata a Ovelha
                self.model.grid.remove_agent(sheep_to_eat)
                self.model.schedule.remove(sheep_to_eat)

        # Morte ou Reprodução
        if self.energy < 0:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
        
        else:
            if self.random.random() < self.model.wolf_reproduce and not self.doente:
                # Create a new wolf cub
                self.energy /= 2

                cub = Wolf(
                    self.model.next_id(), self.pos, self.model, self.moore, self.energy
                )

                if self.imune:
                    if self.random.random() < self.model.predator_imune_gene:
                        cub.imune = True
                
                self.model.grid.place_agent(cub, cub.pos)
                self.model.schedule.add(cub)
    
    def contamina(self):
        if not self.imune:
            self.doente = True


    def area_lobos(self, pos, this_cell):
        pos_x = pos[0]
        pos_y = pos[1]
        w = self.model.width-1
        h = self.model.height-1

        # Centro
        if pos_x < w and pos_y < h and pos_x > 0 and pos_y > 0:
            this_cell += self.model.grid.get_cell_list_contents([(pos_x+1, pos_y)])
            this_cell += self.model.grid.get_cell_list_contents([(pos_x-1, pos_y)])
            this_cell += self.model.grid.get_cell_list_contents([(pos_x+1, pos_y+1)])
            this_cell += self.model.grid.get_cell_list_contents([(pos_x, pos_y+1)])
            this_cell += self.model.grid.get_cell_list_contents([(pos_x-1, pos_y+1)])
            this_cell += self.model.grid.get_cell_list_contents([(pos_x+1, pos_y-1)])
            this_cell += self.model.grid.get_cell_list_contents([(pos_x, pos_y-1)])
            this_cell += self.model.grid.get_cell_list_contents([(pos_x-1, pos_y-1)])
            return this_cell
        else:
            # Quina 0
            if pos_x == 0 and pos_y == 0:
                this_cell += self.model.grid.get_cell_list_contents([(pos_x+1, pos_y)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x+1, pos_y+1)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x, pos_y+1)])
                return this_cell
            
            # Quina x
            if pos_x == w and pos_y == 0:
                this_cell += self.model.grid.get_cell_list_contents([(pos_x-1, pos_y)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x-1, pos_y+1)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x, pos_y+1)])
                return this_cell

            # Quina y
            if pos_x == 0 and pos_y == h:
                this_cell += self.model.grid.get_cell_list_contents([(pos_x+1, pos_y)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x+1, pos_y-1)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x, pos_y-1)])
                return this_cell
            
            # Quina x_y
            if pos_x == w and pos_y == h:
                this_cell += self.model.grid.get_cell_list_contents([(pos_x-1, pos_y)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x-1, pos_y-1)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x, pos_y-1)])
                return this_cell
            
            # Meio x
            if pos_x > 0 and pos_x < w and pos_y == 0:
                this_cell += self.model.grid.get_cell_list_contents([(pos_x-1, pos_y)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x-1, pos_y+1)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x, pos_y+1)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x+1, pos_y+1)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x+1, pos_y)])
                return this_cell
            
            # Meio y
            if pos_y > 0 and pos_y < h and pos_x == 0:
                this_cell += self.model.grid.get_cell_list_contents([(pos_x, pos_y+1)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x+1, pos_y+1)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x+1, pos_y)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x+1, pos_y-1)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x, pos_y-1)])
                return this_cell

            # Meio yh
            if pos_x > 0 and pos_x < w and pos_y == h:
                this_cell += self.model.grid.get_cell_list_contents([(pos_x+1, pos_y)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x+1, pos_y-1)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x, pos_y-1)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x-1, pos_y-1)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x-1, pos_y)])
                return this_cell
            
            # Meio xw
            if pos_y > 0 and pos_y < h and pos_x == w:
                this_cell += self.model.grid.get_cell_list_contents([(pos_x, pos_y+1)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x-1, pos_y+1)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x-1, pos_y)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x-1, pos_y-1)])
                this_cell += self.model.grid.get_cell_list_contents([(pos_x, pos_y-1)])
                return this_cell

    def print_thiscell(self, this_cell):
        print ("============== Nesta Area:")
        print ("[", end="")
        for x in this_cell:
            if isinstance(x, Wolf):
                if x.doente:
                    print('\033[47m'+'\033[1m'+'\033[31m'+ " Lb. Doente," +'\033[0;0m', end="")
                else:
                    if x.imune:
                        print('\033[47m'+'\033[1m'+'\033[34m'+ " Lobo Imune," +'\033[0;0m', end="")
                    else:
                        print('\033[47m'+'\033[1m'+'\033[32m'+ " Lobo Comun Saudavel," +'\033[0;0m', end="")
            if isinstance(x, Sheep):
                print(" Ovelha,", end="")
            if isinstance(x, GrassPatch):
                print(" Grama,", end="")
        print ("]")
        print ("==============\n")

class GrassPatch(mesa.Agent):
    """
    Um pedaço de grama que cresce a uma taxa fixa e é comido por ovelhas.
    """

    def __init__(self, unique_id, pos, model, fully_grown, countdown):
        """
        Cria um novo pedaço de grama

        Args:   
            grown: (boolean) Se o pedaço de grama está totalmente crescido ou não.
            countdown: Tempo para o pedaço de grama crescer totalmente, novamente.
        """
        super().__init__(unique_id, model)
        self.fully_grown = fully_grown
        self.countdown = countdown
        self.pos = pos

    def step(self):
        if not self.fully_grown:
            if self.countdown <= 0:
                # Set as fully grown
                self.fully_grown = True
                self.countdown = self.model.grass_regrowth_time
            else:
                self.countdown -= 1
