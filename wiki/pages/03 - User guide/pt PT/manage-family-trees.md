---
title: Gramps 6.0 Wiki Manual - Manage Family Trees/pt PT
categories:
- Pt PT:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 113356
wiki_fetched_at: '2026-05-30T19:49:10Z'
lang: pt PT
---

{{#vardefine:chapter\|5}} {{#vardefine:figure\|0}} Uma exploração detalhada da manutenção e movimentação de dados (em operações de lote) em bases de dados de árvores genealógicas.

Neste capítulo, estudamos a mecânica de gestão das suas árvores genealógicas (bases de dados), bem como as opções de partilha dos seus dados com outros genealogistas. Isto inclui criar árvores em branco, converter formatos antigos de bases de dados, criar salvaguardas, renomear árvores, eliminar árvores e importar e exportar árvores completas ou parciais.

<span id="Starting a new Family Tree">

## Começar uma árvore genealógica

</span> ![[_media/Menubar-FamilyTrees-overview-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - &quot;Árvores genealógicas&quot; - menu principal]] Para começar uma árvore genealógica, escolha ou clique em , ou use o [atalho](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT) . Qualquer uma das opções abre a janela do .

Clique em para adicionar uma nova árvore à lista de árvores genealógicas. Para alterar um nome, seja o pré-definido *`Árvore genealógica 1`* ou outro atribuído ao criar a árvore, clique em e escreva o nome desejado.

Para abrir uma nova árvore vazia, seleccione-a e faça duplo clique sobre ela ou clique em . {{-}} <span id="Manage databases">

### Gerir bases de dados

</span> ![[_media/ManageDatabases-icon-toolbar-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Gerir bases de dados - ícone na barra de ferramentas (igual a menu ).]] {{-}}

<span id="Family Trees (manager) window">

### Janela do gestor de árvores genealógicas

</span> Árvores genealógicas é aquilo que o Gramps cchama à estrutura de base de dados usada para armazenar e organizar dados genealógicos. Tem de criar uma árvore genealógica antes de inserir quaisquer dados, [restaurados de uma salvaguarda](wiki:How_to_restore_a_backup), [importados de outro programa](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Importing_data), ou mesmo manualmente.

As árvores podem ser renomeadas, convertidas para outros motores de base de dados, repairadas ou eliminadas. Um "erro" aqui não será irrecuperável. O maior erro potencial, uma eliminação acidental, requer sempre uma confirmação.

![[_media/FamilyTreesManager-window-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Janela do gestor de árvores genealógicas]]

Clicar em abre o , que permite gerir as árvores encontradas na [caminho das bases de dados](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Family_Tree) do Gramps.

O gestor de árvores genealógicas permite-lhe criar uma árvore genealógica, mudar o nome de uma árvore genealógica existente, eliminar uma árvore genealógica, carregar uma árvore genealógica, ou obter informações sobre a árvore genealógica seleccionada. Todos os nomes das suas árvores genealógicas aparecem na lista. Se uma árvore genealógica estiver aberta, aparece um ícone ao lado do nome na coluna de estado. É mostrado o tipo de base de dados, bem como uma indicação da data e hora em que a árvore foi acedida pela última vez.

- cria uma árvore genealógica.

- mostra seleccionada.

- a árvore seleccionada, com um pedido de confirmação final.

- a árvore seleccionada, escrevendo o novo nome.

- a árvore seleccionada.

- a árvore selecionada. Veja [Converter uma árvore antiga BSDDB](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Converting_a_BSDDB_Family_Tree_to_SQLite) para [SQlite](wiki:Gramps_Glossary#sqlite) ( [BSDDB](wiki:Gramps_Glossary#bsddb) )

- a árvore seleccionada, só disponível se o Gramps detectar um problema.

- uma árvore. Esta opção só está disponível se o programa [GNU Revision Control System](http://www.gnu.org/software/rcs/) (RCS) estiver instalado.

- uma árvore, usado em conjunto com e a opção só está disponível se o programa [GNU Revision Control System](http://www.gnu.org/software/rcs/) (RCS) estiver instalado.

- \- abre a janela do navegador do sistema nesta secção do manual em rede.

- \- fecha o .

- abre a árvore seleccionada para trabalho, e bloqueia a base de dados para que ninguém a edite entretanto, podendo causar conflitos de edição.

{{-}}

<span id="Database information dialog">

#### Janela de informação da base de dados

</span> ![[_media/Database-information-dialog-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Janela de informação da base de dados, mostrada ao clicar em  com uma árvore que não esteja carregada seleccionada.]]

Mostrada ao clicar em com uma árvore que não esteja carregada seleccionada.

Similar ao relatório e ao .

{{-}}

<span id="Opening a Family Tree">

## Abrir uma árvore genealógica

</span>

Para abrir uma árvore, escolha no menu ou clique em . Verá o com uma lista de todas as árvores conhecidas pelo Gramps. Na coluna de , um ícone (que parece uma pasta aberta) aparecerá ao lado da árvore actualmente aberta. Seleccione a árvore desejada e clique em . Em alternativa, pode fazer duplo clique na árvore desejada. <span id="Load Family Tree button">

### Botão Carregar árvore genealógica

</span> No seleccione a árvore em que deseja trabalhar e clique em . {{-}}

<span id="Connect to a recent database">

### Ligar a uma base de dados recente

</span> ![[_media/ConnectToARecentDatabase-icon-toolbar-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Ligar a uma base de dados recente - lista pendente na barra de ferramentas, igual a]]

Para abrir uma árvore recentemente utilizada, escolha o menu ou clique na lista pendente , junto ao botão e seleccione a árvore na lista. {{-}} <span id="Could not load a recent Family Tree. warning">

#### Aviso Impossível carregar a árvore recente

</span>

![[_media/Could-not-load-a-recent-Family-Tree-warning-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Aviso Impossível carregar a árvore recente]]

Se a árvore na lista de recentes não estiver disponível, verá este aviso.

{{-}}

<span id="Read Only Mode">

### Modo só de leitura

</span>

<span id="Saving changes to your Family Tree">

## Gravar alterações à árvore

</span>

O Gramps grava as suas alterações assim que as aplica. Isto significa, por exemplo, que sempre que clicar em ao usar o Gramps, as suas alterações são imediatamente gravadas. Não existe um comando "gravar" separado.

Pode desfazer as alterações seleccionando . Se seleccionar este comando repetidamente, as alterações mais recentes serão anuladas, uma de cada vez. Para reverter vários comandos de uma só vez, pode utilizar o diálogo .

Se quiser voltar a pôr a árvore como estava quando a abriu, seleccione (é como sair sem gravar noutros programas). Há um limite para o número de alterações que podem ser ignoradas com este comando. Caso o exceda, receberá um aviso e não poderá sair do programa sem as gravar.

Se pretender gravar uma cópia da sua árvore genealógica com um nome diferente, terá de a exportar e depois importá-la para uma nova árvore genealógica. O formato de base de dados *Gramps XML* é recomendado para este efeito.

<span id="Opening a GEDCOM or XML database">

## Abrir um ficheiro Gedcom ou uma base de dados XML

</span>

O Gramps permite abrir certas bases de dados que não foram gravadas no formato de arquivo do próprio Gramps a partir da linha de comando, veja [Referências da linha de comandos](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/pt_PT#Opening_options). Estas incluem bases de dados XML e GEDCOM. Mas deve estar ciente de que se a base de dados XML ou GEDCOM for relativamente grande, vai encontrar problemas de desempenho e, no caso de uma falha, os seus dados podem ficar corrompidos. Por isso, normalmente é melhor criar uma nova árvore genealógica do Gramps (base de dados) e importar para aí os seus dados XML/GEDCOM.

<span id="Deleting a Family Tree">

## Eliminar uma árvore genealógica

</span>

A remoção de uma árvore genealógica elimina "completamente" a árvore genealógica, sem possibilidade de recuperar os dados. Considere fazer uma salvaguarda dos seus dados exportando-os para o [formato Gramps XML](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Gramps_XML_and_XML_Package_import), e armazenando esse ficheiro.

<span id="Remove the <XXXXXXXX> Family Tree? dialog">

### Diálogo Remover a árvore <XXXXXXXX>?

</span>

![[_media/Remove-the-family_tree_name-Family-Tree-dialog-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo Remover a árvore <XXXXXXXX>?]]

Seleccione a árvore genealógica que pretende remover e clique em no gestor de árvores, e depois, no diálogo Remover a árvore <XXXXXXXX>? seleccione ou .

{{-}}

<span id="Renaming a Family Tree">

## Renomear uma árvore de família

</span>

Pode mudar o nome de uma árvore (ou de um ficheiro da mesma) seleccionando a árvore que pretende renomear e clicando em . Também pode clicar no nome na lista de árvores.

Em qualquer um dos casos, basta escrever o novo nome para que ele entre em vigor.

<span id="Backing up a Family Tree">

## Fazer uma salvaguarda da sua árvore

</span>

A forma mais segura de fazer uma salvaguarda da sua árvore Gramps é exportar sem opções de privacidade e filtros para o formato **Gramps XML** (ou **Gramps XML Package** para incluir itens da sua galeria) e copiar o ficheiro resultante para um local seguro, de preferência num suporte diferente.

<span id="Backup dialog">

### Diálogo de salvaguardas

</span>

![[_media/MakeBackup-GrampsXML-Backup-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fazer uma salvaguarda]]

No menu, seleccione

Verá a janela .

Pode inserir manualmente o onde deseja armazenar a salvaguarda, ou usar o botão para abrir o diálogo .

Pode inserir manualmente um nome de ou usar o nome gerado automaticamente.

Pode escolher *Incluir* ou **Excluir**(pré-definição) a .

{{-}}

- Pode utilizar a funcionalidade Arquivar (ver secção seguinte) para gravar instantâneos da sua árvore. Estes instantâneos podem ser utilizados como salvaguardas simples, muito úteis se quiser experimentar algo que mais tarde poderá querer desfazer. No entanto, este método não deve ser utilizado para salvaguardas padrão, uma vez que não sobreviverá a uma falha do disco rígido ou à maioria dos outros desastres que podem ocorrer num computador.

<!-- -->

- *Para utilizadores avançados:* cada base de dados é gravada na sua própria sub-pasta em ~/.gramps. Embora se possa fazer uma salvaguarda normal a partir duma segurança desta pasta, não é recomendado. Recomenda-se vivamente que, em vez disso, utilize uma salvaguarda Gramps XML.

<span id="Backup on exit">

### Salvaguarda ao sair

</span> Nas preferências, separador , o Gramps pode ser definido para criar uma salvaguarda quando o Gramps fechar. Note que isto só cria uma salvaguarda para a árvore genealógica aberta. Se a árvore for fechada antes de sair do Gramps, nenhuma salvaguarda será criada.

- [Preferências Árvore genealógica](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Family_Tree)

<span id="Automatic backup">

### Salvaguarda automática

</span> No separador das preferências, pode definir um intervalo para , para verificar se houve alterações à árvore durante a sessão em curso e, se for o caso, fazer uma salvaguarda. A contagem começa desde que o Gramps é iniciado ou desde que a selecção do intervalo é alterada. Este accionamento é diferido se o computador tiver sido suspenso e atrasado durante o despertar.

Os intervalos de salvaguarda automática podem ser definidos para "Cada 15 minutos", "Cada 30 minutos", "Cada hora", "Cada 12 horas" e "Cada dia".

Cada salvaguarda (sem multimédia) é gravada na pasta especificada em . O nome do ficheiro tem um padrão:

- <small>*<Nome da árvore>*</small>`-aaaa-mm-dd-hh-mm-ss.gramps`

#### Veja também

- [Settings Family Tree](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Family_Tree)
- [Advanced backup filename setting](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Advanced_backup_filename_setting) - Where you can also define the naming pattern for the backup filename.
- [Omissões na salvaguarda](wiki:Template:Backup_Omissions/pt_PT) - o que não é incluído numa salvaguarda

<span id="Archiving a Family Tree">

## Arquivar uma árvore genealógica

</span>

![[_media/ManageFamilyTrees-Archive-RevisionComment-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Arquivar uma árvore genealógica]]

Pode as suas árvores genealógicas com o Gramps para manter uma cópia antes de qualquer alteração importante e poder voltar a uma versão conhecida.

Para tal:

1.  carregue a sua árvore genealógica;
2.  clique em { (aparece quando passa o rato sobre ele);
3.  clique na árvore genealógica que acabou de carregar: deve aparecer o botão ;
4.  clique em e poderá inserir no diálogo uma *Descrição da versão* para o seu arquivo.

Após o arquivamento, a lista de árvores genealógicas passa a mostrar a sua árvore genealógica original com um triângulo apontando para a direita à sua esquerda.

- Clique no triângulo para ver o nome do arquivo (clique novamente para recolher a lista de arquivos).

Os arquivos podem ser , e .

<span id="Archiving Prerequisite">

### Pré-requisito de arquivamento

</span> Requer que o programa [GNU Revision Control System](http://www.gnu.org/software/rcs/) (RCS) esteja instalado e disponível para o Gramps.

{{-}}

<span id="Extracting a Family Tree Archive">

## Extrair um arquivo de árvore genealógica

</span>

![[_media/ManageFamilyTrees-Archive-Selected-to-Extract-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gestor de árvores - Arquivo seleccionado e pronto a extrairt]]

Para recuperar uma versão de uma árvore genealógica anteriormente arquivada, no gestor de árvores, seleccione o arquivo que pretende restaurar e clique em .

{{-}} ![[_media/ManageFamilyTrees-Archive-Extracted-version-highlighted-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gestor de árvores - Arquivo extraído e seleccionado]]

O arquivo será então restaurado numa nova árvore e será listado no gestor de árvores. O nome da árvore baseia-se no nome original e no nome do arquivo, por exemplo: *<nome da árvore original>`:`<nome do arquivo>* (veja também [Arquivar uma árvore genealógica](#Archiving_a_Family_Tree))

Esta pode ser uma forma útil de preservar um arquivo, porque os arquivos desaparecem se a árvore de origem for apagada; e *'eles não são incorporados numa exportação Gramps XML da árvore genealógica*. {{-}}

<span id="Unlocking a Family Tree">

## Desbloquear uma árvore genealógica

</span> ![[_media/FamilyTreesManager-Dialog-ShowingLocked-Sample-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gestor de árvores - Árvore genealógica bloqueada realçada]] O Gramps é uma aplicação de base de dados de utilizador único e identifica os ficheiros de base de dados da árvore como ocupados com um "cadeado" ![[_media/22x22-gramps-lock.png]] quando em uso. Quando o Gramps abre uma árvore, coloca um ficheiro de `bloqueio` (que lista o nome de utilizador e o domínio) na sub-pasta da árvore na pasta `grampsdb` do [Pasta do utilizador](wiki:Gramps_6.0_Wiki_Manual_-_User_Directory/pt_PT). O Gramps recusa o acesso a essa árvore em simultâneo. Uma segunda instância do Gramps será capaz de abrir outra árvore genealógica, mas qualquer árvore que já esteja aberta aparecerá com o ícone de cadeado na coluna de estado do gestor de árvores. Fechar a árvore na primeira cópia do Gramps elimina o ficheiro de bloqueio e tornará a árvore disponível para ser aberta na segunda instância.

Se *pudesse* abrir a mesma árvore em duas instâncias do Gramps ao mesmo tempo, é provável que os seus dados fossem danificados, uma vez que os dois substituem o trabalho um do outro.

\<span id="Break the lock on the "Family Tree name" database? dialog"\>

### Diálogo Quebrar o bloqueio da base de dados <XXXXXXXXX>?

![[_media/ErrorParsingArguments-dialog-DatabaseIsLocked-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Erro ao analisar os argumentos - Base de dados bloqueada]] No caso improvável de o Gramps falhar, a árvore genealógica será deixada num estado bloqueado (indicado por um ícone de bloqueio ![[_media/22x22-gramps-lock.png]] na coluna junto ao nome da árvore genealógica).

Para desbloquear a árvore genealógica durante o arranque:

- se as [Preferências -&gt; Árvore genealógica](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Family_Tree) foram definidas para abri uma árvore automaticamente ao iniciar, verá o diálogo **Erro ao analisar os argumentos**, que frisa que a **base de dados está bloqueada**. Clique em e escolha no menu .
- senão, o aparece automaticamente no início do Gramps.

{{-}} ![[_media/Break-the-lock-on-the-database-Dialog-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo Quebrar o bloqueio da base de dados ?]] Escolha a árvore bloqueada e clique em . Verá o diálogo **Quebrar o bloqueio da base de dados <XXXXXXXXX>?**.

Clique em e o já não deverá ter o ícone de bloqueio.

Escolha de novo a árvore, antes bloqueada, e clique em para continuar o seu trabalho. {{-}}

<span id="The database is locked dialog">

### Diálogo A base de dados está bloqueada

</span> ![[_media/TheDatabaseIsLocked-dialog-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo A base de dados está bloqueada - Use a opção --force unlock]]

Se receber o aviso , use a opção de linha de comandos [--force unlock](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Command_Line:Force_unlock_option). Certifique-se de que a base de dados não está em uso.

<span id="Command Line:Force unlock option">

#### Linha de comandos: opção --force unlock

</span>

- [Linha de comandos: opção --force unlock option](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#Force_unlock_option) - Em alternativa, pode tentar recuperar de uma falha que deixa a árvore genealógica (base de dados) bloqueada, a partir da linha de comandos.

{{-}}

<span id="Repairing a damaged Family Tree">

## Reparar uma árvore genealógica danificada

</span>

![[_media/FamilyTreesManager-Dialog-ShowingRedErrorStatusIcon-Sample-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gestor de árvores - Ícone de erro mostrado a vermelho]]

Se a sua árvore ficar danificada ou corrompida de alguma forma, o gestor de árvores do Gramps exibirá um ícone de erro, vermelho, na coluna . Para que o Gramps tente reparar o dano, seleccione a árvore e clique em . O Gramps tentará reconstruir sua árvore a partir de salvaguardas criadas automaticamente ao sair.

Veja também:

- [Recover corrupted family tree](wiki:Recover_corrupted_family_tree)

{{-}}

<span id="Converting a BSDDB Family Tree to SQLite">

## Converter um ficheiro BSDDB para SQLite

</span>

![[_media/ManageFamilyTrees-Convert-the-database-dialog-example-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo <strong>Converter a base de dados <XXXXXXXXX>?</strong>]]

Se tiver uma **base de dados** antiga em formato [BSDDB](wiki:Gramps_Glossary#bsddb) mostrada no gestor de árvores, seleccioná-la activará o botão .

Quando tudo estiver pronto, clique em e verá o diálogo com a mensagem **Deseja converter esta árvore genealógica numa base de dados SQLite??**. Pode seleccionar para parar ou para iniciar o processo. Uma vez concluído, o gestor de árvores mostrará uma nova entrada para a cópia convertida da sua árvore genealógica, mas com o *tipo de base de dados SQLite*.

Pode então renomear a árvore genealógica original da BSDDB com a palavra **OLD** (ou outro nome qualquer), ou pode apagá-la para evitar confusões, e depois renomear a nova base de dados SQLite.

{{-}}

<span id="Importing data">

## Importar dados

</span>

A importação permite-lhe transferir dados de outros programas de genealogia para uma árvore do Gramps. O Gramps inclui um conjunto básico de métodos de importação seleccionados automaticamente com base na extensão do ficheiro. E o [tipo de extensão de terceiros](wiki:Third-party_Addons) "Importar" pode ser instalado e a automatização reconhecerá as novas extensões de ficheiro.

A automatização pode ser substituída (o que é útil quando os formatos são actualizados e tornam as extensões principais obsoletas). Utilize o menu no diálogo para seleccionar entre os seguintes formatos:

- Detectada automaticamente *(pré-definição)*;
- [Folha de cálculo Comma Separated Values (CSV)](#Gramps_CSV_import) (extensão de ficheiro `.csv`);
- [GEDCOM](#GEDCOM_import) (versão 5.5.1, extensão de ficheiro `.ged`) formato de ficheiro padrão para troca de dados entre programas de genealogia;
- GeneWeb (extensão de ficheiro `.gw`) - o [GeneWeb](https://en.wikipedia.org/wiki/GeneWeb) é um programa de genealogia com ambiente em rede;
- [Gramps Package (XML portátil)](#Gramps_XML_and_XML_Package_import) (extensão de ficheiro `.gpkg`) [.tar.gz](https://wikipedia.org/wiki/.tar.gz), um formato de salvaguarda de arquivo comprimido; suporta a inclusão de multimédia;
- [Árvore genealógica Gramps XML](#Gramps_XML_and_XML_Package_import) (extensão de ficheiro `.gramps`) formato de troca nativo do Gramps em texto descomprimido e comprimido em [gzip](https://wikipedia.org/wiki/Gzip);
- [Base de dados Gramps 2.x](#GRAMPS_V2.x_database_import) (extensão de ficheiro `.grdb`);
- [Pro-Gen](wiki:Import_from_another_genealogy_program#Pro-Gen) (extensão de ficheiro `.def`) - o [Pro-Gen](https://www.pro-gen.nl/gbhome.htm) é muito popular na Holanda e na Alemanha do Noroeste. É muito usado por pessoas que começaram a recolher dados em 1989. Era um programa baseado em DOS que foi reparado para funcionar em Windows 10;
- vCard (extensão de ficheiro `.vcf`) - [Virtual Contact File](https://wikipedia.org/wiki/VCard) é um formato padrão de ficheiro para cartões de visita electrónicos;

----

- [JSON Import](wiki:Addon:JSON_Export_Import) (extensão de ficheiro `.json`) - [JavaScript Object Notation](https://www.json.org/) é um formato leve de troca de dados; ***extensão***;
- SQLite Import (extensão de ficheiro `.sql`) - [Base de dados SQLite](https://www.sqlite.org/fileformat.html); ***[extensão](wiki:Addon:SQLite_Export_Import)***.

<span id="Import Family Tree dialog">

### Diálogo Importar árvore genealógica

</span>

![[_media/Importfamilytree-dialog-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo Importar árvore genealógica]]

Primeiro crie uma [árvore vazia](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Starting_a_new_Family_Tree). Em seguida, escolha ou use o [atalho](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT#2) para importar dados ou restaurar uma árvore do Gramps previamente salvaguardada (por uma versão anterior do Gramps ou pela versão actual). Verá o diálogo ****, pedindo-lhe que especifique o ficheiro a importar.

![[_media/UndoHistoryWarning-Import-dialog-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Aviso de importação]]Ao tentar importar para uma árvore genealógica ***não vazia***, verá o diálogo de . Isto lembra-o de que deve fazer uma salvaguarda antes de importar. Em vez disso, crie uma árvore, a não ser que esteja a tentar unir dados conscientemente.

O Gramps usa um [selector de ficheiros GTK](https://developer.gnome.org/gtk3/stable/GtkFileChooser.html) para seleccionar o ficheiro a importar. As opções básicas para navegar para um ficheiro são familiares e óbvias.

A opção de exibição padrão para o caminho do ficheiro é mostrar cada nível de pasta como [navegação por migalhas clicáveis](https://en.wikipedia.org/wiki/Breadcrumb_navigation). O caminho pode ser inserido numa caixa de texto editável, premindo .

A extensão do tipo de ficheiro permitirá normalmente que a opção espere que um determinado padrão de dados seja convertido para o formato nativo da base de dados. Pode anular esta opção escolhendo opções diferentes para a lista ****. A lista de ficheiros pode ser filtrada alterando a escolha .

Quando planear utilizar a importação repetidamente (para actualizações contínuas ou incluindo investigação genealógica), pode [personalizar o diálogo](https://gramps.discourse.group/t/need-help-doing-a-cross-os-linux-mac-verification/1068/5) adicionando botões para caminhos de pastas com marcadores. Clique com o botão direito do rato no nome de uma pasta e seleccione no menu emergente.

<span id="GRAMPS V2.x database import">

### Importação de base de dados GRAMPS V2.x

</span>

GRAMPS V2.x database (.grdb): antes da versão 3.0 do Gramps, este formato de base de dados nativo do Gramps era uma forma específica da base de dados Berkeley (BSDDB) com uma estrutura especial de tabelas de dados. Este formato era binário e dependente de arquitectura. Era muito rápido e eficiente, mas não era geralmente portátil em computadores com diferentes arquitecturas binárias (por exemplo, i386 vs. alpha).

A importação do formato de base de dados GRAMPS V2.x só é suportada pelo Gramps versão 3.0.x. A importação do V2.x para o Gramps V3.0.x não perderá nenhuns dados.

\<span is="Moving a Gramps 2.2 databases to Gramps 3.x!\>

#### Mover uma base de dados Gramps 2.2 para o Gramps 3.x

</span>

Para mover os seus dados do Gramps 2.x para a versão 6.0.x, deve importar a base de dados v2.x para o Gramps v3.0.x anterior, gravar a base de dados e importá-la depois para o Gramps 6.0.x, ou exportar a base de dados em formato [XML](wiki:XML) da versão anterior do Gramps e importá-la para o Gramps 6.0.x.

Por favor, consulte o [manual do utilizador](wiki:Previous_releases_of_Gramps) para versões anteriores do Gramps para obter instruções sobre a importação de bases de dados v2.x para o Gramps v3.x. {{-}}

<span id="Gramps XML and XML Package import">

### Importação de Gramps XML e XML Package

</span>

As bases de dados Gramps [XML](wiki:XML) e Gramps [XML](wiki:XML) Package são os formatos nativos do Gramps. Não há risco de perda de informação ao importar (restaurar) ou exportar para estes formatos.

- Gramps [XML](wiki:XML) (.gramps): o ficheiro [XML](wiki:XML) do Gramps é o formato padrão de troca de dados e salvaguardas do Gramps, e era também o formato padrão da base de dados de trabalho para versões mais antigas (pré 2.x) do Gramps. Ao contrário do formato .grdb do GRAMPS V2.x, é independente da arquitectura do computador e legível por humanos. A base de dados pode também ter referências a objectos multimédia não locais (externos), pelo que não é garantido que seja completamente portável (para uma portabilidade total, deve usar o Gramps [XML Package](wiki:XML_Package) (.gpkg) para incluir objectos multimédia). A base de dados [XML](wiki:XML) do Gramps é criada através de ) para esse formato.

<!-- -->

- Gramps [XML](wiki:XML) Package (.gpkg): o Gramps [XML](wiki:XML) Package é um formato de arquivo **comprimido** contendo o ficheiro Gramps [XML](wiki:XML) e todos os objectos [multimédia](wiki:Gramps_Glossary#media) (imagens, som, etc.) que a base de dados referencia. Uma vez que contém todos os objectos multimédia, este formato é completamente portátil. O formato Gramps [XML](wiki:XML) Package é criado através de ) para esse formato.

Se importar informação de outra base de dados do Gramps ou da base de dados [XML](wiki:XML) do Gramps, verá o progresso da operação na barra de progresso da janela principal do Gramps. Quando a importação termina, uma janela de resumo mostra o número de objectos importados. Se os dados importados tiverem origem na mesma árvore genealógica em que importou os dados, o resumo da importação dá sugestões sobre o que pode ser unido; a união não é feita automaticamente por si. Se pretender unir dados básicos de genealogia automaticamente, considere a exportação/importação de folhas de cálculo CSV.

\<span id"Gramps CSV import"\>

### Importação Gramps CSV

</span>

O formato Folha de cálculo Gramps CSV permite a importação e exportação de um subconjunto dos seus dados Gramps num formato simples de folha de cálculo. Veja [Importação e exportação CSV](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#:_CSV_Import_and_Export) para mais informações.

<span id="GEDCOM import">

### Importação Gedcom

</span>

Primeiro crie uma [árvore genealógica vazia](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Starting_a_new_Family_Tree). Em seguida, seleccione ou use o [atalho](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT#2) e depois use o diálogo para seleccionar o ficheiro Gedcom a importar. Dependendo do tipo de Gedcom, poderá ver o diálogo .

Quando importa informações do Gedcom, a janela principal do Gramps mostrará uma [barra de progresso](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Status_Bar_and_Progress_Bar). Quando a importação GEDCOM termina, a janela e o **** mostram os resultados e/ou avisos.

- Na secção [Importar](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Import) das preferências do Gramps pode optar por e também . Ambas podem abrandar significativamente a importação dos dados.

{{-}} <span id="GEDCOM Encoding dialog">

#### Diálogo Codificação do Gedcom

</span>

![[_media/GEDCOM-Encoding-dialog-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo Codificação do Gedcom]]

O diálogo será mostrado quando o ficheiro Gedcom que está a importar se identificar como estando a usar o formato de codificação ANSEL. Por vezes, isto é um erro. Se, após a importação do GEDCOM, notar que os seus dados contêm caracteres invulgares, desfaça a importação e substitua o conjunto de caracteres, seleccionando uma codificação diferente na lista disponível.

- **pré-definição**
- ANSEL (American National Standard Extended Latin)
- ANSI (American National Standards Institute; similar a ISO-8859-1)
- ASCII (American Standard Code for Information Interchange)
- UTF8 (Unicode Transformation Format 8-bit)

{{-}}

\<span id="Import Statistics dialog\>

#### Diálogo Estatísticas da importação

</span>

![[_media/ImportStatistics-dialog-example-GrampXML-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo Estatísticas da importação]] Mostra detalhes das estatísticas de importação, dependendo do tipo de ficheiro importado.

- Gramps XML - Mostra as estatísticas de importação e a mensagem:
  - 
- GEDCOM - sem estatísticas de importação (só relata se for bem sucedido)

{{-}}

<span id="GEDCOM import report dialog">

#### Diálogo Relatório de importação Gedcom

</span>

![[_media/GEDCOM-import-report-result-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo Relatório de importação Gedcom]]

O **** detalha a maioria das linhas do Gedcom que foram ignoradas ou não puderam ser compreendidas. Estas provavelmente não fazem parte do padrão GEDCOM 5.6.0. (veja [Addon:GEDCOM_Extensions](wiki:Addon:GEDCOM_Extensions)). O conteúdo da linha Gedcom (ou linhas onde há linhas de continuação) também é mostrado. Nalguns casos, as linhas podem não ser exactamente o que está contido no ficheiro Gedcom de entrada, porque a linha é reconstruída após algum processamento. {{-}}

<span id="Reading the report">

##### Ler o relatório

</span>

![[_media/Source-Note-GEDCOMImportNote-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nota de importação Gedcom indicando dados omitidos anexados a nota da fonte]]

O Gramps usa um modelo de dados mais avançado do que o Gedcom, portanto alguns dados no Gedcom não podem ser importados para o Gramps (veja [Gramps and GEDCOM](wiki:Gramps_and_GEDCOM)). As principais excepções são:

- algumas estruturas de atributos Gedcom são tratadas como Gramps e, por conseguinte, muitos dos elementos primitivos Gedcom não podem ser armazenados;
- os elementos DATA de um SOURCE_RECORD (que indicam os eventos registados e o organismo responsável) são ignorados;
- as citações de fontes nas notas são ignoradas;
- muitos elementos primitivos do Gedcom não têm elementos de dados exactamente correspondentes no Gramps, pelo que são armazenados como com nomes apropriados, normalmente a etiqueta GEDCOM. Isto aplica-se particularmente ao cabeçalho, investigador e registos GEDCOM de submissão, e campos particulares como REFN, RFN, RIN e AFN.

Quando os dados são listados como "ignorados", a sua omissão é reportada no resumo no final da importação e é incluída numa anexada a um objecto relevante com um tipo personalizado . Veja, por exemplo, o objecto Fonte na imagem de exemplo, em cima à esquerda.

Quando os dados são listados como "silenciosamente ignorados", não são reportados nem incluídos numa nota. Actualmente , isto pode ser considerado como algo que não foi detectado pelo Gramps e deve ser levantado como uma questão . {{-}}

<span id="GEDCOM import limitations">

#### Limitações da importação Gedcom

</span> Esta secção descreve quaisquer dados GEDCOM que não podem ser representados directamente no Gramps, e como eles são tratados. Para informações adicionais sobre os limites das importações (e exportações) GEDCOM, por favor leia a secção [Gramps and GEDCOM](wiki:Gramps_and_GEDCOM).

<span id="HEADer, SUBMitter and SUBmissioN">

##### Etiquetas HEAD, SUBM e SUBN

</span>

O Gramps não tem uma representação directa destes dados, pelo que todas as informações aí contidas têm de ser armazenadas noutros objectos. Dependendo das [Preferências de importação](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Source_GEDCOM_import), pode ser criado um objecto "fonte pré-definida. Se este for criado, muitos dos dados são armazenados nesse objecto , ou em ligados a essa fonte.

<span id="HEADer">

###### HEAD

</span>

`   HEADER:=`  
`        n HEAD                                          {1:1}`  
`          +1 SOUR `<APPROVED_SYSTEM_ID>`                  {1:1}  (Rubrica de dados da "fonte por defeito")`  
`            +2 VERS `<VERSION_NUMBER>`                    {0:1}  (Rubrica de dados da "fonte por defeito")`  
`            +2 NAME `<NAME_OF_PRODUCT>`                   {0:1}  (Rubrica de dados da "fonte por defeito")`  
`            +2 CORP `<NAME_OF_BUSINESS>`                  {0:1}  (Repositório da "fonte pré-definida")`  
`              +3 <`<ADDRESS_STRUCTURE>`>                  {0:1}  (Repositório da "fonte pré-definida")`  
`            +2 DATA `<NAME_OF_SOURCE_DATA>`               {0:1}  (Rubrica de dados da "fonte por defeito")`  
`              +3 DATE `<PUBLICATION_DATE>`                {0:1}  (Rubrica de dados da "fonte por defeito")`  
`              +3 COPR `<COPYRIGHT_SOURCE_DATA>`           {0:1}  (Rubrica de dados da "fonte por defeito")`  
`          +1 DEST `<RECEIVING_SYSTEM_NAME>`               {0:1*} (Rubrica de dados da "fonte por defeito")`  
`          +1 DATE `<TRANSMISSION_DATE>`                   {0:1}  (Rubrica de dados da "fonte por defeito")`  
`            +2 TIME `<TIME_VALUE>`                        {0:1}  (Rubrica de dados da "fonte por defeito")`  
`          +1 SUBM @`<XREF:SUBM>`@                         {1:1}  (Rubrica de dados da "fonte por defeito")`  
`                                                               (Também utilizado para determinar o SUBMITTER_RECORD)`  
`                                                               (que deve ser armazenado como o proprietário da base de dados)`  
`          +1 SUBN @`<XREF:SUBN>`@                         {0:1}  (ignorada)`  
`          +1 FILE `<FILE_NAME>`                           {0:1}  (Rubrica de dados da "fonte por defeito")`  
`          +1 COPR `<COPYRIGHT_GEDCOM_FILE>`               {0:1}  (armazenado como a informação de publicação da "fonte pré-definida")`  
`          +1 GEDC                                       {1:1}`  
`            +2 VERS `<VERSION_NUMBER>`                    {1:1}  (Rubrica de dados da "fonte por defeito")`  
`            +2 FORM `<GEDCOM_FORM>`                       {1:1}  (Rubrica de dados da "fonte por defeito")`  
`          +1 CHAR `<CHARACTER_SET>`                       {1:1}  (Rubrica de dados da "fonte por defeito")`  
`            +2 VERS `<VERSION_NUMBER>`                    {0:1}  (Rubrica de dados da "fonte por defeito")`  
`          +1 LANG `<LANGUAGE_OF_TEXT>`                    {0:1}  (Rubrica de dados da "fonte por defeito")`  
`          +1 PLAC                                       {0:1}`  
`            +2 FORM `<PLACE_HIERARCHY>`                   {1:1}  (ver abaixo)`  
`          +1 NOTE `<GEDCOM_CONTENT_DESCRIPTION>`          {0:1}  (nota anexa à "fonte pré-definida")`  
`            +2 [CONT|CONC] `<GEDCOM_CONTENT_DESCRIPTION>` {0:M}`  
`            `  
`   * NOTA: os envios ao Departamento de História da Família para o Ancestral File ou para a autorização de ordenanças do templo devem utilizar um`  
`     DESTino de ANSTFILE ou TempleReady.`

A etiqueta PLAC FORM é armazenado internamente e utilizado para governar a interpretação dos lugares (de acordo com a especificação Gedcom).

<span id="SUBmissioN">

###### Etiqueta SUBN

</span>

A etiqueta SUBMISSION_RECORD (deve haver apenas uma, mas isto não é verificado) é armazenada como um item da "fonte pré-definida".

`    SUBMISSION_RECORD:=`  
`        n @`<XREF:SUBN>`@ SUBN                            {1:1]`  
`          +1 SUBM @`<XREF:SUBM>`@                         {0:1}`  
`          +1 FAMF `<NAME_OF_FAMILY_FILE>`                 {0:1}`  
`          +1 TEMP `<TEMPLE_CODE>`                         {0:1}`  
`          +1 ANCE `<GENERATIONS_OF_ANCESTORS>`            {0:1}`  
`          +1 DESC `<GENERATIONS_OF_DESCENDANTS>`          {0:1}`  
`          +1 ORDI `<ORDINANCE_PROCESS_FLAG>`              {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`

<span id="SUBMitter">

###### SUBM

</span>

As etiquetas SUBMITTER_RECORDs (pode haver mais de uma) são armazenadas como ligados à "fonte pré-definida", excepto nos casos indicados a negrito abaixo. O SUBMITTER_RECORD que corresponde ao registo SUBM no HEAD é utilizado para definir o [dono da base de dados](wiki:Gramps_6.0_Wiki_Manual_-_Tools/pt_PT#Edit_Database_Owner_Information) e pode ser copiado para a [informação do investigador](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Researcher), se necessário.

`   SUBMITTER_RECORD:=`  
`        n @`<XREF:SUBM>`@   SUBM                          {1:1}`  
`          +1 NAME `<SUBMITTER_NAME>`                      {1:1}`  
`          +1 <`<ADDRESS_STRUCTURE>`>                      {0:1}`  
`          `**`+1 <`<MULTIMEDIA_LINK>`> {0:M}`**  
`          `**`+1 LANG `<LANGUAGE_PREFERENCE>` {0:3}`**  
`          `**`+1 RFN `<SUBMITTER_REGISTERED_RFN>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- Ligação multimédia é ignorada
- LANG é ignorada
- RFN e RIN são ignoradas

<span id="INDIvidual">

##### INDIvíduo

</span>

A etiqueta INDIVIDUAL_RECORD é guardado como um registo Gramps , excepto nos casos indicados a negrito abaixo.

`   INDIVIDUAL_RECORD: =`  
`        n @`<XREF:INDI>`@  INDI                           {1:1}`  
`          +1 RESN `<RESTRICTION_NOTICE>`                  {0:1}`  
`          +1 <`<PERSONAL_NAME_STRUCTURE>`>                {0:M}`  
`          +1 SEX `<SEX_VALUE>`                            {0:1}`  
`          +1 <`<INDIVIDUAL_EVENT_STRUCTURE>`>             {0:M}`  
`          `**`+1 <`<INDIVIDUAL_ATTRIBUTE_STRUCTURE>`> {0:M}`**  
`          +1 <`<LDS_INDIVIDUAL_ORDINANCE>`>               {0:M}`  
`          +1 <`<CHILD_TO_FAMILY_LINK>`>                   {0:M}`  
`          +1 <`<SPOUSE_TO_FAMILY_LINK>`>                  {0:M}`  
`          `**`+1 SUBM @`<XREF:SUBM>`@ {0:M}`**  
`          +1 <`<ASSOCIATION_STRUCTURE>`>                  {0:M}`  
`          +1 ALIA @`<XREF:INDI>`@                         {0:M}`  
`          `**`+1 ANCI @`<XREF:SUBM>`@ {0:M}`**  
`          `**`+1 DESI @`<XREF:SUBM>`@ {0:M}`**  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 RFN `<PERMANENT_RECORD_FILE_NUMBER>`         {0:1}`  
`          +1 AFN `<ANCESTRAL_FILE_NUMBER>`                {0:1}`  
`          +1 REFN `<USER_REFERENCE_NUMBER>`               {0:M}`  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`  
`   `

- O indicador de ligação ao investigador, de interesse dos ascendentes e de interesse dos descendentes são silenciosamente ignorados.
- O indicador de pseudónimo ("Um indicador para ligar diferentes descrições de registo de uma pessoa que pode ser a mesma pessoa") é guardado como uma chamada "Aliás".
- O REFN e o REFN:TYPE são armazenados como do , mas se houver mais do que um REFN, pode não ser claro qual o TYPE associado a cada REFN.

O tratamento da estrutura INDIVIDUAL_ATTRIBUTE_STRUCTURE é bastante complicado. As seguintes etiquetas:

- EDUC (NMR (Número de casamentos)
- OCCU (Profissão)
- PROP (Posses)
- RELI (Filiação religiosa)
- RESI e
- TITL (Título de nobreza)

são todas tratadas como Gramps e a informação associada é armazenada na estrutura do evento. Os pormenores que se seguem à etiqueta principal (apresentados entre parênteses na lista acima) são armazenados como do . O <EVENT_DESCRIPTOR> que se segue à etiqueta TYPE substitui a , se <EVENT_DESCRIPTOR> não for o nome do atributo.

As seguintes etiquetas:

- CAST (Nome de casta)
- DSCR (Descrição física)
- INDO (Número de identificação nacional)
- NATI (Origem nacional ou tribal)
- NCHI (Contagem de crianças)
- SSN (Número de segurança social)

são todos tratados como Gramps e a maioria dos campos, excepto os detalhes a seguir à etiqueta principal (indicados entre parênteses na lista acima), a citação da fonte e a estrutura da nota são ignorados, como indicado a negrito abaixo.

`   INDIVIDUAL_ATTRIBUTE_STRUCTURE: =`  
`        n  CAST `<CASTE_NAME>`                            {1:1}`  
`          +1 <`<EVENT_DETAIL>`>                           {0:1}`  
`             etc.`  
`   `  
`   EVENT_DETAIL: =`  
`        `**`n TYPE `<EVENT_DESCRIPTOR>` {0:1}`**  
`        `**`n DATE `<DATE_VALUE>` {0:1}`**  
`        `**`n <`<PLACE_STRUCTURE>`> {0:1}`**  
`        `**`n <`<ADDRESS_STRUCTURE>`> {0:1}`**  
`        `**`n AGE `<AGE_AT_EVENT>` {0:1}`**  
`        `**`n AGNC `<RESPONSIBLE_AGENCY>` {0:1}`**  
`        `**`n CAUS `<CAUSE_OF_EVENT>` {0:1}`**  
`        n  <`<SOURCE_CITATION>`>                          {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`        `**`n <`<MULTIMEDIA_LINK>`> {0:M}`**  
`        n  <`<NOTE_STRUCTURE>`>                           {0:M}`  
`        `  
`        `

- A estrutura dos atributos individuais, o tipo, a data, a estrutura do local, a estrutura do endereço, a idade, a agência, a causa e a ligação multimédia são ignorados.

<span id="FAM_RECORD">

##### FAM_RECORD

</span>

A etiqueta FAM_RECORD é armazenada como do Gramps.

`   FAM_RECORD:=`  
`        n @`<XREF:FAM>`@   FAM                            {1:1}`  
`          +1 <`<FAMILY_EVENT_STRUCTURE>`>                 {0:M}`  
`          +1 HUSB @`<XREF:INDI>`@                         {0:1}`  
`          +1 WIFE @`<XREF:INDI>`@                         {0:1}`  
`          +1 CHIL @`<XREF:INDI>`@                         {0:M}`  
`          +1 NCHI `<COUNT_OF_CHILDREN>`                   {0:1}`  
`          +1 SUBM @`<XREF:SUBM>`@                         {0:M}`  
`          +1 <`<LDS_SPOUSE_SEALING>`>                     {0:M}`  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 REFN `<USER_REFERENCE_NUMBER>`               {0:M}`  
`            +2 TYPE `<USER_REFERENCE_TYPE>`               {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- A ligação ao investigador é silenciosamente ignorada.
- REFN e REFN:TYPE são armazenadas como da , mas se houver mais do que um REFN, pode não ser claro qual o TYPE associado a cada REFN.

<span id="SOURCE_RECORD">

##### SOURCE_RECORD

</span>

A etiqueta SOURCE_RECORD é armazenada como Gramps, excepto como indicado a negrito abaixo.

`   SOURCE_RECORD:=`  
`        n @`<XREF:SOUR>`@ SOUR                            {1:1}`  
`          `**`+1 DATA {0:1}`**  
`            `**`+2 EVEN `<EVENTS_RECORDED>` {0:M}`**  
`              `**`+3 DATE `<DATE_PERIOD>` {0:1}`**  
`              `**`+3 PLAC `<SOURCE_JURISDICTION_PLACE>` {0:1}`**  
`            `**`+2 AGNC `<RESPONSIBLE_AGENCY>` {0:1}`**  
`            `**`+2 <`<NOTE_STRUCTURE>`> {0:M}`**  
`          +1 AUTH `<SOURCE_ORIGINATOR>`                   {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_ORIGINATOR>`          {0:M}`  
`          +1 TITL `<SOURCE_DESCRIPTIVE_TITLE>`            {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_DESCRIPTIVE_TITLE>`   {0:M}`  
`          +1 ABBR `<SOURCE_FILED_BY_ENTRY>`               {0:1}`  
`          +1 PUBL `<SOURCE_PUBLICATION_FACTS>`            {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_PUBLICATION_FACTS>`   {0:M}`  
`          +1 TEXT `<TEXT_FROM_SOURCE>`                    {0:1}`  
`            +2 [CONT|CONC] `<TEXT_FROM_SOURCE>`           {0:M}`  
`          +1 <`<SOURCE_REPOSITORY_CITATION>`>             {0:1}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 REFN `<USER_REFERENCE_NUMBER>`               {0:M}`  
`            +2 TYPE `<USER_REFERENCE_TYPE>`               {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- DATA e os seus registos subsidiários são ignorados

<span id="REPOSITORY_RECORD">

##### REPOSITORY_RECORD

</span>

A etiqueta REPOSITORY_RECORD é armazenada como Gramps, excepto como indicado a negrito abaixo.

`   REPOSITORY_RECORD: =`  
`        n @`<XREF:REPO>`@ REPO                            {1:1}`  
`          +1 NAME `<NAME_OF_REPOSITORY>`                  {0:1}`  
`          +1 <`<ADDRESS_STRUCTURE>`>                      {0:1}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          `**`+1 REFN `<USER_REFERENCE_NUMBER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- REFN, REFN:TYPE e RIN são ignoradas

<span id="MULTIMEDIA_RECORD">

##### MULTIMEDIA_RECORD

</span>

A etiqueta MULTIMEDIA_RECORD é armazenada como Gramps, excepto como indicado a negrito abaixo.

`   MULTIMEDIA_RECORD:=`  
`        n @`<XREF:OBJE>`@ OBJE                            {1:1}`  
`          +1 FORM `<MULTIMEDIA_FORMAT>`                   {1:1}`  
`          +1 TITL `<DESCRIPTIVE_TITLE>`                   {0:1}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          `**`+1 BLOB {1:1}`**  
`            `**`+2 CONT `<ENCODED_MULTIMEDIA_LINE>` {1:M}`**  
`          +1 OBJE @`<XREF:OBJE>`@     /* chain to continued object */  {0:1}`  
`          `**`+1 REFN `<USER_REFERENCE_NUMBER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**

- Espera-se que exista uma etiqueta FILE para indicar o ficheiro que contém o objecto multimédia. Esta utilização é retirada do GEDCOM 5.6.0, mas a possibilidade de ter mais do que uma <MULTIMEDIA_FILE_REFN> e de ter as etiquetas FORM, TYPE e TITL subsidiárias da linha FILE não é suportada (um FILE posterior pode substituir um anterior - não há verificação de erros).
- BLOB é ignorada
- REFN, REFN:TYPE e RIN são ignoradas

<span id="NOTE_RECORD">

##### NOTE_RECORD

</span>

A etiqueta NOTE_RECORD é armazenada como Gramps, excepto como indicado a negrito abaixo.

`   NOTE_RECORD:=`  
`        n @`<XREF:NOTE>`@ NOTE `<SUBMITTER_TEXT>`           {1:1}`  
`          +1 [ CONC | CONT] `<SUBMITTER_TEXT>`            {0:M}`  
`          `**`+1 <`<SOURCE_CITATION>`> {0:M}`**  
`          `**`+1 REFN `<USER_REFERENCE_NUMBER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- citação de fonte ignorada
- REFN, REFN:TYPE e RIN são ignoradas

<span id="Exporting data">

## Exportar dados

</span>

Para exportar dados, escolha ou use o [atalho](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/pt_PT#) (ou em Apple Mac). Isto abre o diálogo .

A exportação permite-lhe partilhar qualquer parte da sua árvore Gramps (base de dados) com outros investigadores, bem como transferir os seus dados para outro computador.

O Gramps pode exportar dados para os seguintes formatos de ficheiro:

- [Folha de cálculo Comma Separated Values (CSV)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Comma_Separated_Values_Spreadsheet.28CSV.29_export);
- [GEDCOM](#GEDCOM_export);
- GeneWeb;
- Gramps [XML](wiki:Gramps_XML) (árvore genealógica);
- Gramps [XML](wiki:Gramps_XML) Package (árvore genealógica e multimédia);
- Web Family Tree;
- vCalendar;
- vCard.

{{-}} <span id="Export Assistant dialog">

### Diálogo Assistente de exportação

</span>

As páginas do guiá-lo-ão através da [selecção do formato de saída](#Choose_the_output_format), e, em seguida, das opções de exportação específicas para esse formato de ficheiro. Após a , a exportação será efectuada de acordo com as escolhas que tiver feito. Em qualquer altura, pode clicar no botão e rever qualquer selecção, e depois avançar para continuar a exportação. {{-}} <span id="Saving your data">

#### Gravar os seus dados

</span> ![[_media/ExportAssistant-SavingYourData-wizard-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Assistente de exportação: gravar os seus dados]]Informações gerais sobre a exportação a partir do Gramps.

Clique em para continuar. {{-}}

<span id="Choose the output format">

#### Escolher o formato de saída

</span>

![[_media/ExportAssistant-ChooseTheOutputFormat-wizard-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Escolha do formato de saída]]Seleccionar o formato de ficheiro para o qual exportar os dados:

- [Folha de cálculo Comma Separated Values (CSV)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Comma_Separated_Values_Spreadsheet.28CSV.29_export);
- [GEDCOM](#GEDCOM_export);
- GeneWeb;
- **Gramps [XML](wiki:Gramps_XML) (árvore genealógica)**(pré-definição);
- Gramps [XML](wiki:Gramps_XML) Package (árvore genealógica e multimédia);
- Web Family Tree;
- vCalendar;
- vCard.

Clique em para continuar. {{-}}

<span id="Export options">

#### Opções de exportação

</span> ![[_media/ExportAssistant-ExportOptions-CSV-defaults-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pré-definições para &quot;Folha de cálculo Comma Separated Values (CSV)&quot;) com destaque da secção inferior para opções específicas do formato de ficheiro]]

Depois de ter ajustado as suas opções nas duas secções.

- Secção superior não rotulada: [Filtros e privacidade](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Filters_and_privacy)
- Secção inferior não rotulada: [Opções específicas do formato de ficheiro](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#File_format_specific_export_options)

Clique em para continuar. {{-}} <span id="Filters and privacy">

##### Filtros e privacidade

</span>

O Gramps permite-lhe exportar a árvore genealógica seleccionada para formatos de ficheiro comuns. Os filtros seguintes fornecem opções que lhe permitem afinar a exportação. Os filtros permitem-lhe exportar uma quantidade limitada de dados, com base nos critérios seleccionados. <span id="Privacy Filter:">

###### Filtro de privacidade

</span>

  
marque esta caixa para impedir que registos ![[_media/22x22-gramps-lock.png]][privados](wiki:Gramps_Glossary#private) sejam incluídos no ficheiro exportado (caixamarcada por pré-definição).

<span id="Living Filter:">

###### Filtro de vivos

</span>

Esta opção restringe os dados e ajuda a limitar as informações exportadas para pessoas vivas. Isto significa que todas as informações relativas ao seu nascimento, morte, endereços, acontecimentos importantes, etc., serão omitidas no ficheiro exportado. Por exemplo, pode optar por substituir o nome próprio pela palavra **Vivo** (veja as suas [definições](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Text)); é possível excluir notas; e é possível excluir fontes para [indivíduos vivos](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive).

Por vezes, nem sempre é óbvio, a partir dos dados se alguém está efectivamente vivo. O Gramps utiliza um algoritmo avançado para tentar determinar [se uma pessoa ainda pode estar viva](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive/pt_PT). Lembre-se, o Gramps está a fazer a sua melhor suposição e pode não ser sempre capaz de adivinhar correctamente. Por favor, verifique sempre os seus dados.

Seleccione uma das seguintes opções:

- (pré-definição)

- 

- 

- 

<span id="Person Filter:">

###### Filtro de indivíduos

</span>

Seleccione uma das seguintes opções:

- (pré-definição)

- 

- 

- 

- 

- Criar um filtro personalizado seleccionando o *ícone de edição* para mostrar o diálogo .

<span id="Note Filter:">

###### Filtro de notas

</span>

Seleccione uma das seguintes opções:

- (pré-definição)

- Criar um filtro personalizado seleccionando o ícone *Editar* para mostrar o diálogo .

<span id="Reference Filter:">

###### Filtro de referências

</span> Seleccione uma das seguintes opções:

- (pré-definição)

- 

<span id="File format specific export options">

##### Opções específicas do formato de ficheiro

</span>

Dependendo do formato de ficheiro escolhido, poderá encontrar várias opções de exportação específicas do formato de ficheiro listadas na secção "Filtros e privacidade".

Consulte a secção relevante para cada um dos formatos de ficheiro listados que têm opções de exportação específicas:

- [Folha de cáculo Comma Separated Values (CSV)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Comma_Separated_Values_Spreadsheet.28CSV.29_export);
- [Gramps XML (árvore genealógica)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Gramps_XML_.28family_tree.29_export).

<span id="Select save file">

#### Seleccionar o ficheiro a gravar

</span>

![[_media/ExportAssistant-SelectSaveFile-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Seleccionar o ficheiro a gravar]]

Insira um de ficheiro `Sem_Título_1.`<extensão do tipo de ficheiro>(pré-definição)e escolha a localização da pasta onde pretende gravar o ficheiro de exportação, numa unidade local ou externa.

Clique em para continuar.

Se não tiver permissão para gravar o ficheiro nessa localização, verá o diálogo de aviso e depois o aviso do assistente de exportação . Clique em e inicie novamente a exportação, desta vez escolhendo uma pasta adequada. {{-}}

<span id="Final confirmation">

#### Confirmação final

</span>

![[_media/ExportAssistant-FinalConfirmation-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Confirmação final da exportação]]

A permite-lhe verificar os detalhes resumidos (formato/nome/localização) do ficheiro de exportação a criar. Nesta altura, pode clicar em para rever as suas opções ou para abortar o processo.

Clique em para continuar. {{-}}

<span id="Summary">

#### Resumo

</span> ![[_media/ExportAssistant-YourDataHasBeenSaved-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Conclusão da exportação]]

O do assistente de exportação mostra o *Nome do ficheiro:* ao fundo e confirma que os dados de exportação foram gravados com sucesso.

Clique em para sair do assistente de exportação. {{-}} <span id="Comma Separated Values Spreadsheet(CSV) export">

### Exportação para folha de cálculo Comma Separated Values (CSV)

</span>

![[_media/ExportAssistant-ExportOptions-CSV-defaults-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pré-definições para "Folha de cálculo Comma Separated Values (CSV)" com destaque da secção inferior para opções específicas do formato de ficheiro]]

Folha de cálculo Comma Separated Values (CSV): permite exportar (e importar) um subconjunto dos seus dados Gramps num formato simples de folha de cálculo.

Veja [Importação e exportação CSV](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT:_CSV_Import_and_Export) para informações adicionais e exemplos.

Folha de cálculo Comma Separated Values (CSV) tem as seguintes [opções de exportação específicas do formato de ficheiro](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#File_format_specific_export_options):

- Incluir indivíduos
- Incluir casamentos
- Incluir filhos
- Incluir locais
- Traduzir cabeçalhos

{{-}} Veja também [Exportar vista](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Export_View) como folha de cálculo.

<span id="GEDCOM export">

### Exportação Gedcom

</span>

O Gramps permite-lhe exportar uma base de dados para o formato comum .

A exportação não tem [opções de exportação específicas do formato de ficheiro](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#File_format_specific_export_options) mas pode alterar o seguinte:

- Certifique-se de que adiciona a sua informação de para criar um ficheiro Gedcom válido, isto também pode ser feito com a ferramenta .

Para mais informações sobre o formato GEDCOM, consultar:

- <https://en.wikipedia.org/wiki/GEDCOM>
- <https://www.familysearch.org/developers/docs/guides/gedcom>
- <https://www.familysearch.org/developers/docs/gedcom/>

Veja [Gramps and GEDCOM](wiki:Gramps_and_GEDCOM) para obter pormenores sobre os dados que não são exportados para Gedcom (). {{-}}

<span id="GeneWeb export">

### Exportação GeneWeb

</span>

A exportação gravaar uma cópia dos seus dados no formato genealógico GeneWeb. Para saber mais sobre o GeneWeb e o seu formato, visite:

- <http://www.geneweb.org>

não tem [opções de exportação específicas do formato de ficheiro](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#File_format_specific_export_options) {{-}}

<span id="Gramps XML (family tree) export">

### Exportação Gramps XML (árvore genealógica)

</span>

![[_media/ExportAssistant-ExportOptions-GrampsXMLFamilyTree-defaults-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pré-definições para "Gramps XML (árvore genealógica)" com destaque da secção inferior para opções específicas do formato de ficheiro]]

O formato (.gramps):este é o formato padrão para troca de dados e salvaguardas (ver o formato .gpkg abaixo para portabilidade total, incluindo objectos multimédia). A exportação para o formato [XML](wiki:XML) do Gramps produzirá uma base de dados portátil. Como XML é um formato baseado em texto legível por humanos, também pode usá-lo para dar ver os seus dados. O Gramps assegura-se de que pode abrir estes XML de versões mais antigas do Gramps na versão mais recente do Gramps (mas não o contrário!).

Se um ficheiro multimédia não for encontrado durante a exportação, verá o mesmo diálogo que encontra na exportação GEDCOM.

O tem as seguintes [opções de exportação específicas do formato de ficheiro](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#File_format_specific_export_options):

- \- opção para permitir que o Gramps exporte um ficheiro .gramps, sem o comprimir (marcada por pré-definição).

{{-}} <span id="What's not included:">

#### O que não é incluído

</span>

<span id="Gramps XML Package (family tree and media) export">

### Exportação Gramps XML Package (árvore genealógica e multimédia)

</span>

Exportação (.gpkg): exportar para o formato de pacote Gramps criará um ficheiro comprimido que contém a base de dados Gramps XML e cópias de todos os ficheiros multimédia associados. Isto é útil se quiser mover a sua base de dados para outro computador ou partilhá-la com alguém. Se um ficheiro multimédia não for encontrado durante a exportação, verá o mesmo diálogo que encontra na exportação GEDCOM.

não tem [opções de exportação específicas do formato de ficheiro](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#File_format_specific_export_options)

<span id="What's not included:">

#### O que não é incluído

</span>

<span id="Web Family Tree export">

### Exportação Web Family Tree

</span>

A exportação cria um ficheiro de texto que pode ser utilizado pelo programa **Web Family Tree**.

Para saber mais sobre a Web Family Tree e o seu formato, visite

- [`http://www.simonward.com/cgi-bin/page.pl?family/tree`](http://www.simonward.com/cgi-bin/page.pl?family/tree) - [linkrot](https://wikipedia.org/wiki/Link_rot). *see* [2016 **Internet Archive** snapshot](https://web.archive.org/web/20160316080343/http://www.simonward.com/cgi-bin/page.pl?family/tree)

O ficheiro não tem [opções de exportação específicas do formato de ficheiro](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#File_format_specific_export_options). {{-}}

<span id="vCalendar export">

### Exportação vCalendar

</span>

A exportação grava informações no formato utilizado em muitas aplicações de calendário, por vezes chamadas PIM, para Personal Information Manager.

Para mais informações sobre o formato vCalendar, consultar:

- <https://en.wikipedia.org/wiki/ICalendar#vCalendar_1.0>

O ficheiro não tem [opções de exportação específicas do formato de ficheiro](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#File_format_specific_export_options). {{-}}

<span id="vCard export">

### Exportação vCard

</span> A exportação grava informações num formato utilizado em muitas aplicações de livros de endereços, por vezes chamadas PIM, para Personal Information Manager.

Para mais informações sobre o formato vCard, consultar:

- <https://en.wikipedia.org/wiki/VCard>

O ficheiro não tem [opções de exportação específicas do formato de ficheiro](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#File_format_specific_export_options). {{-}}

[Category:Pt PT:Documentation](wiki:Category:Pt_PT:Documentation)
