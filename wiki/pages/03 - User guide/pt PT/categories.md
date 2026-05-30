---
title: Gramps 6.0 Wiki Manual - Categories/pt PT
categories:
- Pt PT:Documentation
managed: false
source: wiki-scrape
wiki_revid: 113652
wiki_fetched_at: '2026-05-30T19:37:58Z'
lang: pt PT
---

{{#vardefine:chapter\|4}} {{#vardefine:figure\|0}}

A [informação genealógica](https://en.wikipedia.org/wiki/Genealogy#Types_of_information) é muito vasta e pode ser extremamente detalhada. A sua apresentação representa um desafio que o Gramps enfrenta dividindo e organizando a informação numa série de categorias, cada uma com as suas próprias vistas. Cada vista apresenta uma parte da informação total, seleccionada de acordo com uma determinada categoria. Isto tornar-se-á mais claro à medida que explorarmos as diferentes categorias.

<span id="Categories of the Navigator">

## Categorias do navegador

</span>

![[_media/Gramps-navigator-sidebar-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Navegador com selector de modo da categoria]] O navegador está situado à esquerda da janela e permite selecionar as diferentes categorias. As diferentes categorias do [navegador](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Navigator):

-   
  mostra diferentes Gramplets de uso geral, pequenos widgets que podem ajudar na sua pesquisa genealógica.

<!-- -->

-   
  lista de indivíduos na árvore genealógica.

<!-- -->

-   
  mostra as relações entre o indivíduo activo e outros indivíduos de forma textual. Inclui pais, irmãos, cônjuges e filhos do indivíduo.

<!-- -->

-   
  lista de famílias na árvore genealógica.

<!-- -->

-   
  mostra árvores gráficas do indivíduo seleccionado.

<!-- -->

-   
  lista de eventos na árvore genealógica.

<!-- -->

-   
  lista de locais na árvore genealógica.

<!-- -->

-   
  mostra dados dos locais na árvore genealógica num mapa.

<!-- -->

-   
  lista de fontes na árvore genealógica.

<!-- -->

-   
  lista de citações na árvore genealógica.

<!-- -->

-   
  lista de repositórios na árvore genealógica.

<!-- -->

-   
  lista de objectos multimédia na árvore genealógica.

<!-- -->

-   
  lista de notas na árvore genealógica.

{{-}} ![[_media/Navigator-mode-selection-drop-down-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Lista pendente de modos da categoria Indivíduos]]

As categorias podem conter várias formas de mostrar os dados. Cada forma específica é designada por vista. Por exemplo:

- *Categoria* **Indivíduos**

  - **** - *modo hierárquico pré-definido*
  - **** - *modo de lista simples alternativo*

{{-}} Para cada categoria, existem várias formas de alternar entre os diversos modos:

1.  seleccionando o ícone relevante na barra de ferramentas;
2.  no menu
3.  pelos [atalhos de teclado](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#List_Views), baseados no número para *alternar para o modo correspondente ao número premido ///../ na categoria indicada*;
4.  pelo navegador, quando seleccionou a exibição de categorias pendente ou expandida (veja [Alternar entre modos de navegação](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Switching_Navigator_modes))

{{-}} .{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Lista pendente de selecção de modos de navegação. Veja [Alternar entre modos de navegação](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Switching_Navigator_modes) \]\]}}

{{-}} As secções seguintes fornecem uma breve descrição de cada categoria e dos respectivos modos.

<span id="Dashboard Category">

## Categoria Painel

</span>

![[_media/DashboardCategory-DashboardView-default-gramplets-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Painel (Modo pré-definido)]] ![[_media/SessionLogGramplet-example-shown-embeded-on-DashboardCategory-60-pt_PT.png|Gramplet Diário da sessão - exemplo (mostrar na área de exibição/Menu contextual &quot;Adicionar um gramplet&quot; também visível)]] A categoria **Painel** mostra um dado número de utilitários, chamados [Gramplets](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#What_is_a_Gramplet), que podem ajudar na pesquisa.

Há dois gramplets mostrados no arranque ([Apelidos mais frequentes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Top_Surnames) e [Boas-vindas ao Gramps!](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Welcome)) numa disposição em duas colunas. Pode alterar o número de colunas com a [disposição de gramplets](#Gramplet_Layout) Os controlos de configuração estão na barra de ferramentas e no menu . A barra lateral direita e a barra inferior não estão disponíveis na categoria Painel.

Pode alterar os gramplets visíveis utilizando o menu contextual (clicando com o botão direito do rato) numa área vazia do painel. Isto mostrará um menu , populado com a lista dos gramplets que pode adicionar a esta categoria em particular. Alguns gramplets só estão disponíveis nalgumas categorias. É melhor ter uma árvore genealógica aberta ao trocar os gramplets. A resposta adicional de alguns dados da árvore nos gramplets ajudará a fazer escolhas sobre a configuração da disposição.

- \- lista de indivíduos vivos e as suas idades numa determinada data

- \- lista de estatísticas de duração de vida num número de gráficos

- \- eventos individuais numa dada data, ou mês no passado

- \- perguntas frequentes sobre o Gramps.

- \- nomes próprios mais populares

- \- vista rápida do indivíduo actual

- \- recordes mundiais dos seus dados

- \- rastreio do que fez e que registos visitou

- gera [códigos SoundEx](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Soundex) para os nomes dos indivíduos na base de dados.

- \- estatísticas da base de dados

- \- apelidos mais frequentes em forma de "nuvem"

- \- um bloco de notas para ajudar na investigação

- \- os 10 apelidos mais populares *(pré-definição)*

- \- uma mensagem de acolhimento do Gramps *(pré-definição)*

- \- o que há a fazer a seguir

Para além disso, há uma série de gramplets de terceiros que pode instalar e utilizar facilmente. Estes incluem:

- \- notícias recentes e actuais sobre o Gramps

- \- editar nome, nascimento e óbito do indivíduo activo e adicionar indivíduos

- \- uma consola Python

- \- ver e editar nota pessoal primária do indivíduo activo

e muitos outros. Veja [Extensões de terceiros](wiki:Extensões_de_terceiros) para mais detalhes.

Para obter informação mais detalhada sobre como utilizar gramplets instalados, veja [Gramplets](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets).

O menu pendente da categoria Painel disponibiliza as opções e . Está disponível um menu pendente similar na [barra de menu de gramplets](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Gramplet_Bar_Menu), nas barras inferior e lateral direita de outras categorias. {{-}} ![[_media/Dashboard_ConfigureActiveView-icon-and-text-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Botão  (com a extensão Preferências do tema para mostrar texto sob os ícones)]] <span id="Gramplet Layout">

### Disposição dos gramplets

</span>

Pode alterar o do painel no separador de disposição dos gramplets ou alterar as opções dos outros gramplets nos respectivos separadores, clique em ![[_media/Gramps-config.png]]. Em alternativa, pode escolher no menu . {{-}}

<span id="People Category">

## Categoria Indivíduos

</span> ![[_media/Menubar-View-overview-example-52_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu Ver da categoria Indivíduos - modo Indivíduos agrupados]] Na , os modos (pré-definição) ou mostram uma lista de todos os indivíduos na árvore genealógica, sem as suas ligações. A partir desta categoria, pode adicionar, editar, eliminar, exportar dados, ou unir indivíduos. Cada modo (agrupados ou em lista) mostra várias colunas de dados sobre cada indivíduo.

Estão disponíveis mais opções quando selecciona um indivíduo na lista e clica com o botão direito para abrir o seu [menu contextual](wiki:Gramps_Glossary#context_menu):

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- - 

  - 

  - 

  - 

  - 

  - 

  - 

  - 

{{#vardefine:viewmode\|categoria Indivíduos}} Por pré-definição inclui: e . O modo Indivíduos também reverte para mostrar os separadores [Barra lateral](wiki:/pt_PT#People_Category_Sidebar) e [Barra inferior](wiki:/pt_PT#People_Category_Bottombar_tabs). Nenhum dos gramplets pré-definidos da barra lateral (veja [Detalhes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Details), [Galeria](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Gallery), [Eventos](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Events), [Filhos](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Children), [Citações](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Citations), [Notas](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Notes), [Atributos](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Attributes), [Referências](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#References)) ou outros (veja [Filtro](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#People_Filter)) têm opções configuráveis.

##### Colunas da {{#var:viewmode}}

Por pré-definição, as tabelas da {{#var:viewmode}} mostrarão as colunas seleccionadas nas opções de configuração, com uma linha para cada indivíduo. Pode seleccionar colunas adicionais no diálogo de opções de configuração. As alterações à configuração aparecem quando clica em .

As colunas disponíveis são:

-  (1ª coluna **requerida** para o modo Indivíduos agrupados. Não aparece como opção configurável)

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

Veja também:

- [Utilizar a categoria Indivíduos](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/pt_PT#Using_the_People_Category)
- [Editar informação sobre indivíduos](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/pt_PT#Editing_information_about_people)

{{-}} ![[_media/People-tree-view-grouped-people-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Indivíduos - Árvore - Indivíduos agrupados]] <span id="Tree View - Grouped People">

### Árvore - Indivíduos agrupados

</span>

Os indivíduos são agrupados de acordo com os seus apelidos. À esquerda de cada nome de apelido encontra-se, normalmente, uma seta ou outro tipo de indicador (e.g., ). Clicar nesse indicador uma vez revela a lista completa dos indivíduos que partilham esse apelido. Clicá-lo outra vez recolhe a lista, mostrando só o apelido.

<span id="Tree View - People List View">

### Árvore - Lista de indivíduos

</span>

![[_media/People-tree-view-people-list-view-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Indivíduos - Árvore - Lista de indivíduos]]

Lista de todos os indivíduos na base de dados, ordenados pela primeira coluna que, por pré-definição, é .

Estão disponíveis opções adicionais seleccionando um indivíduo da lista e utilizando o menu contextual, mostrado ao clicar com o botão direito do rato:

- 

- 

- 

- 

- 

- 

- 

- 

- - 

  - 

  - 

  - 

  - 

  - 

  - 

  - 

{{-}}

<span id="People Category Bottombar tabs">

### Separadores da barra inferior da categoria Indivíduos

</span> Ambos os modos (Indivíduos agrupados e Lista de indivíduos) têm os seguintes separadores na [barra inferior](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar), sendo a configuração independente entre modos: {{-}} <span id="Details">

#### [Detalhes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Details)

</span> <span id="Gallery">

#### [Galeria](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Gallery)

</span> <span id="Events">

#### [Eventos](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Events)

</span> <span id="Children">

#### [Filhos](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Children)

</span> <span id="Citations">

#### [Citações](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Citations)

</span> <span id="Notes">

#### [Notas](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Notes)

</span> <span id="Attributes">

#### [Atributos](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Attributes)

</span> <span id="References">

#### [Referências](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#References)

</span> <span id="People Category Sidebar tabs">

### Separadores da barra lateral da categoria Indivíduos

</span>

Ambos os modos (Indivíduos agrupados e Lista de indivíduos) têm os seguintes separadores na [barra lateral](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar), sendo a configuração independente entre modos: {{-}} <span id="Filter">

#### [Filtro](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Filter)

</span>

![[_media/Relationships-category-view-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Parentescos]] <span id="Relationships Category">

## Categoria Parentescos

</span>

![[_media/gramps-relation.png]] A Categoria Parentescos mostra todas as relações do indivíduo activo (a pessoa seleccionada). Especificamente, mostra os pais, irmãos, cônjuges e filhos dessa pessoa.

A categoria Parentescos foi concebida para permitir uma navegação rápida. Pode alterar rapidamente o indivíduo activo clicando no nome de qualquer pessoa listada na página. Cada nome é, na realidade, uma [hiperligação](http://en.wikipedia.org/wiki/Hyperlink), similar a uma página web.

O nome do indivíduo activo está em **negrito**. Os outros nomes são mostrados com ou sem ênfase a **negrito** e *itálico*, dependendo da existência de determinadas relações para a pessoa nomeada. Para uma pessoa listada como pai ou cônjuge do indivíduo activo, o nome é realçado se essa pessoa tiver um conjunto de pais. Para uma pessoa listada como irmão ou filho do indivíduo activo, o nome é realçado se essa pessoa tiver filhos.

As datas estão normalmente em estilo normal e em estilo *tálico* se o evento mostrado for um evento de recurso, ou seja, um evento substituto de outro evento em falta. Pode ser um evento de baptismo para um evento de nascimento, um evento de inumação para um evento de óbito, etc. {{-}} <span id="Relationships Category view">

### Vista da categoria Parentescos

</span>

Para as vistas da categoria Parentescos, através do menu ou da barra de ferramentas, pode seleccionar:

- ou o ícone  - abre o diálogo ;

- ou o ícone  - para criar uma nova família com o indivíduo activo listado como filho....}} ou o ícone  - que abre o [Selector Seleccionar família](wiki:Gramps_6.0_Wiki_Manual_-_Categories/pt_PT#Select_Family_selector), permitindo-lhe escolher a partir de uma lista de famílias existentes, e depois adicionar a pessoa como filho a essa família;

- ou o ícone ;

- ou o ícone  - para abrir o diálogo [Reordenar parentescos](wiki:Gramps_6.0_Wiki_Manual_-_Categories/pt_PT#Reorder_Relationships_dialog).

{{-}}

Estão disponíveis as seguintes secções: <span id="Active Person">

#### Indivíduo activo

</span>

- Na parte superior do ecrã é mostrada informação de nome, , e , assim como a idade calculada do indivíduo activo. Pode realçar e selccionar os campos de e .

<!-- -->

- No lado direito, será mostrada uma fotografia da pessoa, se disponível. Esta fotografia mostra a primeira imagem disponível no separador (se existir). Pode clicar na fotografia para a abrir no visualizador de imagens do sistema. Veja também [Objectos multimédia em falta](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Missing_Media_Objects_.27broken_link.27_icon_of_a_box_with_a_red_.27x.27) )

<!-- -->

- Ao lado do nome da pessoa encontra-se um símbolo que indica o sexo, e um botão . Clicá-lo permite-lhe editar todas as informações individuais no diálogo .

<!-- -->

- Veja também: [Definir o indivíduo inicial](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/pt_PT#Setting_the_Active_Person).

<span id="Parents">

#### Pais

</span>

A secção Pais mostra as famílias em que o indivíduo é filho. Uma vez que é possível que uma pessoa tenha vários conjuntos de pais, pode haver várias secções Pais. Pode editar os pais existentes clicando em ao lado dos pais. Se clicar em junto a um conjunto de pais, o indivíduo activo será removido desse conjunto de pais. Este botão não elimina a relação entre os pais.

Ver a secção para configurar os pormenores a mostrar ou ocultar, etc...

<span id="Select Family selector">

##### Selector Seleccionar família

</span> ![[_media/SelectFamily-SelectorDialog-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Selector Seleccionar família]]

O diálogo permite-lhe ligar a uma família já existente.

São mostrads as seguintes colunas: ID (ordem pré-definida para a lista), Pai, Mãe, Última alteração.

Pode utilizar o botão para filtrar a lista com base numa das opções da lista pendente:

- **ID contém** (pré-definição)
- *ID não contém*
- *Pai contém*
- *Pai não contém*
- *Mãe contém*
- *Mãe não contém*
- *Última alteração contém*
- *Última alteração não contém*

Use para fazer nova procura.

Note que em alguns relatórios a lista é restrita até marcar a caixa . {{-}}

<span id="Siblings">

##### Irmãos

</span>

A secção Irmãos mostra os irmãos e irmãs do indivíduo activo e ele próprio. {{-}}

<span id="Family">

#### Família

</span>

Semelhante à secção Pais, a secção Família mostra as famílias onde o indivíduo activo é um dos pais. Como é possível que tenha sido parte em várias famílias, o Gramps permite várias secções Família. Cada secção de família apresenta o cônjuge e quaisquer filhos. Os filhos que foram filhos biológicos de ambos os parceiros de uma família, podem ser enteados ou adoptados por outro parceiro numa família formada posteriormente.

Pode adicionar uma família clicando em na barra de ferramentas.

Clicar em ao lado do cônjuge permite-lhe editar a família mostrada. Clicar em removerá a pessoa dessa família.

{{-}}

{{-}} <span id="Reorder Relationships dialog">

###### Diálogo Reordenar parentescos

</span> Clique em ![[_media/Stock_reorder.png]] para abrir o diálogo . A família mais acima é considerada a **família primária** e é a família utilizada para tabelas, gráficos e resumos.

![[_media/ReorderRelationships-dialog-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo Reordenar parentescos]]

Quando existir mais do que um conjunto de pais ou de cônjuges para o indivíduo activo, seleccione uma das seguintes opções:

- menu ;
- botão na barra de ferramentas;
- ícone junto ao rótulo ;
- ícone junto ao rótulo ;

para abrir o diálogo , que permite reorganizar:

- a ordem dos pais na secção superior utilizando os botões de seta para cima/para baixo;
- ou a ordem das famílias na secção inferior utilizando os botões de seta para cima/para baixo.

{{-}}

<span id=Children">

##### Filhos

</span>

Os filhos do indivíduo activo {{-}}

{{#vardefine:viewmode\|categoria Parentescos}}

![[_media/ConfigureRelationshipsView-Content-tab-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Configurar a categoria Parentescos - separador Conteúdo]] <span id="Content">

##### No separador 

</span>

- -  mostrar ou ocultar as informações sobre o nascimento e o óbito (todos excepto o indivíduo activo);

  -  mostrar ou ocultar os irmãos do indivíduo.

{{-}} ![[_media/ConfigureRelationshipsView-Layout-tab-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Configurar a categoria Parentescos - separador Disposição]] <span id="Layout">

##### No separador 

</span>

- - ;

  -  mostrar ou ocultar o botão junto a cada indivíduo;

  - {{-}}

<span id="Relationships Category Bottombar tabs">

### Barra inferior da categoria Parentescos

</span> A não mostra nenhum gramplet na [barra inferior](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar). Pode adicioná-los à sua vontade. {{-}} <span id="Relationships Category Sidebar tabs">

### Barra lateral da categoria Parentescos

</span> A não mostra nenhum gramplet na [barra direita](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar). Pode adicioná-los à sua vontade. {{-}}

<span id="Families Category">

## Categoria Famílias

</span>

![[_media/gramps-family.png]] ![[_media/Families-category-list-view-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Famílias - Lista]]

Na a mostra uma lista de todas as famílias da base de dados.

Pode usar os botões na [barra de ferramentas](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Toolbar) para:

- ;

- ;

- ;

- ![[_media/Gramps_Merge48x48_win.png]] na lista (só duas de cada vez);

- ![[_media/16x16-gramps-tag.png]] .

As colunas pré-definidas da lista são `ID, Pai, Mãe, Parentesco e Data de casamento`. Se configurar a vista activa, pode ocultar colunas existentes, mostrar colunas adicionais como `Privado, Etiquetas, Última alteração` ou reorganizar a ordem das colunas, arrastando e largando.

Estão disponíveis opções adicionais seleccionando uma família da lista e utilizando o menu contextual, mostrado ao clicar com o botão direito do rato:

- 

- 

- 

- 

- 

- 

- 

- 

- - 

  - 

<!-- -->

- Veja também:
  - [Utilizar a categoria Famílias](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/pt_PT#Using_the_Families_Category)
  - [Editar informação sobre parentescos](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/pt_PT#Editing_information_about_relationships)

{{-}}

{{#vardefine:viewmode\|categoria Famílias}}

![[_media/FamiliesCategory-FamiliesView-Configure-dialog-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Famílias - Configurar a vista activa - separador Colunas]]

##### Colunas

Tal como acontece com a maioria das listas, o diálogo de configuração permite personalizar as colunas que serão mostradas e a sua ordem. As colunas pré-definidas da lista são `ID, Pai, Mãe, Parentesco e Data de casamento`. Se configurar a vista activa, pode ocultar colunas existentes, mostrar colunas adicionais como `Privado, Etiquetas, Última alteração` ou reorganizar a ordem das colunas, arrastando e largando.

##### Dialecto CSV

No separador de [Dialecto CSV](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#CSV_Dialect) pode escolher o formato CSV e o delimitador a usar ao [exportar a lista](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Export_View).

{{-}}

<span id="Families Category Bottombar tabs">

### Separadores da [barra inferior](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar) da categoria Famílias

</span>

#### Gramplet [Galeria](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Gallery)

#### Gramplet [Eventos](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Events)

#### Gramplet [Filhos](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Children)

#### Gramplet [Citações](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Citations)

#### Gramplet [Notas](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Notes)

#### Gramplet [Atributos](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Attributes)

#### Gramplet [Referências](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#References)

<span id="Families Category Sidebar tabs">

### Separadores da [barra lateral](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar) da categoria Famílias

</span>

#### Gramplet [Filtro](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Filter)

<span id="Charts Category">

## Categoria Gráficos

</span> ![[_media/gramps.png]] A categoria Gráficos mostra várias representações gráficas da ascendência ou descendência do indivíduo activo.

Por defeito, o Gramps mostra o diagrama . Com os diagramas , e disponíveis na barra de ferramentas ou no menu

<span id="Pedigree View">

### Diagrama Costados

</span>

![[_media/ChartsCategory-pedigreeview1-horizontal-right-standard-5gen-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Costados - Diagrama Costados]]

O diagrama mostra até nove gerações ascendentes do indivíduo activo. Poderá precisar de utilizar as barras de rolamento para ver outras parte da árvore.

Cada pessoa é indicada por uma caixa com o seu nome, informações de nascimento (indicadas por um asterisco \*), informações de óbito (indicadas por um mais +), é mostrada uma faixa preta no canto superior esquerdo da caixa se a pessoa tiver falecido (ou determinado pelo Gramps que já não está viva) e, opcionalmente, a imagem principal, se disponível.

Duas linhas partem de cada caixa individual. A linha superior conduz ao pai da pessoa e a linha inferior conduz à mãe. As linhas sólidas representam a relação biológica do tipo nascimento, enquanto as linhas tracejadas representam relações não-nascimento, tais como adopção, padrasto ou madrasta, tutela, etc. O botão de seta para a esquerda ao lado do indivíduo activo só pode ser clicado se o indivíduo activo tiver filhos. Ao seleccionar um dos filhos, esse filho passa a ser o indivíduo activo do gráfico.

O aparecimento dos nomes dos filhos no menu diferencia os ramos mortos da árvore dos ramos contínuos. Aqueles que têm descendência posterior estão a ***itálico negrito***, ao passo que os que são ramos finais estão em letra normal. Se o indivíduo activo tiver apenas um filho, não aparece nenhum menu (uma vez que só há uma escolha) e o filho torna-se o indivíduo activo quando se clica no botão de seta.

O lado direito da janela mostra dois botões de seta para a direita. Quando se clica no botão de cima, , o pai do indivíduo activo passa a ser o indivíduo activo. Quando se clica no botão inferior , a mãe do indivíduo activo torna-se o indivíduo activo.

{{-}} ![[_media/ChartsCategory-PedigreeView-PersonContextMenu-showing-Children-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diagrama Costados - Menu contextual individual - Submenu Filhos]] <span id="Pedigree View Context menus">

#### Menus contextuais do diagrama Costados

</span> <span id="Pedigree View Person Context menu">

##### Menu contextual das caixas individuais

</span>

Clicar com o botão direito do rato na caixa de qualquer pessoa no diagrama Costados, abre o menu contextual individual. Entre outros itens úteis, dispõe de sub-menus que listam , , , e . Estes últimos são pessoas que partilham um evento com o indivíduo na caixa. Veja o tópico do Discourse "[Who are the "Related" in Charts context menus](https://gramps.discourse.group/t/who-are-the-related-in-charts-context-menus/6498)" para mais informação.

Os submenus "a cinzento" indicam a ausência de dados na categoria adequada. Os menus dos filhos e pais distinguem as linhas contínuas dos becos sem saída. O botão abre esta página de ajuda.

<span id="Pedigree View Blank Context menu">

##### Menu contextual do fundo da diagrama

</span> Se clicar com o botão direito do rato numa área vazia do fundo do diagrama Costados, aparece o mesmo menu, mas com opções limitadas, perdendo-se tudo o que é específico do indivíduo na caixa. {{-}}

![[_media/ChartsCategory-PedigreeView-ConfigureCharts-dialog-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Gráficos - Diagrama Costados - Configurar a vista activa]]

{{#vardefine:viewmode\|Diagrama Costados}}

O separador do diagrama tem as seguintes opções:

- ;

- ;

- ;

- ;

- - **Padrão**(pré-definição);
  - Compacta;
  - Expandida;

{{-}} ![[_media/ChartsCategory-pedigreeview2-horizontal-left-standard-5gen-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diagrama Costados - Horizontal (←)]] ![[_media/ChartsCategory-pedigreeview2-vertical-up-standard-5gen-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diagrama Costados - Vertical (↑)]] ![[_media/ChartsCategory-pedigreeview2-vertical-down-standard-5gen-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diagrama Costados - Vertical (↓)]]

- - Vertical (↑);
  - Vertical (↓);
  - **Horizontal (→)**(pré-definição);
  - Horizontal (←);

- deslizador entre 2 e 9 gerações. Pré-definido para `5`

{{-}} {{-}}

<span id="Fan Chart View">

### Diagrama em leque

</span>

![[_media/ChartsCategory-fanchartview-halfcircle-7gen-Royals-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diagrama em leque - Meio círculo]]

O mostra a ascendência dos indivíduos activos como um gráfico circular. Clicar num nome no gráfico duplicará a secção atribuída a essa pessoa, colapsando a secção do cônjuge. Um segundo clique faz com que o gráfico volte à sua forma original.

Clicar com o botão direito do rato abre um menu contextual como na vista de linhagem, permitindo navegar para outras pessoas. Esta vista permite ver grandes ascendências de uma forma mais compacta e ver rapidamente quais as partes de uma ascendência que necessitam de mais investigação.

Pode rodar a vista clicando no espaço vazio e arrastando. Pode mover a vista clicando no centro do gráfico e arrastando.

- A vista pode ser um círculo, um meio-círculo ou um quadrante de um círculo. Os últimos estão sempre ligados à parte inferior ou lateral da vista.
- Os filhos do indivíduo central são mostrados dentro do anel no centro.
- Arraste e largue pessoas para o centro para alterar a pessoa ativa.
- Opções de cor;
  - Cores das caixas de acordo com a idade das pessoas;
  - Cores das caixas de acordo com o período de tempo em que a pessoa viveu;
  - Cores brancas, clássicas, baseadas no sexo e definidas pelo utilizador.
- Filtragem: utilize o filtro de indivíduos na barra lateral para obter rapidamente informações sobre os indivíduos mostrados. Por exemplo, que pessoas têm eventos de nascimento, quem tem o atributo "olhos azuis", ... . Os resultados filtrados têm letra a negrito, os que não satisfazem o filtro são mostrados transparentes
- Mostrar a dez gerações no diagrama.
- Imprimir o diagrama a partir da barra de ferramentas. O diagrama tal como o vê (depois de rodar, expandir e mudar de cor) pode ser impresso através do botão . Pode ser impressa em papel ou utilizar a opção Imprimir para ficheiro para gravar em qualquer um dos seguintes formatos: SVG (que pode ser editado em ferramentas como o Inkscape ou visto em navegadores como o Firefox), PostScript (.ps) ou PDF.
- O tipo de letra utilizado pode ser seleccionado e ajustado automaticamente para caber dentro das caixas. Num fundo mais escuro, o tipo de letra é branco e vice-versa.

{{-}} ![[_media/ChartsCategory-FanChartView-ConfigureCharts-dialog-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Gráficos - Opções de configuração - Diagrama em leque]]

{{#vardefine:viewmode\|Diagrama em leque}}

- *9* (pré-definição)

- *Sans* (pré-definição)

- - Cores dos sexos
  - **Gradação baseada em gerações** (pré-definição)
  - Gradação baseada na idade(0-100)
  - Cor única principal (filtro)
  - Gradação baseada em períodos de tempo
  - Branco
  - Esquema de cores clássico do relatório
  - Esquema de cores clássico do diagrama

- *\#ef2929* (pré-definição)

- *\#3d37e9* (pré-definição)

- - **Círculo completo** (pré-definição)
  - Semi-círculo
  - Quarto de círculo

- 

- 

- 

- 

#### Veja também

{{-}}

<span id="Descendant Fan View">

### Leque de descendentes

</span> ![[_media/ChartsCategory-descendantfan-fullcircle-9gen-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Leque de descendentes - Círculo completo]] O diagrama **Leque de Descendentes** mostra interactivamente os descendentes do indivíduo activo num formato de gráfico circular. O leque de descendentes fornece uma forma abrangente e visualmente apelativa de explorar e analisar os descendentes de um indivíduo na sua árvore genealógica.

Clicar num nome no gráfico colapsa as secções de irmãos do gráfico circular, enquanto um segundo clique reverte o gráfico para a sua forma original. Clicar com o botão direito do rato abre um menu contextual semelhante ao da vista de genealogia, permitindo a navegação para outros indivíduos. Os pais do indivíduo activo central são mostrados no anel mais interior.

Esta vista permite aos utilizadores visualizar árvores de descendentes de grandes dimensões de forma mais compacta, e identificar rapidamente áreas que requerem mais investigação.

Características principais:

- As dicas de ferramentas aparecem (com o nome da pessoa, informações de nascimento e morte) após um pequeno atraso ao indicar um segmento de leque;
- Arraste e largue indivíduos para o centro para mudar o individuo activo (ou [navegue para o indivíduo activo](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/pt_PT#Setting_the_Active_Person) usando os métodos padrão);
- Clicar no nome de um descendente no gráfico colapsa (ou expande) as secções de irmãos;
- Rode o diagrama clicando e arrastando no fundo do gráfico em leque ou dentro da região interior (branca);
- Arraste o ponto preto central para mover o diagrama na área principal;
- Mova o foco central horizontalmente arrastando a barra de rolamento inferior;
- Mova o foco central verticalmente arrastando a barra de rolamento direita ou com a roda do rato;
- Os apelidos aparecem em negrito;
- Mostre até 16 gerações;
- Selecção de letra ajustável com dimensionamento automático para caber dentro das caixas.

Pode utilizar o gramplet Filtro, as opções de configuração e as variantes escuras (da extensão Tema nas preferências) para ajustar a forma como os dados são exibidos.

Utilize o filtro de indivíduos na barra lateral para obter informações rápidas (por exemplo, indivíduos com eventos de nascimento, atributos específicos). Os resultados filtrados são mostrados em cores de saturação total, enquanto as cores das entradas não correspondentes são semi-transparentes.

<span id="Printing">

#### Imprimir

</span>

Imprima o diagrama a partir da barra de ferramentas, incluindo quaisquer rotações, expansões ou alterações de cor. Utilize a opção Imprimir para ficheiro para gravar em vários formatos:

- SVG (editável em ferramentas como o Inkscape ou aberto em navegadores);
- PostScript (.ps);
- PDF;

{{-}}

{{#vardefine:viewmode\|Leque de descendentes}}

![[_media/ChartsCategory-DescendantFanChartView-ConfigureCharts-dialog-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Gráficos - Leque de descendentes - Opções de configuração]]

- *9* (pré-definição)

- *Sans* (pré-definição)

- - Cores dos sexos
  - **Gradação baseada em gerações** (pré-definição)
  - Gradação baseada na idade(0-100)
  - Cor única principal (filtro)
  - Gradação baseada em períodos de tempo
  - Branco
  - Esquema de cores clássico do relatório
  - Esquema de cores clássico do diagrama

- *\#ef2929* (pré-definição)

- *\#3d37e9* (pré-definição)

- 

- - **Círculo completo** (pré-definição)
  - Semi-círculo
  - Quarto de círculo

- - Distribuição homogénea dos filhos
  - **Tamanho proporcional ao número de descendentes** (pré-definição)

- 

- 

- 

#### Veja também

- [Diagrama Leque de descendentes](https://gramps-project.org/blog/2012/09/descendant-fanchart/) (anúncio no blogue)

- 

{{-}}

<span id="2-Way Fan View">

### Leque de 2 vias

</span>

![[_media/ChartsCategory-2wayfan-fullcircle-ances4gen-descen4gen-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Leque de 2 vias - 4 gerações de ascendentes e de descendentes]]

Gráfico composto por ascendentes e descendentes. O leque de duas vias mostra de forma interactiva os ascendentes e descendentes do indivíduo activo num formato de gráfico circular. O leque proporciona uma forma abrangente e visualmente apelativa de explorar e analisar os ascendentes e descendentes de um indivíduo na sua árvore familiar.

Clicar num nome no gráfico colapsa as secções de irmãos do gráfico circular, enquanto um segundo clique reverte o gráfico para a sua forma original. Clicar com o botão direito do rato abre um menu contextual semelhante ao da vista de genealogia, permitindo a navegação para outros indivíduos. Os pais do indivíduo activo central são mostrados no anel mais interior.

Esta vista permite aos utilizadores visualizar árvores de descendentes de grandes dimensões de forma mais compacta, e identificar rapidamente áreas que requerem mais investigação.

Características principais:

- As dicas de ferramentas aparecem (com o nome da pessoa, informações de nascimento e morte) após um pequeno atraso ao indicar um segmento de leque;
- Arraste e largue indivíduos para o centro para mudar o individuo activo (ou [navegue para o indivíduo activo](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/pt_PT#Setting_the_Active_Person) usando os métodos padrão);
- Clicar no nome de um descendente no gráfico colapsa (ou expande) as secções de irmãos;
- Rode o diagrama clicando e arrastando no fundo do gráfico em leque ou dentro da região interior (branca);
- Arraste o ponto preto central para mover o diagrama na área principal;
- Mova o foco central horizontalmente arrastando a barra de rolamento inferior;
- Mova o foco central verticalmente arrastando a barra de rolamento direita ou com a roda do rato;
- Os apelidos aparecem em negrito;
- Mostre até 11 gerações ascendentes;
- Mostre até 11 gerações descendentes;
- Selecção de letra ajustável com dimensionamento automático para caber dentro das caixas.

Pode utilizar o gramplet Filtro, as opções de configuração e as variantes escuras (da extensão Tema nas preferências) para ajustar a forma como os dados são exibidos.

Utilize o filtro de indivíduos na barra lateral para obter informações rápidas (por exemplo, indivíduos com eventos de nascimento, atributos específicos). Os resultados filtrados são mostrados em cores de saturação total, enquanto as cores das entradas não correspondentes são semi-transparentes.

<span id="Printing">

#### Imprimir

</span>

Imprima o diagrama a partir da barra de ferramentas, incluindo quaisquer rotações, expansões ou alterações de cor. Utilize a opção Imprimir para ficheiro para gravar em vários formatos:

- SVG (editável em ferramentas como o Inkscape ou aberto em navegadores);
- PostScript (.ps);
- PDF;

{{-}}

{{#vardefine:viewmode\|Leque de 2 vias}}

![[_media/ChartsCategory-2-WayFanChartView-ConfigureCharts-dialog-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Gráficos - Leque de 2 vias - Opções de configuração]]

- *4* (pré-definição)

- *4* (pré-definição)

- *Sans* (pré-definição)

- - Cores dos sexos
  - **Gradação baseada em gerações** (pré-definição)
  - Gradação baseada na idade(0-100)
  - Cor única principal (filtro)
  - Gradação baseada em períodos de tempo
  - Branco
  - Esquema de cores clássico do relatório
  - Esquema de cores clássico do diagrama

- *\#ef2929* (pré-definição)

- *\#3d37e9* (pré-definição)

- 

- 

- *\#ef2929* (pré-definição)

- *\#3d37e9* (pré-definição)

- 

- - Distribuição homogénea dos filhos
  - **Tamanho proporcional ao número de descendentes** (pré-definição)

- 

- 

- 

#### Veja também

- [Feature: Gep-030 FanChart2Way](https://github.com/gramps-project/gramps/pull/222) (anúncio no blogue)

- 

{{-}}

<span id="Charts Category Bottombar tabs">

### Separadores da barra inferior da categoria Gráficos

</span> A não mostra nenhum gramplet na [barra inferior](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar). Pode adicioná-los à sua vontade. {{-}} <span id="Charts Category Sidebar tabs">

### Separadores da barra lateral da categoria Gráficos

</span> A não mostra nenhum gramplet na [barra lateral](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar). Pode adicioná-los à sua vontade. {{-}} <span id="Filter">

#### Filtro

Só os diagramas e têm o filtro activo por defeito.

Veja Gramplet [Filtro](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Filter) {{-}}

<span id="Events Category">

## Categoria Eventos

</span> ![[_media/gramps-event.png]] A mostra a com todos os eventos registados na árvore genealógica.

Quando é criado pela primeira vez, espera-se que um Evento seja sobre um incidente (ou facto) para uma pessoa ou família específica (primária). Os detalhes do evento registam a sua categorização, a data (que pode ser uma data exacta ou um intervalo de datas) e o local onde ocorreu, e incluem frequentemente uma breve descrição quando a categorização é vaga. Uma categoria "Nascimento" é frequentemente suficientemente específica para não necessitar de uma descrição. Mas um evento Profissão quase não tem sentido sem uma descrição que contenha o tipo específico de vocação.

Os eventos/factos podem ser partilhados entre várias pessoas e várias famílias. Cada pessoa ou família pode ter tido um papel diferente nos eventos partilhados.

Ver também:

- [Editar informação sobre eventos](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/pt_PT#Editing_information_about_events)

{{-}}

<span id="Events View">

### Lista de eventos

</span> ![[_media/EventsCategory-EventsListView-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Eventos - Lista de eventos]]

Na dispõe das seguintes colunas: , , , , , e .

Pode usar o para adicionar, remover e redispor as colunas. Aceda-lhe a partir do botão na barra de ferramentas.

A lista de eventos pode ser ordenada da forma habitual, clicando no título da coluna.

As opções adicionais estão disponíveis seleccionando um evento da lista e utilizando o menu contextual mostrado ao clicar com o botão direito do rato:

- 

- 

- 

- 

- 

- 

- - 

  - 

{{#vardefine:viewmode\|Lista de eventos}}

![[_media/EventsCategory-EventsView-Configure-dialog-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Eventos - Lista de eventos - Opções de configuração]]

##### Colunas

Tal como acontece com a maioria das listas, o separador de configuração das colunas permite personalizar as colunas mostradas e a sua ordem de apresentação:

- 

- 

- 

- 

- 

- 

- 

- 

- 

Arraste e largue colunas para alterar a sua ordem na lista de eventos. A lista não será alterada a não ser que clique em . Se clicar em sem primeiro clicar em , as alterações serão abandonadas.

{{-}}

##### Dialecto CSV

No separador [Dialecto CSV](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#CSV_Dialect) pode seleccionar o formato CSV para o delimitador a utilizar ao [exportar esta lista](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Export_View).

{{-}}

<span id="Events Category Bottombar tabs">

### Separadores da barra inferior da categoria Eventos

</span>

A categoria mostra os seguintes separadores na [barra inferior](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar): {{-}} <span id="Gallery">

#### [Galeria](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Gallery)

</span> <span id="Citations">

#### [Citações](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Citations)

</span> <span id="Notes">

#### [Notas](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Notes)

</span> <span id="Attributes">

#### [Atributos](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Attributes)

</span> <span id="References">

#### [Referências](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#References)

</span> <span id="Events Category Sidebar tabs">

### Separadores da barra lateral da categoria Eventos

</span>

A categoria mostra os seguintes separadores na [barra lateral](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar): {{-}} <span id="Filter">

#### [Filtro](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Filter)

</span>

{{-}}

<span id="Places Category">

## Categoria Locais

![[_media/gramps-place.png]] A categoria tem duas formas de mostrar os [locais](wiki:Gramps_Glossary#place):

- como [árvore](wiki:Gramps_6.0_Wiki_Manual_-_Categories/pt_PT#Place_Tree_View) - agrupados hierarquicamente, como uma árvore de ficheiros;
- como [lista simples](wiki:Gramps_6.0_Wiki_Manual_-_Categories/pt_PT#Places_List_View).

Cada vista enumera os locais geográficos em que ocorreram os eventos da base de dados. Estes podem ser locais de nascimento, morte e casamento de pessoas, bem como os seus endereços de residência, emprego, educação ou qualquer outra referência concebível à localização geográfica.

![[_media/Toolbar-Place-Options_60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Locais - Botões na barra de ferramentas]] Tal como nas outras listas, todas as colunas podem ser utilizadas para ordenação, bastando clicar num cabeçalho de coluna.

<span ID="Places Tree View">

### Árvore de locais

</span> ![[_media/PlacesCategory-PlaceTreeView-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Locais - Locais em árvore]]

A árvore de locais agrupa os locais numa dada hierarquia: país, concelho, etc.. Pode expandir a listagem utilizando as setas .

Todos os nós podem ser simultaneamente colapsados ou expandidos a partir do menu contextoual, mostrado ao seleccionar um local e clicar com o botão direito do rato:

- ;

- ;

- ;

- ;

- ;

- ;

- ;

- ;

- ;

- .

{{-}}

{{#vardefine:viewmode\|Locais em árvore}}

![[_media/ConfigurePlaceView-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Locais - Locais em árvore - Opções de configuração]]

##### Colunas

Tal como acontece com a maioria das listas, o separador Colunas permite personalizar as colunas a mostrar e a sua ordem:

- Nome (deve ser a primeira coluna;
- Título;
- ID;
- Tipo;
- Código;
- Latitude;
- Longitude;
- Privado;
- Etiquetas;
- Última alteração.

Clicar uma vez no cabeçalho da coluna ordena por ordem ascendente, clicar novamente ordena por ordem descendente ou alterna a ordenação.

Estas opções de configuração e os [filtros](wiki:Gramps_6.0_Wiki_Manual_-_Filters/pt_PT) em vigor restringem os dados exportados via .

##### Dialecto CSV

No separador [Dialecto CSV](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#CSV_Dialect) pode seleccionar o formato CSV para o delimitador a utilizar ao [exportar esta lista](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Export_View).

![[_media/PlacesCategory-PlacesList-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Locais - Lista de locais]] <span id="Places List View">

### Lista de locais

</span>

A lista de locais mostra todos os locais numa lista longa. Estão disponíveis opções adicionais seleccionando um local da lista e utilizando o menu contextual mostado ao clicar com o botão direito do rato:

- ;

- ;

- ;

- ;

- ;

- ;

- ;

- .

{{-}}

<span id="Places Category Bottombar tabs">

### Separadores da barra inferior da categoria Locais

</span>

A categoria mostra os seguintes separadores na [barra inferior](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar): {{-}} <span id="Details">

#### [Detalhes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Details)

</span> <span id="Locations">

#### [Locais](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Locations)

</span> <span id="Gallery">

#### [Galeria](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Gallery)

</span> <span id="Events">

#### [Eventos](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Events)

</span> <span id="Citations">

#### [Citações](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Citations)

</span> <span id="Notes">

#### [Notas](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Notes)

</span> <span id="References">

#### [Referências](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#References)

</span> <span id="Places Category Sidebar tabs">

### Separadores da barra lateral da categoria Locais

</span>

A categoria mostra os seguintes separadores na [barra lateral](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar): {{-}} <span id="Filter">

#### [Filtro](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Filter)

</span>

{{-}}

<span id="Map Service">

### Serviço de mapas

![[_media/PlacesCategory-AttemptToSeeSelectedLocation-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Locais - Mapeamento - Botão na barra de ferramentas]]

Se um local tiver sido realçado, pode ver o local num navegador da web clicando em ou utilizando o menu contextual do botão direito do rato para . O seu navegador web deve abrir-se, tentando utilizar as coordenadas registadas (longitude e latitude) ou o nome do local e utilizando o sítio web do fornecedor de mapas escolhido. Diferentes serviços de mapas podem ter requisitos diferentes para a descrição do local.

{{-}} ![[_media/PlacesCategory-MapServices-list-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Locais - Mapeamento - Lista de serviços disponíveis]]

Na lista pendente , pode escolher o serviço que deseja utilizar:

- **** - Utiliza coordenadas de longitude e latitude, se existirem; caso contrário, utiliza a cidade e o país, ou utiliza a descrição do local;
- ** - Válido para locais na Suécia e na Dinamarca, apenas se a longitude e a latitude estiverem disponíveis; caso contrário, utiliza a cidade e o país, ou utiliza a descrição do local;
- ** - Utiliza coordenadas de longitude e latitude, se existirem; caso contrário, utiliza a cidade e o país, ou utiliza a descrição do local.

{{-}} Veja também:

- [Serviços de mapas - Google Earth](wiki:Addon:MapService-GoogleEarth) - uma extensão que lhe permite utilizar o Google Earth.

<span id="Geography Category">

## Categoria Geografia

</span>

![[_media/GeographyCategory-GeoPlacesView-AllKnownPlaces-openstreemap-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Geografia - Todos os locais - Openstreetmap]]

![[_media/Gramps-geo.png]]A categoria mostra um evento num mapa. Contém muitas vistas geográficas, o que lhe permite ver as pessoas e os seus eventos colocados num mapa através de um fornecedor de mapas da Internet (OpenStreetMap, Google maps ...).

Estão disponíveis as seguintes vistas:

- [Todos os locais conhecidos para um indivíduo](#All_known_places_for_one_Person);
- [Todos os locais conhecidos para uma família](#All_known_places_for_one_Family);
- [Todas as residências e deslocações de um indivíduo e seus descendentes](#Every_residence_or_move_for_a_person_and_any_descendants);
- [Conseguiram estas duas famílias encontrar-se?](#Have_these_two_families_been_able_to_meet_.3F);
- [Conseguiram encontrar-se?](#Have_they_been_able_to_meet_.3F);
- [Todos os locais conhecidos](#All_known_places);
- [Todos os locais relacionados com eventos](#All_places_related_to_Events) com a opção de ;
- Há [extensões de terceiros](wiki:6.0_Addons#Addon_List) adicionais disponíveis.

Estas vistas estão acessíveis através dos botões da barra de ferramentas. Para filtrar por locais ou eventos, active a barra lateral de filtros.

<span id="Prerequisites">

### Pré-requisitos

</span> Se o ícone não está visível no navegador, provavelmente terá de instalar o [programa <code>OsmGpsMap</code>](wiki:Gramps_6.0_Wiki_Manual_-_Categories/pt_PT#Prerequisites_to_see_the_geography_view).

Para que estas vistas geográficas funcionem correctamente, é necessário:

- ter eventos relacionados com locais;
- estes locais têm de ter coordenadas: latitude e longitude;
- se um local não tiver coordenadas, nunca aparecerá no mapa;
- se tiver uma ligação à Internet activa, todos os movimentos no mapa, todas ampliações, todos os mosaicos são gravados;
  - quando não há ligação à Internet, todos os mapas memorizados da sessão anterior poem ser usados;
  - assim, o mapa pode ser utilizado sem ligação à Internet e todos os locais já visitados podem ser mostrados de novo;
  - só tem de seleccionar cada local ou área que pretende utilizar sem ligação à Internet e ampliar esses locais; poderá voltar a utilizá-los sem ligação à Internet.

<span id="The different views">

#### As diferentes vistas

<span> ![[_media/GeographyCategory-GeoPlacesView-AllKnownPlaces-BottomSideBarHidden-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Geografia - Todos os locais - Openstreetmap - Barras lateral e inferior ocultas]] <span id="All known places">

##### Todos os locais conhecidos

</span>

Esta vista mostra todos os locais com coordenadas na base de dados.

Por motivos de desempenho, por pré-definição, a vista mostra apenas o local relacionado com o histórico de locais ou os locais filtrados. Se quiser ver todos os locais, tem de seleccionar no menu contextual do [botão direito do rato](wiki:Gramps_6.0_Wiki_Manual_-_Categories/pt_PT#button_3_.28_right_button_.29) . {{-}} ![[_media/GeographyCategory-AllKnownPlaces-Configure-tab-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Configurar a vista activa - Separador  da vista &quot;Todos os locais conhecidos&quot;]]

A vista é a única que permite alterar a cor usada para os marcadores de local.

No menu Configurar a vista activa - Separador , as cores são verdes para os seguintes serviços de mapas:

- Openstreetmap;
- Maps for free;
- Opencyclemap and Public transport.

Todos os outros serviços são assinalados a vermelho.

Clique em na barra de ferramentas e escolha o separador . A cor pré-definida para cada tipo de local é verde "#008b00". ![[_media/PickAColor-selector-dialog-60-pt_PT.png]] Para cada tipo de local, pode seleccionar e escolher uma cor. Quando aparecer o diálogo **Escolha uma cor**, pode arrastar uma amostra de cor desse diálogo para as amostras de . Não é necessário clicar em para cada jurisdição e depois reabrir o diálogo.

Veja também:

- [Podemos mudar a cor do marcador?](wiki:Gramps_6.0_Wiki_Manual_-_Categories/pt_PT#Can_we_change_the_marker.27s_color_.3F)

{{-}}

![[_media/GeographyCategory-AllKnownPlacesForOneFamily-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Geografia - Todos os locais de uma família - Openstreetmap]] <span id="All known places for one Family">

##### Todos os locais conhecidos para uma família

</span>

Esta vista mostra todos os locais visitados por todos os membros da família activa durante as suas vidas. Não está ligada a quaisquer filtros. Depende apenas da família activa e do histórico.

O menu de configuração desta vista, separador não tem opções adicionais. The configuration menu tab for this view has no additional options. {{-}}

<span id="Have they been able to meet ?">

##### Conseguiram encontrar-se?

</span>

![[_media/GeographyCategory-HaveTheyBeenAbleToMeet-Configure-tab-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Geografia - Configurar a vista activa - Parâmetros da selecção]] ![[_media/GeographyCategory-HaveTheyBeenAbleToMeet-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Geografia - Conseguiram encontrar-se? - Openstreetmap]]

Esta vista é utilizada para mostrar se duas pessoas se encontraram durante a sua vida.

É necessário seleccionar uma pessoa de referência, seja no menu contextual, seja na barra de ferramentas.

Quando a pessoa de referência estiver activa, verá o seu percurso de vida. Para cada local conhecido com coordenadas, verá um círculo ou uma oval, dependendo da longitude. O raio do círculo pode ser ajustado na configuração da vista, separador . Este valor é definido em décimos de grau.

{{-}}

![[_media/GeographyCategory-AllPlacesRelatedToEvents-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Geografia - Todos os locais relacionados com eventos - Openstreetmap]] <span id="All places related to Events">

##### Todos os locais relacionados com eventos

</span>

Por motivos de desempenho, a vista mostra inicialmente apenas os locais relacionados com o histórico de eventos ou os eventos filtrados. Esta vista também pode ser utilizada para mostrar todos os locais relacionados com eventos. No entanto, pode demorar algum tempo a mostrar quando a árvore regista muitos eventos e muitos locais.

<span id="show all events"> Se realmente quiser ver todos os eventos, tem de seleccionar "mostrar todos os eventos" a partir do menu contextual [botão direito](wiki:Gramps_6.0_Wiki_Manual_-_Categories/pt_PT#button_3_.28_right_button_.29).</span>

Configurar a vista activa  
separador

O separador desta vista não tem opções adicionais. {{-}}

![[_media/GeographyCategory-AllKnownPlacesForOnePerson-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Geografia - Todos os locais de um indivíduo - Openstreetmap]] <span id="All known places for one Person">

##### Todos os locais conhecidos para um indivíduo

</span>

Esta vista mostra todos os locais visitados por uma pessoa durante a sua vida. Não está ligada a filtros. Depende apenas do indivíduo activo e do histórico.

Se pretender utilizar a funcionalidade de animação, clique com o [botão direito](wiki:Gramps_6.0_Wiki_Manual_-_Categories#button_3_.28_right_button_.29) do rato. No menu, pode seleccionar "animar" para ver o percurso de vida da pessoa atual: se a pessoa ativa tiver vários eventos relacionados, pode ver um movimento virtual entre esses marcadores. O movimento está relacionado com os anos ou a distância e pode ser modificado nas preferências do mapa da pessoa. Se a distância entre dois marcadores for superior a um valor em décimos de grau, mostramos os movimentos em função da distância em vez dos anos. Neste caso, o número de passos entre estes dois marcadores pode ser modificado. É possível modificar a velocidade da animação entre as etapas. Os movimentos começam no primeiro ano do evento até ao último ano do evento. {{-}}

![[_media/GeographyCategory-AllKnownPlacesForOnePerson-Configure-tab-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Geografia - Todos os locais de um indivíduo - Configurar a vista activa]]

Configurar a vista activa  
separador

Consulte o separador do menu de configuração para ver as seguintes opções que pode alterar:

- Um cursor para definir a (pré-definição: *100*)
- Um cursor para definir (pré-definição: *20*)
- Um cursor para definir a (pré-definição: *30*)

{{-}} <span id="All known places for one person with graphical information (KML files)">

###### Todos os locais conhecidos para um indivíduo com informação gráfica (ficheiros KML)

</span>

![[_media/gramps-person-kml.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Um indivíduo com três ficheiros KML]]

Se os ficheiros KML forem adicionados como objectos multimédia no separador Galeria para os vários registos, esta vista geográfica mostrará um caminho ou uma superfície para cada ficheiro KML. No exemplo seguinte, vêem-se 3 ficheiros KML em camadas , desenhados a partir de diferentes separadores da galeria referenciados por esta pessoa:

- um KML de contorno de limites de uma quinta no evento de nascimento;
- um KML de caminho utilizado para ir à escola no evento de educação;
- um KML de contorno de limites de uma paróquia (ou município) na galeria de locais para o evento de baptismo.

No caso do esboço dos limites da exploração agrícola, o KLM foi adicionado ao separador Galeria do evento de nascimento (em vez de ser aplicado ao separador do evento reutilizável) [local tipo "Quinta"](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/pt_PT#Place_Editor_dialog)) porque a área foi comprada e vendida ao longo dos anos. Este esboço representa a dimensão da quinta à data do nascimento.

Ver [Adicionar locais de ficheiros KML](wiki:Gramps_6.0_Wiki_Manual_-_Categories/pt_PT#Adding_places_from_KML_files)

{{-}} ![[_media/GeographyCategory-EveryResidenceOrMoveForAPersonAndAnyDescendants-Configure-tab-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Geografia - Configurar a vista activa]] ![[_media/GeographyCategory-EveryResidenceOrMoveForAPersonAndAnyDescendants-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Geografia - Todas as residências e deslocações de um indivíduo e seus descendentes - Openstreetmap]] <span id="Every residence or move for a person and any descendants">

##### Todas as residências e deslocações de um indivíduo e seus descendentes

</span>

Esta vista é utilizada para mostrar todos os locais na vida de uma pessoa e dos seus descendentes. São apresentados por geração. Pode alterar o intervalo entre a apresentação das gerações na configuração da vista.

Esta vista não está ligada a filtros. Depende apenas do [indivíduo activo](wiki:Gramps_Glossary#active_person) e seu histórico.

Configurar a vista activa  
separador

Veja o separador do menu de configuração para as seguintes opções que pode alterar:

- um cursor para definir a mostrar (pré-definição: *10*)
- um cursor para definir (pré-definição: *500*){{-}}

![[_media/GeographyCategory-HaveTheseTwoFamiliesBeenAbleToMeet-Configure-tab-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Geografia - Configurar a vista activa]] ![[_media/GeographyCategory-HaveTheseTwoFamiliesBeenAbleToMeet-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Geografia - Conseguiram estas duas famílias encontrar-se? - Openstreetmap]] <span id="Have these two families been able to meet ?">

##### Conseguiram estas duas famílias encontrar-se?

</span>

Esta vista é utilizada para mostrar se duas famílias se encontraram durante a sua vida. Deve seleccionar uma família de referência:

- a partir do menu contectual: escolha a família de referência;
- a partir da barra de ferramentas.

Quando a família de referência está activa, verá o percurso de vida de todos os seus membros. Para cada local conhecido com coordenadas, verá um círculo ou uma oval, dependendo da longitude. O raio do círculo pode ser ajustado na vista de configuração. Este valor é definido em décimos de grau.

Configurar a vista activa  
se+arador .

{{-}}

<span id="Usage">

### Uso

{{#vardefine:viewmode\|Uso}}

![[_media/ConfigureGeography-the-map-tab-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Geografia - Configurar a vista activa - Separador Mapa]] <span id="All views">

##### Todas as vistas

</span>

O separador contém opções comuns a todas as vistas:

- (por defeito, em `~/.cache/gramps/maps` em sistemas POSIX e em `C:\Users\`*<utilizador>*`\appdata\local\gramps\maps` em Windows); se necessário, pode alterar a pasta onde os ficheiros de mosaicos do mapa estão armazenados no seu computador; ;

  - botão ;

- um cursor para definir a (pré-definição: *12*). O nível de ampliação para quando centramos o mapa ou quando seleccionamos um marcador; sempre que a vista geográfica redesenha o mapa, este nível é utilizado;

- um cursor para definir o (pré-definição: *5000*); reduza este número para desenhar o mapa mais rapidamente, mas com menos formas.

- .

{{-}}

<span id="Specific views">

##### Vistas específicas

</span>

Veja a descrição de cada vista.

<span id="Print or save the Map">

#### Imprimir ou gravar o mapa

</span> Para cada uma das vistas da categoria Geografia, através do menu ou da barra de ferramentas, pode seleccionar:

- menu
- botão da barra de ferramentas
- o atalho de teclado

<span id="How to zoom and move around the map ?">

#### Como ampliar e deslocar o mapa

</span> <span id="Zoom in and Zoom out the map">

###### Ampliar e reduzir o mapa

</span> Para ampliar, use:

- os botões +/- no canto superior esquerdo do mapa;
- a roda do rato;.
- as teclas "+" ou "-" no teclado numérico.

É possível substituir o teclado numérico pelo teclado alfanumérico no [separador Mapa](wiki:Gramps_6.0_Wiki_Manual_-_Categories/pt_PT#All_views).

<span id="Move around the map">

###### Deslocar o mapa

Para se deslocar no mapa, pode:

- clicar no mapa e arrastá-lo;
- utilizar as setas.

<span id="The mouse actions on the map">

#### As acções do rato no mapa

</span> ![[_media/Geography_MiddleButton-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rectângulo de ampliação desenhado com o botão central do rato]] O botão direito abaixo é para uma pessoa destra. Será o botão esquerdo para uma pessoa canhota.

###### Botão esquerdo

Tem duas utilizações para o botão 1:

1.  seleccionar o marcador;
2.  validar a selecção da região.

###### Botão central

A única utilização para o botão central é desenhar uma região rectangular no mapa através de clique e arrastamento:

1.  quando premido: inicia a selecção da região
2.  quando libertado, termina a selecção da região.

Um clique com o botão esquerdo ampliará o mapa para o encaixar no rectângulo.

###### Botão direito

Utilização única deste botão:

- mostrar o menu contextual.

###### Rato sobre um marcador

Quando o rato é colocado sobre um marcador, é mostrado o nome do local na barra de estado à esquerda.

<span id="The menu popup">

#### O menu contextual

</span> A partir deste menu contextual, tem à sua disposição as seguintes funções:

- ocultar ou mostrar a mira;
- bloquear ou desbloquear a ampliação;
- alterar o forncedor de mapas pré-definido;
- adicionar um local e ligar um local à posição do rato;
- adicionar um local a partir de um ficheiro kml;
- centrar o mapa na posição do rato;
- centrar o mapa em função de um local a partir do sub-menu;
- remover todos os mosaicos já carregados para o fornecedor actual;
- "mostrar todos os locais" ou "mostrar todos os eventos" para as vistas "todos os locais conhecidos" ou "todos os locais relacionados com eventos".

<span id="Click on a marker">

#### Clique num marcador

</span>

Temos dois casos:

1.  eventos: para cada evento, podemos editar este evento ou centrar o mapa neste local;
2.  locais: para cada local, podemos editar este local ou centrar o mapa neste local.

Ao centrar o mapa, a ampliação utilizada é definida no [separador Mapa](wiki:Gramps_6.0_Wiki_Manual_-_Categories/pt_PT#All_views).

Podemos ter vários marcadores na área de clique, dependendo da ampliação. Neste caso, é mostrado para cada marcador todos os eventos e/ou locais relacionados. Resulta numa mistura entre os dois casos descritos acima.

![[_media/GeographyCategory-MapContextMenu-AddPlace-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Adicionar um local]] <span id="Adding or Linking to a place">

#### Adicionar ou ligar um local

</span>

Para isto, clique no botão direito do rato, obtém um menu contextual. Neste menu, pode seleccionar ou .

Quando adiciona um local ou tenta ligar um local à posição do rato, obtém uma selecção de local numa região. No mapa, verá um círculo no qual pode escolher os nomes dos locais dos marcadores. Pode ajustar o tamanho do círculo com o cursor. Dependendo do diâmetro deste círculo, é criada uma lista. Se o local já tiver alguns campos preenchidos, verá esses valores numa linha de cor verde. Se estiver de acordo, faça duplo clique nessa linha. Se não estiver de acordo, pode escolher outra linha.

Outra forma de definir a latitude e a longitude :

- Transferir a [ferramenta de conclusão de locais](wiki:Place_completion_tool) via [gestor de extensões](wiki:6.0_Addons#Installing_Addons_in_Gramps). Se transferir os dados do seu país, esta ferramenta pode adicionar a latitude e longitude a todos os seus locais.

{{-}} <span id="Adding places from KML files">

#### Adicionar locais de ficheiros KML

</span>

Para o fazer, clique com o botão direito, verá o menu contextual, onde pode seleccionar

Verá o diálogo . Seleccione o ficheiro desejado. Se tiver vários locais no mesmo ficheiro KML, obterá um editor de locais para cada local. Tenha cuidado.

<span id="How to change the map provider ?">

#### Como mudar o fornecedor de mapas?

</span>

<table>
<thead>
<tr>
<th colspan="3">![[_media/OpenStreetMap_5.15.10.png|Center|OpenStreetMap]]</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>![[_media/MapsForFree_5.15.10.jpg|Left|Maps For Free]]</td>
<td>![[_media/OpenCycleMap_5.15.10.png|Center|OpenCycleMap]]</td>
<td>![[_media/PublicTransport_5.15.10.png|Right|Public Transport]]</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>![[_media/GoogleStreet_5.15.10.png|Center|Google street]]</td>
<td>![[_media/GoogleSat_5.15.10.jpg|Center|Google sat]]</td>
<td>![[_media/GoogleHybrid_5.15.10.jpg|Center|Google hybrid]]</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>![[_media/Virtualearthstreet_5.15.10.png|Center|Virtualearth street]]</td>
<td>![[_media/VirtualearthSat_5.15.10.jpg|Center|Virtualearth sat]]</td>
<td>![[_media/VirtualearthHybrid_5.15.10.jpg|Center|Virtualearth hybrid]]</td>
</tr>
</tbody>
</table>

Existem vários fornecedores de mapas disponíveis no Gramps. Clique com o botão direito para obter o menu contextual. Na parte inferior deste menu, pode seleccionar um novo fornecedor.

Estão disponíveis os seguintes fornecedores :

- **OpenStreetMap** (pré-definição): a vantagem do [OpenStreetMap](http://www.openstreetmap.org/) é que é um projecto livre, onde pode actualizar os mapas com informações em falta através do seu sítio Web.
- Maps For Free
- OpenCycleMap
- Public Transport
- [Google - ruas](https://www.google.com/intl/en_ALL/help/terms_maps.html)
- [Google - satélite](https://www.google.com/intl/en_ALL/help/terms_maps.html)
- [Google - híbrido](https://www.google.com/intl/en_ALL/help/terms_maps.html)
- [Virtualearth - ruas](http://www.microsoft.com/maps/product/terms.html)
- [Virtualearth - satélite](http://www.microsoft.com/maps/product/terms.html)
- [Virtualearth - híbrido](http://www.microsoft.com/maps/product/terms.html)

Note que o Virtualearth é agora o Bing maps. {{-}} <span id="Can we change the marker's color ?">

#### Pode-se alterar a cor do marcador?

</span>

Só a vista suporta alterar as cores dos marcadores de tipo de local, todas as outras vistas estão codificadas no Gramps. {{-}}

<span id="How to get/remove the crosshair ?">

#### Como obter/remover a mira

</span> Pode ser útil ter a mira visível para ver o centro do mapa. Esta funcionalidade está disponível com uma opção do menu contextual, obtido com um clique direito no mapa. Seleccione ou , o que é útil para adicionar ou ligar locais às coordenadas correctas de latitude/longitude.

<span id="How to lock/unlock the map ?">

#### Como bloquear o mapa

</span> Quando mudamos o mapa (indivíduo para família, ...), a ampliação é recalculada. Pode ser útil, nalguns casos, manter a mesma ampliação e posição quando mudamos o fornecedor do mapa. Para isso, clique no botão direito do rato, obterá um menu contextual. Neste menu, pode seleccionar bloquear ou desbloquear a ampliação e a posição.

<span id="Prerequisites to see the geography view">

### Pré-requisitos para utilizar a categoria Geografia

</span> Para o Gramps 6.x, tem de instalar o [osmgpsmap](http://nzjrs.github.io/osm-gps-map/) versão 1.0 e superiores e o pacote gir associado (**G**Object **I**ntrospection **R**epository).

Por exemplo no ubuntu, tem de ter: `gir1.2-osmgpsmap-1.0` and `libosmgpsmap-1.0-0`

<span id="Possible problems">

#### Possíveis problemas

</span>

- Não há ícone da categoria Geografia na barra lateral do navegador: tem o pré-requisito `osmgpsmap` instalado? (*`'gramps -v`* a partir da linha de comandos pode ajudar).
- Não há mosaicos: tem uma ligação à Internet activa?
- Não há mosaicos de um fornecedor: se os outros fornecedores estiverem correctos, registe um erro.
- Mosaicos em falta: não tem ligação à Internet e é a primeira vez que tenta mostrar o local actual.
- Mosaicos em falta: pode ser o mesmo que não ter mosaicos para um fornecedor se este modificar as regras de acesso (i.e. utilizador-agente)
- Outros: [Relatar um erro](wiki:Using_the_bug_tracker).

<span id="Geography Category Bottombar tabs">

### Separadores da barra inferior da categoria Geografia

</span>

A por pré-definição não mostra nenhum gramplet na [barra inferior](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar). Pode adicioná-los conforme necessário.

{{-}}

<span id="Geography Category Sidebar tabs">

### Separadores da barra lateral da categoria Geografia

</span>

A por pré-definição não mostra nenhum gramplet na [barra lateral](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar). Pode adicioná-los conforme necessário.

{{-}} <span id="Geography Filter">

#### Filtro

</span>

O tipo de filtro pode mudar consoante a vista seleccionada. Ver [Gramplet filtro](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Filter) {{-}}

<span id="Sources Category">

## Categoria Fontes

</span> ![[_media/gramps-source.png]] A oferce dois modos, a (pré-definição), que lista as fontes de determinadas informações armazenadas na árvore genealógica, e a . A seleção de registos, configuração de colunas e selecções Gramplet são independentes para cada modo de visualização.

As fontes podem incluir vários documentos: certidões de nascimento, óbito e casamento, livros, filmes, diários, diários privados - quase tudo o que pode ser descrito como evidência genealógica. O Gramps dá-lhe a opção de fornecer citações de fontes para cada objecto (Evento, Indivíduo, Lugar, Multimédia, Nota, etc.) que criar.

Pode clicar em para criar uma fonte ou em para editar fontes já presentes na lista. Qualquer um abre o diálogo .

- Ver [Editar informação sobre as fontes](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/pt_PT#Editing_information_about_sources).

{{-}} <span id="Citation Tree View">

### Árvore de citações

</span>

![[_media/SourcesCategory-CitationTreeView-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Fontes - Árvore de citações]]

A também mostrará todas as fontes. Além disso, permite ao utilizador ver as [citações](#Citations_Category) associadas a cada fonte clicando nos triângulos para expandir ou para colapsar.

Todos os nós da árvore podem ser simultaneamente colapsados ou expandidos a partir do menu contextual, mostrado ao clicar com o botão direito do rato:

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

{{-}} ![[_media/SourcesCategory-CitationTree-Configure-ColumnsTab-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Fontes - Configurar a vista activa - separador Colunas]] {{#vardefine:viewmode\|Citações em árvore}}

##### Colunas

O separador do diálogo Configurar fontes pode ser utilizado para adicionar, remover e reorganizar as colunas mostradas. Clique em ![[_media/gramps-config.png]] , seleccione Configurar… no menu , ou prima para abrir o diálogo.

##### Dialecto CSV

No separador [Dialecto CSV](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#CSV_Dialect) pode escolher o delimitador a utilizar quando [exporta esta lista](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Export_View).

{{-}}

<span id="Sources List View">

### Lista de fontes

</span>

![[_media/SourcesCategory-SourcesListView-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Fontes - Lista de fontes]]

Por defeito, a lista de fontes mostra o , a e o da fonte, assim como qualquer informação de associada. A lista de fontes pode ser reordenada clicando num título de coluna diferente. Clicar no cabeçalho pela primeira vez ordena as linhas por ordem ascendente com base nessa coluna. Clicar novamente inverte a ordem para ordem decrescente.

Estão disponíveis opções adicionais seleccionando uma fonte da lista e utilizando o menu contextual mostrado ao clicar com o botão direito do rato:

- 

- 

- 

- 

- 

- 

- 

{{-}} ![[_media/SourcesCategory-SourcesList-Configure-ColumnsTab-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Fontes - Configurar a vista activa - separador Colunas]] {{#vardefine:viewmode\|Lista de fontes}}

##### Colunas

O separador do diálogo Configurar fontes pode ser utilizado para adicionar, remover e reorganizar as colunas mostradas. Clique em ![[_media/gramps-config.png]] , seleccione Configurar… no menu , ou prima para abrir o diálogo.

##### Dialecto CSV

No separador [Dialecto CSV](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#CSV_Dialect) pode escolher o delimitador a utilizar quando [exporta esta lista](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Export_View). {{-}}

<span id="Sources Category Bottombar tabs">

### Separadores da barra inferior da categoria Fontes

</span>

A mostra os seguintes separadores na [barra inferior](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar):

#### Gramplet [Galeria](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Gallery)

#### Gramplet [Notas](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Notes)

#### Gramplet [Referências](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#References)

<span id="Sources Category Sidebar tabs">

### Separadores da barra lateral da categoria Fontes

</span>

A mostra os seguintes separadores na [barra lateral](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar):

#### Gramplet [Filtro](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Filter)

{{-}}

<span id="Citations Category">

## Categoria Citações

</span> ![[_media/gramps-citation.png]] A mostra a lista de citações de determinadas informações armazenadas na árvore genealógica.

As citações especificam que partes de uma fonte são relevantes para a informação na base de dados. Por exemplo, uma fonte pode ser um livro, e a citação pode ser uma página específica do livro. O Gramps dá-lhe a opção de fornecer uma citação para cada evento que registar (nascimentos, mortes, casamentos, etc.).

{{-}} <span id="Citations List View">

### Lista de citações

</span>

![[_media/CitationsCategory-CitationsListView-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Citações - Lista de citações]]

A lista de citações mostra os campos , e da citação, bem como a nas citações.

A lista de citações pode ser ordenada clicando num título de coluna. Clicar uma vez ordena por ordem crescente, clicar novamente ordena por ordem decrescente.

Estão disponíveis opções adicionais seleccionando uma citação da lista e usando o menu contextoual mostrado ao clicar com o botão direito do rato:

- 

- 

- 

- 

- 

- 

- 

{{-}} ![[_media/CitationsCategory-CitationsList-Configure-ColumnsTab-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Citações - Configurar a vista activa - separador Colunas]] {{#vardefine:viewmode\|Lista de citações}}

##### Colunas

O separador do diálogo Configurar fontes pode ser utilizado para adicionar, remover e reorganizar as colunas mostradas. Clique em ![[_media/gramps-config.png]] , seleccione Configurar… no menu , ou prima para abrir o diálogo.

##### Dialecto CSV

No separador [Dialecto CSV](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#CSV_Dialect) pode escolher o delimitador a utilizar quando [exporta esta lista](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Export_View). {{-}}

<span id="Citations Category Bottombar tabs">

### Separadores da barra inferior da categoria Citações

</span>

A mostra os seguintes separadores na [barra inferior](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar):

#### Gramplet [Galeria](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Gallery)

#### Gramplet [Notas](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Notes)

#### Gramplet [Referências](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#References)

<span id="Citations Category Sidebar tabs">

### Separadores da barra lateral da categoria Citações

</span>

A mostra os seguintes separadores na [barra lateral](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar):

#### Gramplet [Filtro](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Filter)

{{-}}

<span id="Repositories Category">

## Categoria Repositórios

</span> ![[_media/gramps-repository.png]] A mostra a lista de repositórios. Um repositório pode ser considerado como uma colecção de fontes. Cada fonte na árvore genealógica pode ser uma referência a um repositório (como uma biblioteca) ao qual pertence.

{{-}} ![[_media/RepositoriesCategory-RepositoriesListView-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Repositórios - Lista de repositórios]] <span id="Repository List View">

### Lista de repositórios

</span>

Esta vista mostra uma lista de todos os repositórios registados.

Estão disponíveis opções adicionais seleccionando um repositório da lista e utilizando o menu contextual mostrado ao clicar com o botão direito do rato:

- 

- 

- 

- 

- 

- 

- 

{{-}} ![[_media/RepositoriesCategory-RepositoriesList-Configure-ColumnsTab-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Repositórios - Configurar a vista activa - separador Colunas]] {{#vardefine:viewmode\|Lista de repositórios}}

##### Colunas

O separador do diálogo Configurar fontes pode ser utilizado para adicionar, remover e reorganizar as colunas mostradas. Clique em ![[_media/gramps-config.png]] , seleccione Configurar… no menu , ou prima para abrir o diálogo.

##### Dialecto CSV

No separador [Dialecto CSV](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#CSV_Dialect) pode escolher o delimitador a utilizar quando [exporta esta lista](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Export_View). {{-}}

<span id="Repository Category Bottombar tabs">

### Separadores da barra inferior da categoria Repositórios

</span>

A mostra os seguintes separadores na [barra inferior](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar):

#### Gramplet [Detalhes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Details)

#### Gramplet [Notas](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Notes)

#### Gramplet [Referências](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#References)

<span id="Repository Category Sidebar tabs">

### Separadores da barra lateral da categoria Repositórios

</span>

A mostra os seguintes separadores na [barra lateral](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar):

#### Gramplet [Filtro](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Filter)

{{-}}

<span id="Media Category">

## Categoria Multimédia

</span> ![[_media/gramps-media.png]] A mostra a lista de multimédia, com os objectos armazenados na árvore genealógica. Os objectos multimédia são tecnicamente quaisquer ficheiros que se relacionem de alguma forma com os dados genealógicos armazenados. Mais frequentemente, são imagens, ficheiros de áudio, ficheiros de animação, etc. {{-}} ![[_media/MediaCategory-MediaListView-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Multimédia - Lista de objectos multimédia]] <span id="Media List View">

### Lista de objectos multimédia

</span>

A lista de objectos multimédia mostra, por defeito, as colunas , , , e do objecto multimédia.

Seleccionar um item multimédia da lista e usar o menu contextual (clicando com o botão direito do rato) oferece as seguintes opções:

- 

- 

- \- mostrar o item usando um programa externo

- \- abre a pasta que contém o ficheiro multimédia

- 

- 

- 

- 

- 

{{-}} ![[_media/MediaCategory-MediaList-Configure-ColumnsTab-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Multimédia - Configurar a vista activa - separador Colunas]] {{#vardefine:viewmode\|Lista de objectos multimédia}}

##### Colunas

O separador do diálogo Configurar fontes pode ser utilizado para adicionar, remover e reorganizar as colunas mostradas. Clique em ![[_media/gramps-config.png]] , seleccione Configurar… no menu , ou prima para abrir o diálogo.

##### Dialecto CSV

No separador [Dialecto CSV](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#CSV_Dialect) pode escolher o delimitador a utilizar quando [exporta esta lista](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Export_View). {{-}}

<span id="Media Category Bottombar tabs">

### Separadores da barra inferior da categoria Multimédia

</span>

A mostra os seguintes separadores na [barra inferior](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar):

#### Gramplet [Antevisão](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Media_Preview)

#### Gramplet [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Citations)

#### Gramplet [Notas](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Notes)

#### Gramplet [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Attributes)

#### Gramplet [Image Metadata](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Image_Metadata)

#### Gramplet [Referências](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#References)

<span id="Media Category Sidebar tabs">

### Separadores da barra lateral da categoria Multimédia

</span>

A mostra os seguintes separadores na [barra lateral](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar):

#### Gramplet [Filtro](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Filter)

{{-}}

<span id="Notes Category">

## Categoria Notas

</span> ![[_media/gramps-notes.png]] A mostra uma lista que inventaria as notas de texto (puro ou pré-formatado) que podem ser referenciadas pelos outros objectos.

Ver também:

- [Usar o editor de notas](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/pt_PT#Editing_information_about_notes) para fazer novas anotações ou editar informações sobre notas existentes.

{{-}} ![[_media/NotesCategory-NotesListView-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Notas - Lista de notas]] <span id="Notes List View">

### Lista de notas

</span>

Esta é uma lista de notas de texto. A sua funcionalidade é semelhante à das outras listas, contendo todas as gravadas na árvore genealógica.

O pode ser ([entre outros](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/pt_PT#note_type)): *Nota de evento*, *Nota de endereço*, *Texto de origem*, *Nota de local*. Na versão 6.0, a lista interna inclui: *Citação*, *Personalizado*, *Geral*, *Código HTML*, *Ligação*, *Relatório*, *Pesquisa*, *Texto fonte*, *Para fazer*, *Transcrição* e *Desconhecido*.

Seleccionar um item de nota da lista e utilizar o menu contextual clicando com o botão direito do rato, oferece as seguintes opções:

- 

- 

- 

- 

- 

- 

- - 

  - 

Clicar duas vezes numa nota na lista abrirá a janela do [editor de notas](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/pt_PT#Note_editor_dialog) onde pode editar a nota. Pode alterar os tipos de letra, a cor da letra e a cor de fundo. Está disponível um [corrector ortográfico](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Environment_Settings) para *Inglês* e o seu idioma. {{-}} ![[_media/NotesCategory-MediaList-Configure-ColumnsTab-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Notas - Configurar a vista activa - separador Colunas]] {{#vardefine:viewmode\|Lista de notas}}

##### Colunas

O separador do diálogo Configurar fontes pode ser utilizado para adicionar, remover e reorganizar as colunas mostradas. Clique em ![[_media/gramps-config.png]] , seleccione Configurar… no menu , ou prima para abrir o diálogo.

##### Dialecto CSV

No separador [Dialecto CSV](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#CSV_Dialect) pode escolher o delimitador a utilizar quando [exporta esta lista](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Export_View). {{-}}

<span id="Notes Category Bottombar tabs">

### Separadores da barra inferior da categoria Notas

</span>

A mostra os seguintes separadores na [barra inferior](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar):

#### Gramplet [Referências](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#References)

<span id="Media Category Sidebar tabs">

### Separadores da barra lateral da categoria Notas

</span>

A mostra os seguintes separadores na [barra lateral](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Bottombar_and_Sidebar):

#### Gramplet [Filtro](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Filter)

{{-}}

[Category:Pt PT:Documentation](wiki:Category:Pt_PT:Documentation)
