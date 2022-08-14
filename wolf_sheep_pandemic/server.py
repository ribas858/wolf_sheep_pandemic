import mesa

from wolf_sheep.agents import Wolf, Sheep, GrassPatch
from wolf_sheep.model import WolfSheep


def wolf_sheep_portrayal(agent):
    if agent is None:
        return

    portrayal = {}

    if type(agent) is Sheep:
        portrayal["Shape"] = "wolf_sheep/resources/sheep.png"
        # https://icons8.com/web-app/433/sheep
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 1

    elif type(agent) is Wolf:
        if agent.doente:
            portrayal["Shape"] = "wolf_sheep/resources/wolf_doente.png"
        else:
            if agent.imune:
                portrayal["Shape"] = "wolf_sheep/resources/wolf_imune.png"
            else:
                portrayal["Shape"] = "wolf_sheep/resources/wolf.png"
        # https://icons8.com/web-app/36821/German-Shepherd
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 2
        portrayal["text"] = round(agent.energy, 1)
        portrayal["text_color"] = "White"

    elif type(agent) is GrassPatch:
        if agent.fully_grown:
            portrayal["Color"] = ["#00FF00", "#00CC00", "#009900"]
        else:
            portrayal["Color"] = ["#84e184", "#adebad", "#d6f5d6"]
        portrayal["Shape"] = "rect"
        portrayal["Filled"] = "true"
        portrayal["Layer"] = 0
        portrayal["w"] = 1
        portrayal["h"] = 1

    return portrayal


canvas_element = mesa.visualization.CanvasGrid(wolf_sheep_portrayal, 20, 20, 500, 500)
chart_element = mesa.visualization.ChartModule(
    [
        {"Label": "Lobos Comuns", "Color": "black"},
        {"Label": "Ovelhas", "Color": "yellow"},
        {"Label": "Grama", "Color": "#00AA00"},
        {"Label": "Lobos Doentes", "Color": "#AA0000"}
    ]
)

imunes = mesa.visualization.ChartModule(
    [
        {"Label": "Lobos Imunes", "Color": "#1e12f3"},
    ]
)


model_params = {
    # The following line is an example to showcase StaticText.
    "title": mesa.visualization.StaticText("Parametros:"),
    "grass": mesa.visualization.Checkbox("Habilitar Grama", True),
    "grass_regrowth_time": mesa.visualization.Slider("Tempo de Revitalização da Grama", 20, 1, 50),
    "initial_sheep": mesa.visualization.Slider(
        "População Inicial de Ovelhas", 100, 10, 300
    ),
    "sheep_reproduce": mesa.visualization.Slider(
        "Taxa de Reprodução de Ovelhas", 0.04, 0.01, 1.0, 0.01
    ),
    "initial_wolves": mesa.visualization.Slider("População Inicial de Lobos", 50, 10, 300),
    "wolf_reproduce": mesa.visualization.Slider(
        "Taxa de Reprodução dos Lobos",
        0.05,
        0.01,
        1.0,
        0.01,
        description="The rate at which wolf agents reproduce.",
    ),
    "wolf_gain_from_food": mesa.visualization.Slider(
        "Energia Obtida pelos Lobos ao Devorar Ovelhas", 20, 1, 50
    ),
    "sheep_gain_from_food": mesa.visualization.Slider("Energia Obtida da Grama pelas Ovelhas", 4, 1, 10),
    "predator_imune": mesa.visualization.Slider("Chance do Predador ser Imune", 0.05, 0.01, 1.0, 0.01),
    "predator_imune_gene": mesa.visualization.Slider("Chance do Gene da Imunidade aos Filhos do Predador", 0.05, 0.01, 1.0, 0.01),
    "predator_init_doente": mesa.visualization.Slider("Número Inicial de Predadores Doentes", 1, 1, 100)
}

server = mesa.visualization.ModularServer(
    WolfSheep, [canvas_element, chart_element, imunes], "Wolf Sheep Pandemic", model_params
)
server.port = 8521
