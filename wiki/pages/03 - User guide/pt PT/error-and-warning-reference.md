---
title: Gramps 6.0 Wiki Manual - Error and Warning Reference/pt PT
categories:
- Pt PT:Documentation
- Stub
- Troubleshooting
managed: false
source: wiki-scrape
wiki_revid: 113403
wiki_fetched_at: '2026-05-30T19:47:14Z'
lang: pt PT
---

{{#vardefine:chapter\|E}} {{#vardefine:figure\|0}} Esta secção explica o que fazer quando algo inesperado acontece.

<span id="When something goes wrong">

## Quando algo corre mal

</span>

Às vezes algo corre mal, seja porque pediu para fazer algo que o Gramps não sabe fazer, ou porque aconteceu algo que os programadores do Gramps não previram, ou porque há um erro no código do Gramps.

.

<span id="Alerts">

## Alertas

</span>

Um alerta é um diálogo que aparece quando o Gramps precisa de lhe entregar uma mensagem importante sobre uma condição de erro ou avisá-lo sobre situações ou consequências potencialmente perigosas.

A maioria dos alertas são auto-explicativos, e o mesmo tipo de alertas que pode obter com qualquer aplicação. Estes não são discutidos aqui.

No entanto, alguns alertas requerem acções mais complicadas, pelo que são descritos abaixo. {{-}}

<span id="Are you sure you want to upgrade this Family Tree?">

### Tem a certeza de que deseja actualizar esta árvore?

</span>

![[_media/AreYouSureYouWantToUpgradeThisFamilyTree-dialog-DbUpgradeRequiredError-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Are you sure you want to upgrade this Family Tree?" dialog - Db Upgrade Required - example]]

Este diálogo (mais ou menos variante, conforme a versão do programa) aparece pelos seguintes motivos:

- "Actualização da BD requerida” - se tentar abrir uma árvore genealógica Db(Sqlite3) criada com uma versão anterior do Gramps com uma versão mais recente do Gramps.
- “Erro de actualização da BSDDB requerida” - base de dados de família [BSDDB](wiki:Gramps_Glossary#bsddb) substituída deve ser convertida para um motor de base de dados actual (tipicamente SQLite) para o Gramps.
- “Erro de actualização da BSDDB requerida” - se tentar abrir uma árvore genealógica BSDDB criada com uma versão anterior do Gramps com uma versão mais recente do Gramps.
- “Erro de desactualização da BSDDB requerida” - se tentar abrir uma árvore genealógica BSDDB criada com uma versão anterior mais antiga do BSDDB com uma versão mais recente do BSDDB.
- “Erro de actualização do Python requerida” - se tentar abrir uma árvore genealógica BSDDB criada com uma versão anterior mais antiga do Gramps usando Python 2 com uma versão mais recente do Gramps, que usa Python 3.

Por cada uma destas razões, pode seguir o mesmo conselho geral: se ainda tiver a versão mais antiga do Gramps disponível, então deve:

- cancelar este diálogo e sair do Gramps;
- abrir a árvore com a versão anterior do Gramps (reinstale-a, se necessário);
- exportar a árvore em formato [Gramps XML (só a árvore genealógica)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Gramps_XML_.28family_tree.29_export) ou [Gramps XML Package (árvore e multimédia)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Gramps_XML_Package_.28family_tree_and_media.29_export);
- sair da versão antiga do Gramps e iniciar a nova versão do Gramps;
- abrir o ficheiro exportado na nova versão e clicar em  
  .

{{-}}

<span id="Error parsing arguments">

### Erro ao analisar os argumentos

</span>

![[_media/ErrorParsingArguments-dialog-DatabaseIsLocked-example-60_pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}Diálogo Erro ao analisar os argumentos - Base de dados bloqueada]] A base de dados da árvore está bloqueada enquanto em uso por outro utilizador ou porque o Gramps saiu de forma anormal durante a utilização anterior.

Veja [Desbloquear uma árvore genealógica](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Unlocking_a_Family_Tree)

<span id="Database is locked. cannot open it!">

### A base de dados está bloqueada. Impossível abrir!

</span> A base de dados da árvore está bloqueada enquanto em uso por outro utilizador ou porque o Gramps saiu de forma anormal durante a utilização anterior.

Veja [Desbloquear uma árvore genealógica](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Unlocking_a_Family_Tree) {{-}}

<span id="Cannot open database">

### Impossível abrir a base de dados

</span>

![[_media/Cannot_open_database.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo com o erro de ambiente da base de dados]]

![[_media/DbVersionError.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo com o erro de versão da base de dados]]

Como explicado no diálogo, a árvore foi provavelmente criada com uma versão antiga do programa de base de dados Berkeley. Isto não é exactamente a mesma coisa que uma versão antiga do programa Gramps, porque a versão do programa Gramps e a versão da base de dados Berkeley são independentes. No entanto, o efeito é de certa forma o mesmo. Como sugerido no diálogo, se tem a versão antiga do Gramps e o seu programa de apoio, então deve:

- cancelar este diálogo;
- abrir a árvore genealógica com a versão anterior do Gramps;
- exportar a sua árvore genealógica no formato de exportação de base de dados XML do Gramps ou no formato de exportação de pacote do Gramps (ver [Exportar para formatos do Gramps](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Export_into_Gramps_formats));
- iniciar a nova versão do Gramps;
- abrir o diálogo "Gerir árvores genealógicas";
- clicar em e criar uma nova árvore;
- carregar a nova árvore;
- importar o Gramps XML ou o pacote Gramps.

Em alternativa, poderá ser possível utilizar as ferramentas de recuperação. Veja "obter as ferramentas de recuperação bsddb" sob [Recover corrupted family tree](wiki:Recover_corrupted_family_tree) {{-}}

<span id="Low level database corruption detected">

## Detectada corrupção de baixo nível na base de dados

</span>

![[_media/LowLevelDatabaseCorruptionDetected-dialog-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Low level database corruption detected" dialog - example]]

Este diálogo aparece quando é detectado um problema com a base de dados subjacente que suporta as árvores genealógicas. Para o tentar resolver:

- fechar o diálogo;
- clicar em "Gerir árvores genealógicas";
- selecionar a árvore que estava a tentar abrir;
- o botão deve estar disponível; clique-o;
- depois de a árvore ter sido reparada, deve ser possível abri-la da forma normal.

Se isto não funcionar, tente "obter as ferramentas de recuperação bsddb" sob [Recover corrupted family tree](wiki:Recover_corrupted_family_tree) {{-}}

<span id="Error detected in database">

### Erro detectado na base de dados

</span> ![[_media/RunDatabaseRepair.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo com reparação da base de dados]]

Executar a acção sugerida. {{-}}

<span id="Warnings">

## Avisos

</span> ![[_media/Status-bar-warning-button-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramps Main Window showing Warning button on the Status bar]] Se o Gramps detectar um erro menor, ou quiser notificá-lo de uma ocorrência no programa, poderá ver um botão de na barra de estado, como mostrado abaixo. O botão só é mostrado por 180 segundos, se o vir, clique-o imediatamente se quiser ver as mensagens.

{{-}} <span id="Gramps Warnings dialog">

### Diálogo de avisos do Gramps

</span>

Se clicar no botão de , verá um diálogo com as últimas 20 mensagens recebidas. Saiba [Mais detalhes sobre o sistema de rastreio](wiki:Logging_system). ![[_media/Gramps-warnings-dialog-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo de avisos do Gramps com mensagem de alerta]] {{-}}

Alguns dos avisos que podem aparecer são descritos abaixo:

<span id="Locale warnings">

### Avisos de idioma

</span>

Por vezes, ocorrem problemas com o idioma que escolheu.

Se instalou o Gramps com o método de instalação padrão da sua plataforma (gestor de pacotes/instalador AIO/pacote de aplicação) e estiver a usar o mecanismo integrado da sua plataforma (Configuração do sistema/Painel de controlo/Preferências do sistema) para escolher o idioma/ordem/formatos em que o executa, esses erros não devem ocorrer e podem significar que há um problema no Gramps.

No entanto, se tiver definido o idioma/ordem/formatos manualmente ao definir o "ambiente" veja [idiomas](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Language), particularmente se executa o Gramps a partir da linha de comandos, pode ser um problema naquilo que escreveu. A mensagem (da qual só parte é mostrada abaixo) deverá ajudar a compreender que erro é este:

- O analisador de datas para "%s" não disponível, a usar a pré-definição;
- O visualizador de datas para "%s" não está disponível, a usar a pré-definição;
- O tradutor de relações familiares não disponível para o idioma "%s",
- Impossível determinar o seu idioma, a usar o inglês;
- A biblioteca de localização libintl não está no %PATH%, a localização estará incompleta;
- Não foram encontradas traduções para %s, a usar o inglês dos EUA;
- Impossível criar colagem: %s;
- Nenhum idioma fornecido, a usar o inglês dos EUA;
- Não foram encontrados idiomas utilizáveis na lista, a usar o inglês dos EUA;
- Nenhum dos idiomas pedidos (%s) estava disponível, a usar %s.

<span id="Module not loaded warnings">

### Avisos de módulos não carregados

A aplicação Gramps contém muitos módulos diferentes. Alguns desses módulos são necessários para o Gramps funcionar; alguns são "fortemente recomendados", e alguns são opcionais.

Se instalou o Gramps usando o método de instalação padrão da sua plataforma (Gestor de pacotes/Instalador AIO/Pacote de aplicação), o construtor do pacote terá decidido quais os módulos presentes. Deverá ter incluído todos os módulos necessários, porque caso contrário o Gramps não funcionará. Mas pode escolher quais dos pacotes recomendados e opcionais inclui. Consulte a documentação do seu pacote para determinar quais módulos estão incluídos.

Se tentar fazer algo que necessite de um módulo que não está incluído, receberá um aviso como os abaixo (apenas a primeira parte da mensagem está incluída). O que pode fazer depende da sua plataforma:

**Linux** Deverá ser capaz de instalar o pacote usando o gestor de pacotes padrão da sua distribuição ou o GUI do gestor de pacotes. No entanto, nalguns casos, precisará de construir o módulo a partir da fonte.

**MS Windows e macOS** O instalador do MS Windows AIO e o pacote de aplicação macOS vêm com determinados módulos integrados. Não é possível ao utilizador normal adicionar mais módulos. Portanto, se achar que um módulo deveria ter ser incluído, publique no [fórum](wiki:Contact#Official) do Gramps (provavelmente na secção Desenvolvimento) explicando por que é que acha que a omissão é um erro:

- AVISO: Módulo PIL não carregado;
- ICU não carregada porque %s. A localização será prejudicada;
- Módulo OsmGpsMap não carregado;
- Módulo GExiv2 não carregado;
- Módulo Webkit não carregado;
- PIL (Python Imaging Library) não carregado;
- GtkSpell não carregado.

<span id="Show plugin status dialog on plugin load error">

#### Mostrar diálogo de estado das extensões se ocorrer um erro ao carregá-las

Permite mostrar o diálogo seguindo o processo de registo da [extensão](wiki:Gramps_Glossary#plugin) ao iniciar o Gramps. O diálogo relata extensões que causam erros durante o registo. Isto permite que os utilizadores encontrem e resolvam problemas de extensões.

O diálogo pode ser suprimido com a opção no separador do diálogo .

As condições de erro que accionariam o diálogo de estado das extensões são tratadas principalmente na função "load_plugin" da classe "PluginManager". Aqui estão as principais condições de erro:

1\. Erro de registo das extensões:

- gramps_target_version em falta ou inválido ([gen/plug/\_manager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1050-L1056))
- Formato de versão da extensão incorrecto ([gen/plug/\_manager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1058-L1062))
- Atributos requeridos do tipo específico de extensão em falta ([gen/plug/\_manager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1064-L1068))

2\. Erros de importação do módulo:

- O ficheiro Python principal da extensão não pode ser importado ([gen/plug/\_manager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1070-L1074))

3\. Plugin Initialization Erros de inicialização da extensão:

- Excepções ocorridas durante o processo de inicialização da extensão ([gen/plug/\_manager.py](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1076-L1080))

4\. Incompatibilidade de versão:

- O gramps_target_version da extensão não corresponde à versão Gramps em execução ([gen/plug/\_manager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1082-L1086))

5\. IDs de extensão duplicadas:

- São detectadas múltiplas extensões com a mesma ID ([gen/plug/\_manager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1088-L1092))

6\. Tipo de extensão inválido:

- [PTYPE](wiki:Addons_development#Create_a_Gramps_Plugin_Registration_file) especificado não reconhecido ([gen/plug/\_manager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gen/plug/_manager.py#L1094-L1098) e [gui/viewmanager](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/gramps/gui/viewmanager.py#L615-L618))

<span id="Configuration warnings">

### Avisos de configuração

</span>

Por vezes, vale a pena eliminar os ficheiros de configuração antigos.

- Importar ficheiros chave antigos "keys.ini"..." (o ficheiro `.gramps/keys.ini` ficou obsoleto no Gramps 3.2, é agora `.gramps/gramps``/gramps.ini` );
- Importação do antigo ficheiro de chaves “keys.ini” concluída;
- Não é possível encontrar o filtro %s nos filtros personalizados definidos;
- O número de argumentos não corresponde ao número de +;
- Valor "%(val)s" não encontrado para a opção “%(opt)s”;
- Não foi possível abrir o ficheiro recente %s porque %s;
- AVISO: a ignorar a chave antiga “%s”;
- AVISO: ignorar chave com tipo incorrecto;
- Falha na análise das opções do documento;
- Saltou uma linha na listagem da extensão: ;
- Falha ao carregar gramplets de %s porque %s;

<span id="Other warnings">

### Outros avisos

</span>

{{-}} <span id="Cannot save person">

#### Impossível gravar indivíduo

![[_media/CannotSavePerson-dialog-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Impossível gravar indivíduo (janela de aviso)]] A tentativa de gravar um indivíduo sem quaisquer dados do editor mostra este aviso. É necessária pelo menos uma letra para o primeiro nome.

**Impossível gravar indivíduo**  
Não há dados para este indivíduo. Por favor, insira-os ou cancele a edição.  
{{-}}

<span id="Cannot merge <object>">

#### Impossível unir <objecto>

</span> ![[_media/CannotMergePeople_dialog-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Impossível unir indivíduo (janela de aviso) - exemplo]] A tentativa de unir mais do que dois registos de um dado tipo mostra este diálogo de aviso.

Por exemplo:

**Impossível unir indivíduo**  
Devem ser seleccionadas exactamente duas pessoas para realizar uma união. Pode seleccionar-se um segundo indivíduo mantendo premida a tecla Ctrl enquanto se clica no indivíduo desejado. {{-}}

<span id="Duplicate Family warning dialog">

#### Diálogo de aviso de família duplicada

</span> ![[_media/DuplicateFamily-warning-dialog-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Família duplicada (janela de aviso)]]

Se criar uma família e seleccionar pais que já pertencem a uma família existente, o Gramps emitirá o aviso de . Se prosseguir com a gravação da nova família, terá uma família duplicada.

{{-}}

<span id="Suppress warning when adding parents to a child">

#### Suprimir avisos ao adicionar pais a um filho

</span>

Pode ser activado com a opção no diálogo [Preferências &gt; Avisos](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Warnings).

{{-}} <span id="Adding parents to a person dialog">

##### Adicionar pais a um indivíduo

</span> ![[_media/AddingParetsToA-Person-warning-dialog-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Adicionar pais a um indivíduo (janela de aviso)]]

{{-}}

<span id="Suppress warning when cancelling with changed data">

#### Suprimir aviso ao cancelar com dados alterados

</span>

Pode ser desactivado com a opção no diálogo [Preferêmcias &gt; Avisos](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Warnings) dialog.

Usado pelo diálogo [Editar indivíduo](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/pt_PT#Edit_Person_dialog).

<span id="Save Changes? dialog">

#### Diálogo Gravar alterações?

</span> ![[_media/SaveChanges-alert-dialog-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Gravar alterações?&quot; (janela de aviso)]]

{{-}}

<span id="Suppress warning about missing researcher when exporting to GEDCOM">

#### Suprimir avisos sobre a falta de dados do investigador ao exportar para Gedcom

</span>

Pode ser desactivado com a opção no diálogo [Preferências &gt; Avisos](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Warnings).

{{-}}

<span id="Undo history warning">

#### Aviso do histórico de Desfazer

![[_media/UndoHistoryWarning-Tool-dialog-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ferramenta &quot;Aviso do histórico de desfazer&quot; (janela de aviso)]] ![[_media/UndoHistoryWarning-Import-dialog-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Importação &quot;Aviso do histórico de desfazer&quot; (janela de aviso)]] O diálogo será mostrado e pode ou . É recomendado que pare e faça uma salvaguarda da sua base de dados, para que possa futuramente reverter o processo de correr a ferramenta (ou importação), se necessário. {{-}}

{{-}}

<span id="No selected book item">

#### Nenhum item escolhido no livro

</span> ![[_media/No-selected-book-item-warning-60-pt_PT.png|Nenhum item escolhido no livro (janela de aviso)]] {{-}}

<span id="Person <____> is not in the Database">

#### \<\_\_\_\_\> não está na base de dados

</span>

![[_media/PersonNotInDatabase-warning-60-pt_PT.png|&lt;____&gt; não está na base de dados}} (janela de aviso)]] O aviso será mostrado se o indivíduo inicial de um relatório estiver marcado como vivo ou privado e as opções do relatório (2) não permitirem a impressão de indivíduos privados ou vivos.

{{-}}

<span id="Autobackup...">

#### Salvaguarda automática

</span> ![[_media/Autobackup.notification.on.exit-60-pt_PT.png|Aviso de &quot;Salvaguarda automática&quot; ao sair (janela de aviso)]] O diálogo de aviso de **Por favor aguarde que a salvaguarda termine.** é mostrado ao sair do Gramps para indicar que está em curso uma salvaguarda automática.

Veja também:

- separador , opções de [Gestão de salvaguardas](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Backup_Management) para e .

<!-- -->

- [Salvaguarda: Adicionar um diálogo para mostrar o estado do Gramps \#1416](https://github.com/gramps-project/gramps/pull/1416)

{{-}}

<span id="Errors">

## Erros

</span>

Problemas mais sérios podem merecer um , através de um diálogo que descreverá as acções a tomar.

{{-}} <span id="Error Report">

### Relatório de erro

</span> ![[_media/ErrorReport-dialog-collapsed-ErrorDetail-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Assistente de relatório de erro - sem detalhes do erro]] ![[_media/ErrorReport-dialog-expanded-ErrorDetail-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Assistente de relatório de erro - detalhes expandidos]] O diálogo de aparece sempre que algo inesperado acontece no Gramps.

Leia o artigo [How to create a good bug report](wiki:How_to_create_a_good_bug_report). Se acha que sabe como reproduzir o erro, clique em para iniciar o , e siga as instruções. {{-}}

<span id="Error Reporting Assistant dialog">

### Assistente de relatório de erros

</span>

Oferece uma oportunidade de compilar um relatório de erro e, em seguida, enviá-lo manualmente para o sistema de relatórios de erros do Gramps (terá de ter uma conta registada no sistema do Gramps e iniciar sessão na sua conta).

- [Using the bug tracker](wiki:Using_the_bug_tracker)

{{-}} <span id="Report a bug page">

#### Página inicial do assistente

</span>

![[_media/ErrorReportingAssistant-ReportABug-page-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Página inicial do assistente]]

Este é o assistente de relatórios de erros. Ajuda a criar um relatório o mais detalhado possível para os programadores do Gramps resolverem o problema.

O assistente faz algumas perguntas e reúne algumas informações sobre o erro que acabou de ocorrer e o ambiente em que ocorreu.

No final do processo, ser-lhe-á solicitado que envie o relatório para o [sistema de rastreio de erros do Gramps](https://gramps-project.org/bugs/my_view_page.php).

O assistente copiará o relatório de erros para a área de transferência do sistema operativo. Poderá depois colá-lo no formulário do [sistema de rastreio](https://gramps-project.org/bugs/my_view_page.php) e rever exactamente que informação deseja incluir. {{-}}

<span id="Error Details page">

#### Página de detalhes do erro

</span>

![[_media/ErrorReportingAssistant-ErrorDetails-page-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Página de detalhes do assistente (com exemplo de erro)]]

Se conseguir identificar alguma informação pessoal nos detalhes, agora é a altura de a remover.

Esta é a informação detalhada do erro do Gramps, não se preocupe se não a compreender. Terá a oportunidade de adicionar mais detalhes sobre o erro nas páginas seguintes do assistente. {{-}}

<span id="System Information page">

#### Página de informação do sistema

</span>

![[_media/ErrorReportingAssistant-SystemInformation-page-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Página de informação do sistema]]

Estas são as informações do seu sistema que ajudarão os programadores a corrigir o erro. {{-}}

<span id="Further Information page">

#### Página de informações extra

</span>

![[_media/ErrorReportingAssistant-FurtherInformation-page-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Página de informação extra]]

Por favor, forneça o máximo de informações possível sobre o que estava a fazer quando o erro ocorreu.

Esta é a sua oportunidade de descrever exactamente o que motivou o erro. {{-}}

<span id="Bug Report Summary page">

#### Página de resumo do relatório de erro

</span>

![[_media/ErrorReportingAssistant-BugReportSummary-page-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Página de resumo do relatório de erro]]

Este é o relatório de erros concluído. A próxima página do assistente ajudá-lo-á a registar o erro no sítio do sistema de rastreio de erros do Gramps. {{-}}

<span id="Send Bug Report page">

#### Página de envio do relatório

</span>

![[_media/ErrorReportingAssistant-SendBugReport-page-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Página de envio do relatório]]

Use os dois botões abaixo para primeiro copiar o relatório para a área de transferência e, em seguida, abrir um navegador web para criar um relatório em <https://gramps-project.org/bugs/login_select_proj_page.php?ref=bug_report_page.php>

- \- Este é o passo final. Use os botões nesta página para iniciar um navegador web e criar um relatório no sistema de rastreio de erros do Gramps (pressupõe que já tenha uma conta, se não, inscreva-se primeiro e depois inicie sessão na sua conta):

  - \- Use este botão para iniciar um navegador e criar um relatório no sistema de rastreio de erros do Gramps;

  - \- Use este botão para copiar o relatório para a área de transferência. Em seguida, vá ao sítio de rastreio de erros usando o botão abaixo, cole o relatório e envie o relatório.

{{-}}

<span id="Complete page">

#### Página final

</span>

![[_media/ErrorReportingAssistant-Complete-page-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Página final]]

O Gramps é um projecto Open Source. O seu sucesso depende dos utilizadores. Os seus comentários e relatórios são importantes. Obrigado por gastar um pouco de tempo para enviar um relatório de erros. {{-}}

<span id="Other Errors">

### Outros erros

</span> <span id="Report could not be created">

#### Impossível criar o relatório

</span> Este diálogo, , pode ocorrer por vários motivos, e.g.: o papel personalizado que escolheu para o relatório é demasiado grande para o formato PDF em uso.

<span id="Seeing all the error messages">

## Ver todas as mensagens de erro

</span>

Por vezes, nem todas as informações necessárias para entender o que correu mal estarão visíveis. Por exemplo, se iniciar o Gramps com uma configuração de idioma inválida (ou alguns componentes ausentes), a mensagem que aparecerá no diálogo de será:

![[_media/Warning_message_GExiv2.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo com avisos limitados]] {{-}} Contudo, o conjunto completo de mensagens de aviso é:

`(process:10929): Gtk-WARNING **: Locale not supported by C library.`  
`   Using the fallback 'C' locale.`  
`2013-03-13 18:49:04.376: WARNING: __init__.py: line 69: Date parser for 'xx_XX.UTF-8' not available, using default`  
`2013-03-13 18:49:04.547: WARNING: __init__.py: line 85: Date displayer for 'xx_XX.UTF-8' not available, using default`  
`2013-03-13 18:49:05.949: WARNING: spell.py: line 74: Spelling checker is not installed`  
`2013-03-13 18:49:16.023: WARNING: gramplet.gpr.py: line 400: WARNING: GExiv2 module not loaded.  Image metadata functionality will not be available.`

Pode acontecer simplesmente que o Gramps não inicia e nada aparece no ecrã, ou que o Gramps de repente sai. Nesses casos, pode precisar fazer algo diferente para ver todos os erros.

<span id="Linux">

### Linux

</span>

Pode iniciar o Gramps a partir da linha de comando, como descrito [aqui](wiki:Gramps_6.0_Wiki_Manual_-_Getting_started/pt_PT#Linux). Verá então todas as informações de diagnóstico no terminal.

<span id="MS Windows">

### MS Windows

</span>

Pode iniciar o Gramps a partir da linha de comando, como descrito [aqui](wiki:Gramps_6.0_Wiki_Manual_-_Getting_started#MS_Windows). Verá então todas as informações de diagnóstico no terminal.

<span id="macOS">

### macOS

</span>

Pode iniciar o Gramps a partir da linha de comando, como descrito [aqui](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/pt_PT#macOS). Verá então todas as informações de diagnóstico no terminal.

<span id="Console application">

#### Aplicação de consola

</span>

Também pode ver as mensagens do diário do Gramps usando a da Apple. A aplicação da consola está localizada na pasta Utilitários do Mac, na pasta Aplicações (um atalho das versões recentes do macOS é premir Command e a barra de espaço para iniciar uma pesquisa Spotlight; na janela resultante, insira os primeiros caracteres da palavra "Consola" e seleccione a aplicação Console).

Por exemplo, um dos primeiros lançamentos alfa do Gramps simplesmente não começava e não mostrava nada no ecrã. No entanto, ao abrir a aplicação Console e escrever Gramps no filtro no canto superior direito, algumas informações de diagnóstico apareceram. Na verdade, escrevemos "gramps \[" porque havia algumas outras mensagens que não eram relevantes, mas não importava se também fossem incluídas. ![[_media/Console_output.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Saída da aplicação Console]] {{-}} Ao clicar em shift para seleccionar todas as mensagens relevantes e copiá-las, obtemos:

`01/03/2013 00:08:02 [0x0-0x88088].org.gramps-project.gramps[1867] 2939: ERROR: importer.py: line 51: Could not find any typelib for Gtk `  
`01/03/2013 00:08:05 [0x0-0x88088].org.gramps-project.gramps[1867] Gtk typelib not installed. Install Gnome  Introspection, and pygobject version 3.3.2 or later. `  
`01/03/2013 00:08:05 [0x0-0x88088].org.gramps-project.gramps[1867] Gramps will terminate now. `

Neste caso em particular, foi o suficiente para ajudar o programador a identificar o problema.

{{-}}

[Category:Pt PT:Documentation](wiki:Category:Pt_PT:Documentation) [Category:Troubleshooting](wiki:Category:Troubleshooting)
