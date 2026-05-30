---
title: Gramps 6.0 Wiki Manual - Getting started/pt PT
categories:
- Pt PT:Documentation
managed: false
source: wiki-scrape
wiki_revid: 113253
wiki_fetched_at: '2026-05-30T19:48:07Z'
lang: pt PT
---

{{#vardefine:chapter\|2}} {{#vardefine:figure\|0}}

Nesta secção, vamos começar pelo básico. Primeiro, vamos descrever os conceitos básicos do Gramps. Depois, veremos como iniciar o Gramps e como obter ajuda, quando necessário. \_\_FORCETOC\_\_ <span id="Overview of Gramps">

## Visão geral do Gramps

</span>

O Gramps é um programa livre e de código aberto, desenhado para ser uma ferramenta poderosa e flexível para genealogia. É uma estrutura para recolha de dados genealógicos, anotando como cada peça de informação se inter-relaciona e apresentando essas relações.

Geralmente, pode-se usar o Gramps da maneira que desejar. Não existe um método único e correcto de trabalhar ou registar os dados. No entanto, se deseja colaborar com outros investigadores ou utilizar outros programas, estar em conformidade com algumas directrizes comuns ajuda. Mesmo que esteja familiarizado com as práticas comuns de pesquisa genealógica, será sempre necessário perceber como é que o Gramps funciona. Mais tarde, poderá utilizar o Gramps de uma forma que complemente o seu estilo de pesquisa genealógica em particular.

O Gramps separa toda a informação genealógica em 9 categorias primárias:

- [Indivíduos](wiki:Gramps_Glossary#person)

- [Famílias](wiki:Gramps_Glossary#family)

- [Eventos](wiki:Gramps_Glossary#event)

- [Locais](wiki:Gramps_Glossary#place)

- [Fontes](wiki:Gramps_Glossary#source)

- [Citações](wiki:Gramps_Glossary#citation)

- [Repositórios](wiki:Gramps_Glossary#repository)

- [Multimédia](wiki:Gramps_Glossary#media)

- [Notas](wiki:Gramps_Glossary#note)

Cada uma destas é composta por itens independentes. Isto significa que pode inserir na sua árvore genealógica um item de cada vez e na ordem desejada. Pode ligar os itens entre si ou deixá-los desligados (ou mesmo caoticamente desorganizados), mas pesquisáveis. Ou pode começar com um dado desenho de árvore em mente e preenchê-lo ligando novos itens à medida que avança.

Por exemplo, pode querer inserir cada indivíduo primeiro, ligando-os posteriormente e assim criando famílias. Ou pode começar com uma família, ancorar a família adicionando um novo indivíduo como filho ou pai e depois, adicionar parentes, eventos e fontes nos espaços preparados da estrutura da família. Ou pode começar com fontes e só criar um indivíduo quando a sua pesquisa incluir uma menção a alguém. Ou pode misturar estes estilos de inserção de dados adicionando alguns notas e fontes, depois famílias e, posteriormente, voltas às notas e fontes. Em suma, faz a sua pesquisa genealógica como desejar.

Quando tiver questões adicionais, o Gramps tem uma comunidade de utilizadores e programadores a quem pode recorrer:

- a lista de [FAQ](wiki:Gramps_6.0_Wiki_Manual_-_FAQ/pt_PT) (perguntas frequentes);
- a [lista de correio](wiki:Contact#Mailing_lists);
- um [rastreio de erros, funcionalidades e problemas](wiki:Using_the_bug_tracker);
- as [salas de conversa em linha](wiki:Contact#Chat_Room)
- os [fóruns da comunidade](wiki:Contact#Forum).

\<span id="Connections\>

### Ligações

</span>

Estes 9 itens primários estão ligados de várias formas. Algumas destas ligações são mantidas implicitamente. Por exemplo, adicionar um indivíduo a uma família como pai ou filho cria automaticamente uma ligação especial, chamada **Referência**. Pode ver as famílias a que um indivíduo está ligado no separador **Referências** na janela principal do indivíduo. Há muitas outras maneiras de ver essas ligações no Gramps, incluindo a categoria Parentescos.

Para evitar a repetição de informação, o Gramps permite reutilizar ou partilhar itens. Estas são também ligações especiais, chamadas **ligações**. Por exemplo, um indivíduo pode ser ligado a qualquer número de notas. Se uma nota mencionar duas pessoas diferentes, pode fazer sentido partilhar essa única nota com ambos os indivíduos.

Algumas ligações têm, elas próprias, informação. Por exemplo, é possível ligar um indivíduo ao evento de casamento de um casal, por exemplo, porque o indivíduo foi testemunha no seu casamento. No entanto, o marido e a mulher estão ligados ao evento de casamento num papel *primário*, enquanto um convidado desempenha um papel diferente, por exemplo, como *testemunha*. Este tipo de informação é mantido na própria ligação, na propriedade de papel.

<span id="Privacy">

### Privacidade

</span>

O Gramps suporta dois diferentes métodos de protecção da privacidade de dados sensíveis da sua árvore genealógica. Estes métodos são utilizados ao partilhar a sua informação com outrem, seja pela criação de um relatório, pela exportação de dados, ou pela criação de uma página web.

O primeiro método protege informações sobre pessoas que o Gramps acredita estarem vivas. Se não tiver indicado especificamente que um indivíduo está morto (adicionando-lhe um evento de óbito), o Gramps tem uma função sofisticada e automática para determinar se alguém está vivo. Os indivíduos vivos têm os seus dados sensíveis ocultados quando se utiliza este método. Por exemplo, um indivíduo de nome "Silva, José" pode aparecer como "Silva, \[Vivo\]".

![[_media/Include-data-marked-private-52_Pt.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ignorar privacidade em relatórios]] O segundo método de privacidade é um sinalizador explícito ["privado"](wiki:Gramps_Glossary#private_tag) que pode ser definido em cada item. Por exemplo, pode ter informações sensíveis e pessoais numa nota. Se marcar essa nota como privada, essa nota não será mostrada em relatórios textuais e narrativos, ou em exportações. Tenha também em atenção que algumas ligações também podem ser marcadas como privadas. Isto é útil quando se pretende marcar a ligação de, por exemplo, um indivíduo a um evento como privada, mas ainda assim ter a pessoa e o evento disponíveis no relatório, exportação ou sítio Web.

Para activar estes dois métodos de privacidade, terá de indicar a sua utilização quando criar alguns relatórios ou exportar os seus dados. {{-}}

<span id="GEDCOM">

### GEDCOM

</span>

O Gramps deriva a sua estrutura central de itens de um padrão chamado GEDCOM. No entanto, o Gramps estende este padrão onde for considerado necessário. Se planeia usar os dados da sua família noutro sistema que usa GEDCOM, então provavelmente vai querer tentar restringir o uso de funcionalidades exclusivas do Gramps. Por outro lado, se não estiver limitado por outro programa genealógico, pode introduzir os seus dados da forma que mais lhe convier.

Pode ler mais detalhes sobre este assunto na secção [Gramps e Gedcom](wiki:Gramps_and_GEDCOM).

<span id="Start Gramps">

## Iniciar o Gramps

</span>

A melhor forma de aprender o Gramps é trabalhando com os seus dados. Vamos a isto!

A forma de iniciar o Gramps depende do sistema operativo que utiliza.

Além de iniciar o Gramps usando o ambiente gráfico do utilizador (GUI) como descrito abaixo, também é possível iniciar o Gramps usando a linha de comando (CLI). O uso da CLI pode produzir relatórios (até alguns que não estão disponíveis através do GUI), fazer conversões, etc., tudo sem abrir uma janela, e pode fornecer [informação extra](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference/pt_PT#Seeing_all_the_error_messages) em caso de problemas. Para mais informação, consulte o [apêndice Linha de comandos](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/pt_PT).

<span id="Linux">

### Linux

</span>

Apenas a plataforma Linux é oficialmente suportada, pois os programadores do Gramps usam e testam o código-fonte nessa plataforma, corrigindo quaisquer problemas que surjam devido a actualizações.

Supondo que tenha usado o gestor de pacotes padrão (seja através de uma CLI ou um GUI) da sua distribuição Linux, vai iniciar o Gramps da maneira *normal* para essa distribuição. Por exemplo, no Ubuntu 18.04, é colocado um ícone no lançador, ou o programa pode ser iniciado a partir do Dash. Para outras distribuições, pode ser criada uma entrada no menu Aplicações (normalmente na secção **Escritório**).

Iniciar o Gramps através da CLI em Linux é explicado [aqui](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/pt_PT#Linux).

<span id="MS Windows">

### MS Windows

</span>

A versão para MS(Microsoft) Windows é uma plataforma [suportada pela comunidade](wiki:Download#MS_Windows). Se instalar o executável [GrampsAIO64](wiki:All_In_One_Gramps_Software_Bundle_for_Windows), terá um ícone da aplicação na área de trabalho, assim como um atalho no menu Iniciar, onde pode clicar para iniciar o Gramps.

Iniciar o Gramps através da CLI em MS Windows é explicado [aqui](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/pt_PT#MS_Windows).

Há outras formas de instalar o Gramps em MS Windows, mas são bastante complicadas e saem do âmbito deste manual.

<span id="macOS">

### macOS

</span>

A versão para Apple macOS (originalmente Mac OS X encurtada para OS X) é uma plataforma [suportada pela comunidade](wiki:Download). Se transferiu a imagem de disco macOS (.dmg), simplesmente arraste a aplicação para a pasta de aplicações (ou onde deseje armazená-la) e faça duplo clique no ícone, como de costume.

Iniciar o Gramps através da CLI em macOS é explicado [aqui](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/pt_PT#macOS).

Há outras formas de instalar o Gramps em macOS, mas são bastante complicadas e saem do âmbito deste manual.

![[_media/Dashboard-category-view-first-open-no-family-tree-loaded-52_Pt.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Painel - Abertura do Gramps sem árvore carregada (Gramps 6.0.0)]] <span id="Choosing a Family Tree">

### Seleccionar uma árvore genealógica

</span>

Se o Gramps for iniciado sem uma árvore genealógica seleccionada, o ecrã inicial terá pouca funcionalidade. A maioria das operações não estará disponível. Para carregar uma árvore genealógica (também designada por "base de dados"), seleccione no menu para abrir o gestor de árvores, ou clique no ícone  
, na barra de ferramentas. O Gramps mantém um registo dos ficheiros recentes, de onde pode seleccionar o desejado clicando na seta junto ao ícone .

Para informação detalhada sobre o gestor de bases de dados e o menu de árvores genealógicas, veja o capítulo [Gerir árvores genealógicas](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT).

{{-}}

<span id="Tell me how to start right now!">

## Digam-me como começar já!

</span>

Aconselhamos toda a gente a ler o manual para aprender tudo sobre a utilização do Gramps. A genealogia leva tempo, por isso, aprender as ferramentas não é tempo perdido.

No entanto, se quiser realmente saber o mínimo para começar, então leia isto:

- [Inserir e editar dados: breve](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_brief/pt_PT)
- [Como começar em genealogia com o Gramps](wiki:Start_with_Genealogy).

<span id="Obtaining Help">

## Obter ajuda

</span>

O Gramps tem um menu que pode consultar a qualquer momento.

- Veja a secção .

{{-}}

[Category:Pt PT:Documentation](wiki:Category:Pt_PT:Documentation)
