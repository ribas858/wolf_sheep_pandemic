from datetime import datetime
from wolf_sheep_pandemic.model import WolfSheepPandemic
from mesa import *
import pandas as pd
from datetime import datetime
import numpy as np



params = {"width": 20, "height": 20,
        "initial_sheep": 150,
        "initial_wolves": 100,
        "sheep_reproduce": np.arange(0, 1, 0.1),
        "wolf_reproduce": 0.05,
        "wolf_gain_from_food": 20,
        "grass": True,
        "grass_regrowth_time": range(20, 50, 5),
        "sheep_gain_from_food": 4,
        "predator_init_doente": range(1, 10, 1),
        "predator_imune": 0.05,
        "predator_imune_gene": np.arange(0, 1, 0.1)
    }

experimentos_por_paremtro = 2;
passos_max_por_simulacao = 150;

results = batch_run(
    WolfSheepPandemic,
    parameters=params,
    iterations= experimentos_por_paremtro,
    max_steps= passos_max_por_simulacao,
    number_processes=1,
    data_collection_period=-1,
    display_progress=True,
)

temp_now = datetime.now()
temp_now = str(temp_now.strftime('%d/%m/%Y %H:%M'))
for rep in ((":", "_"), (" ", "_"), (".", "_"), ("/", "_")):
    temp_now = temp_now.replace(*rep)

name_file = ("_it_" + str(experimentos_por_paremtro) +
            "_steps_" + str(passos_max_por_simulacao) +
            "_data_" + temp_now)

results_df = pd.DataFrame(results)


results_df.to_csv("wolfsheep_pandemic_model_data" + name_file + ".csv")