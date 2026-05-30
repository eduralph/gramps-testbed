---
title: Gramps 6.0 Wiki Manual - FAQ/pt PT
categories:
- Pt PT:Documentation
managed: false
source: wiki-scrape
wiki_revid: 128631
wiki_fetched_at: '2026-05-30T19:47:59Z'
lang: pt PT
---

{{#vardefine:chapter\|A}} {{#vardefine:figure\|0}} Este apêndice contém uma pequena lista de **perguntas frequentes** (FAQ), que são repetidamente colocadas em listas de correio e fóruns do Gramps.

Não está de nenhuma forma completa. Se desejar adicionar perguntas/respostas a esta lista, por favor [junte-se a nós](wiki:Contact#Mailing_lists) e envie as suas sugestões para a lista dos programadores: `gramps-devel@lists.sourceforge.net`.

Considere também espreitar as seguintes categorias na wiki do Gramps:

- [Como é que eu...](wiki::Category:How_do_I...)
- [Tutoriais do Gramps](wiki::Category:Tutorials)

Poderá achar útil rever

- [Glossário do Gramps](wiki::Gramps_Glossary) - visão geral dos termos utilizados no Gramps
- [Glossário de genealogia](wiki::Genealogy_Glossary) - termos genealógicos e seu significado.

<span id="General">

## Geral

</span>

<span id="What is Gramps?">

### O que é o Gramps

</span> O Gramps é um conjunto de ferramentas de genealogia pessoal que permitem armazenar, editar e pesquisar dados genealógicos. Ajuda a resolver as complexas relações entre várias pessoas, lugares e eventos. O Gramps oferece muitas maneiras diferentes de registar os muitos detalhes da vida de um indivíduo. Toda a sua pesquisa é mantida organizada. Veja [Acerca](wiki:Gramps:About).

<span id="Where do I get it and how much does it cost?">

### Onde o obtenho e quanto custa?

</span> O Gramps pode ser \[\[Installation\|instalado\] sem custos. É um projecto de código sob a GNU General Public License. Tem acesso total ao código-fonte e permissão para distribuir o programa e o código-fonte livremente.

<span id="Do I need to register as a user to use Gramps, I am not a programmer?">

### Preciso de me registar como utilizador do Gramps, não sou um programador?

</span> Não, o registo só é necessário se quiser enviar um relatório de erro (ou pedido de funcionalidade) ou editar/escrever uma página wiki.

Não necessita de capacidades de programação para isso.

<span id="Does Gramps exist in other languages?">

### O Gramps existe noutros idiomas?

</span> Sim, à data de lançamento do Gramps foi traduzido para 28 idiomas, veja [Gramps translations](wiki:Gramps_translations).

<span id="How do I keep backups?">

### Como é que faço salvaguardas?

</span> A salvaguarda automática é uma funcionalidade que protege os seus dados genealógicos no Gramps. Foi automatizado em 2018). O intervalo, o caminho da salvaguarda e a opção de a fazer ao sair do Gramps estão no separador do diálogo . Adicionalmente, pode fazer uma salvaguarda manual no menu .

É extremamente importante manter salvaguardas dos seus dados, e mantê-las a bom recato. O Gramps tem um formato de ficheiro portátil, pequeno e humanamente legível, identificado pela extensão `.gramps`. Veja a secção "[Salvaguarda da árvore genealógica](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/pt_PT#Backing_up_a_Family_Tree)" no manual. É também importante ter noção do que [foi omitido na salvaguarda do Gramps](wiki:Template:Backup_Omissions/pt_PT).

Pode copiar esta salvaguarda de tempos a tempos para uma localização mais segura (<abbr title="exempli gratia - frase latina significando ''por exemplo''">e.g.</abbr>, uma pen USB). \[Nota: os ficheiros `.gramps` são sempre comprimidos. Clicá-los abrirá o Gramps. Para ver o código XML, seleccione o arquivo `.gramps` e abra-o com um utilitário de descompressão (como ark, gunzip, 7-zip), após o que pode extrair o ficheiro de texto XML, humanamente legível, veja mais [detalhes](wiki:Generate_XML#How_do_I_uncompress_the_file?).

O Gramps faz uma salvaguarda oculta rápida para permitir o restauro, se se encontrar um erro. Se o pacote correcto estiver instalado, poderá usar um sistema de controlo de versão.

Outro método é copiar a pasta oculta *`/.gramps`*. Esta situa-se na sua [pasta de utilizador](wiki:Gramps_6.0_Wiki_Manual_-_User_Directory). Salvaguardar esta pasta significa salvaguardar as suas bases de dados e repectivas revisões. Em Windows 10 está sob *`/Users/`<utilizador>`/AppData/Roaming/gramps`*.

**Não mantenha salvaguardas em formato GEDCOM**. Nem toda a informação do Gramps pode ser escrita em formato GEDCOM. Logo, uma operação de exportação/importação do Gramps para GEDCOM e re-importada para o Gramps, significa que **perde** [dados](wiki:Gramps_and_GEDCOM). Use o formato de ficheiro `.gramps` para salvaguardas!

**Não mantenha salvaguardas em formato GRDB**. GRDB é uma base de dados, o que pode variar de computador para computador (a leitura, não o trabalho noutro computador). Pequenas alterações num ficheiro GRDB também são impossíveis de reparar. Use o formato de ficheiro `.gramps` para salvaguardas!

<span id="Does Gramps support Unicode fonts?">

### O Gramps suporta letras Unicode?

</span>

Em particular, suporta fontes Unicode não romanas? Sim. O Gramps funciona internamente com Unicode (UTF-8), para que todos os alfabetos possam ser usados em todos os campos de entrada.

Não há assistência especial para inserir símbolos Unicode que não estejam directamente rotulados no teclado. Pode encontrar ajuda para inserir [caracteres pré-compostos](https://wikipedia.org/wiki/Precomposed_character) com acentos fora do programa. Poderá achar os [teclados multilíngue virtuais da Lexilogos](https://www.lexilogos.com/keyboard/latin_alphabet.htm) úteis.

Todos os relatórios suportam integralmente Unicode, [embora para PDF/PS](#Why_are_non-Latin_characters_displayed_as_garbage_in_PDF.2FPS_reports.3F) precise de trabalhar com o gnome-print ou o [LibreOffice](http://www.documentfoundation.org/download/).

<span id="Installation">

## Instalação

</span>

<span id="What is needed to install Gramps under Linux, Solaris, or FreeBSD?">

### O que é preciso para instalar o Gramps sob Linux, Solaris, ou FreeBSD?

</span> O Gramps é uma aplicação [GTK](http://en.wikipedia.org/wiki/Gtk). Necessita das bibliotecas [PyGObject](http://en.wikipedia.org/wiki/PyGObject) instaladas no seu sistema. Desde que essas bibliotecas estejam instaladas, o Gramps deverá funcionar em GNOME, KDE ou em qualquer distribuição. Se as ligações do GNOME para Python estiverem instaladas no sistema, o Gramps terá funcionalidades adicionais. Verifique se atende às recomendações do projecto Gramps em relação à versão GTK a usar.

<span id="Does Gramps work on Windows?">

### O Gramps funciona em Windows?

</span>

Sim, o Windows é uma plataforma suportada pela comunidade Gramps.

Pode [transferir](wiki:Download#MS_Windows) o [GrampsAIO](wiki:GrampsAIO)(All In One Gramps Software Bundle for Windows).

Faremos o nosso melhor para resolver quaisquer problemas relacionados com o Windows relatados. Ver [aqui](wiki:Contact).

<span id="Does Gramps work on the Mac?">

### O Gramps funciona em Mac?

</span>

Sim, o macOS é uma plataforma suportada pela comunidade Gramps.

Pode [transferir](wiki:Download#macOS) a versão macOS.

Faremos o nosso melhor para resolver quaisquer problemas relacionados com o macOS relatados. Ver [aqui](wiki:Contact).

Ver [aqui](wiki:Mac_OS_X:Application_package).

<span id="Does Gramps work on my mobile device?">

### O Gramps funciona em dispositivos móveis?

</span>

A resposta curta é não, o Gramps não pode ser instalado no seu telemóvel ou tablet( [Google Android](https://en.wikipedia.org/wiki/Android_(operating_system)) ou [Apple iOS](https://wikipedia.org/wiki/IOS) )

Uma resposta mais técnica é 'sim', mas ***não**'' como uma aplicação***nativa**''. Usar o Gramps exigiria uma de:

:# instale uma versão dos sistemas operacionais Linux no dispositivo móvel junto com todos os pacotes de suporte;

:# configurar um servidor local ou em rede com uma versão de [Gramps designed for collaboration](wiki:Web_Solutions_for_Gramps#Interactive_web_apps) (tal como o [Gramps Web](wiki:Web_Solutions_for_Gramps#GrampsWeb)), e trabalhar com o Gramps a partir do navegador.

<span id="Does Gramps work on my Google Chromebook?">

### O Gramps funciona em Google Chromebook?

</span>

Sim, mas com alguns problemas, pode instalar o Gramps no seu [Chromebook](https://en.wikipedia.org/wiki/Chromebook) ([ChromeOS](https://en.wikipedia.org/wiki/ChromeOS)).

Veja:

- Drag and Drop Not Working in Crostini\[Linux\] num Pixelbook

<span id="What are the Minimum Specs to run Gramps?">

### Quais são as especificações mínimas para executar o Gramps?

</span> Recomendamos pelo menos uma resolução de vídeo 1920x1080. Os primeiros requisitos de memória para Gramps foram reduzidos, eram bastante altos. Começando com o Gramps 3.0, o programa poderia ser executado com bastante eficiência num sistema de 256 MB, mantendo consideravelmente mais pessoas. Um sistema com 512 MB deve ter capacidade para cerca de 200.000 pessoas. No entanto, os requisitos de espaço em disco para bases de dados são consideravelmente maiores, com uma base de dados típica tendo vários megabytes de tamanho. Para 120.000 pessoas deve considerar pelo menos 530 MB para o banco de dados. As imagens são armazenadas no disco separadamente, portanto, se foem muitas, é necessário um disco rígido grande.

<span id="How do I upgrade Gramps?">

### Como é que actualizo o Gramps?

</span>

As actualizações começam com a criação de [salvaguardas](wiki:How_to_make_a_backup) de TODAS as suas árvores. Mas, além disso, consulte a lista [Omissão de salvaguardas](wiki:Template:_Backup_Omissions/pt_PT) para determinar os itens de adições que pode querer arquivar (os itens mais importantes são anotar o caminho da base de dados, o caminho da salvaguarda e o caminho relativo da multimédia no diálogo Preferências. Se não conseguir encontrar os seus dados após uma actualização, ficará muito infeliz).

Uma vez que as salvaguardas estejam armazenadas em segurança, a abordagem mais segura para a actualização é: transferir o instalador mais recente, desinstalar o Gramps existente e reinstalar a partir do instalador.

Inicie o Gramps (o primeiro arranque será lento, o Gramps tem de recompilar e armazenar em memória os ficheiros de código fonte Python) Em “Editar -\> Preferências...”, insira o seu caminho de multimédia no separador Geral, o caminho da base de dados no separador Árvore genealógica, o caminho das salvaguardas no separador Árvore genealógica. Tente em seguida carregar a árvore através do menu Árvores genealógicas.

Se se tratar de uma actualização “menor” (contendo apenas correcções de erros), a actualização deve encontrar a sua configuração e as suas extensões sem qualquer esforço adicional. Se for uma actualização de núcleo, terá de repor todas as suas personalizações de configuração e transferir as extensões compatíveis.

<span id="Preferences">

## Preferências

</span>

<span id="Can I change the dates in reports to 'day month year'?">

### Posso alterar as datas em relatórios para "dia mês ano"?

</span>

Sim, em , separador altere o do Granps para o formato desejado (e.g. AAAA-MM-DD ou dia mês ano), e crie o relatório. Será usada a sua escolha global de formato de data.

<span id="Is there a Dark Mode?">

### Há um tema escuro?

</span> Só instalando a [extensão Tema](wiki:Addon:ThemePreferences), que adiciona um separador às . Esta extensão é útil se tiver problemas de sensibilidade à luz e/ou se preferir um modo escuro para uso noturno ou em geral. No separador Tema, pode activar a opção "", disponível na maioria dos temas. Também pode aumentar o tamanho da letra para cansar menos a vista.

<span id="Collaboration-Portability">

## Colaboração - Portabilidade

</span>

<span id="Is Gramps compatible with other genealogical software?">

### O Gramps é compatível com outros programas de genealogia?

</span>

O Gramps faz todos os esforços para manter a compatibilidade com a norma [GEDCOM](wiki:GEDCOM), o padrão internacional para gravar informação genealógica. Temos filtros de importação e exportação que permitem ao Gramps ler e escrever ficheiros GEDCOM.

É importante compreender que a norma GEDCOM está mal implementada -- praticamente todos os programas genealógicos têm o seu próprio “sabor” de GEDCOM. À medida que vamos conhecendo novas variantes, os filtros de importação/exportação podem ser criados muito rapidamente. No entanto, para descobrir as variantes desconhecidas são necessários [comentários dos utilizadores](wiki:Contact). Por favor, sinta-se à vontade para nos informar sobre qualquer versão GEDCOM não suportada pelo Gramps, e nós faremos o nosso melhor para adicioná-la!

Há um artigo específico nesta wiki que discute o [Gramps o e a norma GEDCOM](wiki:Gramps_o_e_a_norma_GEDCOM). Há tamb+em um artigo sobre as idiossincrasias dos [dialectos GEDCOM ao importar de outros programas](wiki:Import_from_another_genealogy_program).

<span id="Can Gramps read files created by other genealogy programs?">

### O Gramps consegue ler ficheiros criados por outros programas de genealogia?

</span> Sim, pode ler ficheiros GEDCOM criados por outros programas de genealogia.

- [Veja acima.](wiki:Gramps_6.0_Wiki_Manual_-_FAQ/pt_PT#Is_Gramps_compatible_with_other_genealogical_software.3F)

<span id="Can Gramps write files readable by other genealogy programs?">

### O Gramps pode criar ficheiros legíveis por outros programas de genealogia?

</span> Sim, pode escrever ficheiros GEDCOM criados por outros programas de genealogia.

- [Veja acima.](wiki:Gramps_6.0_Wiki_Manual_-_FAQ/pt_PT#Is_Gramps_compatible_with_other_genealogical_software.3F)

<span id="What standards does Gramps support?">

### Que padrões é que o Gramps suporta?

</span>

O bom dos padrões é que nunca escasseiam. O Gramps foi testado para suportar os seguintes sabores de GEDCOM 5.6.0, Brother's Keeper, Family Origins, Family Tree Maker, Ftree, GeneWeb, Legacy, Personal Ancestral File, Pro-Gen, Reunion, e Visual Genealogie.

<span id="How do I import data from another genealogy program into Gramps?">

### Como é importo dados de outros programas de genealogia para o Gramps?

</span>

A melhor maneira é criar uma nova árvore genealógica e seleccionar a opção de importação no menu Ficheiro. Aqui, seleccione o GEDCOM que gerou com o outro programa e importe-o.

<span id="Can I install Gramps on a Linux Web Server and use it via a web browser?">

### Posso instalar o Gramps num servidor web Linux e utilizá-lo via navegador web?

</span>

Isto permitiria que as minhas relações em todo o mundo lhe acedessem e actualizassem.

Embora o Gramps possa gerar sítios web, não fornece um ambiente web que permita a edição. Se isto é um requisito, a [GeneWeb](http://geneweb.org) ou o [webtrees](http://www.webtrees.net/) são programas mais susceptíveis de preencher as suas necessidades. Experimente também o nosso programa em teste, o [gramps-online](https://github.com/gramps-project/gramps-online). No entanto, faça a si mesmo as seguintes perguntas:

1.  Quero realmente que parentes ou outras pessoas editem directamente a minha base de dados de genealogia?
2.  Confio implicitamente, sem verificação, em quaisquer dados que as pessoas possam inserir?
3.  Essas pessoas têm a mesma compreensão da boa prática genealógica que eu?

Uma abordagem melhor poderá ser fornecer um formulário web que permita que outras pessoas insiram dados, que são então mantidos para exame posterior. Pode então decidir se as informações devem ser ou não inseridas na base de dados.

Também pode considerar os efeitos de um possível tempo de inactividade do seu sítio web, se não puder pagar um serviço de hospedagem de qualidade na web.

<span id="Reports">

## Relatórios

</span>

<span id="Can Gramps print a genealogical tree for my family?">

### O Gramps pode imprimir uma árvore genealógica da minha família?

</span>

Sim. Pessoas diferentes têm ideias diferentes sobre o que é uma árvore genealógica. Alguns pensam que é um gráfico que parte de um antepassado distante e enumera todos os seus descendentes e respectivas famílias. Outros pensam que deve ser um gráfico que parte da pessoa para trás no tempo, enumerando os antepassados e as suas famílias. Outras ainda pensam numa tabela, num relatório de texto, etc.

O Gramps pode produzir qualquer um dos itens acima e muitos outros gráficos e relatórios diferentes. Além disso, a arquitectura de extensões permite aos utilizadores criar as suas próprias extensões, que podem ser novos relatórios, gráficos ou ferramentas de pesquisa.

<span id="How can the relationship between people on the tree be determined?">

### Como é que se pode determinar o parentesco entre indivíduos na árvore?

</span>

Alguns utilizadores estão interessados em mostrar apenas as relações genéticas de ascendentes ou descendentes directos. Outros estão também interessados nas linhas colaterais (primos!) ou nos sogros imediatos. E ainda outros estão interessados em saber como as ligações mais indirectas influenciam uma comunidade.

Assim, o Gramps oferece uma variedade de ferramentas, relatórios e métodos em constante expansão para determinar como as pessoas estão ligadas na base de dados de uma dada árvore. Após uma discussão na [lista de correio dos utilizadores](wiki:Contact#Mailing_lists), as sugestões apresentadas foram coligidas e desenvolvidas no artigo "[How to find the relationship between people](wiki:How_to_find_the_relationship_between_people)" na categoria "[Como é que eu...](wiki::Category:How_do_I...)" da wiki.

<span id="In what formats can Gramps output its reports?">

### Em que formatos é que o Gramps imprime os relatórios?

</span>

Os relatórios de texto estão disponíveis em formatp HTML, PDF, ODT, LaTeX, e RTF. Os relatórios gráficos (árvores e diagramas) estão disponíveis em formato PostScript, PDF, SVG, ODS, e [GraphViz](wiki:Output_formats#Graphviz).

<span id="How can I change the default language in reports?">

### Como é que altero o idioma pré-definido nos relatórios?

</span>

Os relatórios estão no idioma da sua instalação. A maioria dos relatórios permite-lhe seleccionar o idioma de saída para procurar a opção para seleccionar a tradução a usar para o relatório. Pode alterá-la instalando pacotes de idiomas extra, consulte [Howto:Mudar o idioma dos relatórios](wiki:Howto:Mudar_o_idioma_dos_relatórios).

<span id="Is Gramps compatible with the Internet?">

### O Gramps é compatível com a Internet?

</span> Sim, de várias maneiras. Existem recursos para referenciar dados externos ligados, ferramentas de arquivo para os recolher para armazenamento interno e, embora o Gramps esteja projectado para ser uma aplicação local, foi criado um rico conjunto de ferramentas para publicar algumas ou todas as suas pesquisas na web.

O Gramps podem armazenar endereços da web e direccionar o seu navegador. Pode importar dados que transfere da Internet. Pode exportar dados para envio pela Internet. O Gramps está familiarizado com os formatos de ficheiro padrão amplamente utilizados na Internet (<abbr title=" exempli gratia - frase latina que significa ''por exemplo''">e.g.</abbr> JPEG, PNG e imagens GIF, ficheiros de som MP3, OGG e WAV, QuickTime, MPEG e ficheiros de filmes AVI, etc.). Se o seu navegador estiver configurado para aceder a outros tipos de ficheiro, o Gramps herdará essa capacidade.

Existem ferramentas adicionais para procurar ajuda na procura de registos em fontes em rede. É uma variedade crescente de outros [soluções web para o Gramps](wiki:Web_Solutions_for_Gramps).

Os relatórios podem opcionalmente gerar conteúdo em formatos adequados para publicação como páginas web ou mesmo como sítios completos. E existem versões de desenvolvimento que convertem o Gramps em sistemas de gestão de conteúdo genealógico em rede. Alguns são sistemas de apresentação dinâmicos para publicação de pesquisas, outros oferecem edição colaborativa limitada.

#### Veja também

- [Soluções web para o Gramps](wiki:Soluções_web_para_o_Gramps)

<span id="Can I create custom reports/filters/whatever?">

### Posso criar relatórios/filtros/algo personalizados?

</span>

Sim. Existem muitos níveis de personalização. Um deles é criar ou modificar os modelos usados para os relatórios. Isto oferece algum controlo sobre as letras, cores e alguma disposição dos relatórios. Também pode usar controlos Gramps nos diálogos do relatório para saber que conteúdo deve ser usado para um relatório específico. Além disso, tem a capacidade de criar os seus próprios filtros - o que é útil na selecção de indivíduos com base em critérios definidos por si. Pode combinar esses filtros para criar filtros novos e mais complexos. Finalmente, tem uma opção para criar as suas próprias extensões. Podem ser novos relatórios, ferramentas de pesquisa, filtros de importação/exportação, etc. Isto pressupõe algum conhecimento de programação em Python.

<span id="Why are non-Latin characters displayed as garbage in PDF/PS reports?">

### Porque é que caracteres não-Latim são mostrados como lixo em relatórios PDF/PS?

</span>

Esta é uma limitação das fontes integradas dos formatos PS e PDF. Para imprimir texto não latino, use Imprimir... no menu de selecção de formato no diálogo do relatório. Isto força o uso do motor `gnome-print`, que suporta criação de PS e PDF, bem como impressão directa (nota: talvez seja necessário instalar o gnome-print separadamente, não é necessário ao Gramps).

Se tiver apenas texto em latim, a opção PDF produzirá um PDF menor comparado ao criado pelo gnome-print, simplesmente porque nenhuma informação da letra será incorporada.

<span id="I would like to contribute to Gramps by writing my favorite report. How do I do that?">

### Gostava de ajudar o Gramps programando o meu relatório favorito. Como é que o faço?

</span>

TA maneira mais fácil de contribuir para relatórios, filtros, ferramentas, etc. é copiar um relatório, filtro ou ferramenta Gramps existente. Se consegue criar o que quiser modificando o código existente, óptimo! Se a sua ideia não se encaixa na lógica de qualquer ferramenta Gramps existente, terá de escrever a sua própria extensão do zero. Há ajuda disponível no [portal dos programadores](wiki:Portal:_Developers), ou na [lista de correio dos programadores](wiki:Contact): gramps-devel@lists.sourceforge.net.

Para testar seu trabalho em curso, grave a sua extensão na pasta `$HOME/.gramps/plugins` e deverá assim ser encontrado e importado no arranque. A extensão correctamente escrita regista-se no Gramps, cria um item de menu, e assim por diante.

Se está contente com o seu trabalho e gostaria de contribuir com o seu código para o projecto Gramps, convidamo-lo a fazê-lo, juntando-se a nós e contactando-nos na lista de correio gramps-devel@lists.sourceforge.net.

<span id="Database - Gramps file formats">

## Base de dados - formatos de ficheiro do Gramps

</span>

O formato de ficheiro pré-definido é o [Gramps XML](wiki:Gramps_XML), que é utilizado para exportações, salvaguardas e importações, e preserva os dados genealógicos inseridos sem perda de dados, em comparação com o formato GEDCOM.

<span id="What is the maximum database size (bytes) Gramps can handle?">

### Qual é o tamanho máximo da base de dados (bytes) que o Gramps pode gerir?

</span>

O Gramps não tem limites rígidos para o tamanho da base de dados que pode manipular. A partir da versão 2.0.0, o Gramps já não carrega todos os dados na memória, o que lhe permite trabalhar com uma base de dados muito maior do que antes. Na realidade, no entanto, existem limites práticos. Os principais factores limitantes são a memória disponível no sistema e o tamanho da memória utilizada para o acesso à base de dados BSDDB. Com os tamanhos de memória comuns hoje em dia, o Gramps não deve ter problemas em usar bases de dados com [milhões de indivíduos](wiki:Gramps_Performance#JohnBoyTheGreat_2019-12.2C_version_6.0.1).

<span id="How many people can Gramps database handle?">

### Quantos indivíduos pode a base de dados do Gramps gerir?

</span>

Veja acima. De novo, dependendo da memória e espaço em disco disponíveis, veja os [Gramps Performance](wiki:Gramps_Performance).

<span id="My database is really big. Is there a way around loading all the data into memory?">

### A minha base de dados é enorme. Há alguma forma de contornar o carregamento dos dados em memória?

</span>

A partir da versão 2.0.0, o Gramps já não carrega todos os dados em memória, o que permite que funcione com uma base de dados muito maior do que antes. O formato de ficheiro utilizado é `.grdb`, que significa <i>base de dados Gramps</i>.

<span id="Can I run Gramps from a database on a NFS share?">

### Posso executar o Gramps a partir de uma base de dados numa partilha NFS?

</span>

Sim, pode editar uma base de dados Gramps numa partilha [NFS(NetworkFile System)](https://en.wikipedia.org/wiki/Network_File_System).

\<span id="What does "portable" mean?"\>

### O que significa "portátil"?

</span>

Uma base de dados Gramps 3 (e qualquer ficheiro .grdb) é muito dependente das versões do programa que a criaram. Por exemplo, não se pode simplesmente mover os dados do Gramps nestes formatos para um sistema operativo diferente (ou mesmo para uma versão diferente de um sistema operativo) e esperar que seja capaz de ler os seus dados. Os dados não são “portáteis”. Portanto, não pode confiar apenas nas salvaguardas destes formatos, também deve exportar ocasionalmente para um formato que seja portátil. Existem dois formatos portáteis possíveis: GEDCOM e Gramps XML (.gramps ou .gpkg). Apenas o Gramps XML é recomendado, uma vez que guarda fielmente todos os seus dados.

<span id="Why is the database format (GRDB) not portable?">

### Porque é que o formato da base de dados (GRDB) não é portátil?

</span>

O maior problema com a portabilidade do Gramps reside nas "transacções". Com o Gramps 2.2, adicionámos suporte para transacções atómicas para proteger os dados. Com transacções atómicas, são submetidas múltiplas alterações como uma única unidade. Ou todas as mudanças resultam, ou nenhuma das mudanças resulta. Nunca fica com um conjunto parcial de mudanças. Um benefício colateral do uso de transacções é que o acesso à base de dados (leituras e gravações) é mais rápido.

O problema com as transações (pelo menos com BSDDB) é que não permitem que todos os dados sejam armazenados num único ficheiro. São necessários diários de alterações para acompanhar as coisas. Estes diários são mantidos numa pasta DB Environment. Precisamos de uma pasta separada para cada fucheiro, caso contrário, diários podem interferir uns com os outros.

Na 2.2, mantemos os diários sob a pasta `~/.gramps/`, criando uma pasta exclusiva para cada base de dados. O problema é que o ficheiro GRDB precisa dos diários, que estão numa pasta diferente.

Copiar o ficheiro GRDB é copiar apenas uma parte da base de dados.

<span id="Does Gramps have an Example Tree?">

### O Gramps tem alguma árvore de exemplo?

</span>

Sim, tem. Vários exemplos de bases de dados de árvores genealógicas são [incluídos na maioria das instalações de Gramps e podem ser importados](wiki:Example.gramps#Load_example.gramps) para percorrer os tutoriais e explorar em segurança ferramentas ou funcionalidades.

O exemplo de árvore genealógica (ficheiro *'`example.gramps`*) almeja o ideal de ter pelo menos um exemplo de cada uma das coisas obscuras que o Gramps faz. Pode importar o exemplo para uma árvore em branco e, em seguida, cometer erros exploratórios destrutivos com segurança numa base de dados funcional e descartável. E quando suspeitar que descobriu um problema (também conhecido como 'bug') no Gramps, pode primeiro tentar a mesma operação com a árvore genealógica de exemplo para comprovar a sua existência e depois [preencher um relatório de erro](wiki:How_to_create_a_good_bug_report).

- O [artigo da wiki <code>Example.gramps</code>](wiki:Example.gramps) descreve onde encontrar o ficheiro de exemplo de árvore genealógica, como utilizá-lo, e sugere alguns ficheiros alternativos.

<span id="Bugs and requests">

## Problemas e pedidos

</span>

<span id="What do I do if I have found a bug?">

### O que é que faço se encontrar um erro?

</span>

Pode [preencher um relatório de erro](wiki:Using_the_bug_tracker).

Um bom relatório de erro incluiris:

1.  a versão do Gramps (disponível em Ajuda → Acerca...).
2.  Idioma em que estava a executar o Gramps (disponível com o comando de terminal `echo $LANG`).
3.  Sintomas de que isto é realmente um erro.
4.  Quaisquer mensagens de erro, avisos, etc, que surgiram no terminal ou numa janela separada de rastreio.

A maioria dos problemas pode ser reparada rapidamente, desde que haja informação suficiente. Para tal, por favor acompanhe a evolução dos seus relatórios. Assim teremos uma forma de o contactarmos, caso necessitemos de mais informação.

<span id="Requests">

### Pedidos

</span>

- O Gramps devia ser uma aplicação de tipo ....

É óbvio que o Gramps tem de ser uma aplicação cliente-servidor/baseada na web/PHP/weblog/Javascript/C++/distributed/KDE/Motif/Tcl/Win32/C#/Diga-Qual. Quando é que isto vai acontecer?

A maneira mais segura de ver isso acontecer é fazê-lo. Como o Gramps é gratuito/de código aberto, ninguém impede que pegue no código e continue o seu desenvolvimento na direcção que achar melhor. Ao fazê-lo, pode considerar dar outro nome ao seu novo projecto para evitar confusão com o desenvolvimento contínuo do Gramps. Se desejar que o projecto Gramps forneça aconselhamento, experiência, filtros, etc., teremos prazer em cooperar com o seu novo projecto, para garantir a compatibilidade ou opções de importação/exportação para o seu novo formato.

Se, no entanto, gostaria que o projecto Gramps adoptasse a sua estratégia, teria de convencer os programadores do Gramps de que sua estratégia é boa para o Gramps e superior à actual estratégia de desenvolvimento.

<span id="Adding to and editing my database">

## Adicionar a e editar a base de dados

</span>

<span id="What is the difference between a residence and an address?">

### Qual a diferença entre uma residência e um endereço?

</span>

Uma residência é um local onde alguém viveu por um dado período de tempo. Um endereço é o nome de uma residência formatado da forma esperada pelo sistema postal. Portanto, cada residência também pode ter um endereço, se for útil. Ver também: [Porquê um evento de residência e não um endereço?](wiki:Why_residence_event_and_not_Address%3F)

<span id="How do I change the order of children?">

### Como é que altero a ordem dos filhos?

</span>

Os filhos podem ser movidos no [editor de famílias](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_1/pt_PT#Editing_information_about_relationships), separador [Filhos](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/pt_PT#Children) por [arrastar e largar](http://en.wikipedia.org/wiki/Drag-and-drop) ou usando os botóes e .

<span id="How do I change the order of spouses?">

### Como é que altero a ordem dos cônjuges?

</span>

Os cônjuges (também listados como Parentescos ou como Família em diferentes partes da wiki) podem ser reordenados a partir do[Categoria Parentescos](wiki:Gramps_6.0_Wiki_Manual_-_Categories/pt_PT#Reorder_Relationships_dialog) clicando em na barra de ferramentas, ou seleccionando . Em alternativa, o separador Eventos lista uma família dobrável para cada cônjuge ao editar um indivíduo. Quando há múltiplas famílias, seleccionar uma delas e clicar nos botões acima ou abaixo sob os cabeçalhos dos separadores reordenará a família seleccionada.

<span id="How do I add an additional spouse?">

### Como é que adiciono outro cônjuge?

</span> See [Add a spouse](wiki:Add_a_spouse)

<span id="How do I remove a spouse?">

### 

</span>

Remover um cônjuge (sem eliminar o indivíduo da árvore) requer apenas um único clique no diálogo [Editar família](wiki:Gramps_Glossary#family). Basta clicar em "Remover indivíduo como mãe/pai" (-) logo acima do nome do cônjuge.

‘’O nome, nascimento e óbito serão limpos e os botões "Adicionar um novo indivíduo como mãe/pai" (+) e "Seleccionar um indivíduo como mãe/pai" substituirão os botões (-) e "Editar".

Para remover completamente o cônjuge da árvore, seleccione o indivíduo na categoria Indivíduos e clique no botão "Eliminar o indivíduo seleccionado" (-) na barra de ferramentas. Verá um diálogo de confirmação. Confirme, clicando em "Eliminar indivíduo".

*O indivíduo será removido de todas as famílias em que é cônjuge ou filho. Os eventos, as citações, as notas e os meios de comunicação anexados ficarão órfãos. Os outros objectos secundários serão eliminados juntamente com o seu indivíduo.*

<span id="How do you add photos to an item?">

### 

</span> Veja [Adicionar fotografias e outros objectos multimédia](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_brief#Adding_photos_and_other_media_objects).

<span id="How do you find unused media?">

### Como é que encontro multimédia não usada?

</span> Multimédia que não foi associada a qualquer objecto pode ser encontrada criando um [filtro personalizado](wiki:Gramps_6.0_Wiki_Manual_-_Filters/pt_PT#Custom_Filters) na categoria Multimédia. Use a regra [Objectos multimédia com <n> referências](wiki:Gramps_6.0_Wiki_Manual_-_Filters/pt_PT#Media_objects_with_a_reference_count_of_.3Ccount.3E) para localizar multimédia com menos de uma referência.

<span id="How can I publish a genealogy web site with Gramps?">

### Como é que publico um sítio de genealogia com o Gramps

</span>

<span id="How can I publish web sites generated by GRAMPS?"> </span>

O Gramps tem múltiplas opções no menu de relatórios para criar páginas web com base na sua árvore.

O tutorial [Como fazer: criar um sítio web de genealogia com o Gramps](wiki:Howto:_Make_a_genealogy_website_with_Gramps) descreve a utilização do [relatório web narrativo](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7/pt_PT#Narrated_Web_Site). Aí, saberá como gerar um sítio web à volta de um conjunto de indivíduos na sua árvore genealógica.

Uma vez gerado, pode enviar os ficheiros a um serviço de alojamento. Também os pode distribuir numa unidade amovível, ou CD.

<span id="See Also">

#### Veja também

</span>

- [Web Solutions for Gramps](wiki:Web_Solutions_for_Gramps)

<!-- -->

- Ou também pode instalar relatórios complementares de terceiros para criar outros estilos de conteúdo da web. Veja [lista de extensões](wiki:6.0_Addons#Addon_List).

{{-}} <span id="The FAQ does not solve my problem.">

## As FAQ não resolvem o meu problema

</span>

Sinta-se à vontade para entrar em contato connosco através de qualquer um dos métodos oficiais listados na página “[Contact](wiki:Contact)”. {{-}}

[Category:Pt PT:Documentation](wiki:Category:Pt_PT:Documentation)
