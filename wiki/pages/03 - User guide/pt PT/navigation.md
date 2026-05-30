---
title: Gramps 6.0 Wiki Manual - Navigation/pt PT
categories:
- Pt PT:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 113358
wiki_fetched_at: '2026-05-30T19:49:55Z'
lang: pt PT
---

{{#vardefine:chapter\|10}} {{#vardefine:figure\|0}} Enquanto qualquer base de dados de uma [árvore genealógica](wiki:Genealogy_Glossary#family_tree) estiver aberta, o Gramps centra-se numa única pessoa, normalmente designada por [indivíduo activo](wiki:Gramps_Glossary#active_person). Isto permite-lhe ver ou modificar os dados relativos a esta pessoa e à sua família directa, etc.. [Navegar na árvore genealógica](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/pt_PT#Setting_the_Active_Person) (i.e. passar de pessoa para pessoa) não é, de facto, mais do que mudar o indivíduo activo.

Esta secção descreve muitas formas alternativas de navegar através da base de dados usando tanto as formas complexas como as convenientes que o Gramps fornece. Todas estas formas atingem fundamentalmente o mesmo resultado, mas alguns métodos de navegação serão mais convenientes do que outros, dependendo do que está a fazer no Gramps no momento.

<span id="Using the People Category">

## Utilizar a categoria Indivíduos

</span>

A maneira mais intuitiva de mudar o indivíduo activo é usar a [categoria Indivíduos](wiki:Gramps_6.0_Wiki_Manual_-_Categories/pt_PT#People_Category). Quando estiver na categoria Indivíduos, basta seleccionar o nome da pessoa desejada na lista clicando nessa entrada. A pessoa que seleccionou torna-se activa. A barra de estado é actualizada para reflectir a mudança.

Ver também

- [Editar informação sobre indivíduos](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/pt_PT#Editing_information_about_people)

\<span id="Using the Relationships Category

## Utilizar a categoria Parentescos

</span>

Na [categoria Parentescos](wiki:Gramps_6.0_Wiki_Manual_-_Categories/pt_PT#Relationships_Category), pode navegar facilmente entre os membrosda família mostrada como segue:

Clique no nome sublinhado da pessoa a quem deseja ir e esta pessoa será o novo indivíduo activo da categoria Parentescos.

O nome da pessoa actualmente activa não está sublinhado.

Além disso, o Gramps oferece um extenso conjunto de opções de navegação com o teclado. A referência detalhada atalhos de teclado é encontrada no [Apêndice B: Referência de atalhos](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT).

<span id="Using the Families Category">

## Utilizar a categoria Famílias

</span>

Na [categoria Famílias](wiki:Gramps_6.0_Wiki_Manual_-_Categories/pt_PT#Families_Category), pode navegar facilmente entre as famílias mostradas.

As famílias podem ser usadas para comparar visualmente uma série de famílias em busca de possíveis duplicatas e dados em falta. A classificação nas diferentes colunas permite colocar parceiros com nomes semelhantes próximos, permitindo que os cônjuges sejam comparados. Pode combinar por nome próprio ou apelido alterando temporariamente o "formato de nome" nas [separador Mostrar](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Display) no diálogo . Por exemplo, um formato de nome de "Nome próprio Apelido Sufixo" faria a ordenação da coluna pelo sufixo.

A união de duas famílias não só combinará os objectos secundários da família, mas também e simultaneamente os dois pais e as duas mães.

O gramplet Filtro da vista Família permite procurar indivíduos em diferentes funções familiares. Pode procurar famílias com um pai chamado "João", uma mãe chamada "Maria" e uma criança chamada "Tomás".

<span id="Using the [[File:22x22-gramps-pedigree.png]] Charts Category">

## Utilizar a categoria ![[_media/22x22-gramps-pedigree.png]] Gráficos

</span> ![[_media/TimelinePedigreeView-Addon-Person-ContextMenu-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Cronologia de costados - Extensão de terceiros - menu contextual]] O Gramps depende muito de disposições baseadas em formulários de itens de lista vinculados. Isto implica relações entre registos na árvore genealógica. A **categoria Gráficos** fornece uma forma alternativa, mais visual, de representar essas relações. As posições, formas e cores dos recipientes, juntamente com as linhas de ligação e setas podem mostrar uma profundidade extra de inter-relação com diferentes factores. Os contentores podem ser caixas simples preenchidas por cores, arcos, fitas ou muitos outros formatos.

Mas a [categoria Gráficos](wiki:Gramps_6.0_Wiki_Manual_-_Categories/pt_PT#Charts_Category) também fornece uma maneira alternativa de navegar pela árvore genealógica. O benefício deste método é que pode ver mais de uma geração da árvore genealógica. Pode ir directamente de um bisneto para um bisavô sem passar pelas gerações intermediárias.

Note que depois de alterar o [indivíduo activo](wiki:Gramps_Glossary#active_person) na categoria Gráficos, o gráfico é reajustado para focar o indivíduo activo recém-seleccionado. Quando estiver na categoria Gráficos, poderá navegar facilmente entre os membros da árvore genealógica exibida da seguinte forma:

Para fazer com que qualquer pessoa exibida se torne no indivíduo activo, clique com o botão esquerdo na caixa correspondente. Clicar com o botão direito abre um menu contextual com opções apropriadas ao conteúdo.

O menu contextual de uma caixa individual pode conter ▶ sub-menus listando todos os cônjuges, irmãos, filhos e pais desse indivíduo. A primeira entrada no menu geralmente será o nome (pode alternativamente ser uma opção Editar.) Seleccionar o nome da pessoa mudará o foco da mesma forma que clicar com o botão esquerdo na caixa. Também pode alterar o foco para qualquer um dos cônjuges, irmãos, filhos ou pais de qualquer pessoa exibida.

Alguns gráficos têm uma correlação de navegação óbvia. Mover-se através de gerações corresponde intuitivamente a mover-se para a esquerda, direita, para cima ou para baixo no gráfico. Podem ter botões de navegação direccionais personalizados para permitir a navegação clicando em vez de arrastando.

Como exemplo, para alterar o foco da [vista Costados](wiki:Gramps_6.0_Wiki_Manual_-_Categories/pt_PT#Pedigree_View) para um filho (se existir) do indivíduo activo, cliclique em (*Seta esquerda*) à esquerda da caixa do indivíduo activo. Se houver apenas um filho, o foco muda imediatamente. Caso contrário, o botão (*Left Arrowhead*) expande-se com um menu com uma lista seleccionável dos filhos. Para este botão (*Seta esquerda*), a lista defilhos é ordenada por casamentos dos pais, sub-ordenada por ordem de nascimento. Estas [ordens podem ser alteradas](wiki:Gramps_6.0_Wiki_Manual_-_FAQ/pt_PT#How_do_I_change_the_order_of_children.3F) globalmente na categoria Parentescos.

Assim como as caixas, os botões podem ter recursos alternativos acedidos clicando com o botão direito e escolhendo num menu contexual.

Outros botões são auxílios menos óbvios para navegar, não para indivíduos, mas para recursos do Gramps. Usando o exemplo da [vista Costados](wiki:Gramps_6.0_Wiki_Manual_-_Categories/pt_PT#Pedigree_View) novamente, pairar sobre as linhas entre as caixas mostra uma dica com quaisquer detalhes básicos conhecidos sobre o relacionamento e clicar duas vezes nessas linhas abre o editor nessa família. E clicar duas vezes na caixa do indivíduo activo abre o seu editor. Vale a pena ler a documentação detalhada em cada vista do gráfico para descobrir esses atalhos ocultos para os recursos favoritos.

As vistas internas da [categoria Gráficos](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Charts_Category) são apresentadas na secção [Categories](wiki:Gramps_6.0_Wiki_Manual_-_Categories/pt_PT). Algumas são descritas com maior profundidade em artigos listados na parte inferior da secção introdutória da vista.

A colecção de vistas na categoria Gráficos pode ser expandida com extensões de terceiros usando o [gestor de extensões](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager/pt_PT) do Gramps. As extensões disponíveis podem ser encontrados na coluna *'View* da [lista de extensões](wiki:6.0_Addons#Addon_List). A manutenção de algumass extensões de terceiros foi adoptada pela equipa de voluntários do Gramps ao longo dos anos. Estes tornaram-se "internos" após serem examinados, e depois incluídos nas principais versões do Gramps. Os artigos sobre como usar cada extensão estão ligados à coluna *'Plugin/Documentation*. A qualidade da documentação varia dramaticamente para esses artigos.

<span id="Using Gramplets">

## Utilizar gramplets

</span>

![[_media/DashboardCategoryView-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Painel - Gramplets vários]]

Nas [barras lateral e inferior](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#The_split-screen_Sidebar_.26_Bottombar), pode adicionar gramplets para expandir as opções de navegação além da distância de uma única geração. Alguns exemplos são:

- [Parentes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Relatives)
- [Descendentes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Descendants)
- [Costados](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Pedigree)
- [Leque](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Fan_Chart)

Estes exemplos fornecem a capacidade de navegar do indivíduo activo para parentes, descendentes ou ascendentes próximos. Os futuros gramplets poderão permitir a navegação por proximidade geográfica, [comparação de ADN](wiki:Addon:DNASegmentMapGramplet) ou qualquer outra ligação ainda não considerada.

Os gramplets baseados em texto tendem a ter nomes [ligados à navegação](#Hotlink_Navigation), enquanto os gráficos recorrem mais a [menus contextuais](#Contextual_Menu_Navigation).

{{-}}

<span id="Setting the Home Person">

## Definir o indivíduo inicial

</span>

Uma (e apenas uma) pessoa na base de dados pode ser designada como [indivíduo inicial](wiki:Gramps_Glossary#home_person). Uma vez designado, devolver o foco do [indivíduo activo](wiki:Gramps_Glossary#active_person) a essa pessoa passa a ser uma questão de um único clique, independentemente de qual categoria está a usar no momento.

Para definir o indivíduo inicial, primeiro [navegue](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/pt_PT#Setting_the_Active_Person) até ao indivíduo desejado com o seu método preferido. Em seguida, escolha a categoria Indivíduos e seleccione . Feito isto, pode passar para o indivíduo inicial de qualquer local da base de dados de dados simplesmente clicando no ícone da barra de ferramentas . Também pode escolher o menu , seleccionar item em qualquer menu contextual disponível no clique direito, ou usar o atalho de teclado .

- [Definir o indivíduo inicial](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Setting_Home_person)
- No [diálogo Editar indivíduo](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/pt_PT#Edit_Person_dialog) pode seleccionar no menu contextual.

<span id="Setting the Active Person">

## Definir o indivíduo activo

</span>

O [indivíduo activo](wiki:Gramps_Glossary#active_person) é tido como foco de acções, relatórios e edições contextuais. São o item seleccionado na categoria Indivíduos ou Parentescos.

O indivíduo activo pode ser seleccionado directamente ou "navegado para" indirectamente. Os métodos incluem:

- clicar na pessoa na categoria Indivíduos;
- seleccionar a pessoa no menu [Marcadores](#Bookmark_Navigation);
- [usando o histórico de navegação](#Using_history-based_Navigation) (botões e na barra de ferramentas e o menu );
- [navegação por hiperligações](#Hotlink_Navigation);
- [menus contextuais](#Contextual_Menu_Navigation);
- [notas como atalhos de navegação](#Notes_as_Navigational_Shortcuts).

Há um realce de selecção como uma dica visual do indivíduo activo na categoria Indivíduos. Na categoria Parentescos, o indivíduo activo é mostrado numa secção separada na parte superior. Todas as outras pessoas mostradas abaixo têm um parentesco imediato (pai, irmão, cônjuge, filho) com o indivíduo activo. Opcionalmente, a [barra de estado](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Display) pode ser configurada para mostrar a o objecto em foco na vista (o indivíduo activo é o foco em várias vistas).

<span id="Hotlink Navigation">

### Navegação por hiperligações

</span>

![[_media/Relationships-category-view-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Parentescos]]Normalmente, simplesmente clicar no nome hiperligado de uma pessoa seleccionará essa pessoa e mudá-la-á para o foco contextual de indivíduo activo.

O nome de cada pessoa nas categorias Indivíduos e Parfentescos é uma hiperligação. Alterar o foco do indivíduo activo na categoria Indivíduos parece apenas alterar qual registo está realçado. Mas também faz com que o conteúdo dos gramplets seja actualizado e as categorias Parentescos, Gráficos e Geografia sejam reorientadas para o novo indivíduo activo.

Seleccionar um nome hiperligado diferente na categoria Parentescos causa uma mudança menos súbtil. A perspectiva de como os dados familiares são representados muda para esse foco. Os seus detalhes passam para a secção superior e a sua família imediata é reorganizada abaixo.

{{-}}

<span id="Contextual Menu Navigation">

### Navegação pelo menu contextual

</span> ![[_media/QuickViewReport-EditPerson-context-menu-popup-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu contextual no editor de indivíduos]]No entanto, nomes hiperligados nos separadores Referências e Notas (e nalguns gramplets) apenas abrirão a janela do editor de indivíduos *sem* mudar o foco para essa pessoa (essas ligações comportam-se como se tivesse clicado em em vez de numa hiperligação). Isto facilita a edição rápida de indivíduos em torno do indivíduo activo, sem a desorientação de uma mudança de foco.

O foco pode ser definido enquanto estiver no diálogo [Editar indivíduo](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/pt_PT#Edit_Person_dialog) usando o menu contextual (clicando com o botão direito) no espaço vazio da área do cabeçalho. A opção nesse menu contextual altera o foco para a pessoa em edição.

{{-}}

<span id="Using history-based Navigation">

### Utilizar navegação por histórico

</span>

![[_media/History-based-navigation-tools-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Exemplo de ferramentas de navegação por histórico]]

O Gramps também dispõe de um poderoso conjunto de ferramentas de navegação baseadas no histórico. Estas ferramentas são semelhantes às comummente usadas em navegadores da web.

Incluem itens e , disponíveis no menu , em menus contextuais (nas categorias Indivíduos, Famílias e Costados), e os botões da barra de ferramentas ![[_media/Gramps_Go-Previous48x48_win.png]]![[_media/Go-next48x48_win.png]]. Também incluem a lista das selecções recentes disponíveis no menu , que permitem saltar directamente para qualquer uma delas. Por fim, clicar com o botão direito do rato nos ícones e chama o menu com a parte correspondente do histórico. Seleccione qualquer item desse menu para lhe aceder directamente. {{-}}

<span id="Bookmark Navigation">

### Navegação por marcadores

</span>

![[_media/Gramps_Go-Home48x48_win.png]] O botão Início na barra de ferramentas é um marcador especial. Desloca o foco do indivíduo activo para o indivíduo actualmente definido como [indivíduo inicial](wiki:Gramps_Glossary#Home_Person). Isto é tão frequentemente útil que esta funcionalidade também tem um [atalho de teclado](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT#Common_keybindings).

À semelhança da definição dindivíduo inicial, pode marcar outros indivíduos da base de dados para simplificar a navegação. Para marcar tal, primeiro navegue até ao indivíduo desejado e, em seguida, seleccione . Para ir para esse indivíduo noutra parte da base de dados, vá a a partir da lista de marcadores mostrada. As outras categorias têm a sua própria lista de marcadores.

![[_media/Organizebookmarks-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Organizar marcadores]]Pode gerir os seus marcadores seleccionando ou premindo o [atalho](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT) . Isto abre o diálogo , com a lista de marcadores e os controlos para modificar essa lista.

Utilize os botões e para alterar a sequência. Use o botão para eliminar um marcador. O botão abre esta mesma página, e o botão encerra o diálogo .

A lista de indivíduos marcados pode ser seleccionada através da categoria Indivíduos, como explicado acima, mas também é partilhada com as categorias Parentescos e Gráficos.

De forma semelhante, são mantidas listas separadas de marcadores em cada uma das seguintes categorias: Famílias, Eventos, Locais, Fontes, Citações, Repositórios, Multimédia e Notas.

{{-}}

<span id="Notes as Navigational Shortcuts">

### Notas como atalhos de navegação

</span> ![[_media/NoteLinkingHints-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Editor de notas - Ligar texto]]Existem listas de marcadores separadas em várias categorias. Mas continuam a ser apenas listas simples. As listas longas de marcadores tornam-se rapidamente difíceis de gerir.

Podem ser criadas ligações persistentes em [notas](wiki:Gramps_Glossary#note). Use o [editor de ligações](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/pt_PT#Link_Editor) em notas para organizar ligações de navegação para diferentes tipos de registos do Gramps, de acordo com os seus próprios métodos de organização. Uma vez que uma nota tenha um texto ligado, esse texto pode ser usado como um marcador. Nos gramplets de notas onde a edição não está activa, clicar na hiperligação abre o editor de objectos para essa ligação (requer um modificador extra no editor de notas: navegue até esse registo mantendo premida a tecla e clicando no texto ligado). Uma nota pode ser usada como índice ligado a outras notas com diferentes conjuntos de ligações.

Um exemplo de uma nota ligada pode incluir um obituário em que todas as pessoas, locais ou mesmo eventos estão ligados. Isto torna mais fácil navegar para os porta-estandartes, [oficiantes](wiki:Gramps_Glossary#officiator) de funerais, ou participantes indirectamente relacionados (ou mesmo não relacionados).

Outra nota pode ser a bibliografia transcrita para a pesquisa original publicada de outro genealogista. À medida que recolhe cópias digitais dessas referências originalmente citadas, a bibliografia ligada pode ser usada como uma lista de verificação de aquisição de fontes. Quando completamente ligada, a bibliografia pode ser utilizada para navegar através das fontes para cada citação enquanto procura conclusões não suportadas, inexactidões ou omissões. {{-}}

<span id="Finding records">

## Localizar registos

</span>

<span id="Browse to a record">

### Navegar para um registo

</span>

Para encontrar um registo numa das categorias, comece por mudar para a categoria adequada que fornece a lista dos registos pretendidos: Indivíduos, Fontes, Locais ou Multimédia. Em seguida, desloque-se para o registo pretendido. O foco do registo activo para a categoria é alterado ao seleccionar um registo. Ir simplesmente para a categoria não altera o foco do registo activo.

Por defeito, a lista será ordenada pela primeira coluna dos dados da tabela. Nos registos agrupados (Indivíduos) ou em árvore hierárquica (Locais), a primeira coluna tem de ser a coluna "Nome". Nos indivíduos, o agrupamento é baseado no apelido preferido. Nos locais, o agrupamento baseia-se na ordem dos locais envolventes.

A ordem e a exibição (ou não) das colunas podem ser configuradas. Aparece um diálogo depois de seleccionar (ou clicando em Configurar na barra de ferramentas ou premindo o [atalho comum](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT#Common_keybindings).

A lista de registos na categoria pode ser reduzida através da filtragem com a [Barra de procura](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Search_Bar) ou o [gramplet Filtro](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#Filter). {{-}}

<span id="Find a Record">

### Localizar um registo

</span>

![[_media/Find-people-list-view-typeahead-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Indivíduos (agrupados) - Procura interactiva]]

Também referida como "procura interactiva ao escrever".

Seleccione uma linha na lista para obter o foco e, em seguida, comece a escrever informações que possam estar contidas nos dados da coluna de ordenação (nome de indivíduos ou o título de fontes, locais ou multimédia). O foco mudará para o primeiro registo que corresponda ao texto na caixa de pesquisa (a amarelo na figura {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}}). Em alternativa, depois de clicar em qualquer parte da área principal para obter o foco, prima o [atalho](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT#All_List_Views_bindings) ( em macOS) para activar a caixa de pesquisa. Estatalho é muitas vezes ignorado, uma vez que o simples facto de começar a escrever também é suficiente para abrir a caixa e começar a inserir o termo de pesquisa.

À medida que escreve, o primeiro registo correspondente na coluna de ordenação da lista desloca-se para o centro da lista e é seleccionado. À medida que escreve mais caracteres, a correspondência será refinada. Enquanto a caixa de pesquisa estiver visível, se premir a seta para baixo passa para a correspondência seguinte e se premir a seta para cima passa para a correspondência anterior. A caixa desaparece depois de estar inactiva (sem escrever nada durante 5 a 15 segundos). Sem a caixa activa, as teclas de controlo do cursor voltam a mover a selecção de registos para cima e para baixo na lista.

Alterar a coluna de ordenação (clicando no cabeçalho) também altera a coluna que está a ser comparada. A procura numa coluna de ordenação diferente funciona melhor nos modos de lista plana.

As categorias Indivíduos ou Locais com agrupamento hierárquico são um pouco menos reactivas do que as listas planas, já ordenadas alfabeticamente. A funcionalidade Indivíduos agrupados é a mais complexa. Por defeito, é ordenada pelo nome do grupo e depois sub-ordenada pela coluna "Nome" escolhida no separador Dados, [Formato do nome](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Display_Name_Editor), nas preferências. Este será o nome preferido/primário no formato "Apelido, Sufixo Nome próprio" e "Apelido" inclui o prefixo e os ligadores. No entanto, as definições "Agrupar como", "Ordenar como" e "Mostrar como" podem ser utilizadas para substituir a ordem utilizando a opção "[Editor de nomes](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data%3A_detailed_-_part_3/pt_PT#Name_Editor).' {{-}}

<span id="Jump to by Gramps ID">

### Ir para ID Gramps

</span> ![[_media/Jump-to-by-Gramps-ID-dialog-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo Ir para ID Gramps]]

Se souber a ID do registo de destino na categoria actualmente activa, a funcionalidade **Ir para** pode ser a forma mais eficiente de navegar para esse destino. Premir o [atalho](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT#Common_keybindings) abre o diálogo , que lhe permite inserir a [ID Gramps](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#ID_Formats) para a qual pretende activar o foco.

só procura uma correspondência de texto exacta. A ID do Gramps pode ser gerada automaticamente quando o campo ID é deixado em branco ao adicionar um registo ou [inserida manualmente](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/pt_PT#ID) como substituição.

É semelhante a localizar, excepto que não é interactiva e SÓ funciona no campo ID do Gramps, em vez da coluna que está actualmente seleccionada para ordenação. E pode alterar o foco do registo activo em todas as categorias, excepto nas categorias Geografia e Painel.

#### Veja também

- Discussão [The “Jump to” Gramps ID feature](https://gramps.discourse.group/t/the-ctrl-j-jump-to-gramps-id-feature/3756)

<!-- -->

- GEPS: [Propostas de concepção do selector](wiki:GEPS_041:_New_Selector)

{{-}}

<span id="Navigation History">

### Histórico de navegação

</span>

É seguido um histórico dos registos recentemente activos para o foco da categoria activa. Os últimos dez registos estão acessíveis através do menu e respectivos [atalhos](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT#Common_keybindings). Ou pode percorrer o histórico com os botões e .

<span id="Using the Clipboard">

## Utilizar a área de transferência

</span>

![[_media/Clipboard-dialog-example-context-menu-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Área de transferência - Menu contextual (clique direito)]]

Para uma aplicação como o Gramps, a é muito importante, pois ajudará a reduzir a entrada repetitiva de dados.

A ferramenta fornece um bloco de notas temporário para armazenar registos da base de dados para fácil reutilização durante uma única sessão do Gramps, por exemplo, até sair do Gramps. Em resumo, esta é uma espécie de funcionalidade de copiar e colar estendida de objectos textuais para outros tipos de registos usados no Gramps. A área de transferência faz uso extensivo da técnica [*arrastar e largar*](http://en.wikipedia.org/wiki/Drag-and-drop).

Para abrir a , escolha , clique em ![[_media/Gramps_Clipboard48x48_win.png]] ou use o [atalho](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT#8) .

A suporta endereços, atributos (individuais e familiares), eventos (individuais e familiares), nomes, referências a objectos multimédia, citações, URLs e, claro informação textual de notas e comentários. Para armazenar qualquer tipo destes registos, basta arrastar o registo existente para a a partir do editor correspondente. Para reutilizar o registo, arraste-o da área de transferência para o local correspondente no editor, por exemplo, o separador Endereço, o separador Atributo, etc..

{{-}}

<span id="Clipboard context menu">

### Menu contextual da área de transferência

</span>

A selecção de um registo através do menu contextual (clique com o botão direito do rato) mostra as três opções seguintes para cada tipo de registo:

- 

- 

- 

{{-}}

Um exemplo  
encontra-se uma certidão de nascimento de uma pessoa; nesta certidão também são mencionadas as testemunhas; e a certidão de nascimento também determina uma fonte onde a informação foi armazenada; a melhor forma de o fazer é abrir a área de transferência e arrastar para lá a fonte com que pretende trabalhar; depois, arraste e largue para a utilizar nos novos itens que utilizar.

Agora pode finalizar as informações no ecrã do editor de indivíduos. Arraste também essa informação para a área de transferência.

Adicione dois novos indivíduos como testemunhas (assumindo que não os tem já na sua base de dados). Basta arrastar e largar as informações de nascimento no ecrã de eventos de testemunhas. É-lhe então mostrado o ecrã onde pode alterar a função da testemunha para testemunha deste evento de nascimento.

Faz-se o mesmo com a outra testemunha o que poupa muita escrita e evita possíveis erros.

<span id="Using the Addon Manager">

## Utilizar o gestor de extensões

</span>

![[_media/AddonManager-example-listing-60-pt_PT.png|Right\|thumb\|550px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} **Gestor de extensões** - separador]] O Gramps utiliza módulos internos e extensões (também chamadas de "[plug-ins ou add-pns](https://wikipedia.org/wiki/Plug-in_(computing))") para estender as capacidades da aplicação base. Uma das principais vantagens de uma estrutura de extensões é que ela permite a evolução de um recurso específico sem a necessidade de actualizar todo o programa. As extensões não devem ser confundidas como sendo de menor utilidade para os utilizadores básicos do que as funcionalidades principais ou as extensões incorporadas. Nem "de terceiros" significa que uma extensão é de menor qualidade. No entanto, as extensões publicadas no repositório GitHub do Gramps-Project foram verificadas e não alterarão secretamente os dados da sua árvore.

O [gestor de extensões](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/pt_PT#Addon_Manager) fornece uma forma de explorar as extensões que podem melhorar os seus fluxos de trabalho pessoais. E o [gestor de extensões interno](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager/pt_PT) (ou o [gestor de extensões melhorado](wiki:Addon:Plugin_Manager)) fornecem uma forma de personalizar o Gramps para remover a confusão de funcionalidades que não utiliza.

A janela , separador listará as extensões adicionais de terceiros disponíveis nos itens actualmente seleccionados no separador .

{{-}}

<span ID="Addon Manager...">

### Gestor de extensões

</span> O mostra os seguintes separadores:

- , com a lista de extensões disponíveis;

- , com as opções do gestor;

- , onde pode gerir ligações a repositórios locais ou externos.

Para além destes, dispõe de três botões ao fundo da janela, , que abre esta página, , que actualiza a lista de extensões, e , que fecha o gestor de extensões.

{{-}} <span id="Addons">

#### Separador Extensões

</span> ![[_media/AddonManager-default-60-pt_PT.png|Right\|thumb\|550px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} **Gestor de extensões** - filtros pré-definidos - a carregar extensões]]

O separador do é uma lista de todas as extensões disponíveis. Dispõe de uma barra de procura ao cimo, onde pode escrever livremente. A procura é interactiva e selecciona automaticamente as melhores correspondências encontradas. Esta lista pode ser filtrada através das listas pendentes (a amarelo na imagem).

Estes filtros podem ser combinados entre si de múltiplas formas, facilitando a procura daquilo que deseja instalar. {{-}} O primeiro filtra a lista por estado da instalação: {{-}} ![[_media/AddonManager-AddonExample-Installed-60-pt_PT.png|Right\|thumb\|550px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} **Gestor de extensões** - filtros pré-definidos - Extensão instalada]]

  
  
extensão instalada, onde se podem ver as suas características a azul. Em todos os casos, verá um botão Wiki (a amarelo), que o leva à página correspondente à extensão, com informação detalhada;

{{-}} ![[_media/AddonManager-AddonExample-NotInstalled-60-pt_PT.png|Right\|thumb\|550px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} **Gestor de extensões** - filtros pré-definidos - Extensão não instalada]]

  
  
extensão por instalar, reflectido pelo botão à direita dentro da moldura da extensão;

{{-}} ![[_media/AddonManager-AddonExample-RequiresDialog-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gestor de extensões - Requisitos Python]] ![[_media/AddonManager-AddonExample-NotInstalled-Requires-60-pt_PT.png|Right\|thumb\|550px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} **Gestor de extensões** - filtros pré-definidos - Extensão não instalada, que requer outros módulos do sistema operativo]] caso a extensão precise de módulos externos que não existam no seu sistema operativo, verá o botão (a amarelo); clicar neste botão abre o diálogo de requisitos necessários, meramente indicativo, com a lista daquilo que terá de instalar no sistema operativo para que a extensão funcione. [Pode automatizar este processo](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/pt_PT#General) no separador . {{-}} ![[_media/AddonManager-AddonExample-Update-60-pt_PT.png|Right\|thumb\|550px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} **Gestor de extensões** - filtros pré-definidos - Extensão por actualizar]]

  
  
caso a extensão precise de actualização, verá o botão .

{{-}} O segundo filtro utiliza a lista dos repositórios existentes no separador .

O terceiro permite escolher o tipo/finalidade da extensão, podendo ser, entre outros, um gramplet, uma ferramenta, uma barra lateral, etc..

O quarto filtro destina-se à escolha da audiência-alvo, onde poderá especificar o seu interesse, por exemplo, em extensões para programadores.

O último oferece a escolha da versão da extensão, para os mais conservadores a estável, para os mais aventureiros, uma das outras.

À direita dispõe de um botão para repor as pré-definições de filtragem, anulando as escolhas anteriores.

{{-}}

<span id="Settings">

#### Definições

</span>

<span id="General">

##### Geral

</span>

-   
  desmarcada por defeito

![[_media/AddonManager-Settings-tab-default-60-pt_PT.png|Right\|thumb\|550px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} **Gestor de extensões** - separador]] <span id="Scheduled update checks">

##### Procura de actualizações agendada

</span>

A definição seguinte só se aplica ao diálogo .

- seleccione a frequência com que o Gramps procura actualizações para [extensões](wiki:6.0_Addons#Installing_Addons_in_Gramps):

  - *Nunca* - nunca verifica se há actualizações quando inicia o Gramps (*pré-definição*);
  - *Uma vez por mês* - verifica se há actualizações quando se inicia o Gramps uma vez por mês;
  - **Uma vez por semana** - verifica se há actualizações quando se inicia o Gramps uma vez por semana;
  - *Uma vez por dia* - verifica se há actualizações quando se inicia o Gramps uma vez por dia;
  - *Sempre* - verifica se há actualizações quando se inicia o Gramps.

- Quando procura actualizações, verifica:

  - *Só extensões actualizadas* - não procura novas extensões;
  - *Só novas extensões* - não procura extensões actualizadas (*pré-definição*);
  - **Extensões novas e actualizadas** - verifica todaas as extensões novas e actualizadas.

- {:

  - marcada significa que as extensões novas/actualizadas só são questionados uma vez; depois disso não as mostra (*marcada por defeito*);

  - desmarcada significa que as extensões novas/actualizadas são sempre mostrados ao utilizador.

-   
  o botão assume que há uma ligação à **Internet** e, se clicado, forçará uma verificação das extensões com base nas definições acima; se as extensões estiverem disponíveis, ser-lhe-á apresentada a janela , onde as escolhe e instala.

{{-}} ![[_media/AvailableGrampsUpdatesforAddons-example-listing-60-pt_PT.png|Right\|thumb\|550px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Diálogo **Há actualizações para extensões do Gramps**]] <span id="Available Gramps Updates for Addons">

##### Há actualizações para extensões do Gramps

</span>

O diálogo mostrará uma lista dividida por **Tipo**, que pode expandir cada "Tipo".

- Pode então marcar a caixa das extensões que quer instalar.
- Depois, clique em para transferir os ficheiros da *Internet*.
- Uma vez transferidos, clique em .
- No diálogo do antecedente, clique em .
- Para usar as extensões poderá ser necessaŕio e reiniciar o Gramps.

{{-}}

<span id="Projects">

#### Projectos

</span> ![[_media/AddonManager-Projects-tab-default-60-pt_PT.png|Right\|thumb\|550px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} **Gestor de extensões** - separador]]

Onde procurar extensões no servidor principal do Gramps:

- **Gramps**:

:;https://raw.githubusercontent.com/gramps-project/addons/master/gramps60

Ou qualquer servidor de extensões compatível com o Gramps que tenha adicionado. A secção [Outro projectos](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/pt_PT#Other_projects) mostra uma lista de projectos externos conhecidos. Perto do canto inferior esquerdo do separador Projectos tem as seguintes opções:

- \- abre o diálogo para adicionar o nome do projeto e o URL;

- \- elimina os projetos seleccionados (o projecto pré-definido **Gramps** não pode ser eliminado, mas pode ser desmarcado, pelo que nada é verificado nesse servidor);

- \-

- \-

- \- abre o diálogo , onde seleccionar remove todos os outros projectos.

{{-}} <span id="New Project dialog">

##### Diálogo Novo projecto

</span> ![[_media/NewProject-default-dialog-60-pt_PT.png|Right\|thumb\|450px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Diálogo **Novo projecto**]]

O diálogo permite inserir o e de projectos externos, podendo também ser usado para projectos locais. {{-}}

<span id="Other Projects">

##### Outros projectos

</span> ![[_media/AddonManager-Projects-tab-populated-60-pt_PT.png|Right\|thumb\|550px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} **Gestor de extensões** - projectos adicionais no separador]] Lista de outros projectos externos conhecidos (copiar e colar o nome do projecto e o URL, se necessário):

<hr>

- **Nome do projecto:** `Isotammi project addons`

:;URL:

:;https://raw.githubusercontent.com/Taapeli/isotammi-addons/master/addons/gramps60

  
Resumo: [Addon:Isotammi project](wiki:Addon:Isotammi_addons)

<hr>

- **Nome do projecto:** `Jean Michault tools for FamilySearch`

:;URL:

:;https://raw.githubusercontent.com/jmichault/gramps-kromprogramoj/gramps60

  
Resumo: <https://github.com/jmichault/gramps-kromprogramoj> & [PersonFS](https://github.com/jmichault/PersonFS) gramplet (FamilySearch) / <https://github.com/jmichault/gramps-kromprogramoj/blob/gramps60/ReadMe.en.md>

<hr>

- **Nome do projecto:** `GlopGlop’s collection for France`

:;URL:

:;https://raw.githubusercontent.com/grocanar/glopglop-addons/main/gramps60

  
Resumo: GedcomforGeneanet & ImportGenewebPlus

<hr>

- **Nome do projecto:** `ztlxltl experimental FamilyTreeView (FTV) chart view`

:;URL:

:;https://raw.githubusercontent.com/ztlxltl/FamilyTreeView/dist/gramps60

  
Resumo: <https://github.com/ztlxltl/FamilyTreeView>

<hr>

Também pode adicionar projectos locais, ver exemplo da captura de ecrã. Existe um tópico de apoio da comunidade Discourse onde outros ["Project"](https://gramps.discourse.group/t/curated-addon-collections/7170) (ou colecções mantidas de extensões Gramps) estão listados. {{-}}

![[_media/Restore_project_defaults-dialog-60-pt_PT.png|Right\|thumb\|550px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} **Repor pré-definições do projecto**]] <span id="Restore project defaults">

##### Repor pré-definições do projecto

</span>

Se necessário, pode verificar se a opção tem o URL correcto. Para localizar a [lista de extensões](https://raw.githubusercontent.com/gramps-project/addons/master/gramps60/listings/addons-en.json) para o seu idioma e versão, deverá ser:

:;https://raw.githubusercontent.com/gramps-project/addons/master/gramps60. Se não for, clique em . {{-}}

<span id="Main Menus">

## Menus principais

</span> ![[_media/Menubar-MainMenuOverview-NoFamilyTree-Loaded-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Barra de menus - Sem árvore genealógica carregada]]

A barra de menus mostra as opções disponíveis dos menus do Gramps.

Antes de carregar uma árvore, só estarão disponíveis menus muito abreviados. Estes permitem gerir árvores, sair do Gramps, editar preferências de toda a aplicação, activar e desactivar secções do ambiente de trabalho (GUI) e opções de ajuda.

{{-}} ![[_media/Menubar-MainMenuOverview-FamilyTree-Loaded-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Barra de menus - Árvore genealógica carregada]] ![[_media/Menubar-MainMenuOverview-FamilyTree-Loaded-Active-Go-Windows-menus-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Barra de menus - Árvore genealógica carregada com os menus &quot;Ir&quot;, &quot;Marcadores&quot; e &quot;Janelas&quot;em uso]] Depois de carregar uma árvore, os menus [Árvores genealógicas](#Family_Trees), [Relatórios](#Reports), [Ferramentas](#Tools) e [Ajuda](#Help) terão sempre opções consistentes. Mas a disponibilidade das opções dos outros menus é sensível ao contexto. As opções dos menus [Adicionar](#Add), [Editar](#Edit) e [Ver](#View) mudam consoante a categoria activa e alguns itens de menu aparecem "esbatidos" quando os objectos de selecção na vista não permitem a acção.

Os menus [Ir](#Go) e [Marcadores](#Bookmarks) são especificamente constituídos por ligações de navegação dentro de cada vista.

Verá um menu [Janelas](#Windows) aparece quando há janelas ou diálogos abertos a listar. {{-}} ![[_media/Menubar-FamilyTrees-overview-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Barra de menus - Árvores genealógicas]] <span id="Family Trees">

### 

</span>

- \- abre o diálogo [Gerir árvores genealógicas](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Family_Trees_manager_window)

- \- um atalho para abrir uma árvore genealógica recente (na barra de ferramentas: [Ligar a uma base de dados recente](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/pt_PT#.E2.96.BC_Connect_to_a_recent_database))

- \- salvaguardar e fechar aárvore actual

<hr>

- \- Trazer dados de outros [formatos](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Importing_data).  
  *Faça uma cópia de segurança antes de importar! Há [preferências de importação](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Import) para marcar dados importados com um carimbo de data/hora atributos de [etiquetas](wiki:Gramps_Glossary#tag) e/ou [fontes](wiki:Gramps_Glossary#source). Estas opções abrandam significativamente o processo de importação, mas são úteis para a limpeza de dados que se segue.*

- \- [Exportar dados](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Exporting_data) permite-lhe partilhar qualquer parte da sua árvore genealógica do Gramps com outros investigadores, bem como transferir os seus dados para outro computador.

<hr>

- \- opção que só aparece se os dados mostrados puderem ser exportados. O Gramps exportará os dados no ecrã de acordo com a sua escolha, folha de cálculo **CSV** ou **Open Document**.

<hr>

- \- Permite fazer uma [salvaguarda completa Gramps XML](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Backing_up_a_Family_Tree) da árvore actualmente aberta. Note que [alguns itens de configuração e multimédia são omitidos](wiki:Template:Backup_Omissions) de salvaguardas XML.

<hr>

- \- sai do Gramps sem gravar as alterações que estão pendentes.

- \- sai do Gramps, gravando todas as alterações.

{{-}}

![[_media/Menubar-Add-a-new-object-overview-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Barra de menus - Adicionar]] <span id="Add">

###  um novo [objecto](wiki:Gramps_Glossary#primary_object)

</span>

Veja também [Atalhos de teclado](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT).

<hr>

- \- adiciona um [indivíduo](wiki:Gramps_Glossary#person) *([objecto primário](wiki:Gramps_Glossary#primary_object))*

<hr>

- \- adiciona uma [família](wiki:Gramps_Glossary#family) *([objecto primário](wiki:Gramps_Glossary#primary_object))* - abre o diálogo

<hr>

- \- adiciona um [evento](wiki:Gramps_Glossary#event) *([objecto primário](wiki:Gramps_Glossary#primary_object))*

<hr>

- \- adiciona um [local](wiki:Gramps_Glossary#place) *([objecto primário](wiki:Gramps_Glossary#primary_object))*

- \- adiciona uma [fonte](wiki:Gramps_Glossary#source) *([objecto primário](wiki:Gramps_Glossary#primary_object))*

- \- adiciona uma [citação](wiki:Gramps_Glossary#citation) *([objecto primário](wiki:Gramps_Glossary#primary_object))*

- \- adiciona um [repositório](wiki:Gramps_Glossary#repository) *([objecto primário](wiki:Gramps_Glossary#primary_object))*

- \- adiciona [multimédia](wiki:Gramps_Glossary#media) *([objecto primário](wiki:Gramps_Glossary#primary_object))*

- \- adiciona uma [nota](wiki:Gramps_Glossary#note) *([objecto primário](wiki:Gramps_Glossary#primary_object))*

<hr>

{{-}} ![[_media/Menubar-Edit-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Barra de menus - Editar]] <span id="Edit">

### 

</span>

- / - As habituais acções de desfazer ou refazer uma acção anterior

- \- Abre o diaĺogo

<hr>

As opções de menu adicionais dependentes da categoria serão mostradas aqui.

- \- Veja [Etiquetar](wiki:Gramps_6.0_Wiki_Manual_-_Filters/pt_PT#Tagging)

<hr>

- \- A ferramenta Área de transferência fornece um bloco de notas temporário para armazenar registos da base de dados para uma fácil reutilização.

- \- Gestão de extensões de terceiros

<hr>

- \- Abre o diálogo , que permite alterar a maioria das definições no Gramps.

{{-}}

![[_media/Menubar-View-overview-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Barra de menus - Ver]] <span id="View">

### 

</span>

- \- Permite-lhe configurar a vista activa. Oferece opções para ocultar, mostrar e reorganizar elementos. O mesmo que clicar em ![[_media/Gramps-config.png]] na [barra de ferramentas](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Toolbar).

- \- O navegador é uma barra lateral para os ícones de categorias. Quando seleccionada (pré-definição), a barra lateral é mostrada à esquerda da categoria activa. Desmarcar a selecção oculta a barra lateral do navegador. Se os ícones de categoria não couberem no espaço vertical disponível, será criada uma barra de deslocação oculta à direita da barra lateral, que será revelada quando se passar o rato por cima dela.  
  As etiquetas de texto dos ícones podem ser ocultadas através de uma opção no separador [Geral](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Display) das preferências. Pode seleccionar [diferentes modos para o navegador](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Switching_Navigator_modes) na lista pendente ao fundo do navegador.

- \- mostrar (ou ocultar) uma barra de ícones de acções frequentemente utilizadas acima da área da categoria. Os ícones de accão variam de acordo com a categoria.  
  Pode instalar uma [extensão de terceiros](wiki:Third-party_Addons) para complementar as preferências com um separador [Tema](wiki:Addon:ThemePreferences), que oferece, entre outras, uma opção para mostrar rótulos de texto para cada botão da barra de ferramentas.

- \- Mostrar (ou ocultar) um espaço dividido para gramplets à direita da área da categoria.

- \- Mostrar (ou ocultar) um espaço dividido para gramplets na parte inferior da janela, mesmo acima da barra de estado.

- \- Expandir a janela para utilizar todo o espaço disponível no ecrã, desactivando os controlos de arrastamento e redimensionamento da janela. Desmarcar a selecção repõe o tamanho anterior e volta a activar os controlos de arrastamento e redimensionamento da janela.

<hr>

- Dependendo da vista que estiver activa, aparecerão aqui outras opções que podem modificar a forma como a vista organiza os dados (na imagem, controlos extra da categoria Indivíduos a amarelo).

{{-}}

![[_media/History-navigation-tools-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Barra de menus - Ir]] <span id="Go">

### 

</span>

- \- navega a selecção da vista actual para trás, para o item *anterior* no seu [histórico de navegação](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/pt_PT#Using_history-based_Navigation)

- \- navega a selecção da vista actual para diante, para o item *seguinte* no seu [histórico de navegação](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/pt_PT#Using_history-based_Navigation)

<hr>

- \- muda o foco do [indivíduo activo](wiki:Gramps_Glossary#active_person) para o indivíduo [definido](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Setting_Home_person) como [indivíduo inicial](wiki:Gramps_Glossary#home_person)

<hr>

- Lista dinâmica dos 10 registos mais recentes (pessoas, famílias, etc.) seleccionados; a lista depende da categoria que está a utilizar.

{{-}} ![[_media/Menubar-BookmarksOverview-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Barra de menus - Marcadores]] <span id="Bookmarks">

### 

</span>

- \- Cria um marcador a partir do item actualmente seleccionado, por exemplo, um indivíduo, uma família, etc..

- \- Abre a janela [Organizar marcadores](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/pt_PT#Bookmark_Navigation).

<hr>

- Secção dinâmica onde aparecem os marcadores.

{{-}}

<span id="Reports">

### 

</span>

![[_media/Menubar-ReportsOverview-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Barra de menus - Relatórios]]

- \- O relatório [Livros](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_3/pt_PT#Books) permite-lhe criar um livro de genealogia personalizado, que contém uma colecção de relatórios textuais e gráficos do Gramps num único documento (ou seja, um livro).

<hr>

- \-

  - 

  - 

  - 

- \-

  - 

  - 

  - 

  - 

  - 

  - 

  - 

- \-

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

  - 

- \-

  - 

  - 

{{-}}

<span id="Tools">

### 

</span>

![[_media/MenuOverview-Tools-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "" Barra de menus - Ferramentas]]

- \-

  - 

  - 

<!-- -->

- - 

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

- - 

  - 

  - 

  - 

{{-}} ![[_media/Menubar-Windows-overview-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Barra de menus - Janelas]] <span id="Windows">

### 

</span>

- \- Este menu permite um acesso rápido às janelas abertas em que está a trabalhar.

{{-}}

![[_media/Menubar-Help-overview-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Barra de menus - Ajuda]] <span id="Help">

### 

</span>

- \- Ligação directa ao manual de utilizador Gramps em rede que está a ver neste momento. Sim, é necessária uma ligação à Internet para consultar o manual do utilizador Gramps.

- \- Uma ligação às [perguntas frequentes](wiki:Gramps_6.0_Wiki_Manual_-_FAQ/pt_PT) sobre o Gramps.

- \- Uma ligação à [referência de atalhos](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT) do Gramps.

- \- Mostra um diálogo com uma sugestão aleatória sobre a utilização do Gramps.

- \- A partir deste menu, pode gerir as extensões internas, bem como quaisquer [extensões de terceiros](wiki:6.0_Addons) que possa ter instalado.

<hr>

- \- Este item abre o seu navegador web e liga-o ao sítio Web do projecto Gramps.

- \- Este item abre o navegador web na página da lista de discussão do Gramps. Nesta página pode navegar nos arquivos da lista de correio e juntar-se à lista de correio gramps-users para poder partilhar as suas experiências com outros utilizadores do Gramps.

- \- Escolha este item para comunicar um [relatório de erro](wiki:Using_the_bug_tracker) no sistema de rastreio de problemas do Gramps (requer que uma conta registada no sistema de relatório de erros do Gramps). Lembre-se, o Gramps é um projecto vivo. Queremos saber qualquer problema que encontrar para que possamos trabalhá-lo e resolvê-lo para benefício de todos.

- \- Uma ligação para [instalar extensões de terceiros no Gramps](wiki:6.0_Addons).

<hr>

- \- Este item exibe uma caixa de diálogo com informações gerais sobre a versão do Gramps que está a ser executada.

{{-}} <span id="Toolbar">

## Barra de ferramentas

</span> ![[_media/ToolbarIcon-OpenTheToolsDialog-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dica para o botão Ferramentas da categoria Painel]] A [barra de ferramentas](wiki:Gramps_Glossary#toolbar) é um conjunto horizontal de botões de controlo localizada logo abaixo da barra de menus. Dá acesso às funções mais usadas do Gramps.

- A variedade de botões da barra de ferramentas é "contextual" -- os ícones mostrados dependem de qual [categoria](wiki:Gramps_Glossary#view) e [modo](wiki:Gramps_Glossary#view_mode) estão activos
- As etiquetas de texto são mostradas por baixo dos botões da barra de ferramentas.
- Passar o rato sobre um botão da barra de ferramentas mostra uma dica da sua função.
- A barra de ferramentas pode ser ocultada ou mostrada através da opção .

{{-}} <span id="Common Toolbar buttons">

### Botões comuns da barra de ferramentas

</span> ![[_media/ManageDatabases-icon-toolbar-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Gerir bases de dados - ícone e dica na barra de ferramentas]] <span id="Manage databases">

#### ![[_media/Gramps.png]] Gerir bases de dados

</span>

`O botão `![[_media/16x16-gramps-pedigree.png|`16x16-gramps-pedigree.png`]]` é igual a ``.`

{{-}}

![Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Botão "Ligar a uma base de dados recente"](ConnectToARecentDatabase-icon-toolbar-60-pt_PT.png "Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Botão "Ligar a uma base de dados recente"") <span id="Connect to a recent database">

#### <big>▼ </big>Ligar a uma base de dados recente

</span>

`Este botão `<big>`▼ `</big>`abre a lista pendente `` na barra de ferramentas.`

{{-}}

<span id="Go to the previous object in the history">

#### ![[_media/Gramps_Go-Previous48x48_win.png]] Ir para o objecto anterior no histórico

O botão ![[_media/Gramps_Go-Previous48x48_win.png]] é uma alternativa à opção de menu , ou premir o [atalho de teclado](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT#Common_keybindings) . Usa a [navegação baseada no histórico](#Using_history-based_Navigation) para mudar o foco do objecto activo para o objecto previamente seleccionado nesta categoria. <span id="Go to the next object in the history">

#### ![[_media/Go-next48x48_win.png]] Ir para o objecto seguinte no histórico

</span> O botão ![[_media/Go-next48x48_win.png]] é uma alternativa à opção de menu , ou premir o [atalho de teclado](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT#Common_keybindings) . Usa a [navegação baseada no histórico](#Using_history-based_Navigation) para restaurar o objecto activo alterado com .

Este botão só está disponível depois de utilizar a função . <span id="Go to the home person">

#### ![[_media/Gramps_Go-Home48x48_win.png]] Ir para o indivíduo inicial

</span> O botão ![[_media/Gramps_Go-Home48x48_win.png]] é uma alternativa à opção de menu , ou premir o [atalho de teclado](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT#Common_keybindings) . Muda o foco do [indivíduo activo](wiki:Gramps_Glossary#active_person) para o [indivíduo inicial](wiki:Gramps_Glossary#home_person).

Este botão só funciona se o indivíduo inicial tiver sido definido. <span id="Add a new...">

#### ![[_media/Gramps_Add48x48_win.png]] Adicionar novo...

</span> O botão é uma alternativa à opção de menu , ou premir o [atalho de teclado](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT#Common_keybindings) . Abre um editor de objectos em branco que corresponde à categoria de objectos actual.

<span id="Edit the selected...">

####  Editar ... seleccionado

</span> O botão é uma alternativa à opção de menu , ou premir o [atalho de teclado](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT#Common_keybindings) . Abre um editor de objectos para cada objecto seleccionado na categoria.

<span id="Delete the selected...">

#### ![[_media/Gramps_Remove48x48_win.png]] Eliminar ... seleccionado

</span> O botão é uma alternativa à opção de menu , ou premir o [atalho de teclado](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT#Common_keybindings) . Abre um diálogo de confirmação da eliminação.

O item que está prestes a ser eliminado está identificado. Se seleccionou vários itens, aparece um diálogo para cada um. Dispõe da opção .

<span id="Merge the selected...">

#### ![[_media/Gramps_Merge48x48_win.png]] Unir ... seleccionados

</span> O botão é uma alternativa à opção de menu Abre o diálogo [Unir](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data%3A_detailed_-_part_3/pt_PT#Merging_records) para essa categoria de objectos em particular.

A utilização bem sucedida do botão Unir só é possível se dois e **apenas** 2 registos estiverem seleccionados na categoria.

<span id="Tag the selected rows">

#### ![[_media/gramps-tag.png]] Marcar as linhas seleccionadas

</span> Este botão é uma alternativa à opção de sub-menu .

O botão ![[_media/16x16-gramps-tag.png]] abre um sub-menu [Etiqueta](wiki:Gramps_Glossary#tag) com as seguintes opções:

- [Nova etiqueta...](wiki:Gramps_6.0_Wiki_Manual_-_Filters/pt_PT#New_Tag_dialog)
- [Organizar etiquetas...](wiki:Gramps_6.0_Wiki_Manual_-_Filters/pt_PT#Organize_Tags_Window)

Seguida de uma lista de etiquetas actualmente disponíveis que podem ser aplicadas aos objectos seleccionados na categoria.

As [etiquetas são usadas para](wiki:Gramps_6.0_Wiki_Manual_-_Filters/pt_PT#Usage_of_tags) linhas de codificação de cores em vistas de lista, amostras de marcadores nalguns gráficos e marcadores persistentes para filtragem e organização.

<span id="Open the Clipboard dialog">

#### ![[_media/Gramps_Clipboard48x48_win.png]] Abrir o diálogo Área de transferência

</span> ![[_media/Clipboard-dialog-example-context-menu-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo Área de transferência - menu contextual]] Este botão é uma alternativa à opção de menu , ou premir o [atalho de teclado](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT#Common_keybindings) . Abre o diálogo [Área de transferência](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/pt_PT#Using_the_Clipboard) sem adicionar o objecto seleccionado à sua colecção. {{-}} <span id="Configure the active view">

#### ![[_media/Gramps-config.png]] Configurar a vista activa

</span> Este botão é uma alternativa à opção de menu , ou premir o [atalho de teclado](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT#Common_keybindings) .

A maioria das categorias tem um botão ⚙ Opções configuráveis. Clicar neste botão abre o diálogo com os controlos para ajustar essas opções. Esta opção abre um diálogo com escolhas para a apresentação de registos na categoria. O diálogo também terá separadores para qualquer [gramplets com opções configuráveis](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/pt_PT#.E2.9A.99_Configurable_Options_2) que esteja activo na vista actual. ![[_media/ReportSelection-dialog-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo Selecção de relatório]] <span id="Open the reports dialog">

#### ![[_media/Gramps-reports.png]] Abrir o diálogo Relatórios

</span> Esta é uma forma persistente de usar os sub-menus . Ao apresentar os relatórios disponíveis num diálogo flutuante, fica disponível espaço para descrever cada relatório, o seu estado e informações do programador. O diálogo também permite que a exploração dos relatórios seja mais estruturada. {{-}}

![[_media/ToolSelection-dialog-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo Selecção de ferramenta]] <span id="Open the tools dialog">

#### ![[_media/Gramps-tools.png]] Abrir o diálogo de ferramentas

</span>

Esta é uma alternativa persistente à utilização dos sub-menus .

Ao apresentar as ferramentas disponíveis num diálogo flutuante, há espaço para descrever cada ferramenta, o seu estado e informações do programador. O diálogo também permite que a exploração das ferramentas seja mais estruturada.

{{-}}

<span id="Open Addon Manager">

#### Abrir o gestor de extensões

</span>

Abre o diálogo {{-}}

<span id="Open Preferences">

#### Abrir as preferências

</span>

Abre o diálogo

{{-}}

[Category:Pt PT:Documentation](wiki:Category:Pt_PT:Documentation)
