# Wolf-Sheep - Pandemic

Com base em um modelo ecológico simples, composto por três tipos de agentes: lobos, ovelhas e capim. Os lobos e as ovelhas vagam aleatoriamente pela grade. Lobos e ovelhas gastam energia se movendo e a repõem comendo. As ovelhas comem grama e os lobos comem ovelhas caso as encontrem na mesma célula da grade. Se lobos e ovelhas tiverem energia suficiente, eles se reproduzem, criando um novo lobo ou ovelha (neste modelo simplificado, apenas um dos pais é necessário para a reprodução). A grama em cada célula cresce a uma taxa constante. Se algum lobo e ovelha ficar sem energia, eles morrem.

Diante disso foi implantado uma doença contagiosa em um determinado número de Lobos (definido pelo usuário na interface). Enquanto os lobos vagam pela grade em busca de ovelhas, eles podem se deparar com algum lobo infectado, contraindo a doença caso não seja imune.

A partir do momento que um lobo está infectado ele não consegue mais se alimentar e nem se reproduzir, e eventualmente morrerá. Mas antes disso todos os lobos saudáveis que esse predador entrar em contato, ficarão doentes. Além disso, a infecção ocorre não apenas se o outro lobo estiver na mesma célula, mas também se ele estiver na área de uma célula de alcance, ou seja, em qualquer célula ao redor de onde se encontra o predador infectado.  Entretanto existe uma
exceção, a probabilidade de existir predadores imunes, os mesmos não irão contrair a doença mesmo se entrarem em contato com um lobo doente.

Os lobos imunes no momento de sua reprodução, tem chance de passar ou não o gene da imunidade para seus filhos, assim, se o lobo filho não herdar o gene, a probabilidade da população de lobos se extinguir completamente, será maior. As ovelhas, em contrapartida, não são afetadas pela doença e se comportam normalmente.

**Código final na branch** ``main``

## Sumário
- **Alterações no Código**
- **Hipótese Causal**
- **Instalação**
- **Como Executar**
- **Arquivos**
- **Leitura adicional**

O modelo é testado e demonstra vários conceitos e recursos do Mesa:
 - MultiGrid
 - Vários tipos de agentes (lobos, ovelhas, grama)
 - Sobreponha texto arbitrário (energia do lobo) nas formas do agente enquanto desenha no CanvasGrid
 - Agentes que herdam um comportamento (movimento aleatório) de um pai abstrato
 - Escrevendo um modelo composto por vários arquivos.
 - Adicionando e removendo dinamicamente agentes da agenda

## Alterações no Código


### ``wolf_sheep/model.py``

#### **Novas variáveis:**
**predator_init_doente:** Número de predadores doentes ao início da simulação.

**predator_imune:** Chance do Predador ser Imune.

**predator_imune_gene:** Chance do Predador passar o gene da imunidade aos filhos.

#### **Alterações:**

No estágio de criação inicial dos lobos, o código foi alterado para receber um determinado número de lobos doentes. Durante o "``for i in range(self.initial_wolves):``" é imposto uma condição para que parte desses lobos sejam doentes. Além disso, de acordo com a probabilidade de surgir um lobo imune, parte desses predadores serão imunes.

No ``self.datacollector`` foi alterado o idioma das labels, para Português-Brasil. E também foi inserido duas novas labels, "Lobos Doentes", e "Lobos Imunes", aliás a label "Lobos" (Wolves) passou para "Lobos Comuns", que são os lobos não imunes.

### ``wolf_sheep/agents.py``

#### **Novos métodos:**
**``def contamina():``** Contamina um lobo, se ele não for imune.

**``def area_lobos():``** Define a área de alcance de um lobo infectado. Alcance de 1 célula, em 360 graus.

**``def print_thiscell():``** Exibe no terminal os agentes (Lobo, Ovelha, Grama) ao alcance do lobo infectado. Lobos comuns são o alvo.

#### **Alterações:**
No início do ``def step():`` é feita uma checagem se o predador está doente, se sim ele executa o método ``def area_lobos():`` para ver se existe algum lobo em sua célula na grade, ou ao redor. Se existir 1 ou mais lobos ao alcance, então é escolhido aleatoriamente um lobo, e depois chamado o método ``def contamina():``, que irá contaminar o lobo se ele não for imune.

No momento do lobo se alimentar, é feita uma checagem ``if not self.doente:`` para que apenas lobos saudáveis possam comer. Além disso é feito o mesmo processo no momento da reprodução, lobos doentes não se reproduzem.

Caso o lobo seja imune, é seguido uma probabilidade do gene da imunidade para a reprodução desse lobo. Se for atendido, o filho desse lobo também será imune.

## Hipótese Causal

No momento em que o predador for contaminado, ele se manterá em um estado contagioso, ou seja, irá transmitir a doença para qualquer outro predador vulnerável. Caso um possível gene imune não predomine sobre a população, a espécie de predadores eventualmente será extinta.

Diante disso a população da Presa irá crescer consideravelmente, pois seu predador não existe mais no ecossistema, contudo levando a uma falta de recursos, no caso, a grama. Quando a presa não puder mais se alimentar, a mesma será extinta.
	
Concluindo, uma doença infecciosa implantada sobre o predador leva à extinção dos três agentes do ecossistema em questão.

## Installation

To install the dependencies use pip and the requirements.txt in this directory. e.g.

```
    # First, we clone the Mesa repo
    $ git clone https://github.com/projectmesa/mesa.git
    $ cd mesa
    # Then we cd to the example directory
    $ cd examples/wolf_sheep
    $ pip install -r requirements.txt
```

## How to Run

To run the model interactively, run ``mesa runserver`` in this directory. e.g.

```
    $ mesa runserver
```

Then open your browser to [http://127.0.0.1:8521/](http://127.0.0.1:8521/) and press Reset, then Run.

## Files

* ``wolf_sheep/random_walk.py``: This defines the ``RandomWalker`` agent, which implements the behavior of moving randomly across a grid, one cell at a time. Both the Wolf and Sheep agents will inherit from it.
* ``wolf_sheep/test_random_walk.py``: Defines a simple model and a text-only visualization intended to make sure the RandomWalk class was working as expected. This doesn't actually model anything, but serves as an ad-hoc unit test. To run it, ``cd`` into the ``wolf_sheep`` directory and run ``python test_random_walk.py``. You'll see a series of ASCII grids, one per model step, with each cell showing a count of the number of agents in it.
* ``wolf_sheep/agents.py``: Defines the Wolf, Sheep, and GrassPatch agent classes.
* ``wolf_sheep/scheduler.py``: Defines a custom variant on the RandomActivationByType scheduler, where we can define filters for the `get_type_count` function.
* ``wolf_sheep/model.py``: Defines the Wolf-Sheep Predation model itself
* ``wolf_sheep/server.py``: Sets up the interactive visualization server
* ``run.py``: Launches a model visualization server.

## Further Reading

This model is closely based on the NetLogo Wolf-Sheep Predation Model:

Wilensky, U. (1997). NetLogo Wolf Sheep Predation model. http://ccl.northwestern.edu/netlogo/models/WolfSheepPredation. Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.

See also the [Lotka–Volterra equations
](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations) for an example of a classic differential-equation model with similar dynamics.
