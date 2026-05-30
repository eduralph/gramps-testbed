---
title: Gramps 6.0 Wiki Manual - Command Line/pt PT
categories:
- Pt PT:Documentation
managed: false
source: wiki-scrape
wiki_revid: 112821
wiki_fetched_at: '2026-05-30T19:45:49Z'
lang: pt PT
---

{{#vardefine:chapter\|C}} {{#vardefine:figure\|0}} Este apêndice fornece referências para as capacidades disponíveis ao iniciar o **Gramps (para PCs)** a partir de um terminal.

Para o **Gramps Web**, veja "Gerir utilizadores na linha de comando" na página [User System](https://www.grampsweb.org/install_setup/users/) da documentação do Gramps Web. <span id="Start Gramps through the Command Line">

## Iniciar o Gramps a partir da linha de comandos

a/span\>

Normalmente o Gramps é iniciado através da interface gráfica do utilizador (GUI) na [sua plataforma](wiki:Gramps_6.0_Wiki_Manual_-_Getting_started/pt_PT#Start_Gramps).

Também é possível iniciar o Gramps usando uma linha de comandos (CLI). O uso da CLI pode:

- produzir relatórios que não estão disponíveis através da GUI;
- criar relatórios, fazer conversões, etc. sem abrir uma janela;
- pode fornecer [informação extra](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Seeing_all_the_error_messages), em caso de problemas.

Esta secção do manual descreve como iniciar o Gramps através da CLI, e os recursos que estão disponíveis.

A forma de iniciar o Gramps através da CLI depende do sistema operativo que está a utilizar.

Para simplificar a descrição, os exemplos de uso abaixo são escritos do ponto de vista da execução do Gramps no Linux. Os exemplos teriam que ser alterados para outras plataformas. <span id="Linux">

### Linux

</span>

A plataforma Linux é a única plataforma *oficialmente* suportada (outras plataformas são *suportadas pela comunidade*). Isto porque os programadores do Gramps desenham, codificam, utilizam e testam o código-fonte nessa plataforma. Portanto, diagnosticar e corrigir quaisquer problemas que surjam (seja devido a actualizações, seja por outras causas) é feito usando ferramentas Linux.

Assumindo que tenha usado o gestor de pacotes padrão (seja através de CLI ou GUI) da sua distribuição Linux, o Gramps inicia-se através da CLI escrevendo:

`gramps`

Se "[construiu a partir da fonte](https://gramps-project.org/wiki/index.php/Linux:Build_from_source)", navegue até onde instalou a aplicação (a pasta incluirá o ficheiro `Gramps.py`). Escreva:

`python3 Gramps.py`

<span id="MS Windows">

### MS Windows

</span>

O MS Windows é uma plataforma [suportada pela comunidade](wiki:Download). Se instalar o [pacote Windows AIO](wiki:All_In_One_Gramps_Software_Bundle_for_Windows), verá um ícone na área de trabalho, bem como um item de menu no menu 'Iniciar'. No entanto, a pasta de instalação do Gramps não é adicionada ao caminho do sistema e para executar o Gramps via CLI, temos de saber o caminho para essa pasta. Para encontrar a pasta de instalação, consulte a [secção da pasta de instalação do pacote AIO](wiki:All_In_One_Gramps_Software_Bundle_for_Windows#Installation_folder).

Para encontrar o caminho utilizando antes um ícone:

- faça clique direito na aplicação `GrampsAIO64 ``-console`, ou no correspondente item no menu Iniciar;
- anote a localização do ficheiro (a sua pasta "Abrir localização");
- seleccione o caminho completo e copie-o ().

Para executar o Gramps a partir da linha de comandos, é necessário iniciar uma janela de terminal:

- no menu Iniciar, inicie cmd.exe;
- mude a pasta para a pasta de instalação que localizou antes;
- escreva ou cole o caminho, colocando-o entre aspas se houver espaços;
- prima .

Por exemplo, poderia ser:

`cd "C:\Program Files\GrampsAIO64-``"`  
`gramps`

Pode utilizar qualquer uma das opções da linha de comandos juntamente com isto. Por exemplo, para obter uma listagem detalhada de todas as bases de dados genealógicas na sua pasta pré-definida de árvores genealógicas, deveria anexar `-L`

`cd "C:\Program Files\GrampsAIO64-``"`  
`gramps -L`

Veja um exemplo de utilização aqui: <https://github.com/gramps-project/addons-source/pull/121>

<span id="masOS">

### macOS

</span>

O macOS é uma plataforma [suportada pela comunidade](wiki:Download). Se transferiu a imagem macOS (.dmg), basta arrastar a aplicação para a sua pasta de aplicações (ou para qualquer outro local onde a queira guardar) e iniciar o Gramps clicando duas vezes na aplicação da forma normal. O [gestor de pacotes Homebrew](https://github.com/Homebrew) também permite a instalação da aplicação na habitual pasta Aplicações.

Para executar a partir da linha de comandos, é necessário iniciar o terminal, que se encontra na pasta Utilitários da pasta principal Aplicações (/Applications/Utilities). Quando tiver uma janela de terminal aberta, escreva:

` /path/to/Gramps.app/Contents/MacOS/Gramps`

Se instalou o Gramps em Aplicações, juntamente com a maioria das suas outras aplicações, como sugerido acima, seria:

` /Applications/Gramps.app/Contents/MacOS/Gramps`

Pode utilizar qualquer uma das opções da linha de comandos juntamente com isto. Por exemplo, para obter uma listagem detalhada de todas as bases de dados genealógicas na sua pasta pré-definida de árvores genealógicas, deveria anexar:

` /Applications/Gramps.app/Contents/MacOS/Gramps -L`

Há outras formas de instalar o Gramps em macOS, mas são muito mais complicadas e não são cobertas aqui.

<span id="Python options">

## Opções Python

</span>

Nos exemplos de diferentes plataformas acima, e também em comandos em vários ficheiros, pode ver algumas opções após o comando "python", por exemplo '-EO' em

`python3 -EO ..\share\gramps\gramps.py -L`

É importante distinguir entre as **opções python**, neste caso:

`-EO`

e as **opções Gramps**, neste caso:

`-L`

As **opções python** que poderá encontrar são:

- `-E` ignora todas as variáveis de ambiente PYTHON\*, e.g. `PYTHONPATH` e `PYTHONHOME`, que possam estar definidas;
- `-O` activa optimizações básicas; isto altera a extensão do nome de ficheiro para ficheiros compilados (bytecode) de `.pyc` para `.pyo`; veja também PYTHONOPTIMIZE.

A bandeira de optimização `-O` tem vários efeitos no Gramps:

- se não estiver activa, aparece uma entrada adicional no menu ;
- se não estiver activa, [serão imprimidas mensagens início de sessão](wiki:Logging_system#So_how_logging_works_in_Gramps_after_all.3F).
- se não estiver activa, poderão ser activadas [declarações de depuração](wiki:Debugging_Gramps#Add_debug_statements);
- se não estiver activa, estarão disponíveis funcionalidades adicionais no [gestor de extensões](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager/pt_PT).

As **opções do Gramps** são descritas abaixo.

<span id="Available Gramps options">

## Opções do Gramps disponíveis

</span>

Esta secção fornece a lista de referência de todas as opções de linha de comandos disponíveis no Gramps. Se desejar saber mais do que apenas uma lista de opções, veja as secções [Operação](#Operation) e [Exemplos](#Examples). O resumo abaixo é impresso por

`gramps -h`

ou

`gramps --help`

    Utilização: gramps [OPÇÃO...]
      -load-modules=MÓDULO1,MÓDULO2,...      Módulos dinâmicos a carregar

    Opções de ajuda
      -?, --help                             Mostrar  esta mensagem de ajuda
      -usage                                 Mostrar  mensagem de ajuda abreviada

    Opções da aplicação
      -O, --open=ÁRVORE_GENEALÓGICA              Abrir árvore genealógica
      -U, --username=USERNAME                    Utilizador da base de dados
      -P, --password=PASSWORD                    Senha da base de dados
      -C, --create=ÁRVORE_GENEALÓGICA            Criar ao abrir se for uma nova árvore genealógica
      -i, --import=NOME_DO_FICHEIRO              Importar de ficheiro
      -e, -export=NOME_DO_FICHEIRO               Exportar para ficheiro
      -r, --remove=ÁRVORE_GENEALÓGICA_PADRÃO     Remover árvore genealógica (usar expressões regulares)
      -f, --format=FORMATO                       Especificar o formato da árvore genealógica
      -a,--action=ACÇÂO                          Especificar acção
    ..-p, --options=OPÇÕES                       Especificar opções
      -d, --debug=NOME_DO_UTILIZADOR             Activar diários de depuração
      -l [ÁRVORE_GENEALÓGICA_PADRÃO]             Listar árvores genealógicas
      -L [ÁRVORE_GENEALÓGICA_PADRÃO]             Listar árvores genealógicas em detalhe
      -t [ÁRVORE_GENEALÓGICA_PADRÃO]             Listar árvores genealógicas com tabulações
      -u, --force-unlock                         Forçar desbloqueamento da árvore genealógica
      -s, --show                                 Mostrar  definições da configuração
      -c, --config=[definição.config[:valor]]    Definir definições de configuração e iniciar o Gramps
      -y, --yes                                  Não pedir confirmação de acções perigosas (só linha de comando)
      -q, --quiet                                Suprimir indicação de progresso (só linha de comando)
      -v, --version                              Mostrar  versões
      -S, --safe                                 Iniciar o Gramps em modo de segurança
                                                 (usar temporariamente as pré-definições)
      -D, --default=[APXFE]                      Repor as prédefinições
                     A - as extensões são limpas
                     P - Preferências para as pré-definições
                     X - os livros são limpos, relatórios e definições de ferramenta para as pré-definições
                     F - os filtros são limpos
                     E - tudo para as pré-definições ou limpo

A mensagem de utilização é a seguinte:

`gramps --usage`

    Exemplo de uso do Gramps através da linha de comando:

    1. Para importar quatro bases de dados (cujos formatos possam ser determinados pelos seus nomes)
    e verificar se têm erros, poderá digitar:
    gramps -i ficheiro1.ged -i ficheiro2.gpkg -i ~/bd3.gramps -i ficheiro4.wft -a tool -p name=check. 

    2. Para indicar os formatos explicitamente no exemplo acima, acrescente os nomes dos ficheiros com as opções -f apropriadas:
    gramps -i ficheiro1.ged -f gedcom -i ficheiro2.gpkg -f gramps-pkg -i ~/bd3.gramps -f gramps-xml -i ficheiro4.wft -f wft -a tool -p name=check. 

    3. Para gravar a base de dados resultante de todas as importações, indique a opção -e
    (use -f se o nome do ficheiro não permite que o Gramps identifique o seu formato):
    gramps -i ficheiro1.ged -i ficheiro2.gpkg -e ~/novo-pacote -f gramps-pkg

    4. Para gravar todas as mensagens de erro dos exemplos acima nos ficheiros "ficheiro_saída" e "ficheiro_erros", execute:
    gramps -i ficheiro1.ged -i ficheiro2.dpkg -e ~/novo-pacote -f gramps-pkg >ficheiro_saída 2>ficheiro_erros

    5. Para importar três bases de dados e iniciar uma sessão interactiva do Gramps com o resultado:
    gramps -i ficheiro1.ged -i ficheiro2.gpkg -i ~/bd3.gramps

    6. Para abrir uma base de dados e, com base nos dados, gerar um relatório de cronologia em formato PDF,
    colocando o resultado no ficheiro minha_cronologia.pdf:
    gramps -O "Árvore genealógica 1" -a report -p name=timeline,off=pdf,of=minha_cronologia.pdf

    7. Para gerar um resumo da base de dados:
    gramps -O "Árvore genealógica 1" -a report -p name=summary

    8. Listar as opções do relatório
    Use o name=timeline,show=all para encontrar todas as opções disponíveis para o relatório de cronologia
    Para encontrar detalhes de uma opção específica, use show=nome_opção, por exemplo, name=timeline,show=off texto.
    Para saber os nomes de relatórios disponíveis, use name=show texto.

    9. Para converter uma árvore genealógica em tempo real para um ficheiro xml .gramps:
    gramps -O "Árvore genealógica 1" -e saída.gramps -f gramps-xml

    10. Para gerar uma página Web noutro idioma (e.g. alemão):
    LANGUAGE=de_DE; LANG=de_DE.UTF-8 gramps -O "Árvore genealógica 1" -a report -p name=página_web,target=/../de

    11. Finalmente, para iniciar uma sessão interactiva normal, digite:
    gramps

    Nota: estes exemplos são para a linha de comandos bash.
    A sintaxe pode ser diferente para outras, assim como para Windows.

<span id="List options">

### Opções de lista

</span> Imprimir uma lista de árvores conhecidas:

Esparsa  

`-l, Listar árvores genealógicas`

`gramps -l`

    Lista de árvores genealógicas conhecidas no caminho da base de dados


    /home/pmra/Documentos/Genealogias/Pós-de-Mina/67e8df63 com nome "Example"

{{-}}

Detalhada  

`-L, Listar árvores genealógicas em detalhes`

`gramps -L`

    Árvores genealógicas do Gramps:
    Árvore genealógica "Example":
       Base de dados: SQLite
       Bloqueado?: False
       Caminho: /home/pmra/Documentos/Genealogias/Gramps/67cbed59
       Localização do módulo da base de dados: /usr/lib/python3.13/sqlite3/__init__.py
       Número de citações: 1377
       Número de etiquetas: 0
       Número de eventos: 1024
       Número de famílias: 74
       Número de fontes: 111
       Número de indivíduos: 234
       Número de locais: 83
       Número de multimédia: 256
       Número de notas: 722
       Número de repositórios: 4
       Versão da base de dados: 3.46.1
       Versão do esquema: 21.0.0
       Árvore genealógica: Example
       Último acesso: 30/03/2025 07:06:39

{{-}}

<span id="Version options">

### Opções de versão

</span>

`-v ou --version imprime a versão do Gramps e suas dependências,`  
`     informação sobre variáveis de ambiente e caminhos de python e sistema`

`gramps -v`

    Gramps Settings:
    ----------------
     gramps    : 6.0.0
     o.s.      : Linux
     kernel    : 6.12.19-amd64

    Required:
    ---------
     Python    : 3.13.2
     Gtk++     : 3.24.49
     pygobject : 3.50.0
     Cairo     : 1.18.4
     pycairo   : 1.27.0
     Pango     : 1.56.3
     PangoCairo: 1.0
     orjson    : 3.10.7

    Recommended:
    ------------
     osmgpsmap : 1.0
     Graphviz  : 2.42
     Ghostscr. : 10.05.0
     ICU       : 3.13.2
     PyICU     : not found

    Optional:
    ---------
     Gspell     : não encontrado
     RCS        : não encontrado
     PILLOW     : 11.1.0
     GExiv2     : 0.10
     Exiv2 lib. : não encontrado, por o exiv2 não estar instalado
     geocodeglib: não encontrado

    Environment settings:
    ---------------------
     LANG      : pt_PT.UTF-8
     LANGUAGE  : pt_PT
     GRAMPSI18N: not set
     GRAMPSHOME: not set
     GRAMPSDIR : not set
     PYTHONPATH:
        /usr/lib/python3/dist-packages/gramps
        /usr/bin
        /usr/lib/python313.zip
        /usr/lib/python3.13
        /usr/lib/python3.13/lib-dynload
        /usr/local/lib/python3.13/dist-packages
        /usr/lib/python3/dist-packages
        /home/pmra/.local/share/gramps/gramps60/plugins/lib

    System PATH env variable:
    -------------------------
         /home/pmra/.local/MyBins/
         /usr/local/bin
         /usr/bin
         /bin
         /usr/local/games
         /usr/games

    Databases:
    -------------------------
     bsddb     :
         version     : 6.2.9
         db version  : 5.3.28
         location    : /usr/lib/python3/dist-packages/bsddb3/__init__.py
     sqlite3   :
         version     : 3.46.1
         location    : /usr/lib/python3.13/sqlite3/__init__.py

{{-}}

<span id="Format options">

### Opções de formato

</span>

O formato de qualquer ficheiro a abrir, importar, ou exportar pode ser especificado com a opção

    -f formato

. Os valores aceitáveis para *`formato`* são discriminados abaixo.

<span id="Full family tree support">

#### Suporte completo a árvores genealógicas

</span> Estes formatos contêm todos os seus dados presentes numa árvore genealógica:

- **gramps** - formato Gramps XML: este formato está disponível para importação e exportação; quando não especificado, pode ser adivinhado, se o nome do ficheiro terminar com .gramps;
- **gpkg** - formato Gramps package XML: este formato está disponível para importação e exportação; quando não especificado, pode ser adivinhado, se o nome do ficheiro terminar com .gpkg; é criado um pacote comprimido com os seus dados como xml, e todos os seus ficheiros multimédia incluídos;
- **grdb** - pré-base de dados Gramps 3.x: este formato está disponível para importação para suportar o antigo formato de ficheiro do Gramps; tudo no ficheiro grdb é importado; quando não especificado, pode ser adivinhado, se o nome do ficheiro termina com .grdb
- **burn** - iso GNOME para queimar: exportação, só disponível em GNOME, onde o protocolo de queima exista.

<span id="Reduced family tree support">

#### Suporte reduzido a árvores genealógicas

</span> Estes formatos contaêm a maioria, mas nem todos os dados que podem ser criados no Gramps:

- **ged** - formato GEDCOM: este formato está disponível para importação e exportação; quando não especificado, pode ser adivinhado se o nome do ficheiro terminar com .ged;
- **gw** - ficheiro GeneWeb: este formato está disponível para importação e exportação; quando não especificado, pode ser adivinhado se o nome do ficheiro terminar com .gw.

<span id="Subset of your data">

#### Sub-conjunto dos seus dados

</span> Estes formatos contêm um sub-conjunto específico dos seus dados

- **csv** - Comma Separated Value: este formato está disponível para importação e exportação; no entanto, é preciso ter cuidado, a importação deve ser feita com os valores criados pela função de exportação; apenas uma parte dos seus dados está contida na saída;
- **vcf** - formato VCard 3.0: importação e exportação;
- **vcs** - formato VCalendar: exportação;
- **def** - formato antigo Pro-Gen: importação;
- **wft** - Web Family Tree: este formato está disponível apenas para exportação; quando não especificado, pode ser adivinhado, se o nome do ficheiro terminar com .wft

<span id="Opening options">

### Opções de abertura

</span>

Pode abrir uma árvore genealógica, ou pode “abrir” um ficheiro importando-o para uma árvore genealógica vazia.

Para deixar o Gramps lidar com isso automaticamente, basta fornecer a árvore genealógica ou o nome do ficheiro que deseja abrir:

`python gramps.py 'My Fam Tree'`  
`python gramps.py JohnDoe.ged`

O primeiro abre uma árvore genealógica, o segundo importa um GEDCOM para uma árvore genealógica vazia.

Adicionalmente, pode passar ao Gramps o nome da árvore genealógica a abrir:

- use esta opção: `-O famtree` ou `--open=famtree`

`-O`, Abrir uma árvore genealógica. Isto também pode ser feito escrevendo apenas o nome (nome ou pasta da base de dados)

Exemplos:

`python gramps.py 'Family Tree 1'`  
`python gramps.py /home/cristina/.gramps/grampsdb/47320f3d`  
`python gramps.py -O 'Family Tree 1'`  
`python gramps.py -O /home/cristina/.gramps/grampsdb/47320f3d`

<span id="Import options">

### Opções de importação

</span>

Os ficheiros destinados a importação podem ser especificados com a opção `-i nomeficheiro` ou `--import=nomeficheiro`. O formato pode ser especificado com a opção `-f formato` ou `--format=formato`, imediatamente a seguir a *nomeficheiro*. Se não especificada, será adivinhada, baseada em *nomeficheiro*.

Exemplo:

`  python gramps.py -i 'Family Tree 1' -i 'Family Tree 2'`  
`  python gramps.py -i test.grdb -i data.gramps`

Quando é fornecido mais do que um ficheiro de entrada, cada um tem de ser precedido pela bandeira `-i`. Os ficheiros são importados pela ordem especificada, i.e. `-i fich1 -i fich2` e `-i fich2 -i file1` podem produzir diferentes IDs Gramps na base de dados resultante.

<span id="Export options">

### Opções de exportação

</span>

Os ficheiros destinados a exportação podem ser especificados com a opção `-e nomeficheiro` ou `--export=nomeficheiro`. O formato pode ser especificado com a opção `-f` imediatamente a seguir a *nomeficheiro*. Se não especificada, será adivinhada, baseada em *nomeficheiro*. Para formato iso, o *nomeficheiro* é de facto o nome da pasta em que a base de dados do Gramps será escrita. Para gramps-xml, gpkg, gedcom, wft, geneweb, e gramps-pkg, o *nomeficheiro* é o nome do ficheiro resultante.

-e, exporta uma árvore genealógiga no formato requerido. Não é possível exportar para uma árvore genealógica.

Exemplo:

` python gramps.py -i 'Family Tree 1' -i test.grdb -f grdb -e mergedDB.gramps`

Note que o acima não altera "Family Tree 1", dado que tudo acontece através de uma base de dados temporária, onde:

` python gramps.py -O 'Family Tree 1' -i test.grdb -f grdb -e mergedDB.gramps`

importará test.grdb para Family Tree 1, e depois exporta-o para um ficheiro!

Quando fornece mais de um ficheiro de saída, cada um tem de ser precedido pela bandeira `-e`. Os ficheiros são escritos uma aum, na ordem especificada.

<span id="Action options">

### Opções de acções

</span>

A acção a arealizar em dados importados pode ser especificada com a opção `-a acção` ou `--action=acção`. Isto é feito após todas as importações estarem concluídas com sucesso.

As seguintes acções permanecem na mesma:

- *report*: esta acção permite produzir relatórios a partir da linha de comandos;

<!-- -->

- *tool*: esta acção permite executar uma ferramenta a partir da linha de comandos.

Os relatórios e as ferramentas têm geralmente muitas opções próprias, pelo que estas acções devem ser seguidas da cadeia de opções do relatório/ferramenta. A cadeia de caracteres é fornecida usando a opção `-p cadeiaopções` ou `--options=cadeiaopções`.

As acções em versões anteriores do Gramps que foram relocalizadas no Gramps 3.3 são:

- *summary*: esta acção era a mesma que . No Gramps 3.3 foi substituída por (ou renomeada para) **-a report -p name=summary**.

<!-- -->

- *check*: esta acção era a mesma que . No Gramps 3.3 it foi substituída por (ou renomeada para) **-a tool -p name=check**.

<span id="report action option">

#### Opção de acção de relatório

</span> É possível gerar a maioria dos relatórios a partir da linha de comandos utilizando a acção de relatório.

Um exemplo:

`gramps -O "Family Tree 1" -a report -p "name=family_group,style=default,off=html,of=test.html"`

Pode fornecer a folha de estilos css com a opção css:

`gramps -O "Family Tree 1" -a report -p "name=family_group,style=default,off=html,of=test.html,css=Web_Nebraska.css"`

ou sem css na saída html:

`gramps -O "Family Tree 1" -a report -p "name=family_group,style=default,off=html,of=test.html,css="`

A maior parte das opções de relatório são específicas para cada relatório. No entanto, existem algumas opções comuns.

- `name=report_name`: esta opção obrigatória determina o relatório a gerar.

- `of=`: imprime nome de ficheiro e, opcionalmente pasta de destino, e.g.: `of="C:\Users\`<username>`\Desktop\FamilyTree.odt"`
- `off=`: formato saída; estas são a extensões que um formato de saída disponibiliza, e.g., pdf, html, doc, ...
- `style=`: para relatórios de texto, a folha de estilos a usar. Pré-definida como "default";
- `show=all`: produz a lista de nomes de todas as opções disponíveis para um dado relatório;
- `show=option_name`: imprime a descrição da funcionalidade oferecida pela nomeopção, assim como os tipos aceitáveis e seus valores.

Assim, para aprender a usar um relatório, faça, por exemplo:

`gramps -O "Family Tree 1" -a report -p "name=family_group,show=all"`

Quando indica mais de uma acção de saída, cada uma tem de ser precedida da bandeira `-a`. As acções são realizadas uma a uma, pela ordem especificada.

Na linha de comandos, estas listas devem sempre começar com um `[` à esquerda e devem sempre terminar com um `]` à direita, mas como esses parênteses são geralmente "especiais" para o terminal (significam algo para o interpretador de comandos que está a utilizar), deve "escapá-los", para que sejam ignorados pelo seu interpretador.

Os detalhes variam com cada interpretador, mas (em linux/UNIX) geralmente pode precedê-los com uma barra invertida `\` ou pô-los entre aspas, geralmente "únicas" ou "duplas".

O relatório Ampulheta permite colocar uma "nota" no topo do relatório e tal "nota" é um exemplo de uma opção de "lista". Aqui está um exemplo:

`gramps -O "Family Tree 1" -a report -p name=hourglass_graph,note='[line one,line two]'`

o que mostra que dentro de tal lista, diferentes linhas são separadas por vírgulas e que os espaços são aceitáveis, uma vez que as aspas já existem para os parênteses.

Mas se quiser ter uma vírgula dentro do seu relatório, terá que de alguma forma dizer ao Gramps que a vírgula não separa as linhas. Isto consegue-se colocando a linha com a vírgula entre aspas (individual ou dupla).

Se já estiver a usar um conjunto de aspas (para incluir parênteses), deverá usar o outro tipo para anexar a linha com a sua vírgula. Aqui está um exemplo:

`gramps -O "Family Tree 1" -a report -p name=hourglass_graph,note="['line one, also line one','line two, also line two']"`

É possível incluir qualquer carácter numa lista, mas os detalhes estão fora do âmbito desta página do Gramps.

Terá de conhecer os métodos precisos disponíveis para o seu interpretador de comandos em particular para incluir um carácter que seja "especial" para o seu terminal ou "especial" para o Gramps (como a vírgula no exemplo acima), mas, geralmente, terá de o "escapar" duas vezes, uma para o terminal, outra para o Gramps, uma vez que não quer que o terminal pense que se trata de uma instrução a que deve obedecer, e também não quer que o Gramps o faça.

<span id="tool action option">

#### Opção de acção de ferramenta

</span> Pode executar a maioria das ferramentas a partir da linha de comandos com a acção "tool". Para ver quais, escreva:

`gramps -O "Family Tree 1" -a tool -p show=all`

Para ver as opções disponíveis para uma dada ferramenta, e.g. "verify":

`gramps -O "Family Tree 1" -a tool -p name=verify,show=all`

Para executar uma ferramenta, e.g. "verify":

`gramps -O "Family Tree 1" -a tool -p name=verify`

<span id="book action option">

#### Opção de acção de livro

</span> Pode criar livros a partir da linha de comandos usando a acção "book". Para ver quais, escreva:

`gramps -O "Family Tree 1" -a book`

Para ver as opções disponíveis de um livro, por exemplo, um livro chamado "mybook":

`gramps -O "Family Tree 1" -a book -p name=mybook,show=all`

Para executar um livro, por exemplo, um livro chamado "mybook":

`gramps -O "Family Tree 1" -a book -p name=mybook`

<span id="Force unlock option">

### Opção de desbloqueio forçado

</span>

- `-u`: pode estender a bandeira `-O` com `-u` para forçar o desbloqueio de um ficheiro. Isto permite que recupere de uma falha que deixa a árvore genealógica bloqueada, a partir da linha de comandos.

Um exemplo (para desbloquear a base de dados "Family Tree 1"):

  
`gramps -O "Family Tree 1" -a report -u > /dev/null`

Veja também:

- [Gerir árvores genealógicas: desbloquear uma árvore genealógica](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Unlocking_a_Family_Tree)

<span id="Configuration (config) option">

### Opção de configuração

</span> Quando todas as variáveis de configuração estiverem definidas, o Gramps inicia com estes novos valores.

Estas opções podem assumir três formas:

1\) Ver todos os valores de configuração  
`-s` ou `--show`

  
Por exemplo:

`gramps --show`

    Definições do Gramps de /home/pmra/.config/gramps/gramps60/gramps.ini:
    behavior.addmedia-image-dir=''
    behavior.addmedia-relative-path=''
    behavior.autoload=''
    behavior.avg-generation-gap=''
    behavior.check-for-addon-updates=''
    behavior.check-for-addon-update-types=''
    behavior.last-check-for-addon-updates=''
    behavior.previously-seen-addon-updates=''
    behavior.do-not-show-previously-seen-addon-updates=''
    behavior.date-about-range=''
    behavior.date-after-range=''

    ....

{{-}}

2\) Ver um único valor de configuração  
`--config=database.path` ou `-c database.path`

  
Por exemplo:

`gramps --config=database.path`

    Current Gramps config setting: database.path:'/home/<~username>/.gramps/grampsdb'

3\) Definir um valor  
`--config=behavior.database-path:'/media/mydb'` or `-c behavior.database-path:'/media/mydb'`

<!-- -->

3.1) Repor a pré-definição de um valor  
`--config=behavior.database-path:DEFAULT` or `-c behavior.database-path:DEFAULT`

<!-- -->

3.2) Definir mais de um valor  
`--config=behavior.use-tips:False --config=behavior.autoload:True` ou `-c behavior.use-tips:False -c behavior.autoload:True`

\<span id="Safe mode"

### Modo de segurança

`gramps -S` ou `gramps --safe`

Este comando inicia o Gramps como se nunca tivesse sido instalado antes. Neste modo, quaisquer árvores genealógicas anteriores ainda podem ser carregadas, desde que tenham sido armazenadas na pasta padrão. Todas as outras configurações, filtros, livros, complementos, etc. são limpos ou retornados aos seus valores padrão. Outros comandos podem ser usados ou, se não houver, o Gramps iniciará o GUI. Nada, excepto os dados reais da árvore genealógica, é gravado.

Note que isto é normalmente usado para ver se o Gramps se comporta melhor quando está a correr como se com uma instalação totalmente "limpa". NÃO é permanente (se quiser, veja [Pré-definições](#Defaults) abaixo), se iniciar o Gramps normalmente após usar este comando, todas as suas configurações anteriores, etc., ainda estarão lá.

Isto na realidade funciona definindo a pasta que o Gramps usa para armazenar seus dados (excepto para árvores genealógicas) como uma pasta temporária, que é eliminada quando o Gramps fecha.

<span id="Defaults">

### Pré-definições

</span> `gramps -D E` ou `gramps --default=E`

Este comando faz com que o Gramps limpe ou retorne as configurações desejadas às pré-definições. As bases de dados da árvore genealógica NÃO são apagadas ou removidas. Os sub-comandos (substitua o "E" da linha de comandos do exemplo acima por um ou mais dos os caracteres de subcomando) são:

- `A` as extensões instaladas são removidas, assim como a sua configuração;
- `F` os filtros personalizados são removidos;
- `P` as preferências voltam aos valores pré-definidos;
- `X` as configurações de livros, relatórios e ferramentas voltam aos valores pré-definidos;
- `Z` ficheiros ".zip" antigos de actualizações de árvores genealógicas são eliminados;
- `E` tudo excepto os dados da árvore genealógica volta aos valores pré-definidos; faz tudo o acim descrito, mais algumas coisas; elimina miniaturas, mapas, e CSS do utilizador (usada em relatórios web).

Por exemplo:

`gramps -D AP`

faz com que o Gramps remova todas as extensões e reponha as preferências.

<span id="Operation">

## Operação

</span>

Se o primeiro argumento na linha de comando não começar com um traço (ou seja, sem bandeira), o Gramps tentará abrir o ficheiro com o nome dado pelo primeiro argumento e iniciar uma sessão interactiva, ignorando o resto dos argumentos da linha de comando.

Se a bandeira `-O` for indicada, o Gramps tentará abrir o ficheiro fornecido e trabalhar com esses dados, conforme instruído pelos parâmetros adicionais da linha de comando.

Com ou sem a bandeira `-O`, pode haver múltiplas importações, exportações e acções especificadas mais adiante na linha de comando usando `-i`, `-e` e `-a`.

A ordem das opções `-i`, `-e` ou `-a` em relação a cada uma não importa. A ordem de execução real é sempre: todas as importações (se houver) -\> todas as exportações (se houver) -\> todas as acções (se houver).

Se nenhuma opção `-O` ou `-i` for fornecida, o Gramps iniciará a janela principal e iniciará a sessão interactiva habitual com a base de dados vazia, pois de qualquer maneira não há dados para processar (a menos que você já tenha expressado uma "preferência" de que comece com a última base de dados utilizada).

Se nenhuma opção `-e` ou `-a` for fornecida, o Gramps iniciará a janela principal e iniciará a sessão interactiva habitual com a base de dados resultante da abertura e de todas as importações (se houver). Esta base de dados reside numa pasta sob *`~/.gramps/grampsdb/`*.

Quaisquer erros encontrados durante a importação, exportação ou acção serão despejados em stdout (se forem excepções tratadas pelo Gramps) ou em stderr (se não forem tratadas). Use redireccionamentos habituais de terminal de stdout e stderr para gravar mensagens e erros em ficheiros.

<span id="Examples">

## Exemplos

</span>

- Para importar quatro bases de dados (cujos formatos podem ser determinados a partir de seus nomes) e, em seguida, verificar se há erros na base de dados resultante, escreva:

  
`gramps -i file1.ged -i file2.gpkg -i ~/db3.gramps -i file4.wft -a check`

- Para especificar explicitamente os formatos no exemplo acima, anexe nomes de ficheiros com opções -f apropriadas:

  
`gramps -i file1.ged -f gedcom -i file2.gpkg -f gramps-pkg -i ~/db3.gramps -f gramps-xml -i file4.wft -f wft -a check`

- Para registar a base de dados resultante de todas as importações, forneça a opção -e (use -f se o nome do ficheiro não permitir que o Gramps adivinhe o formato):

  
`gramps -i file1.ged -i file2.gpkg -e ~/new-package -f gramps-pkg`

- Para gravar quaisquer mensagens de erro do exemplo acima em ficheiros outfile e errfile, execute:

  
`gramps -i file1.ged -i file2.dpkg -e ~/new-package -f gramps-pkg >outfile 2>errfile`

- Para importar três bases de dados e iniciar sessão interactiva com o resultado:

  
`gramps -i file1.ged -i file2.gpkg -i ~/db3.gramps`

- Para abrir uma base de dados e, com base nesses dados, gerar um relatório de cronologia em formato PDF, colocando a saída no ficheiro my_timeline.pdf:

  
`gramps -O 'Family Tree 1' -a report -p name=timeline,off=pdf,of=my_timeline.pdf`

- Para converter a base de dados bsddb para um ficheiro .gramps xml:

  
`gramps -O 'Family Tree 1' -e output.gramps -f gramps-xml`

- Para gerar um sítio web noutro idioma (alemão):

  
`LANGUAGE=de_DE; LANG=de_DE.UTF-8 gramps -O 'Family Tree 1' -a report -p name=navwebpage,target=/../de`

- Finalmente, para começar uma sessão interactiva normal, escreva session type:

  
`gramps`

<span id="Environment variables">

## Variáveis de ambiente

### GRAMPSHOME

- **GRAMPSHOME** - se definida, [substitui o caminho pré-definido](wiki:Gramps_and_Windows#Setting_the_configuration_path) do perfil, permitindo ao utilizador usar uma unidade de rede externa para armazenar dados e preferências. Para utilizadores avançados que usam várias versões do Gramps, definir diferentes GRAMPSHOME é uma forma de evitar interferência entre elas na [pasta de utilizador](wiki:Gramps_Glossary#user_directory). Pode também ser usada para configurar o Gramps para [executar numa unidade portátil](wiki:Run_Gramps_from_a_portable_drive) ou para preparar uma [instalação manual](wiki:Installation). O caminho também pode ser usado para configurar o caminho para uma [árvore de teste](wiki:Gramps_for_Windows_with_MSYS2#Keep_your_GRAMPSHOME_separate) ou [de desenvolvimento](wiki:Getting_started_with_Gramps_development).

Por exemplo,

    GRAMPSHOME=$HOME/familytrees/paternal

### LANG, LANGUAGE, LC_MESSAGES, LC_TIME

- **LANG**, **LANGUAGE**, **LC_MESSAGES**, e **LC_TIME** - são usadas pelo Gramps para determinar que traduções devem ser carregadas. Veja [locale](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap07.html) para uma discussão geral sobre **LANG**, **LC_MESSAGES**, e **LC_TIME**. Note que, em adição aos formatos de data (que são substituídos pelas preferências) **LC_TIME** também define o idioma de palavras usadas em datas, como nomes de meses e dias. E *no contexto de datas*, palavras como *cerca*, *entre*, e *antes*. **LANGUAGE** é uma lista separada por vírgulas de códigos de idiomas (*não idiomas*, embora alguns, como pt_BR ou cn_TW sejam variantes regionais), isto determina uma lista ordenada por preferência de traduções desejadas. Substitui **LANG** mas não **LC_MESSAGES** ou **LC_TIME**.

### GRAMPSI18N

- [$GRAMPSI18N (para o seu idioma)](wiki:Translating_Gramps#.24GRAMPSI18N_.28for_your_locale.29) - LANG assume que as traduções do Gramps estão instaladas globalmente. Se não for o caso, tem de [indicar ao Gramps a pasta](wiki:Translating_Gramps#.24GRAMPSI18N_.28for_your_locale.29) onde se encontram as traduções. Pode ser usado para temporariamente [alterar o idioma dos relatórios](wiki:Howto:Change_the_language_of_reports) a gerar.

Uma tradução é chamada de `gramps.mo`, pode encontrá-las, em Linux, com o comando locate. Por exemplo, se tiver sueco numa pasta

`/home/me/gramps/mo/sv/gramps.mo``, pode dirigir o Gramps para lá com: `  
`GRAMPSI18N=/home/me/gramps/mo LC_ALL=C.UTF-8 LANG="sv" python3 gramps`

### GRAMPSDIR

- A variável de ambiente GRAMPSDIR é o caminho para a sua [pasta do Gramps](wiki:Translating_Gramps#gramps.sh).

### GRAMPS_RESOURCES

- A variável de ambiente GRAMPS_RESOURCES é o caminho para os ficheiros de recursos integrados do Gramps. Só o deve alterar se usar o Gramps do código-fonte ou de um ambiente personalizado. Um indicador de que precisa de mudar esta variável é se receber um dos seguintes erros:
  - *Erro de codificação ao analisar o caminho do recurso*
  - *Falha ao abrir o ficheiro de recursos*
  - *Caminho de recurso {invalid/path/to/resources} inválido*
  - ''Impossível determinar o caminho do recurso

Exemplo [uso](wiki:Linux:Build_from_source#Running_from_a_tarball_release):

`GRAMPS_RESOURCES=/home/username/gramps/branches/maintenance/gramps52/build/t PYTHONPATH=$GRAMPS_RESOURCES:$PYTHONPATH ./gramps`

{{-}}

[Category:Pt PT:Documentation](wiki:Category:Pt_PT:Documentation)
