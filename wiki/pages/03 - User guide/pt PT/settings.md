---
title: Gramps 6.0 Wiki Manual - Settings/pt PT
categories:
- Pages with broken file links
- Pt PT:Documentation
- Stub
- Tips
managed: false
source: wiki-scrape
wiki_revid: 113361
wiki_fetched_at: '2026-05-30T19:51:52Z'
lang: pt PT
---

{{#vardefine:chapter\|15}} {{#vardefine:figure\|0}} Esta secção trata de várias definições que pode gerir no Gramps.

<span id="Preferences">

## Preferências

</span> ![[_media/EditPreferencesTabsOnly-overview-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Visão geral de todos os separadores das preferências]]

A maioria das configurações que afectam todo o programa Gramps são configuradas no diálogo . Para o chamar, seleccione .

Existem substituições que podem ser definidas *antes* de executar o Gramps (como definir o idioma mostrado no ambiente de trabalho ou para relatórios) que podem ser definidas temporariamente ou permanentemente a partir da [linha de comandos](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/pt_PT).

Para opções de configuração que se limitam à vista actual ou ao conjunto de gramplets, seleccione , clique em ![[_media/Gramps-config.png]], ou prima o [atalho de teclado](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT#Common_keybindings) .

Os separadores na parte superior apresentam as categorias de opções disponíveis da seguinte forma:

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

Também podem ser mostrados *outros* separadores adicionais a partir de quaisquer [extensões](wiki:6.0_Addons#Addon_List) que possa ter instalado. {{-}} <span id="Data">

### Separador Dados

</span> ![[_media/EditPreferences-Data-tab-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Preferências - separador Dados]] O separador contém as preferências relevantes para as duas secções seguintes:

- 

- 

{{-}} <span id="Display Options">

#### Opções de exibição

</span> ![[_media/EditPreferences-Data-tab-DisplayOptions-section-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Preferências - separador Dados - opções de exibição]] A secção contém as seguintes opções:

- Esta opção controla a exibição dos locais.

Esta funcionalidade foi identificada como "Activar a geração automática de títulos de local" na revisão 5.0 e como "Formato de local (título de local automático)" na revisão 5.1. A [hierarquia de locias](wiki:Gramps_4.1_Wiki_Manual_-_What&#39;s_new?/pt_PT#Place_hierarchies) foi novidade na versão [4.1.0](wiki:Template:Releases/4.1.0) e o separador [Locais](wiki:Gramps_4.2_Wiki_Manual_-_Settings/pt_PT#Places) nas preferências só existiu na versão 4.2. Prevêem-se revisões importantes das hierarquias de locais, pelo que é provável que estas opções sejam novamente relocalizadas e renomeadas.

- - **Completo** (pré-definição)
    - Clicar em abre o

- Esta opção controla a visualização das coordenadas (veja [Formatos de longitude/latitude suportados](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/pt_PT#Supported_longitude.2Flatitude_formats))

  - **DEG Graus, minutos e segundos** (pré-definição)
  - DEG-: Graus, minutos e segundos com:
  - D.D4 Graus com 4 casas decimais
  - D.D8 Graus, 8 casas decimais (precisão tipo ISO-DMS)
  - RT90 Formato de saída para o [sistema de coordenadas sueco RT90](https://en.wikipedia.org/wiki/Swedish_grid)

- Esta opção controla a exibição de nomes na base de dados actual (a configuração é gravada na base de dados e não é válida para todo o sistema). No Gramps existem dois tipos de formatos de exibição de nomes: os pré-definidos e os personalizados . Estão disponíveis vários formatos de nomes pré-definidos diferentes: **""Apelido, Nome próprio Sufixo"** (pré-definição), **"Nome próprio Apelido Sufixo"**, **"Nome próprio"**, **"Principal\[ape\] Principal\[con\] Não Patronímico, Nome próprio Patronímico\[ape\] Sufixo Principal\[nome\]"**, **"APELIDO, Nome próprio (Comum)"**

  - Clicando em abrirá uma janela onde a lista de opções disponíveis é mostrada. O formato é dado, bem como um exemplo. Quando os formatos pré-definidos não são adequados, é possível definir o seu próprio formato. Pode utilizar o botão para adicionar um formato de nome à lista. Clicando uma vez, obtém-se um formato **APELIDO, Nome próprio Sufixo (chamada)** e, como exemplo: **SILVA, Eduardo José Sr (Ed)**. Se adicionou novos formatos de nomes à lista, os botões e ficam disponíveis para alterar a lista de formatos de nomes.
    -   
      caixa desmarcada por defeito. Se marcada, permite que o Gramps considere os nomes patronímicos e matronímicos como apelidos.

- Esta opção controla a exibição de datas. É uma configuração global, , e aplica-se à exibição de datas em todas a sbases de dados até que o formato de data seja alterado novamente. Estão disponíveis vários formatos diferentes, que dependerão da sua localização:

  - **AAAA-MM-DD (ISO)** (pré-definição) - 2020-01-01 - Mostra a data utilizando a norma internacional [ISO 8601 Data elements and interchange formats – Information interchange](https://wikipedia.org/wiki/ISO_8601) particularmente útil quando se partilham dados entre países com convenções diferentes para escrever datas e horas numéricas;
  - Numérica;
  - Mês Dia, Ano
  - MÊS Dia, Ano
  - Dia Mês Ano
  - Dia MÊS Ano

<!-- -->

- 

  - **Anos** (pré-definição)
  - Anos, Meses
  - Anos, Meses, Dias

- 

- 

<!-- -->

- **Gregoriano** (pré-definição). Esta opção controla a apresentação do calendário em relatórios, ferramentas, gramplets e vistas. Estão disponíveis vários calendários diferentes (ver [Editar datas](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_1/pt_PT#Editing_dates)). Duas datas com dois calendários diferentes não mostrarão corretcamente a cronologia ou o período (por exemplo, ao utilizar o calendário gregoriano como calendário pré-definido, os utilizadores terão uma melhor coerência na apresentação das datas no período).

- **Gregoriano** (pré-definição).

- **No dia anterior** (pré-definição).

- Esta opção controla a informação apresentada na barra de estado. Pode ser Nome e ID do **[indivíduo activo](wiki:Gramps_Glossary#active_person)** (pré-definição) ou **Parentesco com o [indivíduo inicial](wiki:Gramps_Glossary#home_person)**.

<!-- -->

- **Legado** (pré-definição). Seleccione entre as extensões disponíveis para a composição e visualização dos dados da citação. A extensão interna [CITE](wiki:Addon_list_legend#cite) é compatível com a versão 5.1.6 e anteriores.

<span id="Place Format Editor">

##### Editor de formato de local

</span>

![[_media/EditPreferences-Data-tab-Display-section-PlaceFormatEditor-dialog-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editor de formato de local]]

Accedido a partir de , secção [Opções de exibição](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Display_Options), opção *Automatizar formato de local*.

Este separador contém as preferências relevantes para a forma como os locais devem ser mostrados:

- um nome único para o formato do local;

- os nomes de local a mostrar; cada nível na hierarquia é representado por um número inteiro positivo, começando com 0 para o local seleccionado e aumentando em 1 para cada nível acima na hierarquia; os níveis também podem ser representados por números inteiros negativos, começando com -1 para o nível superior (normalmente um país) e diminuindo 1 para cada nível inferior na hierarquia; além disso, o local povoado (cidade, vila, aldeia ou lugar) é representado pela letra p; pode ser utilizado com um desvio (e.g. p+1 ou p-2); os nomes a mostrar são definidos como uma lista de intervalos separada por vírgulas; um intervalo pode ser um nível único, ou um nível inicial e um nível final separados por dois pontos; o nível inicial deve ser menor que o nível final num intervalo; os níveis inicial e final são pré-definidos como 0 e -1 se não existirem.

- "Nenhum" (pré-definição), "Rua número" ou "Número de rua"; opção para concatenar o número e a rua de modo a suprimir a vírgula; para que esta opção funcione, a rua deve ter the [<strong>tipo</strong>](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/pt_PT#Place_Editor_dialog) *Rua* e o número de porta deve ter o **tipo** *Número*.

- (vazio por defeito) um código de idioma de dois caracteres.

-  (caixa desmarcada por defeito)

Veja tanbém:

- [Diálogo Editor de local](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/pt_PT#Place_Editor_dialog)
- [Diálogo Editor de nomes de local](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/pt_PT#Place_Name_Editor_dialog)

{{-}}

<span id="Display Name Editor">

##### Editor de formato de nomes

</span>

![[_media/EditPreferences-Data-tab-DisplayOptions-section-DisplayNameEditor-dialog-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editor de formato de nomes]] As palavras-chave a seguir são substituídas pela parte do nome apropriada:

- <b>Nome próprio</b> - primeiro nome e outros;
- <b>Título</b> - título (Dr., Sr.);
- <b>Usual</b> - como é chamado;
- <b>Iniciais</b> - primeiras letras dos nomes;
- <b>Principal, Principal\[nom\] ou \[ape\] ou \[con\]</b> - apelido principal completo, prefixo, só apelido, conector;
- <b>Patronímico, ou \[nom\] ou \[ape\] ou \[con\]</b> - apelido pa/matronímico completo, prefixo, só apelido, conector;
- <b>Diminutivo</b> - diminutivo familiar;
- <b>Resto</b> - apelidos secundários;
- <b>Apelidosbrutos</b> - apelidos (sem prefixos/conectores);
- <b>Apelido</b> - apelidos (com prefixos/cnnectores);
- <b>Sufixo</b> - sufixo (Jr., Sr.);
- <b>Alcunha</b> - alcunha;
- <b>Comum</b> - alcunha como primeira opção se existir, usual como segunda opção, caso contrário primeiro nome;
- <b>Prefixo</b> - todos os prefixos (von, de);
- <b>Nãopatronímico</b> - todos os apelidos, excepto pa/matronímico e principal;

. Parênteses extra e vígulas são removidos. Qualquer outro texto aparece literalmente.

![[_media/NameEditor-format_reference_example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editor de nome a mostrar]]

**Exemplo:** Dr. Edwin Jose von der Smith and Weston Wilson Sr (“Ed”) - Underhills *Edwin Jose*: nome próprio, *von der*: prefixo, *Smith* and *Weston*: principal, *e*: <abbr title="um conector">\[con\]</abbr>, *Wilson*: patronímico, *Dr.*: título, *Sr*: sufixo, *Ed*: alcunha, *Underhills* <abbr title="diminutivo familiar">familiar</abbr>, Jose <abbr title="chamado (nome próprio preferido)">usual</abbr>.

Todos os campos do exemplo, excepto o diminutivo familiar, podem ser adicionados no diálogo padrão do editor de indivíduos. No separador Nomes desse editor, faça duplo clique no nome preferido para aceder a campos adicionais, incluindo: o diminutivo familiar, controlos de agrupamento, controlos de ordenação e visualização de excepções e controlos de intervalo de datas para utilizar num nome específico.

Dispõe ainda, neste editor de nomes a mostrar, de três botões ao fundo, para abrir esta página, para cancelar a edição e para sair do editor gravando as alterações.

{{-}}

<span id="Input Options">

#### Opções de entrada

</span>

![[_media/EditPreferences-Data-tab-InputOptions-section-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Preferências - separador Dados - opções de entrada]]

- <span id="surname guessing"><span> esta opção afecta o apelido inicial de um filho quando é adicionado à árvore genealógica:
  - **Apelido do pai** (pré-definição) - utilizará o apelido do pai;
  - *Nenhum* - significa que não se tentará adivinhar o apelido;
  - *Combinação dos apelidos da mãe e do pai* - utiliza o nome do pai seguido do nome da mãe;
  - *[Estilo islandês](https://wikipedia.org/wiki/Icelandic_name)* - utilizará o nome próprio do pai seguido do sufixo "sson" (por exemplo, o filho de Edwin será adivinhado como Edwin*sson*).

.

- \- usada pelo diálogo .

  - **Desconhecido** (pré-definição)
  - *Casados*
  - *Não casados*
  - *União de facto*

<!-- -->

-   
  Santos dos Últimos Dias.

{{-}}

<span id="General">

### Separador Geral

</span>

![[_media/EditPreferences-General-tab-EnviromentSettings-section-default-60-pt_PT.png|Right|thumb|450px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Preferências - separador Geral]]

Este separador contém uma secção com preferências relevantes para o funcionamento geral do programa.

<span id="Environment Settings">

#### Definições do ambiente

-   
  esta caixa controla a activação e desactivação do diálogo :

<!-- -->

-   
  marcar esta caixa faz com que a última base de dados utilizada seja carregada no arranque. Ignora o diálogo **Gerir árvores genealógicas**.

<!-- -->

-   
  esta caixa controla a activação e desactivação de exibição da última [categoria](wiki:Gramps_Glossary#view). A activação leva-o para a categoria/vista onde parou o programa pela última vez.

<!-- -->

-   
  esta caixa controla a activação e desactivação da verificação ortográfica global nas notas. O pacote **[gspell](https://gitlab.gnome.org/GNOME/gspell)** deve ser carregado para que isto tenha efeito.[1](https://github.com/gramps-project/gramps/pull/1450) (Veja: [Troubleshoot Spellcheck](wiki:Troubleshoot_Spellcheck) )

Nota: a opção Editar -\> Preferências activa o Inglês global ou o idioma em que o Gramps é executado e o menu de contexto da nota é por nota no idioma seleccionado à sua escolha.

-   
  esta caixa controla se é ou não apresentada uma descrição de texto junto ao ícone no [navegador](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Navigator) na [janela principal](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Main_Window); entra em vigor depois de o programa ter sido reiniciado.

<!-- -->

- 

- 

- 

- 

- 

<!-- -->

- Se instalou a extensão ***Tema***, terá a opção disponível, com uma lista dos vários estilos disponíveis. Ver [Tema](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Themes)

<!-- -->

- 

<!-- -->

- Pré-definição: `<b>%s</b>`

  - As marcações de conveniência são:
    - <b>\<b\>Negrito\</b\></b>
    - <big>\<big\>Aumenta o tamanho da letra\</big\></big>
    - <i>\<i\>Itálico\</i\></i>
    - <s>\<s\>Rasurado\</s\></s>
    - <sub>\<sub\>Subscrito\</sub\></sub>
    - <sup>\<sup\>Sobrescrito\</sup\></sup>
    - <small>\<small\>Reduz o tamanho da letra\</small\></small>
    - `<tt>Letra mono-espaçada</tt>`
    - <u>\<u\>Sublinhado\</u\></u>
      - Por exemplo: \<u\>\<b\>%s\</b\>\</u\> mostrará a <u><b>data sublinhada a negrito</b></u>.

<!-- -->

- Pré-definição: `150` pixels

![[_media/TipOfTheDay-dialog--example-WhatsThatFor-60-pt_PT.png|Right\|thumb\|400px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Diálogo Dica do dia]] <span id="Tip of the Day dialog">

#### Diálogo Dica do dia

</span>

Quando activado no separador das , o diálogo mostrra sugestões úteis.

Estão disponíveis as seguintes opções:

-  (marcada depois de activada) - desmarque-a, se não desejar ver este diálgo.

- \- Passa à dica seguinte.

- \- sai por esta sessão e até que o Gramps seja reiniciado (ou seja reactivada no menu .

{{-}}

<span id="Family Tree">

### Árvore genealógica

</span>

![[_media/EditPreferences-FamilyTree-tab-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Preferências - separador Árvore genealógica]]

O separador contém as seguintes secções:

<span id="Database Settings">

#### Configuração da base de dados

</span>

- - **[SQLite](wiki:Gramps_Glossary#sqlite)** (*pré-definição*) - o [motor de base de dados DB-API](wiki:motor_de_base_de_dados_DB-API);
  - ... se estiverem instaladas outras extensões de motores de bases de dados, serão adicionadas à lista <abbr title="exempli gratia - frase latina significando 'por exemplo'">e.g.</abbr>: [PostgreSQL](wiki:Addon:PostgreSQL).

O motor de base de dados antigo *[BSDDB](wiki:Gramps_Glossary#bsddb)* do Gramps foi abandonado com o Gramps 5.1.

Veja também:

- Extensão [PostgreSQL](wiki:Addon:PostgreSQL) - adiciona suporte experimental para bases de dados PostgreSQL. Recomendado só para peritos!

<span id="Database Location">

#### Localização da base de dados

</span>

- \- Endereço do servidor ou endereço IP de outro computador para a localização da base de dados.

- \- Número da porta para aceder à base de dados do anfitrião

- \- A menos que tenha uma razão concreta para alterar isto, mantenha o caminho pré-definido. O caminho padrão onde as bases de dados são armazenadas é `grampsdb` dentro da [pasta do utilizador](wiki:Gramps_6.0_Wiki_Manual_-_User_Directory/pt_PT).

<span id="Backup Management">

#### Gestão de salvaguardas

- \- Local onde graar os ficheiros de salvaguardas do Gramps.

- \- Marcar esta caixa salvaguarda a sua árvore ao encerrar o Gramps. O ficheiro é gravado no caminho especificado acima. O nome do ficheiro corresponderá ao da árvore genealógica, acrescido da data e hora actuais.

- \- Intervalo de tempo para activar salvaguardas completas durante as sessões de edição no Gramps.

  - **Nunca** (*pré-definição*)
  - Cada 15 minutos
  - Cada 30 minutos
  - Cada hora
  - Cada 12 horas
  - Cada dia

{{-}}

Veja também:

- [Salvaguardar uma árvore genealógica](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Backing_up_a_Family_Tree)
- [Omissões na salvaguarda](wiki:Template:Backup_Omissions) - o que não é incluído numa salvaguarda

<span id="Family Tree's Media path">

#### Caminho da multimédia da árvore

</span>

- aqui pode preencher um caminho de base para os objectos multimédia. Se clicar em , obtém um diálogo , onde pode preencher o caminho adequado.

Veja também:

- [](wiki:Gramps_6.0_Wiki_Manual_-_Tools/pt_PT#Media_Manager), um grupo de ferramentas, duas das quais permitem:
  - 

  - 

![[_media/EditPreferences-FamilyTree-tab-SelectMediaPath-60-pt_PT.png|Fig. {{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Selector de pasta da multimédia - Clique direito sobre um dos objectos]] <span id="Select media directory dialog">

##### Diálogo Seleccionar pasta da multimédia

</span>

É um selector de ficheiros habitual, onde escolher a localização da pasta com o rato ou com o teclado. Pode a escolha, ou a escolha.

Veja [Selector de ficheiros](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#File_Chooser). {{-}}

![[_media/Broken_Media_Path-60-pt_PT.png|Fig. {{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Objecto multimédia com o caminho errado]] <span id="Missing Media Objects 'broken link' icon of a box with a red 'x'">

##### Objecto multimédia em falta

</span>

Se a antevisão de miniaturas mostrar o ícone de "ligação quebrada" (caixa com um "x" vermelho), terá de corrigir o da sua árvore genealógica na secção .

Veja também:

- [Ligação aos objectos multimédia de exemplo](wiki:Example.gramps#Connecting_to_the_example_Media_Objects)

{{-}}

![[_media/EditPreferences-Import-tab-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Preferências - separador Importar]] <span id=Import">

### Importar

</span>

O separador tem as seguintes secções:

<span id="Tag Records">

#### Etiquetar registos

- (pré-definição: `Importado em %Y/%m/%d %H:%M:%S` ). ****

**Nota - Adicionar uma [etiqueta](wiki:Gramps_Glossary#tag) de data/hora na importação pode abrandar significativamente a importação dos seus dados, mas é útil para a limpeza de dados subsequente.**

<span id="Source GEDCOM import">

#### Fonte na importação GEDCOM

</span>

-   
  esta opção afecta a importação de [dados Gedcom](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#GEDCOM_import). Se marcada, cada item importado conterá uma referência ao ficheiro importado como sendo uma [fonte](wiki:Gramps_Glossary#source).

**Nota - Adicionar uma fonte pré-definida na importação pode abrandar significativamente a importação dos seus dados, mas é útil para a limpeza de dados subsequente.**

{{-}}

![[_media/EditPreferences-Limits-tab-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Preferências - separador Limites]] <span id=Limits">

### Limites

</span>

<span id="Calculation limits">

#### Limites de idades

</span>

Nesta secção pode estabelecer os limites de cálculo de idades, abaixo ou acima dos quais o Gramps entenderá como possível erro, disparando um aviso.

- `50`

  - define o n.º de anos acima ou abaixo da data "`Cerca de `<data do evento>" considerados válidos como filtro;
    - utilizado no cálculo da idade do indivíduo;

- `50`

  - define o n.º de anos após a data "`Depois de `<data do evento>" considerados válidos como filtro;
    - utilizado no cálculo da idade do indivíduo;

- `50`

  - define o n.º de anos antes da data "`Antes de `<data do evento>" considerados válidos como filtro;
    - utilizado no cálculo da idade do indivíduo;

- `110`

  - Na ausência de um evento de óbito, a idade à qual o Gramps considerará que o indivíduo já faleceu;

- `20`

- `13`

- `20`

- pode inserir o número de gerações para determinar parentescos; A pré-definiçãp é `15`; limita o âmbito das funcionalidades da [Calculadora de parentesco](wiki:Gramps_6.0_Wiki_Manual_-_Tools/pt_PT#Relationship_Calculator).

Veja também:

- [Provavelmente vivo](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive/pt_PT)
- [Editar datas](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/pt_PT#Editing_dates)
- Configurar o ficheiro [.ini de aproximação de datas](wiki:Match_dates#Changing_after.2Fbefore.2Fabout_range) manualmente

{{-}}

![[_media/EditPreferences-Colors-tab-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Preferências - separador Cores]] <span id="Colors">

### Cores

</span>

Este separador está dividido em sete secções, que permitem uma escolha apurada das ***cores das caixas utilizadas em representações gráficas***.

Pode personalizar cada uma das cores utilizando o diálogo [Escolha uma cor](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Pick_a_Color_selector).

<span id="Colors used for boxes in the graphical views">

#### Cores usadas para as caixas nas vistas gráficas

</span>

Pode optar entre um com as opções:

  
  
*Cores claras*;

*Cores escuras*.

- Se clicar em , as cores das caixas serão repostas nos valores originais.

<span id="Colors for Male persons">

#### Cores para indivíduos de sexo masculino

</span>

Pode definir os fundos e contornos das caixas para indivíduos vivos e falecidos. Clicar na cor mostrada abre o diálogo [Escolha uma cor](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Pick_a_Color_selector). Para cada cor é também mostrado o código hexadecimal da cor, utilizado em páginas da Internet, entre outras situações.

<span id="Colors for Female persons">

#### Cores para indivíduos de sexo feminino

</span>

Pode definir os fundos e contornos das caixas para indivíduos vivos e falecidos. Clicar na cor mostrada abre o diálogo [Escolha uma cor](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Pick_a_Color_selector). Para cada cor é também mostrado o código hexadecimal da cor, utilizado em páginas da Internet, entre outras situações.

<span id="Colors for people who are neither male nor female">

#### Cores para indivíduos não são homem nem mulher

</span>

Pode definir os fundos e contornos das caixas para indivíduos vivos e falecidos. Clicar na cor mostrada abre o diálogo [Escolha uma cor](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Pick_a_Color_selector). Para cada cor é também mostrado o código hexadecimal da cor, utilizado em páginas da Internet, entre outras situações.

<span id="Colors for Unknown persons">

#### Cores para indivíduos de sexo desconhecido

</span>

Pode definir os fundos e contornos das caixas para indivíduos vivos e falecidos. Clicar na cor mostrada abre o diálogo [Escolha uma cor](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Pick_a_Color_selector). Para cada cor é também mostrado o código hexadecimal da cor, utilizado em páginas da Internet, entre outras situações.

<span id="Colors for Family nodes">

#### Cores para nós familiares

</span>

Pode definir os fundos e contornos das caixas para indivíduos casados, solteiros, juntos, em situação desconhecida, ou divorciados. Clicar na cor mostrada abre o diálogo [Escolha uma cor](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Pick_a_Color_selector). Para cada cor é também mostrado o código hexadecimal da cor, utilizado em páginas da Internet, entre outras situações.

<span id="Other colors">

#### Outras cores

</span>

Pode definir o fundo da caixa do indivíduo inicial, que recebe uma cor especial. {{-}}

<span id="Genealogical Symbols">

### Símbolos genealógicos

![[_media/EditPreferences-GenealogicalSymbols-tab-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Preferências - separador Símbolos genealógicos]]

Permite-lhe utilizar símbolos genealógicos em vez de abreviaturas de texto em relatórios, gráficos e no ambiente do Gramps.

Este separador dá-lhe a possibilidade de utilizar um tipo de letra que é capaz de mostrar todos os símbolos genealógicos (uma vez configurado, ver: [Pré-requisito para utilizar símbolos genealógicos](#Prerequisite_to_use_Genealogical_Symbols)).

Se marcar a caixa "", o Gramps utilizará o tipo de letra seleccionado, caso exista. Isto pode ser útil se pretender adicionar fonética numa nota para mostrar como se pronuncia um nome ou se misturar vários idiomas, como o grego e o russo. Neste separador, só pode configurar o símbolo pré-definido de óbito.

Na figura {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}}}}} pode-se ver uma lista dos símbolos genealógicos. A sua correspondência é mostrada ao pairar com o rato sobre cada um deles.

| significado      | símbolo | código Unicode | nome                              |
|------------------|---------|----------------|-----------------------------------|
| masculino        | ♂       | U+2642         | masculino                         |
| feminino         | ♀       | U+2640         | feminino                          |
| desconhecido     | ⚪︎      | U+26AA         | Círculo branco médio              |
| hermafrodita     | ⚥       | U+26A5         | masculino e feminino entrelaçados |
| neutro           | ⚲       | U+26B2         | Neutro                            |
| nascimento       | \*      | U+002A         | Asterisco                         |
| baptismo         | ~       | U+007E         | Til                               |
| óbito            | ✝︎       | U+271D         | Cruz latina                       |
| funeral          | ⚰︎       | U+26B0         | Caixão                            |
| cremação         | ⚱︎       | U+26B1         | Urna funerária                    |
| nado morto       | ✝︎\*     | U+0086 U+002A  | Cruz latina, asterisco            |
| ilegítimo        | \*⃝      | U+002A U+20DD  | Asterisco em círculo              |
| ilegítimo        | ⊛       | U+229B         | Operador de asterisco em círculo  |
| morto em serviço | ⚔︎       | U+2694         | Espadas cruzadas                  |
| linha extinta    | ‡       | U+2021         | Dupla faca                        |
| aproximadamente  | ±       | U+00B1         | Mais-Menos                        |
| antes            | \<      | U+003C         | Menor que                         |
| depois           | \>      | U+003E         | Maior que                         |
| noivado          | ⚬       | U+26AC         | Círculo médio-pequeno branco      |
| casamento        | ⚭       | U+26AD         | Símbolo de casamento              |
| divórcio         | ⚮       | U+26AE         | Símbolo de divórcio               |
| união            | ⚯       | U+26AF         | Símbolo de união de facto         |

{{-}} <span id="Prerequisite to use Genealogical Symbols">

#### Pré-requisito para utilizar símbolos genealógicos

</span>

![[_media/EditPreferences-GenealogicalSymbols-tab-default-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Preferências - separador Símbolos genealógicos - Sem letra]] ![[_media/EditPreferences-GenealogicalSymbols-FindFont-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Símbolos genealógicos - Procurar letras]] <span id="Initial setup">

##### Configuração inicial

</span>

Se o [pré-requisito fontconfig](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Prerequisite) foi instalado, no separador clique em , o Gramps tentará detectar quaisquer fontes de texto unicode adequadas que possam ser usadas.

Quando a procura estiver concluída, seleccione uma letra da lista e, em seguida, marque a caixa:

<span id="Prerequisite">

##### Pré-requisito

</span>

Pré-requisito **python-fontconfig**: são necessárias as ligações Python ao fontconfig e suas dependências para a exibição dos símbolos genealógicos.

Veja também:

- Tamura Jones expõe [Genealogical Symbols](https://www.tamurajones.net/GenealogySymbols.xhtml) *(a secção "Unicode" é particularmente relevante)*;
- [GEPS 039: Símbolos genealógicos no Gramps](wiki:GEPS_039:_Genealogical_symbols_in_gramps);
- Pedido de funcionalidade: o Gramps deve poder utilizar símbolos genealógicos em todo o lado;
- [Personalizar a tabela de pesquisa de símbolos genealógicos](wiki:Customize_the_Genealogical_Symbols_lookup_table) localizada na [pasta do utilizador Gramps](wiki:Gramps_6.0_Wiki_Manual_-_User_Directory/pt_PT#MS_Windows) em: [gramps\gen\utils\symbols.py](https://github.com/gramps-project/gramps/blob/maintenance/gramps51/gramps/gen/utils/symbols.py)

{{-}}

<span id="ID Formats">

### Formatos de identificadores

</span>

![[_media/EditPreferences-IDFormats-tab-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Preferências - separador Formatos de ID]]

Este separador contém as preferências relevantes para a geração automática de identificadores Gramps:

- fornece o modelo para gerar identificadores para um indivíduo; pré-definição: `I%04d`;

- fornece o modelo para gerar identificadores para uma família; pré-definição: `F%04d`;

- fornece o modelo para gerar identificadores para um local; pré-definição: `P%04d`;

- fornece o modelo para gerar identificadores para uma fonte; pré-definição: `S%04d`;

- fornece o modelo para gerar identificadores para uma citação; pré-definição: `C%04d`;

- fornece o modelo para gerar identificadores para um objecto multimédia; pré-definição: `O%04d`;

- fornece o modelo para gerar identificadores para um evento; pré-definição: `E%04d`;

- fornece o modelo para gerar identificadores para um repositório; pré-definição: `R%04d`;

- fornece o modelo para gerar identificadores para uma nota; pré-definição: `N%04d`.

Pode usar a ferramenta [Reordenar IDs Gramps](wiki:Gramps_6.0_Wiki_Manual_-_Tools/pt_PT#Reorder_Gramps_ID) para alterar o formato. {{-}}

<span id="Text">

### Texto

</span>

![[_media/EditPreferences-Text-tab-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Preferências - separador Texto]]

Este separador contém as preferências relevantes para a forma como os nomes e registos em falta e privados devem ser mostrados:

- pré-definido como **`[Apelido em falta]`**; pode alterar esta opção para \[--\] ou o que for mais conveniente para si;

- pré-definido como **`[Nome próprio em falta]`**; pode alterar esta opção para \[--\] ou o que for mais conveniente para si;

- pré-definido como **`[Registo em falta]`**; pode alterar esta opção para \[--\] ou o que for mais conveniente para si;

- pré-definido como **`[Vivo]`**; pode alterar esta opção para \[--\] ou o que for mais conveniente para si;

- pré-definido como **`[Vivo]`**; pode alterar esta opção para \[--\] ou o que for mais conveniente para si;

- pré-definido como **`[Registo privado]`**; pode alterar esta opção para \[--\] ou o que for mais conveniente para si;

{{-}}

<span id="Warnings">

### Avisos

</span>

![[_media/EditPreferences-Warnings-tab-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Preferêmcias - separador Avisos]]

Este separador controla a apresentação de diálogos de aviso, permitindo a reactivação de diálogos que tenham sido desactivados:

- . Veja o [diálogo](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference/pt_PT#Suppress_warning_when_adding_parents_to_a_child);

- Veja o [diálogo](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference/pt_PT#Suppress_warning_when_cancelling_with_changed_data);

- Veja o [diálogo](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference/pt_PT#Suppress_warning_about_missing_researcher_when_exporting_to_GEDCOM);

- ;

- Veja o [diálogo](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference#Module_not_loaded_warnings).

Veja a página [Referência de erros e avisos](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference/pt_PT) para exemplos. {{-}}

<span id="Researcher">

### Investigador

</span> ![[_media/EditPreferences-Researcher-tab-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Preferências - separador Investigador]]

Este separador permite nos campos de entrada de texto correspondentes. Embora o Gramps solicite informações sobre si, estas informações são utilizadas apenas para que o Gramps possa criar ficheiros de saída Gedcom válidos. Um ficheiro Gedcom válido requer informações sobre o seu criador. Se preferir, pode deixar as informações vazias, mas nenhum dos seus ficheiros Gedcom exportados será válido.

Os campos de entrada de texto disponíveis são (todos em branco por defeito)):

- 

- 

- 

- 

- 

- 

- 

- 

- 

As informações inseridas neste separador funcionam como valor pré-definido para valores específicos da árvore genealógica que podem ser ajustados com a ferramenta [Editar a informação do dono da base de dados](wiki:Gramps_6.0_Wiki_Manual_-_Tools/pt_PT#Edit_Database_Owner_Information). {{-}}

<span id="Other settings">

## Outras definições

</span>

Além do diálogo , existem outras definições disponíveis no Gramps. Por várias razões, estas foram tornadas mais facilmente acessíveis, tal como indicado abaixo. {{-}} <span id="Column Editor">

### Editor de colunas

</span>

![[_media/ConfigureTheActiveView-icon-on-toolbar-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Seleccionar o botão]] {{-}} ![[_media/ColumnEditor-dialog-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo Editor de colunas - Categoria indivíduos]] ![[_media/ConfigurePersonView-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo Editor de colunas - Categoria indivíduos - Linha Última alteração arrastada]]

As colunas das vistas de lista podem ser adicionadas, removidas ou reordenadas num diálogo .

Para usar o da vista activa, escolha , ou clique em ![[_media/Gramps-config.png]], ou prima o [atalho de teclado](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT#Common_keybindings) .

Apenas as colunas com uma caixa de verificação marcada serão mostradas na vista. Também pode alterar a posição de uma coluna na vista, clicando e arrastando-a para uma nova posição no editor ([*drag and drop*\|arrastar e largar](https://wikipedia.org/wiki/Drag-and-drop)). Depois de fazer as alterações pretendidas, clique em e, em seguida, clique em para sair do editor e ver as alterações na vista. Por defeito, a vista de lista mostra várias colunas de informação sobre a respectiva categoria. A chave de ordenação pré-definida para a vista (sempre ascendente( é o campo mais à esquerda (isto é, no topo do editor de colunas), pelo que alterar o campo que está nessa posição afecta a ordenação pré-definida.

O diálogo terá uma selecção diferente de colunas para cada categoria de vista que apresente uma tabela simples. As alterações só serão aplicadas quando o botão for clicado. Uma vez aplicadas as alterações às colunas da vista, clicar uma vez no cabeçalho da coluna ordena por ordem crescente, clicar novamente ordena por ordem decrescente.

O subconjunto de colunas e os [filtros](wiki:Gramps_6.0_Wiki_Manual_-_Filters/pt_PT) actuais também restringem os dados exportados via . As colunas e registos ocultos não serão exportados. {{-}}

<span id="Sorting columns">

### Ordenar colunas

</span>

![[_media/PeopleCategory-PeopleListView-SortedByBirthDateColumn-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ordenação por data de nascimento]]

Por defeito, cada vista de categoria que mostre dados numa disposição de tabela, ordenará as linhas por ordem ascendente com base nos dados da primeira coluna (mais à esquerda). Se a tabela tiver linhas agrupadas, os dados agrupados serão sub-ordenados. *Tabelas em subconjuntos de dados com separadores, editores e selectores funcionarão de forma semelhante.* Clique uma vez num cabeçalho de coluna diferente para ordenar os dados dessa coluna por ordem ascendente. Clique novamente no cabeçalho para ordenar por ordem inversa.

O pode ser utilizado para adicionar, remover e reorganizar as colunas mostradas. A selecção de uma primeira coluna diferente fará com que essa seja a nova coluna de ordenação pré-definida da vista (embora sempre ascendente). {{-}}

<span id="Setting Home person">

### Definir o indivíduo inicial

</span>

![[_media/MenuEdit-SetHomePerson-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu Editar - Definir indivíduo inicial]]

Para definir o [indivíduo inicial](wiki:Gramps_Glossary#home_person), seleccione a categoria Indivíduos e seleccione o indivíduo pretendido para o designar como [indivíduo activo](wiki:Gramps_Glossary#active_person) e depois escolha .

Em alternativa, ao editar qualquer indivíduo, pode clicar com o botão direito do rato em áreas inactivas (áreas sem uma caixa de entrada de texto) da secção superior, o que abre um menu que inclui uma opção para o . O indivíduo inicial é a pessoa persistentemente designada que se torna o [indivíduo activo](wiki:Gramps_Glossary#active_person) quando ocorre uma das seguintes situações:

- Por defeito, quando a base de dados da árvore genealógica é aberta

  
  
*(O separador [Geral](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#General_Gramps_settings) nas [Preferências](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Preferences) pode modificar este comportamento. A opção "Lembrar a última categoria usada" regressará ao último [indivíduo activo](wiki:Gramps_Glossary#active_person) da sessão anterior.)*;

- Quando se clica no botão da barra de ferramentas;
- Quando o item Indivíduo inicial é seleccionado a partir do menu ou do menu contextual em vistas seleccionadas;
- Quando o [atalho](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT#15) é premido para voltar ao **indivíduo inicial**.

O botão ![[_media/Gramps_Go-Home48x48_win.png]] está disponível nas categorias Indivíduos, Parentescos e Costados.

#### Veja também

- [Definir o indivíduo inicial](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/pt_PT#Setting_the_Home_Person)

{{-}}

<span id="Adjusting viewing controls">

### Ajuste dos controlos de exibição

</span>

O facto de a barra de ferramentas, a barra lateral ou o filtro (não disponível nas vistas Pedigree e Relações) serem apresentados na janela principal é ajustado através do menu Ver.

Nas diferentes vistas, clicar no menu mostrará as caixas em que pode clicar:

- Navegador ;
- Barra de ferramentas;
- Barra lateral ;
- Barra inferior ;
- Ecrã completo .

Além disso, dependendo da vista em que se encontra, estarão disponíveis outras opções em .

- Gramplets:
  - Definir colunas para 1;
  - Definir colunas para 2;
  - Definir colunas para 3.
- Parentescos:
  - Mostrar irmãos;
  - Mostrar detalhes.
- Geografia:
  - Período;
  - Disposição.

Todas as outras vistas/categorias: [editor de colunas](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Column_Editor).

<span id="Export View">

### Exportar vista

</span>

![[_media/Menubar-FamilyTrees-overview-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Árvores genealógicas - Exportar vista]]

Na maioria das [listas das categorias](wiki:Gramps_6.0_Wiki_Manual_-_Categories/pt_PT#Categories_of_the_Navigator) os dados mostrados podem ser expostados via [](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/pt_PT#Main_Menus) .

Este comando de menu só aparece se os dados exibidos puderem ser exportados. O Gramps exportará os dados no ecrã de acordo com a sua escolha, nos formatos **CSV** ou **Open Document**.

Note que a configuração actual das colunas da lista controla os dados que serão exportados. A exportação conterá apenas os dados das colunas mostradas (na mesma ordem) e será limitada aos registos que correspondam a quaisquer [filtros](wiki:Gramps_6.0_Wiki_Manual_-_Filters/pt_PT) aplicados. {{-}} <span id="Export View as Spreadsheet dialog">

#### Exportar vista como folha de cálculo

</span>

![[_media/ExportViewAsSpreadsheet-CSV-file-dialog-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo Exportar vista como folha de cálculo]] ![[_media/ExportViewAsSpreadsheet-exampleODS-Displayed-in-LibreOfficeCalc-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Exemplo de documento ODS - Mostrado no LibreOffice Calc]] O Gramps abre o diálogo onde, depois de escolher uma localização e um nome para o ficheiro, exporta os dados da lista actual para um de dois formatos de folha de cálculo:

:::\* **CSV** (pré-definição);

:::\* **Folha de cálculo OpenDocument** - formato ODS.

<span id="CSV Dialect">

#### Dialecto CSV

</span> CSV significa **[Comma-Separated Values](https://wikipedia.org/wiki/Comma-separated_values)**. É um formato de ficheiro de texto simples que separa os dados em colunas e linhas para facilitar o seu intercâmbio. Originalmente, os dados eram limitados por separação em colunas em posições fixas nos ficheiros de texto `.txt`. Quando foi necessária mais flexibilidade, a vírgula foi escolhida como delimitador de colunas e foi estabelecido o formato `.csv`. Para complicar a situação, os diferentes sistemas operativos marcam o fim da linha e o fim do ficheiro com códigos de terminação diferentes.

Quando as vírgulas eram necessárias com demasiada frequência nos próprios dados, tornou-se popular o formato de ficheiro `.tsv` (Tab-Separated-Values). Quando outros delimitadores começaram a ser adoptados, em vez de se utilizarem mais extensões de ficheiros, CSV tornou-se sinónimo de qualquer formato de texto com colunas marcadas com delimitadores. São apenas 'dialectos' diferentes de "CSV".

{{-}} Todas as tabelas de listas têm um separador Dialeto CSV no menu . Pode escolher o delimitador do formato CSV a usar quando exportar e importar dados no Gramps.

Escolha entre:

- excel
- excel-tab
- unix
- Personalizado
  - Delimitador:
    - . (pré-definição)

    - ;

    -   

    - \|

    - tab

O módulo [Python `csv`](https://docs.python.org/3/library/csv.html) fornece vários dialectos pré-definidos para simplificar a leitura e escrita de ficheiros CSV. Estes dialectos especificam regras para a análise e formatação de dados. Os dialectos padrão incluem , e . Este documento descreve as caraterísticas de cada dialecto, incluindo o seu separador, fim de linha e comportamento de citação.

<span id="Excel Dialect">

##### Dialecto Excel

<span>

O dialecto foi concebido para ser compatível com ficheiros CSV gerados pelo Microsoft Excel. É adequado para dados que tenham sido gravados do Excel como valores separados por vírgulas:

- separador:
- vírgula (`,`\`);
- fim de linha: retorno de carro e avanço de linha`(\r\n`);
- aspas:
  - aspas duplas (`"`\`) são utilizadas para incluir campos que contenham o separador ou outros caracteres especiais;
  - para incluir uma aspa dupla dentro de um campo entre aspas, esta é escapada duplicando-a (por exemplo, `""exemplo""`).

<span id="Excel-tab Dialect">

##### Dialecto Excel-tab

</span>

O dialecto é semelhante ao dialecto "excel" mas utiliza tabulações em vez de vírgulas. Este formato é frequentemente encontrado quando se copia dados de células do Excel para a área de transferência do sistema operativo. Colar dados separados por tabulação na extensão [Importar texto](wiki:Addon:Import_Text_Gramplet) é uma das maneiras mais rápidas de preencher partes de sua árvore:

- separador: Tabulação `(\t`)
- fim de linha: retorno de carro e avanço de linha `(\r\n`)
- aspas:
  - aspas duplas (`"`) são utilizadas para incluir campos que contêm o separador ou outros caracteres especiais;
  - para incluir uma aspa dupla dentro de um campo entre aspas, esta é escapada duplicando-a (por exemplo, `""exemplo""`).

<span id="Unix Dialect">

##### Dialecto Unix

</span>

O dialecto foi concebido para ser utilizado em ambientes do tipo Unix. Utiliza um carácter de avanço de linha como terminador de linha e coloca sempre entre aspas todos os campos:

- separador: vírgula (`,`)
- fim de linha: Avanço de linha `(\n`)
- aspas:
  - todos os campos estão entre aspas duplas (`"`)
  - para incluir uma aspa dupla num campo entre aspas, esta é escapada duplicando-a (por exemplo, `""exemplo""`).

##### Veja também

- [CSV: possibilidade de escolher um dialecto](https://github.com/gramps-project/gramps/pull/1314)

{{-}}

<span id="Modularity and plugins">

### Modularidade e extensões

</span>

O Gramps foi concebido para expansão. A estrutura de extensões (também conhecida como "Plug-ins", "addons") fornece um caminho para o desenvolvimento de terceiros fora das distribuições normais de lançamento do Gramps.

A documentação para cada extensão é mantida fora do fluxo destes capítulos principais do wiki. O ambiente e a funcionalidade do program e da documentação podem não estar de acordo com os estilos vistos no resto do Gramps, embora encorajemos os programadores a tentar fazer as adições tão perfeitas quanto possível. Pode encontrar uma breve descrição e imagem de cada extensão na secção [Lista de extensões](wiki:6.0_Addons#Addon_List) do manual. A página de documentação mantida separadamente para a extensão está ligada a partir da 1ª coluna dessa lista.

Veja [Gestor de extensões](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager/pt_PT) e [Extensões de terceiros](wiki:6.0_Addons). {{-}}

![[_media/TextReports-DocumentOptions-PlainText-output-settings-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Opções do documento]] <span id="Customize report output formats">

### Personalizar o formato de saída dos relatórios

</span>

Para a maioria das caixas de diálogo de relatórios, na parte superior existem separadores de opções especificamente relacionados com esse relatório em particular. A parte inferior terá caraterísticas mais amplamente reutilizáveis e é chamada a secção .

A partir da lista pendente pode escolher um estilo personalizado existente. Ou, para criar o seu próprio estilo, clique em para abrir o diálogo e, em seguida, clicar em para mostrar o diálogo .

Veja [Relatórios](wiki:Gramps_6.0_Wiki_Manual_-_Reports/pt_PT) para mais informação. {{-}} ![[_media/DocumentStyles-dialog-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo Estilos de documento]] <span id="Document Styles dialog">

#### Diálogo Estilos de documento

</span>

O diálogo lista o estilo *pré-definido* e quaisquer estilos personalizados criados para o relatório em causa, permitindo adicionar, editar ou eliminar estilos. Clique em para abrir o diálogo . {{-}}

![[_media/StyleEditor-dialog-Description-tab-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo Editor de estilos]] <span id="Style editor dialog">

#### Diálogo Editor de estilos

</span>

O diálogo permite-lhe personalizar o estilo do documento específico de cada relatório. Altere o campo `Novo estilo` (pré-definição) para um nome único, tal como aparecerá nas . Assim que as alterações ao seu estilo personalizado tiverem sido finalizadas, clique em para gravar as alterações ou para sair.

{{-}} ![[_media/StyleEditor-dialog-FontOptions-tab-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editor de estilos - separador Opções de letra]] ![[_media/StyleEditor-dialog-ParagraphOptions-tab-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editor de estilos - separador Opções de parágrafo)]] <span id="Style editor dialog tabs">

##### Separadores do diálogo Editor de estilos

</span>

No lado esquerdo, verá a coluna que lista as opções de parágrafo específicas desse relatório que pode modificar. Por exemplo, a coluna mostra as opções de estilo para AHN-Entry, AHN-Generation e AHN-Title. No lado direito há três separadores associados a cada estilo listado na coluna da esquerda.

<span id="Description">

###### Descrição

</span>

-   
  (Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}-2}}}}) A descrição descreve o conteúdo de cada parágrafo. Por exemplo, este é o estilo utilizado para o relatório Ahnentafel (AHN-Entry).

<span id="Font options">

###### Opções de letra

</span>

-   
  aqui pode definir o Roman ou Swiss, o seu em pontos, a sua e algumas , como Negrito, Itálico ou Sublinhado.

<span id="Paragraph options">

###### Opções de parágrafo

</span>

-   
  aqui define o , a , a , o e os do seu estilo.

{{-}}

<span id="Context menu">

### Menu contextual

</span> Utilizado em vários locais no Gramps, a forma de aceder ao menu de contexto depende dos sistemas operativos:

- No Microsoft Windows, normalmente, utiliza o botão direito do rato para mostrar o menu contextual ou utiliza o atalho de teclado . Veja [Using Context Menus - Microsoft Docs](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/mpc/using-context-menus);
- No Apple macOS, geralmente prima enquanto clica no botão do rato para mostrar o menu contextual. Veja [Contextual Menus - Menus - macOS - Human Interface Guidelines - Apple Developer](https://developer.apple.com/design/human-interface-guidelines/macos/menus/contextual-menus/).

Veja também:

- [Atalhos](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT)

<span id="Customizing">

## Personalizar

</span> Eis algumas formas de personalizar o Gramps. \<span id="Preferences\>

### Preferências

</span>

O separador Mostrar das Preferências permite seleccionar o formato de nome usado por defeito no Gramps. O botão Editar do abre a janela , permitindo a criação de estilos definidos pelo utilizador (personalizados) para além das opções de formato de nome internas.

Veja [Preferências](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Preferences)

O botão Editar para os nomes preferidos e alternativos de uma pessoa abre a janela , que permite a selecção de excepções ao formato do nome que se sobrepõem ao formato escolhido no separador Mostrar das Preferências para toda a árvore.

O formato do nome, o agrupamento e a ordenação podem ser substituídos para indivíduos e apelidos seleccionados. Os diálogos Editar indivíduo têm dois botões Editar para aceder a esta funcionalidade. O botão para o nome preferido está à direita do campo Sufixo. No entanto, pode fazer duplo clique em qualquer nome seleccionado (Preferido ou Alternativo) no separador Nomes para abrir o editor de nomes. Os formatos de nome a mostrar internos e personalizado podem ser seleccionados com excepção das opções "Agrupar como:" e "Ordenar como:", que têm como pré-definição o formato de nome seleccionado nas preferências.

![[_media/PickAColor-selector-dialog-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Pick a Color&quot; - palette selector dialog]] <span id="Pick a Color selector">

### Selector Escolha uma cor

</span> O separador [Cores](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Colors) das preferências permite personalizar a cor de vários elementos de diagramas da categoria Gráficos.

\<span id="Color Palette\>

#### Paleta de cores

</span>

Seleccione uma cor de entre as 45 [variantes](wiki:Gramps_Glossary#swatches) na área da paleta de cores pré-definida. Ou seleccione a partir das amostras de cores usadas recentemente. Ou clique em para criar a sua própria cor personalizada. Clique com o botão direito do rato em qualquer amostra para adicionar outra cor personalizada e abrir o selector de gradação.

Pode arrastar qualquer amostra de cor para qualquer amostra no diálogo de preferências (ou configuração).

{{-}} ![[_media/PickAColor-gradient-dialog-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo Escolha uma cor -]] <span id="Color Gradient">

#### Gradação de cor

</span>

O diálogo de selecção de gradação serve para ajustar a [cor](wiki:Gramps_Glossary#swatch) ao cimo do diálogo. Uma vez alterada, pode clicar em para aplicar a cor. Arraste a amostra do diálogo de gradação para qualquer amostra no diálogo de preferências (ou configuração).

As cores específicas da amostra podem ser alteradas de várias formas:

- escrevendo directamente o **código hexadecimal da cor** na caixa de texto ao cimo;
- com o deslizador na barra de tons à esquerda; dispõe de um controlo numérico fino (com clique direito do rato);
- clique do rato na barra de cores mono-dimensional à esquerda (tom), ou na área bi-dimensional à direita (brilho e saturação);
- clique direito na área bi-dimensional para ver um controlo numérico fino de brilho e saturação;

{{-}}

![[_media/FileChooser_Bookmarks_Breadcrumbs-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Selector de ficheiros GTK em Linux marcadores e caminho realçados]] <span id="File Chooser">

### Selector de ficheiros

</span> ![[_media/FileChooser_Bookmarks_Breadcrumbs_mac.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Selector de ficheiros GTK em masOS marcadores e caminho realçados]] ![[_media/FileChooser_Bookmarks_Breadcrumbs_win.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Selector de ficheiros GTK em Windows marcadores e caminho realçados]] Os diálogos Abrir e Gravar do Gramps são baseados no [selector de ficheiros do GTK](https://docs.gtk.org/gtk3/iface.FileChooser.html). Cada sistema operativo tem comportamentos próprios, nativos para cliques, cliques duplos, ordenação, [atalhos](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT#Handy_Shortcuts), variáveis ambientais e localizações padrão de ficheiros. No Gramps, alguns destes podem ser personalizadas para se parecerem mais com os selectores de ficheiros nativos do sistema operativo. No entanto, as idiossincrasias dos vários sistemas operativos significam que as pastas de rede partilhadas e outras podem não ser iguais às dos selectores de ficheiros nativos.

O [selector de ficheiros do GTK](https://developer-old.gnome.org/gtk4/stable/GtkFileChooser.html) permite adicionar ligações de navegação rápida aos locais mais utilizados do sistema de ficheiros. Na implementação padrão, são mostradas no painel de navegação da barra lateral esquerda. Pode ser um pouco incerto, no início, o facto de estes atalhos serem provenientes de várias fontes e em vários sabores, por isso vamos explicar a terminologia aqui:

- **[Marcadores](#Bookmarking_file_folders)**: são criados por si, arrastando pastas do painel direito para o painel esquerdo ou com o botão "Adicionar"; podem ser renomeados e eliminados;
- **Atalhos**: podem ser fornecidos pelo Gramps; o programa pode adicionar um atalho para uma pasta Transferências ou Documentos; estes "não podem" ser adicionados ou removidos por si, mas podem ser renomeados via menu contextual;
- **Volumes**: são fornecidos pelo sistema de ficheiros e representam unidades físicas (discos internos ou externos); são as "raízes" do sistema de ficheiros, sendo as ligações Início e Transferências "raízes" comuns; os volumes não podem ser modificados por si.

Imagens

<span id="Context Menu options">

#### Opções do menu contextual

</span> Clique com o botão direito do rato em qualquer ficheiro ou pasta para abrir o menu contextual com as seguintes opções:

- Abrir com o gestor de ficheiros;
- Copiar localização;
- [Adicionar aos marcadores](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Bookmarking_file_folders);
- Renomear;
- Mover para o lixo;
- Mostrar os ficheiros ocultos ❏;
- Mostrar a coluna de tamanho ❏;
- Mostrar a coluna de tipo ❏;
- Mostrar a coluna modificado ❏;
- Ordenar pastas antes de ficheiros ❏;

Clique com o botão direito do rato na barra lateral de navegação para abrir o menu contextual com as seguintes opções:

- Abrir;
- Remover;
- Renomear....

<span id="Breadcrumbs and text-entry address bar">

#### Caminho e barra de endereços

</span> Por defeito, a navegação no selector de ficheiros é feita... navegando. Existem também alguns atalhos à esquerda e caminhos (realçados a verde nas figuras) para uma navegação rápida para cima e para baixo no caminho.

Opcionalmente, pode ser utilizada uma barra de texto para inserir ou colar directamente um caminho. Alterne entre caminhos e barra de endereços premindo o [atalho](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT) .

<span id="Bookmarking file folders">

#### Marcar ficheiros e pastas

</span> Pode definir marcadores de pastas para facilitar a procura de localizações padrão. Estes marcadores são recordados entre sessões e independentemente da árvore carregada. Com qualquer diálogo Abrir ou Gravar aberta, navegue até à localização da pasta a marcar. Crie o marcador, ou arrastando o ícone da pasta para a coluna de navegação à esquerda, ou clicando com o botão direito do rato nessa pasta para usar a opção do menu contextual .

Clicar com o botão direito do rato num marcador existente permite renomeá-lo ou removê-lo.

<span id="File Formats">

#### Formatos de ficheiros

</span> O suporte a vários formatos de ficheiros está integrado na distribuição padrão do Gramps. Pode instalar extensões de importação e exportação para expandir as opções. Veja [Formato de saída](wiki:Output_formats) para uma lista de formatos de ficheiro.

- Veja também
  - [How to Show Text-Entry Address Bar or “Breadcrumbs” (Navigation Buttons)](https://ubuntugenius.wordpress.com/2010/05/14/how-to-show-text-entry-address-bar-or-breadcrumbs-navigation-buttons-in-nautilus-after-ubuntu-10-04-upgrade/) no Nautilus após a actualização para Ubuntu 10.04

<!-- -->

- Discussões no Discourse sobre o selector de ficheiros do GTK:
  - [Documenting the File Chooser in the wiki](https://gramps.discourse.group/t/need-suggestions-for-documenting-the-gtk-file-chooser/1820/8)
  - [Illustrating the File Chooser in the Wiki](https://gramps.discourse.group/t/macos-and-windows-gtk-file-chooser-dialog-capture-request/3364)
  - [File Chooser: Sorting files and folders](https://gramps.discourse.group/t/can-i-cause-folders-to-sort-to-the-top-of-the-list-when-presented-with-the-folder-contents/1708/14)

### Idioma

O Gramps foi traduzido para vários [idiomas](wiki:Portal:Translators). Normalmente, o Gramps inicia automaticamente no idioma base do sistema operativo, mas às vezes isto pode não ser o que deseja. E, noutros casos, um módulo ou extensão ainda não terá sido traduzido e um diálogo de aviso aparecerá dizendo algo como "Aviso: a extensão XYZ não tem tradução para nenhum dos seus idiomas configurados, a usar o inglês dos EUA" Note que o dialecto americano do inglês é o padrão, não o britânico. Isto pode tornar-se irritante ou intrusivo.

A situação mais idealista é ser tão fluente em inglês americano como o idioma seleccionado para o ambiente gráfico do sistema operativo no seu computador. E que aproveitaria a oportunidade para traduzir a funcionalidade do Gramps para os utilizadores que não falam inglês.

Se o seu sistema estiver configurado para mostrar um idioma diferente do inglês, pode substituir isto para o Gramps.

Como exemplo, suponha que um computador na Holanda está configurado para usar o Unicode 8 Dutch por defeito: "LANG: nl_NL.UTF-8". Pode redefinir o idioma do sistema operativo.

Em Windows, utilize o comando SET para alterar a variável de ambiente LANG para "en_GB.UTF-8" para inglês britânico. Pode fazê-lo a partir da linha de comandos ou [criar um atalho de arranque com o seguinte destino](https://gramps-project.org/bugs/view.php?id=11009): `C:\Windows\System32\cmd.exe /c "SET LANG=en_GB.UTF-8 && START /D ^"C:\Program Files\GrampsAIO64-6.0.3^" gramps.exe"`

#### Linux

Se quiser escolher uma variante de idioma para ordenação que não seja a variante padrão, pode iniciar o Gramps a partir do terminal com um ambiente LC_COLLATE diferente. Por exemplo, a variante padrão de ordenação (collation) para o sueco é "reformed", mas pode escolher "standard" escrevendo:

`export LC_COLLATE="sv_SE.UTF-8@collation=standard"`  
`python Gramps.py`

#### macOS

Para macOS, veja [Advanced setup](wiki:Mac_OS_X:Application_package#Advanced_setup) para detalhes sobre a forma como a língua é normalmente escolhida e como escolher uma definição especial, não predefinida, para a língua, a ordem de ordenação ou o formato de elementos como os nomes do dia e do mês e os separadores de números.

#### MS Windows

![[_media/Microsoft_Window_Gramps_AIO_Installer_Choose_Components-Selection-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Microsoft Windows Gramps AIO Escolher componentes.]] Se quiser executar o Gramps noutro idioma que não o inglês usando o instalador do Gramps, deve seleccioná-lo durante o processo de instalação. Caso contrário, ele não estará disponível. Pode encontrar mais informação na página [Idiomas em falta](wiki:Installing_Gramps_for_Windows_computers#Missing_other_languages).

{{-}}

<span id="Add Windows OS Menu Item">

### Adicionar item de menu no Windows

</span> ![[_media/Edit-Target-GrampsAIO64-Properties-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} GrampsAIO64 - Propriedades de idioma para o atalho.]]

Para que o Gramps funcione no idioma seleccionado (ver tabela abaixo para o [código do seu idioma](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Language_codes)), faça o seguinte:

- com o botão direito do rato, clique em "" no ambiente de trabalho e no menu, escolha: ;
- clique com o botão direito em qualquer sítio da área de trabalho e escolha ;
- será criado um novo ícone com o nome: "";
- clique com o botão direito do rato nesse ícone e, no menu, escolha: ;
- será aberta uma nova janela, clique no primeiro separador, e altere o texto de "" para algo mais descritivo como: "":
  - clique no segundo separador, chamado , altere o texto na primeira entrada chamada de (note que o caminho varia dependendo da versão do Gramps usada):
    - `"C:\Program Files\GrampsAIO64-5.x.x\grampsw.exe"` para:
    - `%comspec% /c set LANG=da_DK.UTF-8 && start grampsw.exe"`;
- clique em .

Agora, quando clicar nesse ícone, o Gramps iniciará em dinamarquês.

{{-}} {{-}}

\<span id="Change the windows LANG variables

### Alterar as variáveis de ambiente LANG do Windows

</span> Outra opção se quiser que o Gramps inicie sempre em, digamos: francês canadiano, pode ir a Windows -\> Painel de controlo -\> Sistema -\> Definições avançadas do sistema -\> Avançadas -\> Variáveis de ambiente e adicionar a variável LANG na secção do utilizador do diálogo das variáveis de ambiente com o código apropriado.

Para o exemplo acima, o valor a adicionar é:

    Nome: LANG
    Valor: fr_CA.UTF-8

- Veja também: [How to Set Environment Variables in Windows 10](https://www.redswitches.com/blog/environment-variables/#method-1-set-environment-variables-through-the-gui)

\<span id="Language codes

### Códigos de idiomas

</span> Seleccione a partir da seguinte tabela de [idiomas](wiki:Portal:Translators) em que o Gramps está traduzido:

| Idioma | Código ISO | Exemplo | Notas |
|----|----|----|----|
| Inglês-EUA (pré-definição) | en_US.UTF-8 | %comspec% /c set LANG=en_US.UTF-8 && start grampsw.exe" |  |
| Inglês (britânico) | en_GB.UTF-8 | %comspec% /c set LANG=en_GB.UTF-8 && start grampsw.exe" |  |
| Finlandês | fi.UTF-8 | %comspec% /c set LANG=fi.UTF-8 && start grampsw.exe" |  |
| Russo | ru_RU.UTF-8 | %comspec% /c set LANG=ru_RU.UTF-8 && start grampsw.exe" |  |
| Albanês | sq_AL.UTF-8 | %comspec% /c set LANG=sq_AL.UTF-8 && start grampsw.exe" |  |
| Alemão | de_DE.UTF-8 | %comspec% /c set LANG=de_DE.UTF-8 && start grampsw.exe" |  |
| Francês | fr_FR.UTF-8 | %comspec% /c set LANG=fr_FR.UTF-8 && start grampsw.exe" |  |
| Francês canadiano | fr_CA.UTF-8 | %comspec% /c set LANG=fr_CA.UTF-8 && start grampsw.exe" |  |
| Macedónio | mk_MK.UTF-8 ??? |  |  |
| Holandês | nl_NL.UTF-8 | %comspec% /c set LANG=nl_NL.UTF-8 && start grampsw.exe" |  |
| Belga (holandês) | nl_BE.UTF-8 | %comspec% /c set LANG=nl_BE.UTF-8 && start grampsw.exe" |  |
| Eslovaco | sk_SK.UTF-8 | %comspec% /c set LANG=sk_SK.UTF-8 && start grampsw.exe" |  |
| Hebraico | he_IL.UTF-8 | %comspec% /c set LANG=he_IL.UTF-8 && start grampsw.exe" |  |
| Dinamarquês | da_DK.UTF-8 | %comspec% /c set LANG=da_DK.UTF-8 && start grampsw.exe" |  |
| Grego | el_GR.UTF-8 | %comspec% /c set LANG=el_GR.UTF-8 && start grampsw.exe" |  |
| Italiano | it_IT.UTF-8 | %comspec% /c set LANG=it_IT.UTF-8 && start grampsw.exe" |  |
| Esperanto | eo.UTF-8 ??? |  |  |
| Chinês (simplificado) | zh_CN.UTF-8 | %comspec% /c set LANG=zh_CN.UTF-8 && start grampsw.exe" |  |
| Chinês (Hong Kong) | zh_HK.UTF-8 ??? |  |  |
| Chinês (tradicional) | zh_TW.UTF-8 | %comspec% /c set LANG=zh_TW.UTF-8 && start grampsw.exe" |  |
| Ucraniano | uk_UA.UTF-8 |  |  |
| Português (Portugal) | pt_PT.UTF-8 | %comspec% /c set LANG=pt_PT.UTF-8 && start grampsw.exe" |  |
| Português (Brasil) | pt_BR.UTF-8 | %comspec% /c set LANG=pt_BR.UTF-8 && start grampsw.exe" |  |
| Africander | af_ZA.UTF-8 |  |  |
| Norueguês Bokmål | nb_NO.UTF-8 | %comspec% /c set LANG=nb_NO.UTF-8 && start grampsw.exe" |  |
| Norueguês Nynorsk | nn_NO.UTF-8 | %comspec% /c set LANG=nn_NO.UTF-8 && start grampsw.exe" |  |
| Turco | tr_TR.UTF-8 | %comspec% /c set LANG=tr_TR.UTF-8 && start grampsw.exe" |  |
| Espanhol | es_ES.UTF-8 | %comspec% /c set LANG=es_ES.UTF-8 && start grampsw.exe" |  |
| Polaco | pl_PL.UTF-8 | %comspec% /c set LANG=pl_PL.UTF-8 && start grampsw.exe" |  |
| Esloveno | sl_SI.UTF-8 | %comspec% /c set LANG=sl_SI.UTF-8 && start grampsw.exe" |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

- Os códigos de idioma são códigos ISO de duas letras minúsculas (como "da"), tal como definidos por [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
- Os códigos de país são códigos ISO de duas letras maiúsculas (como "BE"), tal como definidos por [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1).

<span id="Advanced manipulation of settings">

### Manipulação avançada das definições

</span>

Para além das definições disponíveis em Preferências, poderá também querer explorar as definições avançadas.

O Gramps usa **[chaves INI](https://en.wikipedia.org/wiki/INI_file#Keys_(properties))** e [secções INI](https://en.wikipedia.org/wiki/INI_file#Sections) para gerir as preferências do utilizador e as definições do programa. Estas são armazenadas no ficheiro de texto `gramps.ini` na pasta `.gramps/gramps[XX]` na sua pasta pessoal ou de utilizador.

O ficheiro `gramps.ini` tem as seguintes secções:

- \[behavior\] : chaves típicas são: [betawarn](https://github.com/gramps-project/gramps/blob/master/gramps/gui/grampsgui.py#L502), enable-autobackup, use-tips...
- \[colors\] :
- \[csv\] :
- \[database\] : relacionado com as definições da base de dados para a árvore genealógica.
- \[export\] : pastas de exportação e importação
- \[geography\] :
- \[interface\] : muitas teclas relativas à altura e largura das diferentes vistas: e.g. event-height: 450, event-ref-height: 585, event-ref-width: 728, event-width: 712...
- \[paths\] : chaves relacionadas com ficheiros e pastas importados recentemente
- \[plugin\] :
- \[preferences\] : chaves relacionadas com as preferências: todos os prefixos comuns, todas as cores...
- \[researcher\] : todas as informações relativas ao investigador
- \[spacing\] :
- \[test\] :
- \[utf8\] :

<span id="Example <code>gramps.ini</code> file">

#### Ficheiro exemplo `gramps.ini`

</span>

    ;; Gramps key file
    ;; Automatically created at 2023/09/13 14:17:45

    [behavior]
    ;;addmedia-image-dir=''
    ;;addmedia-relative-path=0
    ;;addons-allow-install=0
    ;;addons-projects=[['Gramps', 'https://raw.githubusercontent.com/gramps-project/addons/master/gramps52', True]]
    ;;addons-url='https://raw.githubusercontent.com/gramps-project/addons/master/gramps52'
    ;;autoload=0
    ;;avg-generation-gap=20
    ;;check-for-addon-update-types=['new']
    ;;check-for-addon-updates=0
    ;;date-about-range=50
    ;;date-after-range=50
    ;;date-before-range=50
    ;;do-not-show-previously-seen-addon-updates=1
    ;;generation-depth=15
    ;;immediate-warn=0
    ;;last-check-for-addon-updates='1970/01/01'
    ;;max-age-prob-alive=110
    ;;max-sib-age-diff=20
    ;;min-generation-years=13
    ;;owner-warn=0
    ;;pop-plugin-status=0
    ;;previously-seen-addon-updates=[]
    ;;recent-export-type=3
    ;;runcheck=0
    ;;spellcheck=0
    ;;startup=0
    ;;surname-guessing=0
    translator-needed=0
    ;;use-tips=0
    ;;web-search-url='http://google.com/#&q=%(text)s'
    ;;welcome=100

    [colors]
    ;;border-family=['#cccccc', '#252525']
    ;;border-family-divorced=['#ff7373', '#720b0b']
    ;;border-female-alive=['#861f69', '#261111']
    ;;border-female-dead=['#000000', '#000000']
    ;;border-male-alive=['#1f4986', '#171d26']
    ;;border-male-dead=['#000000', '#000000']
    ;;border-other-alive=['#2a5f16', '#26a269']
    ;;border-other-dead=['#000000', '#000000']
    ;;border-unknown-alive=['#8e5801', '#8e5801']
    ;;border-unknown-dead=['#000000', '#000000']
    ;;family=['#eeeeee', '#454545']
    ;;family-civil-union=['#eeeeee', '#454545']
    ;;family-divorced=['#ffdede', '#5c3636']
    ;;family-married=['#eeeeee', '#454545']
    ;;family-unknown=['#eeeeee', '#454545']
    ;;family-unmarried=['#eeeeee', '#454545']
    ;;female-alive=['#feccf0', '#62242D']
    ;;female-dead=['#feccf0', '#3a292b']
    ;;home-person=['#bbe68a', '#304918']
    ;;male-alive=['#b8cee6', '#1f344a']
    ;;male-dead=['#b8cee6', '#2d3039']
    ;;other-alive=['#94ef9e', '#285b27']
    ;;other-dead=['#94ef9e', '#062304']
    ;;scheme=0
    ;;unknown-alive=['#f3dbb6', '#75507B']
    ;;unknown-dead=['#f3dbb6', '#35103b']

    [csv]
    ;;delimiter=','
    ;;dialect='excel'

    [database]
    ;;autobackup=0
    ;;backend='sqlite'
    ;;backup-on-exit=1
    ;;backup-path='C:\\Users\\[username]'
    ;;compress-backup=1
    ;;host=''
    ;;path='C:\\Users\\[username]\\AppData\\Roaming\\gramps\\grampsdb'
    ;;port=''

    [export]
    ;;proxy-order=[['privacy', 0], ['living', 0], ['person', 0], ['note', 0], ['reference', 0]]

    [geography]
    ;;center-lat=0.0
    ;;center-lon=0.0
    ;;lock=0
    ;;map_service=1
    ;;path=''
    ;;personal-map=''
    ;;show_cross=0
    ;;use-keypad=1
    ;;zoom=0
    ;;zoom_when_center=12

    [interface]
    dbmanager-height=370
    ;;dbmanager-horiz-position=12
    ;;dbmanager-vert-position=85
    ;;dbmanager-width=780
    ;;dont-ask=0
    ;;filter=0
    ;;fullscreen=0
    ;;grampletbar-close=0
    ;;hide-lds=0
    ;;ignore-gexiv2=0
    ;;ignore-osmgpsmap=0
    ;;ignore-pil=0
    ;;main-window-height=500
    ;;main-window-horiz-position=15
    ;;main-window-vert-position=10
    ;;main-window-width=775
    ;;mapservice='OpenStreetMap'
    ;;open-with-default-viewer=0
    ;;pedview-layout=0
    ;;pedview-show-images=1
    ;;pedview-show-marriage=0
    ;;pedview-show-unknown-people=0
    ;;pedview-tree-direction=2
    ;;pedview-tree-size=5
    ;;place-name-height=100
    ;;place-name-width=450
    ;;sidebar-text=1
    ;;size-checked=0
    ;;statusbar=1
    ;;surname-box-height=150
    ;;toolbar-addons=1
    ;;toolbar-clipboard=1
    ;;toolbar-on=1
    ;;toolbar-preference=1
    ;;toolbar-reports=1
    ;;toolbar-text=0
    ;;toolbar-tools=1
    ;;treemodel-cache-size=1000
    ;;view=1
    ;;view-categories=['Dashboard', 'People', 'Relationships', 'Families', 'Ancestry', 'Events', 'Places', 'Geography', 'Sources', 'Citations', 'Repositories', 'Media', 'Notes']

    [paths]
    ;;quick-backup-directory='C:\\Users\\[username]'
    ;;quick-backup-filename='%(filename)s_%(year)d-%(month)02d-%(day)02d.%(extension)s'
    ;;recent-export-dir='C:\\Users\\[username]'
    ;;recent-file=''
    ;;recent-import-dir='C:\\Users\\[username]'
    ;;report-directory='C:\\Users\\[username]'
    ;;website-cal-uri=''
    ;;website-cms-uri=''
    ;;website-directory='C:\\Users\\[username]'
    ;;website-extra-page-name=''
    ;;website-extra-page-uri=''

    [plugin]
    ;;addonplugins=[]
    ;;hiddenplugins=[]

    [preferences]
    ;;age-after-death=1
    ;;age-display-precision=1
    ;;calendar-format-input=0
    ;;calendar-format-report=0
    ;;cite-plugin='cite-default'
    ;;coord-format=0
    ;;cprefix='C%04d'
    ;;date-format=0
    ;;default-source=0
    ;;eprefix='E%04d'
    ;;family-relation-type=3
    ;;family-warn=1
    ;;february-29=0
    ;;fprefix='F%04d'
    ;;hide-ep-msg=0
    ;;invalid-date-format='<b>%s</b>'
    ;;iprefix='I%04d'
    last-view='dashboardview'
    last-views=['dashboardview', '', '', '', '', '', '', '', '', '', '', '', '']
    ;;name-format=1
    ;;no-given-text='[Missing Given Name]'
    ;;no-record-text='[Missing Record]'
    ;;no-surname-text='[Missing Surname]'
    ;;nprefix='N%04d'
    ;;online-maps=0
    ;;oprefix='O%04d'
    ;;paper-metric=0
    ;;paper-preference='Letter'
    ;;patronimic-surname=0
    ;;place-auto=1
    ;;place-format=0
    ;;pprefix='P%04d'
    ;;private-given-text='[Living]'
    ;;private-record-text='[Private Record]'
    ;;private-surname-text='[Living]'
    ;;quick-backup-include-mode=0
    ;;rprefix='R%04d'
    ;;sprefix='S%04d'
    ;;tag-on-import=0
    ;;tag-on-import-format='Imported %Y/%m/%d %H:%M:%S'
    ;;use-last-view=0

    [researcher]
    ;;researcher-addr=''
    ;;researcher-city=''
    ;;researcher-country=''
    ;;researcher-email=''
    ;;researcher-locality=''
    ;;researcher-name=''
    ;;researcher-phone=''
    ;;researcher-postal=''
    ;;researcher-state=''

    [spacing]
    dbman=[22.605613425925927, 5.877459490740741, 9.856047453703704]

    [test]
    ;;january='January'

    [utf8]
    ;;baptism-symbol='~'
    ;;birth-symbol='*'
    ;;buried-symbol='[]'
    ;;cremated-symbol='⚱'
    ;;dead-symbol='✝'
    ;;death-symbol=2
    ;;divorce-symbol='o|o'
    ;;engaged-symbol='o'
    ;;in-use=0
    ;;killed-symbol='x'
    ;;marriage-symbol='oo'
    ;;partner-symbol='o-o'
    ;;selected-font=''

<span id="Advanced backup filename setting">

#### Definição avançada do nome da salvaguarda

</span> Também é possível definir o padrão de nomenclatura para o nome do ficheiro de salvaguarda definindo *`paths.quick-backup-filename`* no ficheiro `~/.gramps/gramps52/gramps.ini` como: {{-}}

`[paths]`  
`;;quick-backup-filename='%(filename)s_%(year)d-%(month)02d-%(day)02d.%(extension)s'`

removendo os dois pontos e vírgulas(`;;`) do início da linha da chave INI e utilizando qualquer uma das seguintes palavras-chave para o padrão de nome de ficheiro:

- filename
- year
- month
- day
- hour
- minutes
- seconds
- extensão do ficheiro:
  - **.gpkg**(por defeito) se incluir multimédia;
  - *.gramps* se não incluir multimédia.

Use o ficheiro ~/.gramps/gramps{XX}/gramps.ini apropriado.

- Gramps :

`~/.gramps/gramps``/gramps.ini`

Veja também:

- [Diálogo de salvaguardas](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Backup_dialog)
- [Opções de configuração](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/pt_PT#Configuration_.28config.29_option)
- [Forçar o uso de BSDDB 3](wiki:Install_latest_BSDDB#Make_Gramps_use_bsddb3)
- [Preferências de símbolos genealógicos](wiki:Customize_the_Genealogical_Symbols_lookup_table#Genealogy_symbols_preferences)

### Tema

O aspecto do Gramps pode ser alterado.

- [Extensão:Preferências do tema](wiki:Addon:ThemePreferences)
- [Temas do Windows AIO](wiki:Windows_AIO_themes)
- [GTK 3 theme - GEPS 029: GTK3-GObject introspection Conversion](wiki:GEPS_029:_GTK3-GObject_introspection_Conversion#GTK_3_theme)
- [Substituir ícones do Gramps](wiki:Overrule_Gramps_Icons) - para versões antigas do Gramps.
- [Estilo do ambiente de trabalho](wiki:UI_style)

Também podem ser alterados alguns relatórios:

- [Temas do relatório Página web](wiki:Website_report_Themes)

{{-}}

[Category:Tips](wiki:Category:Tips) [Category:Pt PT:Documentation](wiki:Category:Pt_PT:Documentation)
