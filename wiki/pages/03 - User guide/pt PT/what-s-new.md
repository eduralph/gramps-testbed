---
title: Gramps 6.0 Wiki Manual - What's new?/pt PT
categories:
- Pt PT:Documentation
managed: false
source: wiki-scrape
wiki_revid: 112809
wiki_fetched_at: '2026-05-30T19:52:55Z'
lang: pt PT
---

{{#vardefine:chapter\|1}} {{#vardefine:figure\|0}}

Esta secção oferece uma visão geral das alterações feitas desde a versão 5.1 do Gramps. É uma versão de "melhorias". Pode incluir novas funcionalidades, assim como reparações de erros. Estas alterações são também descritas em detalhe neste manual. Os utilizadores a actualizar de versões anteriores são encorajados a rever esta secção em [manuais](wiki:User_manual) anteriores, para garantir que usufruem das novas funcionalidades da versão 5.2. Procurem pelo raio "" nas secções marcadas.

<span id="Preliminary change list">

### Lista preliminar de alterações

</span> Uma vez que a documentação do Gramps é criada por voluntários, é publicada incrementalmente *após* o lançamento público. Para itens-chave seleccionados, a documentação está marcada com "</small>" para facilitar a procura. Os colaboradores da wiki escrevem não só da sua experiência a explorar funcionalidades, mas também procurando objectivos de desenvolvimento, pedidos de funcionalidades, relatórios de estado e notas de Pull Request. Se também gosta de explorar, os anúncios abaixo estão parcialmente ligados a esses documentos de referência. Explore à vontade e partilhe a sua experiência para ajudar outros.

<span id="From the Announcements">

#### Dos anúncios

</span>

Da secção **[Announcements](https://gramps.discourse.group/c/gramps-announce/5)** do **[Gramps community support Discourse forum](https://gramps.discourse.group/t/welcome-to-the-gramps-discourse-forum/7)**:

- [6.0.0](https://github.com/gramps-project/gramps/releases/tag/v6.0.0) - a new major release, released 2025-03-19.
- [v6.0.0-rc2](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-rc2) - an experimental pre-release, released 2025-03-16
- [v6.0.0-rc1](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-rc1) - an experimental pre-release, released 2025-03-03
- [v6.0.0-beta2](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-beta2) - an experimental pre-release, released 2025-02-13
- [v6.0.0-beta1](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-beta1) - an experimental pre-release, released 2025-02-05

Discussões entre os programadores sobre futuras versões 6.0:

- [Understanding Gramps 6.0](https://gramps.discourse.group/t/understanding-gramps-6-0/6652) By Doug Blank - Development - Roadmap

<!-- -->

- Toolbar usability improvement shows text under icons by default.[1](https://gramps.discourse.group/t/gramps-6-0-defaults/6990/3)

<span id="Before you upgrade">

## Antes de actualizar

</span>

***Antes*** de actualizar, certifique-se de que os dados da sua árvore genealógica estão seguros. A melhor forma de o fazer é, provavelmente:

1.  iniciar a versão actual do Gramps (Gramps 4.2/5.0/5.1/5.2);
2.  abrir a sua árvore genealógica;
3.  salvaguardar a árvore em formato *gramps xml*, ou *gramps xml package* (o formato *gramps xml package* inclui imagens e outra multimédia associada à sua árvore); salvaguarde a árvore via menu ;
4.  fechar esta árvore e repetir o processo para quaisquer outras que tenha;
5.  manter os ficheiros resultantes em local seguro, idealmente numa unidade externa.

Para mais informação, por favor reveja o artigo [Salvaguardar uma árvore genealógica](wiki:Gramps_5.2_Wiki_Manual_-_Manage_Family_Trees#Backing_up_a_Family_Tree). Note [aquilo que será incluído numa salvaguarda](wiki:Template:Backup_Omissions).

Depois de proteger adequadamente os seus dados, instale o Gramps , usando o processo regular de instalação do seu sistema operativo. Na maioria dos casos, isto garantirá que a nova instalação do Gramps não entre em conflito com a versão mais antiga. No entanto, pode ser mais seguro desinstalar as versões anteriores do Gramps antes de instalar a nova versão, ou certifique-se de que instala o novo Gramps num local diferente. Isto é sempre necessário se estiver a instalar a partir do código-fonte. Para obter mais informações sobre como instalar o Gramps, consulte [Transferir o novo Gramps](wiki:Download)

Depois de instalar o novo Gramps, pode abrir as suas árvores genealógicas existentes e continuar o trabalho. No caso de ter problemas (por exemplo, após uma actualização completa do sistema), importe as salvaguardas criadas acima para recriar sua árvore (ou árvores) genealógica.

<span id="Further information">

## Mais informação

</span>

<span id="Miscellaneous">

### Diversas

</span>

<span id="Localization">

### Localização

</span>

- Traduções actualizadas

<span id=Third-Party Addons>

#### Extensões de terceiros

</span>

- [Weblate para tradução das extensões de terceiros](https://gramps.discourse.group/t/weblate-translation-for-addons-experiment-needs-testers/6964)

<span id="Roadmap">

### Roteiro

</span>

- Explore as notas de lançamento de [versões anteriores do Gramps](wiki:Previous_releases_of_Gramps)
- Veja itens projectados em relação à [próxima versão](https://gramps-project.org/bugs/roadmap_page.php) do Gramps.
- [Gramps Enhancement Proposals (GEPS)](wiki::Category:GEPS) - Veja a coluna **Lançado** para conhecer novos itens implementados na última versão
- [Roteiro {{TEMPLATE:version}}](wiki:Roteiro_{{TEMPLATE:version}}) - wiki

<span id="Changelog">

### Diário de alterações

</span>

- Veja itens relacionados com o Gramps [6.0](https://gramps-project.org/bugs/changelog_page.php) no rastreio de problemas do Gramps.

<!-- -->

- Veja informação adicional das versões de manutenção do Gramps:
  - Gramps [6.0.0](https://github.com/gramps-project/gramps/releases/tag/v6.0.0)
  - ...

{{-}}

<span id="What Was Once New">

### O que já *foi* novo

A página de [Versões anteriores](wiki:Previous_releases_of_Gramps) inclui ligações a listas de alterações a versões principais e de manutenção, lançadas ao longo dos anos.

Contudo, a página **O que há de novo?** na versão do manual wiki fornece mais detalhes:

- [Version 5.2](wiki:Gramps_5.2_Wiki_Manual_-_What%27s_new%3F)
- [Version 5.1](wiki:Gramps_5.1_Wiki_Manual_-_What%27s_new%3F)
- [Version 5.0](wiki:Gramps_5.0_Wiki_Manual_-_What%27s_new%3F)
- [Version 4.2](wiki:Gramps_4.2_Wiki_Manual_-_What%27s_new%3F)
- [Version 4.1](wiki:Gramps_4.1_Wiki_Manual_-_What%27s_new%3F)
- [Version 4.0](wiki:Gramps_4.0_Wiki_Manual_-_What%27s_new%3F)
- [Version 3.4](wiki:Gramps_3.4_Wiki_Manual_-_What%27s_new%3F)
- [Version 3.3](wiki:Gramps_3.3_Wiki_Manual_-_What%27s_new%3F)
- [Version 3.2](wiki:Gramps_3.2_Wiki_Manual_-_What%27s_new%3F)

Foi adicionada ao manual uma versão compacta das melhorias em 2010. Nos primeiros 3 anos da wiki, foi necessário rever todo o manual.

- Versão 5.1 - manual transferível
  - [English 20MiB PDF](wiki::File:Gramps5.1UserManual.pdf)
  - [Nederlands 16 MiB PDF](wiki::File:Gramps5.1UserManual_nl.pdf)
  - [русский 16 MiB PDF](wiki::File:Gramps5.1UserManual_ru.pdf)
  - [עברית Hebrew 24 MiB PDF](wiki::File:Gramps5.1UserManual_he.pdf)

Não listamos todas as reparações ou pequenas melhorias nesta página. Para obter uma lista completa das alterações, deve consultar a página do [histórico de submissões](https://github.com/gramps-project/gramps/commits/maintenance/gramps52) para cada lançamento. {{-}}

[Category:Pt PT:Documentation](wiki:Category:Pt_PT:Documentation)
