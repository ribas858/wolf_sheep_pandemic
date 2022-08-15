<!--
Wolf-Sheep - Pandemic 
================================
Lucas Jr. Ribas - UnB

Baseado no "Wolf Sheep Predation Model"
-->

# Wolf-Sheep - Pandemic

##### *Código final na branch* ***``main``***

Com base em um modelo ecológico simples, e composto por três tipos de agentes: lobos, ovelhas e grama. Os lobos e as ovelhas vagam aleatoriamente pela grade. Lobos e ovelhas gastam energia se movendo, e a repõem comendo. As ovelhas comem grama e os lobos comem ovelhas, caso às encontrem na mesma célula da grade. Se lobos e ovelhas tiverem energia suficiente, eles se reproduzem, criando um novo lobo ou ovelha (neste modelo simplificado, apenas um dos pais é necessário para a reprodução). A grama em cada célula cresce a uma taxa constante. Se algum lobo e ovelha ficar sem energia, eles morrem.

Diante disso foi implantado uma doença contagiosa em um determinado número de Lobos (definido pelo usuário na interface). Enquanto os lobos vagam pela grade em busca de ovelhas, eles podem se deparar com algum lobo infectado, contraindo a doença caso não seja imune.

A partir do momento que um lobo está infectado ele não consegue mais se alimentar, e nem se reproduzir, e eventualmente morrerá. Mas antes disso todos os lobos saudáveis que esse predador entrar em contato, ficarão doentes. Além disso, a infecção ocorre não apenas se o outro lobo estiver na mesma célula, mas também se ele estiver na área de uma célula de alcance, ou seja, em qualquer célula ao redor de onde se encontra o predador infectado. Entretanto existe uma
exceção, a probabilidade de existir predadores imunes, os mesmos não irão contrair a doença mesmo se entrarem em contato com um lobo doente.

Os lobos imunes no momento de sua reprodução, tem chance de passar ou não o gene da imunidade para seus filhos, assim, se o lobo filho não herdar o gene, a probabilidade da população de lobos se extinguir completamente, será maior. As ovelhas, em contrapartida, não são afetadas pela doença e se comportam normalmente.

O modelo é testado, e demonstra vários conceitos e recursos do Mesa:
 - MultiGrid
 - Vários tipos de agentes (lobos, ovelhas, grama)
 - Sobreponha texto arbitrário (energia do lobo) nas formas do agente enquanto desenha no CanvasGrid
 - Agentes que herdam um comportamento (movimento aleatório) de um pai abstrato
 - Escrevendo um modelo composto por vários arquivos.
 - Adicionando e removendo dinamicamente agentes da agenda

## Sumário
- **Alterações no Código**
- **Hipótese Causal**
- **Instalação**
- **Como Executar**
- **Arquivos**
- **Observações**
- **Leitura Adicional**

## Alterações no Código

### ``wolf_sheep_pandemic/model.py``

#### **Novas variáveis:**
**predator_init_doente:** Número de predadores doentes ao início da simulação.

**predator_imune:** Chance do Predador ser Imune.

**predator_imune_gene:** Chance do Predador passar o gene da imunidade aos filhos.

#### **Alterações:**

No estágio de criação inicial dos lobos, o código foi alterado para receber um determinado número de lobos doentes. Durante o "``for i in range(self.initial_wolves):``" é imposto uma condição para que parte desses lobos sejam doentes. Além disso, de acordo com a probabilidade de surgir um lobo imune, parte desses predadores serão imunes.

No ``self.datacollector`` foi alterado o idioma das labels, para Português-Brasil. E também foi inserido duas novas labels, "Lobos Doentes", e "Lobos Imunes", aliás a label "Lobos" (Wolves) passou para "Lobos Comuns", que são os lobos não imunes.

### ``wolf_sheep_pandemic/agents.py``

#### **Novos métodos:**
**``def contamina():``** Contamina um lobo, se ele não for imune.

**``def area_lobos():``** Define a área de alcance de um lobo infectado. Alcance de 1 célula, em 360 graus.

**``def print_thiscell():``** Exibe no terminal os agentes (Lobo, Ovelha, Grama) ao alcance do lobo infectado. Lobos comuns são o alvo.

#### **Alterações:**
No início do ``def step():`` é feita uma checagem se o predador está doente, se sim ele executa o método ``def area_lobos():`` para ver se existe algum lobo em sua célula na grade, ou ao redor. Se existir 1 ou mais lobos ao alcance, então é escolhido aleatoriamente um lobo, e depois chamado o método ``def contamina():``, que irá contaminar o lobo se ele não for imune.

No momento do lobo se alimentar, é feita uma checagem ``if not self.doente:`` para que apenas lobos saudáveis possam comer. Além disso é feito o mesmo processo no momento da reprodução, lobos doentes não se reproduzem.

Caso o lobo seja imune, é seguido uma probabilidade do gene da imunidade para a reprodução desse lobo. Se for atendido, o filho desse lobo também será imune.

### ``wolf_sheep_pandemic/server.py``

#### **Novas imagens:**

- Nova ovelha.
- Lobo Vermelho: Lobo Doente.
- Lobo Cinza: Lobo Saudável.
- Lobo Azul: Lobo Imune.

#### **Alterações:**

Adicionado a interface, o controle das 3 novas variáveis:
- predator_init_doente
- predator_imune
- predator_imune_gene

Adicionado uma nova varável ao gráfico existente:
- Lobos Doentes

Adicionado um novo gráfico, com a variável:
- Lobos Imunes

## Hipótese Causal

No momento em que o predador for contaminado, ele se manterá em um estado contagioso, ou seja, irá transmitir a doença para qualquer outro predador vulnerável. Caso um possível gene imune não predomine sobre a população, a espécie de predadores eventualmente será extinta.

Diante disso a população da Presa irá crescer consideravelmente, pois seu predador não existe mais no ecossistema, assim levando a uma falta de recursos, no caso, a grama. Então quando a presa não puder mais se alimentar, a mesma será extinta.

Quando o lobo e a ovelha não mais habitarem esse ecossistema, a grama eventualmente irá se regenerar.
	
Concluindo, uma doença infecciosa implantada sobre o predador leva à extinção de dois agentes do ecossistema, o lobo e a ovelha.

## Instalação

Para instalar as dependências, use o pip e o requirements.txt neste diretório. Por exemplo:

```
    # Primeiro, clonamos o repositório Mesa.
    $ git clone https://github.com/projectmesa/mesa.git
    # Depois clone este repositório.
    $ git clone https://github.com/ribas858/wolf_sheep_pandemic
    # Então dê um `cd` para o diretório Wolf-Sheep Pandemic.
    $ cd wolf_sheep_pandemic
    $ pip install -r requirements.txt
```

## Como Executar

Para executar o modelo interativamente, execute ``python3 run.py`` ou ``mesa runserver``  neste diretório. 

Por exemplo:

```
    $ python3 run.py
```

```
    $ mesa runserver
```

Em seguida, abra seu navegador para [http://127.0.0.1:8521/](http://127.0.0.1:8521/) e pressione Redefinir e, em seguida, Executar.

## Arquivos

* ``wolf_sheep_pandemic/random_walk.py``: Define o ``RandomWalker`` agente, que implementa o comportamento de se mover aleatoriamente em uma grade, uma célula por vez.Ambos os agentes Wolf e Sheep herdarão dele.
* ``wolf_sheep_pandemic/test_random_walk.py``: Define um modelo simples e uma visualização somente de texto destinada a garantir que a classe RandomWalk esteja funcionando conforme o esperado. Na verdade, isso não modela nada, mas serve como um teste de unidade ad-hoc. Para executá-lo, entre no diretório ``wolf_sheep`` e execute ``python test_random_walk.py``. Você verá uma série de grades ASCII, uma por etapa do modelo, com cada célula mostrando uma contagem do número de agentes nela.
* ``wolf_sheep_pandemic/agents.py``: Define as classes de agente Wolf, Sheep e GrassPatch.
* ``wolf_sheep_pandemic/scheduler.py``: Define uma variante personalizada no agendador RandomActivationByType, onde podemos definir filtros para a função `get_type_count`.
* ``wolf_sheep_pandemic/model.py``: Define o próprio modelo Wolf-Sheep.
* ``wolf_sheep_pandemic/server.py``: Configura o servidor de visualização interativa.
* ``run.py``: Inicia um servidor de visualização de modelo.

## Observações

Após cada alteração nos parâmetros do Simulador, é nescessário clicar em Reset para o início da próxima simulação.

## Leitura Adicional

Este modelo é baseado no modelo Wolf-Sheep Predation da NetLogo:

Wilensky, U. (1997). NetLogo Wolf Sheep Predation model. http://ccl.northwestern.edu/netlogo/models/WolfSheepPredation. Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.

Veja também [Lotka–Volterra equations
](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations) para obter um exemplo de um modelo clássico de equação diferencial com dinâmica semelhante.