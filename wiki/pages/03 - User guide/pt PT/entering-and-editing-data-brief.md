---
title: 'Gramps 6.0 Wiki Manual - Entering and editing data: brief/pt PT'
categories:
- Pt PT:Documentation
managed: false
source: wiki-scrape
wiki_revid: 113103
wiki_fetched_at: '2026-05-30T19:45:53Z'
lang: pt PT
---

{{#vardefine:chapter\|8}} {{#vardefine:figure\|0}} Esta secção fornece os conhecimentos básicos necessários para começar a inserir a sua informação genealógica no Gramps. Explica como inserir pessoas na sua árvore genealógica (também chamada de base de dados) e como especificar os seus relacionamentos familiares (encontra explicações mais pormenorizadas no próximo capítulo: [Inserir e editar dados: detalhado](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed/pt_PT).)

Primeiro, vamos identificar os tipos de informações que podem ser inseridas na sua árvore genealógica usando o Gramps. Estes incluem:

- informações pessoais sobre um indivíduo (nomes, moradas, datas de nascimento e morte, etc.);
- informações sobre as relações de um indivíduo (casamentos, divórcios, uniões civis, etc.);
- informações sobre os pais e filhos de um indivíduo;
- Fontes que documentam a sua pesquisa.

Vamos agora explorar a forma como pode inserir e editar estes vários tipos de informações genealógicas.

<span id="To add or edit a person">

## Adicionar ou editar um indivíduo

</span>

O [menu](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/pt_PT#Add) para cada [categoria](wiki:Gramps_Glossary#category) inclui a opção de adicionar um [indivíduo](wiki:Gramps_Glossary#person). Também é suportado o uso de um [atalho](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT#Common_keybindings) para adicionar indivíduos em todas as categorias.

Existem várias formas de adicionar um novo indivíduo à sua árvore genealógica. Muitas têm um contexto implícito que poupa um passo ao enxertar o indivíduo numa árvore (por exemplo, adicionar um indivíduo a partir do contexto de Família das categorias Parentescos ou Gráficos insere automaticamente o novo indivíduo na família. Não é necessário criá-lo como uma acção separada e, em seguida, localizar e arrastar o novo indivíduo para essa família). Vamos abordar alguns dos diferentes fluxos de trabalho à medida que avançarmos. {{-}}

<span id="Add a new person">

### Adicionar um novo indivíduo

</span>

![[_media/People-tree-view-grouped-people-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Indivíduos - Vista em árvore - Indivíduos agrupados]]

A forma mais óbvia de inserir uma pessoa na sua árvore é adicioná-la a partir da categoria . Na categoria , clique em na barra de ferramentas.

{{-}} ![[_media/Edit-person-window-new-person-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editar indivíduo - Novo editor vazio]]

O diálogo será mostrado, permitindo a inserção de dados conhecidos sobre o indivíduo. Clique em para gravar o novo indivíduo.

{{-}}

<span id="Edit an existing person">

### Editar um indivíduo existente

</span>

![[_media/Edit-person-window-example-existing-person-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editar indivíduo - Indivíduo existente]]

Para editar informações sobre uma pessoa já presente na árvore genealógica, seleccione-a a partir da categoria e clique em .

As pessoas também podem ser adicionadas à árvore genealógica na categoria , diálogo , e noutros locais onde faça sentido.

{{-}}

<span id="To specify a relationship">

## Para especificar um parentesco

</span>

Existem duas formas principais de especificar relações entre indivíduos:

1.  Por família:

<!-- -->

  
<li>

na categoria ; esta é normalmente utilizada para construir múltiplas relações em torno de uma única pessoa;

</li>

<li>

no diálogo na categoria ; esta é normalmente utilizada para construir todos os parentescos dentro de uma única família de cada vez.

</li>

</ol>

1.  Por associação:

<!-- -->

  
<li>

usando o separador do diálogo ; a adição de um indivíduo e a especificação do tipo de associação (padrinho, colega de trabalho, porta-jóias, amigo de infância, etc.) identifica uma relação interpessoal.

</li>

<li>

usando o no diálogo ; a referência cruzada a um indivíduo através de uma ligação pessoal numa nota associará essa pessoa ligada ao indivíduo onde a nota está anexada.

</li>

<li>

As pessoas que partilham uma referência (fontes, notas, colocadas nos mesmos locais, etc.) têm uma relação indirecta ou proximal.

</li>

</ol>

{{-}}

<span id="Specifying a relationship using the Relationships View">

### Especificar um parentesco na categoria Parentescos

![[_media/Relationships-category-view-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Parentescos]]

Para especificar um novo parentesco com o [indivíduo activo](wiki:Gramps_Glossary#active_person), mude para a categoria e verá este indivíduo indicado como "Indivíduo activo". Ao lado do rótulo está um botão (tipicamente representado por um sinal ).

{{-}}

![[_media/FamilyEditor-dialog-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editar uma família]]

Ao clicar no botão aparece o diálogo com o indivíduo activo definido como pai ou mãe.

{{-}}

![[_media/SelectMother-selector-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo Seleccionar mãe]]

E agora uma pergunta, o indivíduo que vai formar o parentesco com o indivíduo activo já existe na árvore genealógica? Se sim, clique em no outro indivíduo. Poderá então navegar pela lista de pessoas na árvore para seleccionar a que pretende. Caso contrário, clique em . Isto permitir-lhe-á adicionar um novo indivíduo à árvore genealógica e especificar a relação que esta pessoa tem com o indivíduo activo.

Para editar uma relação existente a partir da categoria , clique em junto à entrada correspondente da família. Se houver mais do que uma relação na lista, pode seleccionar o cônjuge ou parceiro que pretende clicando em , correspondente ao lado da relação.

{{-}}

<span id="Specifying a relationship using the Families List View">

### Especificar um parentesco usando a categoria Famílias

Para especificar uma nova relação na categoria clique em da barra de ferramentas e verá um diálogo vazio. Nesta altura, pode adicionar pessoas à família.

{{-}}

<span id="To specify parents">

## Para especificar pais

Pode especificar os pais do indivíduo activo na categoria (veja ). É necessário um pouco de cuidado para evitar a criação de . Se pretender adicionar o indivíduo activo a uma família já existente, deve clicar no botão . Se a família, incluindo os pais, ainda não existir, deve clicar em .

{{-}} ![[_media/SelectFamily-SelectorDialog-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo Seleccionar família]]

Se clicar em , é-lhe apresentado o diálogo . Este diálogo permite-lhe seleccionar a família existente e, em seguida, o indivíduo activo será adicionado como filho à família.

Se clicar em , é apresentado um diálogo vazio com o indivíduo activo listado como filho da nova família. Pode adicionar os pais à família, quer adicionando novos indivíduos, quer seleccionando indivíduos existentes como pais.

{{-}} Também pode especificar os pais de uma pessoa na categoria } Editor de referência de filhos\]\]

Se pretender alterar a relação pai/filho da definição pré-definida de **Nascido**, a partir do diálogo seleccione o filho e clique em . Isto abre o diálogo .

{{-}} Se pretender alterar a ordem dos filhos na família, utilize as setas ou a função [*arrastar e largar*](http://en.wikipedia.org/wiki/Drag_and_drop) no separador do . {{-}}

<span id="Adding photos and other media objects">

## Adicionar fotografias e outra multimédia

</span>

Podem ser anexados vários tipos de objectos multimédia (incluindo fotografias, documentos, ficheiros de áudio e ficheiros de vídeo) como [objectos secundários](wiki:Gramps_Glossary#secondary_object). Também pode adicionar imagens que podem não estar limitadas a uma única pessoa ou evento. (Por exemplo, fotografias de grupo de uma reunião de família)

O Gramps suporta vários tipos de objectos multimédia incluindo fotografias, documentos, ficheiros de áudio e ficheiros de vídeo. O método mais comum para adicionar multimédia é através do separador do editor de um objecto primário (como indivíduos, eventos, famílias, locais, citações, fontes, ou repositórios).

Antes de adicionar qualquer objecto multimédia '**'novo**', verifique novamente o no separador das preferências. Ao fazê-lo, confirme que usou o menu contextual , para que haja um botão para esse "caminho base de multimédia" no [selector de ficheiros](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#File_Chooser).

Adicionar informação opcional pode ajudar a categorizar a multimédia para facilitar a pesquisa posterior. Datas, títulos e [etiquetas](wiki:Gramps_Glossary#tag) podem ser adicionados a objectos multimédia.

1.  Abra o editor de objectos para o objecto primário clicando em .
2.  Seleccione o separador Galeria.
3.  Para adicionar um novo objecto multimédia, clique em :
    - navegue até ao ficheiro desejado, decida se deseja usar a opção "Converter para um caminho relativo";
    - clique em .
4.  Para [partilhar](wiki:Gramps_Glossary#sharing) um objecto multimédia existente, clique em :
    - seleccione um objecto existente usando o diálogo [Seleccionar objecto multimédia](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/pt_PT#Select_Media_Object_selector);
    - faça duplo clique no objecto ou clique em .
5.  Adicione informação opcional:
    - se o objecto for uma imagem, crie um retângulo na antevisão para refinar o conteúdo da miniatura.
6.  Expanda a secção e adicione detalhes úteis:
    - um **título** amigável;
    - a **data** em que o objecto foi criado ou que representa;
    - adicione etiquetas.
7.  clique em .

Ao adicionar alguns objectos multimédia, pode ser mais eficiente usar a categoria . Em seguida, use o botão para ligar a vários objectos primários conforme necessário.

span id="Using the Clipboard"\>

### Usar a área de transferência

</span>

![[_media/Clipboard-dialog-example-context-menu-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Área de transferência do Gramps - menu contextual]]

Se adicionar mais do que alguns objectos, considere usar a funcionalidade no [<strong>gestor de multimédia</strong>](wiki:Gramps_6.0_Wiki_Manual_-_Tools/pt_PT#Media_Manager) no menu . Na categoria , vá ao menu e marque Última alteração, ordene para os novos itens e copie-os para a [área de transferência](wiki:Gramps_Glossary#clipboard) do Gramps.

A área de transferência permite arrastar e soltar rapidamente para galerias do editor de objectos. No entanto, ao adicionar um objecto multimédia a várias galerias, partilhar a "referência da multimédia" pode ser mais eficiente do que ter uma cópia separada da referência do objecto multimédia. Após soltar um objecto multimédia numa galeria, copie-o novamente para a área de transferência. Isto cria uma "referência de multimédia" para esse objecto. Em seguida, limpe o objecto multimédia original da área de transferência.

Use convenções de nomenclatura consistentes para os seus ficheiros multimédia e adicione descrições detalhadas para facilitar a pesquisa. Lembre-se de fazer salvaguardas regulares, tanto da base de dados como da multimédia.

{{-}} ![[_media/People-tree-view-grouped-people-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Indivíduos - Vista em árvore - Indivíduos agrupados]]

Se quiser adicionar uma imagem a uma única pessoa, mude para a categoria , seleccione o indivíduo desejado, e clique em . {{-}}

![[_media/Edit-person-window-example-existing-person-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editar indivíduo]]

Seleccione o separador e clique em para abrir o diálogo . Escreva um nome deficheiro ou navegue até encontrar o ficheiro de imagem desejado e forneça um título à imagem. Continue a adicionar imagens até terminar. {{-}} ![[_media/Families-category-list-view-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Famílias]]

Para adicionar imagens relacionadas com um parentesco (por exemplo, um casamento), mude para a categoria e clique duas vezes na caixa Cônjuge. Isto abre o diálogo . Seleccione o separador e clique em para adicionar uma imagem. {{-}}

![[_media/SourcesCategory-SourcesListView-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Fontes]] ![[_media/PlacesCategory-PlaceListView-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Locais]]

Para adicionar imagens relacionadas com uma fonte ou local, primeiro mude para a respectiva categoria ou . Seleccione a fonte ou local desejado e faça duplo clique ou clique em . Seleccione o separador e clique em .

{{-}}

![[_media/MediaCategory-MediaListView-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Multimédia]]

Por fim, para adicionar imagens que deseje incluir na árvore genealógica, mas não estão limitadas a nenhuma pessoa, relacionamento, fonte ou lugar específico, mude para a categoria . Clique em . Se já adicionou alguma imagem a alguma galeria individual, também as encontrará listadas na categoria .

Em qualquer galeria, também pode usar o botão para editar informações de imagem e o botão e para remover a referência de imagem dessa galeria.

<span id="To edit events, citations/sources, places, and repositories">

## Para editar eventos, citações/fontes, locais e repositórios

</span>

Para editar informações sobre eventos, fontes, locais e repositórios já presentes na árvore genealógica, mude para a categoria apropriada, seleccione a entrada que deseja ver/modificar e, em seguida, clique em na barra de ferramentas. Alternativamente, pode clicar duas vezes na entrada para a editar.

![[_media/EventsCategory-EventsListView-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Eventos]]

Para adicionar um evento, uma citação/fonte, um local ou um repositório à árvore genealógica, mude para a categoria apropriada , , , , ou . Depois clique em para adicionar o objecto correspondente. Insira as informações no correspondente editor de eventos.

[Category:Pt PT:Documentation](wiki:Category:Pt_PT:Documentation)
