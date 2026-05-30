---
title: 'Gramps 6.0 Wiki Manual - Entering and editing data: detailed - part 2/pt PT'
categories:
- Pt PT:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 124111
wiki_fetched_at: '2026-05-30T19:46:27Z'
lang: pt PT
---

{{#vardefine:chapter\|9.2}} {{#vardefine:figure\|0}}

A secção anterior ofereceu-lhe uma visão detalhada de como inserir e editar dados para indivíduos, parentescos e datas. Esta secção continua com outros objectos que encontra no Gramps.

<span id="Editing information about events">

## Editar informação sobre eventos

</span> ![[_media/EventsCategory-EventsListView-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Categoria Eventos - Lista de eventos]]

Adicionar um evento a uma pessoa permite-lhe registar informações que encontrou.

Ao adicionar um evento à , verá o diálogo .

Para adicionar ou editar dados de eventos, mude para a categoria e seleccione a entrada pretendida na lista de eventos. Fazer duplo clique nessa entrada ou clicar em na barra de ferramentas. {{-}} <span id="New Event dialog">

### Diálogo Novo evento

</span> ![[_media/EditEvent-dialog-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo Editar evento]] O diálogo pode ser acedido via duplo clique numa linha na categoria Eventos, no [separador](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/pt_PT#Events) do diálogo , ou no [separador](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/pt_PT#Events) no .

A parte superior permite-lhe ver e editar informações básicas sobre o evento:

- o pode ser seleccionado a partir dos tipos disponíveis listados no menu pendente . Por exemplo, **Nascimento** (*pré-definição*), Baptismo, Óbito, Inumação, etc.; pode ainda criar o seu próprio [tipo de evento](wiki:Gramps_Glossary#custom) escrevendo directamente na caixa de texto do [selector](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/pt_PT#Selector_Combo_Boxes);
- a do evento pode ser exacta, um intervalo *de ... até ..., entre ...*, ou imprecisa, *circa...*;
  - button starts the dialog.
- a permite fornecer uma descrição mais detalhada do que é este evento;
  - o botão alterna a privacidade do registo, o que permite omiti-lo de relatórios;
- o pode ser seleccionado de uma lista de ou . Adicionalmente, pode arrastar e largar um local neste campo;
- a é um identificador único para o evento; deixe este campo em branco para permitir que o Gramps gira este valor automaticamente para novos eventos;
- o botão permite seleccionar uma etiqueta existente.

<span id="New Event tab pages">

### Separadores do diálogo Novo evento

</span>

A parte central da janela mostra separadores que contêm diferentes categorias de informação. Clique num separador para ver ou editar o seu conteúdo: <span id="Source Citations">

#### Citações de fontes

</span>

  
permite ver e editar fontes relevantes para um dado evento; a parte central da janela lista todas as referências de fonte armazenadas na base de dados; os botões , e permitem-lhe adicionar, modificar e remover uma referência de fonte associada a um evento, note-se que os botões e só ficam disponíveis quando uma há uma referência de fonte seleccionada na lista;

<span id="Notes">

#### Notas

</span>

  
permite registar notas ou comentários sobre o evento; para acrescentar uma nota ou alterar notas existentes, basta editar o texto no respectivo campo;

<span id="Galeria">

#### Galeria

</span>

  
mostra a associada ao evento;

<span id="Atributos">

#### Atributos

</span>

  
mostra quaisquer que possam estar associados ao evento seleccionado;

<span id="References">

#### Referências

</span>

  
mostra todas as feitas ao evento na base de dados.

Na parte inferior da janela, clicar em aplica todas as alterações feitas em todos os separadores e fecha o diálogo. Clicar em fecha a janela sem aplicar quaisquer alterações. Clicar em abre este manual.

{{-}} ![[_media/EventReferenceEditor-dialog-default-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo Editor de referência a evento]] \<span id=Editing event references"\>

## Editar referências a eventos

</span> As referências a eventos ligam um evento a um indivíduoi e permitem-lhe fornecer informações adicionais sobre o evento.

Ao adicionar referências a eventos a um separador do diálogo [Editar indivíduo](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/pt_PT#Events), verá o diálogo . <span id="Event Reference Editor dialog">

### Diálogo Editor de referência a evento

</span> {{-}} O diálogo inclui duas secções:

<span id="Reference Information">

#### 

</span> ![[_media/EventReferenceEditor-dialog-GeneralTab-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Separador Geral]]

- separador :
  - para o da pessoa neste evento, utilize a [lista pendente](wiki:Gramps_Glossary#selector_combo_box); escolha **[Principal](wiki:Gramps_Glossary#primary)** (*pré-definição* ao adicionar um evento) para o indivíduo principal; seleccione um papel de evento descritivo (por exemplo, [Ajudante](wiki:Gramps_Glossary#aide), [Noiva](wiki:Gramps_Glossary#bride), [Celebrante](wiki:Gramps_Glossary#celebrant), [Clérigo](wiki:Gramps_Glossary#clergy), [Família](wiki:Gramps_Glossary#family_role), [Padrinho](wiki:Gramps_Glossary#godparent), [Noivo](wiki:Gramps_Glossary#groom), ou [Testemunha](wiki:Gramps_Glossary#witness)) para um evento onde o indivíduo não é o participante principal;
  - os eventos adicionados através da partilha ou por arrastar e largar serão atribuídos ao papel **[Desconhecido](wiki:Gramps_Glossary#unknown)**. Se a pessoa tiver um papel igual, defina-o também como principal;
  - se nenhum dos papéis pré-definidos for apropriado, adicione um *[personalizado](wiki:Gramps_Glossary#custom)* na caixa do [selector](wiki:Gramps_Glossary#selector_combo_box); escrever o novo e único nome do papel (em vez de seleccionar um), cria um papel personalizado; os novos papéis personalizados serão adicionados à lista pendente; permanecem aí até que a árvore seja exportada e reimportada ou limpa através de uma [extensão de terceiros](wiki:Third-party_Addons), como a [limpeza de tipos](wiki:Addon:Types_Cleanup_Tool);
  - alguns exemplos de tipos personalizados para papéis de evento são sugeridos no artigo [Roles, Relationships and Associations](wiki:Roles,_Relationships_%26_Associations);

{{-}} ![[_media/EventReferenceEditor-dialog-CitationsTab-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Separador Citações de fontes]]

- separador :
  - pode adicionar, editar ou remover itens da lista;
  - pode ordenar a lista, movendo itens seleccionados abaixo ou acima, clicando nos respectivos botóes.

{{-}} ![[_media/EventReferenceEditor-dialog-AttributesTab-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Separador Atributos]]

- separador :
  - pode adicionar, editar ou remover itens da lista;
  - pode ordenar a lista, movendo itens seleccionados abaixo ou acima, clicando nos respectivos botóes.

{{-}} ![[_media/EventReferenceEditor-dialog-NotesTab-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Separador Notas]]

- separador :
  - pode adicionar, editar ou remover itens da lista;
  - pode ordenar a lista, movendo itens seleccionados abaixo ou acima, clicando nos respectivos botóes.

{{-}} ![[_media/EventReferenceEditor-SharedInfo-GeneralTab-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Separador Geral]] <span id="Shared Information">

#### 

</span>

- ;

- os separadores , e são idênticos aos descritos para a informação de referência;

- o separador permite mover as imagens à esquerda ou à direita;

- o separador só permite a edição de referências existentes.

{{-}} {{-}} <span id="Editing information about media objects">

## Editar informação de objectos multimédia

</span> Para adicionar ou editar dados de multimédia, mude para a categoria e seleccione a entrada pretendida na lista. Faça duplo clique nesse registo ou clique em da barra de ferramentas para abrir o diálogo do editor. <span id="New Media dialog">

### Diálogo Nova multimédia

</span> ![[_media/NewMediaEditor-dialog-example-60-pt_PT.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Diálogo Nova multimédia]]

A secção superior mostra uma miniatura do objecto multimédia, se disponível, juntamente com um resumo das suas propriedades (ID, data, caminho e tipo) que pode editar. Pode escrever estas informações directamente nos campos correspondentes. Para a data, também pode inserir informações clicando em e utilizando o diálogo ****:

- editar um descritivo para este objecto multimédia;
- a é um registo único para identificar o objecto multimédia, deixe em branco para que seja gerado pelo Gramps;
  - a privacidade é alternada para este objecto multimédia (pré-definição) ou ;
- uma associada ao objecto multimédia, por exemplo, para uma fotografia, pode ser a data em que foi tirada;
  - para abrir o diálogo ****;
- editar o do objecto no seu computador; o Gramps não armazena a multimédia internamente, apenas o caminho; defina a opção [Caminho relativo](wiki:Gramps_6.0_Wiki_Manual_-_Settings/pt_PT#Family_Tree&#39;s_Media_path) na entrada no diálogo Preferências -\> Geral para evitar ter de inserir a pasta base comum da multimédia. A ferramenta [Gestor de multimédia](wiki:Gramps_6.0_Wiki_Manual_-_Tools/pt_PT#Media_Manager) pode ajudar a gerir caminhos de de objectos multimédia;
  - clique em para seleccionar ficheiros específicos;
- clique em para as editar.

A secção inferior da janela mostra quatro separadores que contêm diferentes categorias de informação. Clique num separador para ver ou editar o seu conteúdo. A parte inferior da janela tem os botões , e . Clicar em aplica todas as alterações feitas em todos os separadores e fecha a janela de diálogo. Clicar em fecha a janela sem aplicar quaisquer alterações. Clicar em abre este manual.

<span id="New Media tab pages">

### Rótulos dos separadores

</span>

Os separadores representam as seguintes categorias de dados multimédia:

- , e , são idênticos aos descritos para a informação de referência dos eventos;

- o separador só permite a edição de referências existentes.

{{-}} <span id="Editing media object references">

## Editar referências de objectos multimédia

Quando as referências a objectos multimédia ligam um objecto multimédia a outro num separador , o botão abre o diálogo [Seleccionar objecto multimédia](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/pt_PT#Select_Media_Object_selector) e, depois de seleccionar um objecto multimédia, o aparece.

{{-}}

### Select a media object selector

![[_media/SelectAMediaObject-file-selector-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select a media object - (File) Selector Dialog - example]]

The file selector allow you to preview and select a media file you want to attach, and at the same time you may edit the shown (Defaults to the filename without the file extension).

- (checkbox unchecked by default until checked for the first time and remembered for each subsequent image selection.)

See also:

- [Select Media Object selector](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Select_Media_Object_selector)
- [Family Tree's Media path &gt; Base media path:](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Family_Tree.27s_Media_path)

<!-- -->

- [](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Media_Manager) a group of four separate tools two of which allow you to:
  - 

  - 

{{-}}

### Media Reference Editor dialog

![[_media/MediaReferenceEditor-dialog-collapsed-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Media Reference Editor - dialog - collapsed default example]]

The dialog.

See also [How to create image reference regions](wiki:How_to_create_image_reference_regions) {{-}} ![[_media/MediaReferenceEditor-dialog-expanded-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Media Reference Editor - dialog - &quot;Shared Information&quot; section expanded example]]

You may also expand the **Shared Information** section.

{{-}}

#### Top section

##### Top section tab pages

###### General

- Region corners : x1, x2, y1, y2.

The part allows to select a specific region on the Media Object. You can use the mouse cursor on the picture to select a region, or use these spinbuttons to set the top left, and bottom right corner of the referenced region. Point (0,0) is the top left corner of the picture, and (100,100) the bottom right corner.

- Privacy

The button lets you mark whether or not the record is considered private. Check the record box to mark this .

See also the [Narrated Web Site](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_7#Page_Generation) Gallery tab supports output of these referenced regions.

{{-}}

###### Source Citations

{{-}}

###### Attributes

{{-}}

###### Notes

{{-}}

#### Shared Information

##### Shared Information tab pages

###### General

{{-}}

###### References

{{-}}

###### Source Citations

{{-}}

###### Attributes

{{-}}

###### Notes

{{-}}

## Editing information about places

To edit information about places, switch to the and select the desired entry from the list of places. Double-click that entry or click the button on the toolbar to bring up the dialog:

{{-}}

### Place Editor dialog

![[_media/PlaceEditor-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Place editor - dialog]]

To edit information about places, switch to the Places Category and select the desired entry from the list of places. Double-click that entry or click the button on the toolbar to bring up the following dialog:

The following fields are available:

- Title area at top displays the description of this place to be used in reports. Gramps will construct this for you. See [Preferences &gt; Display &gt; Display Options (section) &gt; Automate Place Format](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Options) generation

- the name of this place.

  - button opens the dialog where you can add/edit additional information.

- the place type. All **[Custom Types](wiki:Gramps_Glossary#custom)** are shown at the bottom of the list. Choose from the following default available **Types**:

  - Building
  - Borough
  - Country
  - County
  - City
  - Department
  - District
  - Farm
  - Hamlet
  - Locality
  - Municipality
  - Neighborhood
  - Number - See [Street format:](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Place_Format_Editor)
  - Parish
  - Province
  - Region
  - State
  - Street
  - Town
  - **Unknown**(default)
  - Village

- the position above equation of the place in decimal or degree notation. Eg, valid values are 12.0154, 50°52'21.92\\N, N50º52'21.92\\ or 50:52:21.92. You can set these values via the Geography View by searching the place, or via a map service in the Place view. See: [Supported longitude/latitude formats](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Supported_longitude.2Flatitude_formats) See: [Coordinates format:](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Options) in preferences Display as this option controls the display of Coordinates.

<!-- -->

- the position relative to the Prime, or Greenwich, Meridian of the place in decimal or degree notation. Eg, valid values are -124.3647, 124°52'21.92\\E, E124º52'21.92\\ or 124:52:21.92. You can set these values via the Geography View by searching the place, or via a map service in the Place view. See: [Supported longitude/latitude formats](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Supported_longitude.2Flatitude_formats) See: [Coordinates format:](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Options) in preferences Display as this option controls the display of Coordinates.

-  See: [Coordinates format:](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Options) in preferences Display as this option controls the display of Coordinates.

<!-- -->

- 

- an unique record to identify the place. Leave generated by Gramps.

- a code for this place. For example, an area code or postal code.

- - 

{{-}}

### Place editor tab pages

The tabs represent the following categories of place data:

#### Enclosed By

![[_media/PlaceEditor-EnclosedBy-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Enclosed By" tab from "Place Editor" - dialog - example]]

Places in Gramps are stored in a hierarchy. The tab allows you to link this place to other places, higher in the hierarchy, which enclose it. Each link consists of a place and an optional date range.

To enclose with an existing place, use the use the button to choose a Place from the [Place Selector](#Select_Place_selector). Alternately, drag a place (from the Clipboard, Places Category view, or an Event Editor) into bottom of the tab.

The buttons , , and let you add a new Place as an enclosing hierarchical level, modify the selected enclosing Place, and remove a selected link to an enclosing Place.

Note that the , and re-ordering (up, down) buttons become available only when a link exists and is selected from the list. In general, a country will be a top level place, and will not be linked to any other place.

**See also:**

- [Enclosed By](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Enclosed_By) Gramplet
- [Using the clipboard](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_the_Clipboard)

##### Select Place selector

![[_media/SelectPlace-SelectorDialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select Place - Selector Dialog - example]]

The selector dialog allows you to link to an already existing place and once selected it will be opened in the

You may use the button to filter the list based on one of the options from the drop down list:

- **Name contains** (default)

{{-}}

##### Place Reference Editor

![[_media/PlaceReferenceEditor-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Place Reference Editor - Dialog - example]]

The second part of the window displays seven notebook tabs containing different categories of information. Click a tab to view or edit its contents. The bottom part of the window has and buttons. Clicking will apply all the changes made in all tabs and close the dialog window. Clicking the button will close the window without applying any changes.

{{-}}

#### Alternative Names

  
The tab lets you view and edit other names by which the place might be known. The tab lists all other names of the place stored in the database. The buttons , , and let you add, modify, and remove a name record. Note that the and buttons become available only when a name is selected from the list.

#### Source Citations

  
The tab lets you view and edit sources relevant to a place. The central part of the window lists all such source references stored in the database. The buttons , , and let you add, modify, and remove a source reference associated with a place. Note that the and buttons become available only when a source reference is selected from the list.

#### Notes

  
The tab displays any comments or notes concerning the place. To add a note or modify existing notes simply edit the text in the text entry field.

#### Gallery

  
The tab lets you store and display photos and other media objects associated with a given place. The central part of the window lists all such media objects and gives you a thumbnail preview of image files. Other objects such as audio files, movie files, etc., are represented by a generic Gramps icon. The buttons , , , and let you add a new image, add a reference to an existing image, modify an existing image, and remove a media object's link to the place. Note that the and buttons become available only when a media object is selected from the list.

#### Internet

  
The tab contains Internet addresses relevant to the place. (This tab exhibits identical behavior to the [Internet Tab](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Internet) for the Person editor and its [Internet Address Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Internet_Address_Editor) is the same also.)

<!-- -->

  
The bottom part of the window lists all such Internet addresses stored in the database. The top part shows the details of the currently selected address in the list (if any). The buttons , , and let you add, modify, and remove an Internet address. The button (represented by an icon with a green arrow and yellow circle) opens your browser and takes you to the web page corresponding to the highlighted Internet address. Note that the , , and buttons become available only when an address is selected from the list.

#### References

  
The tab indicates any database records (events or LDS ordinances) that refer to a place. This information cannot be modified from the dialog. Instead, the corresponding database record (e.g., a birth event) has to be brought up and its place reference edited.

{{-}}

### Place Name Editor dialog

![[_media/PlaceNameEditor-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Place Name Editor dialog - default]]

You can access the dialog from the dialogs button.

The dialog allows you to add/edit the following information:

- the name of the place

- Date range in which the place is valid

  - button

- Language in which the name is written. Valid values are two character ISO codes for example: en,fr, de, nl. See Wikipedia for the full list of valid [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) codes.

{{-}}

### Supported longitude/latitude formats

When you create/modify a place, the possible formats used for longitude/latitude coordinates are :

<table>
<thead>
<tr>
<th colspan="2"><p>Longitude &amp; Latitude Formats</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>D.D4</p></td>
<td><p>degree notation, 4 decimals</p>
<dl>
<dt></dt>
<dd>
eg +12.0154 , -124.3647
</dd>
<dd>
4 <a href="https://wikipedia.org/wiki/Decimal_degrees#Precision">decimals of longitude precision</a> allows an 11.132 meter (36.5223097 foot) approximation at the equator.
</dd>
</dl></td>
</tr>
<tr>
<td><p>D.D8</p></td>
<td><p>degree notation, 8 decimals (<a href="https://wikipedia.org/wiki/Decimal_degrees#Precision">precision</a> like ISO-DMS)</p>
<dl>
<dt></dt>
<dd>
eg +12.01543265 , -124.36473268
</dd>
</dl></td>
</tr>
<tr>
<td><p>DEG</p></td>
<td><p>degree, minutes, seconds notation</p>
<dl>
<dt></dt>
<dd>
eg 50°52'21.92"N , 124°52'21.92"E (° symbol has UTF-8 code c2b00a)
</dd>
<dd>
or N50º52'21.92" , E124º52'21.92" (º symbol has UTF-8 code c2ba0a)
</dd>
<dd>
The character for seconds can be either one double quote "
</dd>
<dd>
or two single quote '
</dd>
<dd>
The letters N/S/W/E can be placed before or after the digits.
</dd>
</dl></td>
</tr>
<tr>
<td><p>DEG-</p></td>
<td><p>degree, minutes, seconds notation with :</p>
<dl>
<dt></dt>
<dd>
eg -50:52:21.92 , 124:52:21.92
</dd>
</dl></td>
</tr>
<tr>
<td><p>ISO-D</p></td>
<td><p>ISO 6709 degree notation</p>
<dl>
<dt></dt>
<dd>
i.e. ±DD.DDDD±DDD.DDDD
</dd>
</dl></td>
</tr>
<tr>
<td><p>ISO-DM</p></td>
<td><p>ISO 6709 degree, minutes notation</p>
<dl>
<dt></dt>
<dd>
i.e. ±DDMM.MMM±DDDMM.MMM
</dd>
</dl></td>
</tr>
<tr>
<td><p>ISO-DMS</p></td>
<td><p>ISO 6709 degree, minutes, seconds notation</p>
<dl>
<dt></dt>
<dd>
i.e. ±DDMMSS.SS±DDDMMSS.SS
</dd>
</dl></td>
</tr>
</tbody>
</table>

{{-}}

See: [Coordinates format:](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Options) in preferences Display as this option controls the display of Coordinates.

## Editing information about sources

From either of the category views you can select or create a new source, or if you had chosen the or buttons, then the editor dialog appears.

### New Source dialog

![[_media/NewSource-editor-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} New Source - editor dialog - example]]

For the editor dialog the general information in the top section of the window lets you define basic information about the source: its , , , and . You can type this information directly into the adjacent fields.

- Title of the source.

- Authors of the source.

- Publication Information, such as city and year of publication, name of publisher, ...

- Provide a short title used for sorting, filing, and retrieving source records.

  - Lock icon toggle.

- an unique record to identify the source. Leave generated by Gramps.

- - 

{{-}}

### New Source tab pages

The tabs provide the following information categories of source data:

#### Notes

  
The tab provides a place to record notes or comments about the source. To add a note or modify existing notes simply edit the text in the text entry field. Only primary objects can be shown in the tab: Person, Family, Event, Place, or Media object. Secondary objects such as Names and Attributes can only be accessed through the primary objects to which they belong.

#### Gallery

  
The tab lets you store and display photos and other media objects associated with a given source (for example, a photo of a birth certificate). The central part of the window lists all such objects and gives you a thumbnail preview of image files. Other objects such as audio files, movie files, etc., are represented by a generic Gramps icon. The buttons , , , and let you add a new image, add a reference to an existing image, modify an existing image, and remove a media object's link to the relationship. Note that the and buttons become available only when a media object is selected from the list.

#### Attributes

  
The tab displays "Key/Value" pairs that may be associated with the source. These are similar to the "Attributes" used for other types of Gramps records. The difference between these Key/Value pairs and Attributes is that Attributes may have source references and notes, while Key/Value data may not.

<!-- -->

  
The central part of the window lists all existing Key/Value pairs. The buttons and let you add and remove pairs. To modify the text of Key or Value, first select the desired entry. Then click in either the Key or Value cell of that entry and type your text. When you are done, click outside the cell to exit editing mode.

#### Repositories

![[_media/NewSource-Repositories-tab-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Repositories" tab from "New Source" - dialog - example]]

  
The tab displays the references to the repositories in which the source is contained. The list can be ordered by any of its column headings: , , ,and . Double-clicking an entry allows you to view and edit the record in the . You may also edit the reference. The buttons on the side of the tab allow you add a new repository, link to (or share) an existing repository, edit the reference to the repository, or remove the reference.

##### Repository Reference Editor

![[_media/Repository-Reference-Editor-example-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Repository Reference Editor - Dialog - example]] The **Repository Reference Editor** dialog is opened by double-clicking a record in the tab of the [Source Editor](#Editing_information_about_sources) dialog.

It provides the ability to log the Type and Call Numbers for a Source in a particular Repository. Since a source might exist in multiple repositories. (I might have a photocopy in my personal library. A copy of the original book might be in the holdings of the <abbr title="Allen County Public Library">ACPL</abbr> Genealogy Center in Ft. Wayne, Indiana. The microfilm might being in the FamilySearch Library in Salt Lake City, Utah. Each can be located using different Call Numbers.)

###### Reference information

The Reference Information section has and tabs. The General tab has a text entry field for the and a [selector combo box](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Selector_Combo_Boxes).

Media Type choices: Audio, **Book** *(default)*, Card, Electronic, Fiche, Film, Magazine, Manuscript, Map, Newspaper, Photo, Tombstone, Unknown, Video, [custom types](wiki:Gramps_Glossary#custom).

###### Shared information

The section offers all the options of the [Repository Editor](#New_Repository_dialog) dialogs with General, Addresses, Internet, Notes and References tabs. {{-}}

##### Select Repository selector

![[_media/SelectRepository-SelectorDialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select Repository - Selector Dialog - example]]

The selector dialog allows you to link to an already existing repositories and once selected it will be opened in the <span id="Repository_Reference_Editor"></span>

You may use the button to filter the list based on one of the options from the drop down list:

- **Title contains** (default)
- *Title not contain*
- *ID contains*
- *ID does not contain*
- *Last Change contains*
- *Last Change does not contain*

{{-}}

#### References

  
The tab lists all the database records that refer to this source, if any. The list can be ordered by any of its column headings: , , or . Double-clicking an entry allows you to view and edit the record.

{{-}}

## Editing source citations

Citations connect a Source to another object and allow you to provide additional information about the source. Citations can be attached to a large number of objects,

- [People and various information about people](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Editing_information_about_people) (such as their name, address etc),
- [Relationships (Families) and various information about relationships](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Editing_information_about_relationships),
- [Events and various information about events](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_information_about_events),
- [Media objects and attributes of media objects](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_information_about_media_objects),
- [Places and various information about places](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_information_about_places),
- [Addresses of repositories](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_information_about_repositories).

For each object, a common set of buttons are provided:

-  (Create and add a new citation and a new source). This brings up an empty Citation dialog.

-  (Add an existing citation or source). This brings up the Source or Citation selection dialog box.

-  (Edit the selected citation). This brings up the Citation dialog pre-populated with the Citation and source information.

-  (Remove the existing citation). This removes the citation from the object. It does not delete the citation itself, which could then be connected to another object.

Note that the and buttons become available only when a citation has been selected.

{{-}}

### Select Source or Citation selector

![[_media/SelectSourceOrCitation-SelectorDialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select Source or Citation - Selector Dialog - example]]

When adding an existing citation or source, the [selector](wiki:Gramps_Glossary#selector) dialog appears.

This allows either an existing source or an existing citation (along with its associated source) to be selected. Click on the disclosure triangle alongside a source to see the citations associated with that source. For example, if one of your sources were a book, then the citations would normally refer to a page (or pages) within the book. If you already have a citation that refer to the particular page of the book, then you could select that citation which would then be shared. On the other hand, if this object needs to refer to a new page, then you would select the source and in the subsequent dialog enter the new page.

You may use the button to filter the list based on one of the options from the drop down list:

- **Source: Title or Citation: Volume/Page contains**(default)
- *Source: Title or Citation: Volume/Page does not contain*
- *ID contains*
- *ID does not contain*
- *Last Change contains*
- *Last Change does not contain*

{{-}}

### New Citation dialog

![[_media/NewCitation-editor-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} New Citation - editor Dialog - example]]

Once you have selected a citation or a source, or if you had chosen the or buttons, then the dialog appears.

The dialog includes one section called . {{-}}

#### Citation information

The section indicates the details associated with the particular reference to this Source: , , , and . You can choose the Confidence level from the drop-down menu. The remaining details can be typed in the corresponding text entry fields.

- Date associated with this source reference. Typically used to store the date that the data was entered into the original source document (not the date when the event occurred).

- 

-   
  Specific location with in the information referenced. For a published work, this could include the volume of a multi-volume work and the page number(s). For a periodical, it could include volume, issue, and page numbers. For a newspaper, it could include a column number and page number. For an unpublished source, this could be a sheet number, page number, frame number, etc. A census record might have a line number or dwelling and family numbers in addition to the page number.

-   
  Level conveys the submitter's quantitative evaluation of the credibility of a piece of information, based upon its supporting evidence. It is not intended to eliminate the receiver's need to evaluate the evidence for themselves. (Shown in the as the column)

  - *Very Low* = Unreliable evidence or estimated data.
  - *Low* = Questionable reliability of evidence (interviews, census, oral genealogies, or potential for bias for example, an autobiography).
  - **Normal** - (default) Evidence possibly has no issue or has not been assessed. Not yet validated
  - *High* = Secondary evidence, data officially recorded sometime after event.
  - *Very High* = Direct and primary evidence used, or by dominance of the evidence.

A warning icon  is displayed if the citation is shared.  

{{-}}

##### Select Source selector

![[_media/SelectSource-selector-dialog-example-50.PNG|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select Source - Selector Dialog - example]]

The selector dialog allows you to link to an already existing source.

You may use the button to filter the list based on one of the options from the drop down list:

- **Title contains** (default)
- *Title not contain*
- *Author contains*
- *Author does not contain*
- *ID contains*
- *ID does not contain*
- *Last Change contains*
- *Last Change does not contain*

{{-}}

##### Citation information section tab pages

The tabs provide the following information categories of citation data:

###### Notes

The tab provides a place to record notes or comments about the citation. The central part of the window lists all notes for this citation, and gives you a preview of the beginning of the note. The buttons , , , , and let you add a new note, share the selected note, edit the selected note, remove the selected note and move the selected note up or down the list of notes. Note that the , , , and buttons become available only when a media object is selected from the list. Removing a note only removes the note from this citation, it does not delete the note itself. Please refer to [details on editing notes](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_information_about_notes).

###### Gallery

The tab lets you store and display photos and other media objects associated with a given citation (for example, a photo of a page of a book or a page of a census). The central part of the window lists all such objects and gives you a thumbnail preview of image files. Other objects such as audio files, movie files, etc., are represented by a generic Gramps icon. The buttons , , and let you add a new image, add a reference to an existing image, modify an existing image, and remove a media object's link to the citation. Note that the and buttons become available only when a media object is selected from the list. Please refer to [details on editing media references](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_media_object_references).

###### Attributes

The tab displays "Key/Value" pairs that may be associated with the citation. These are similar to the "Attributes" used for other types of Gramps records. The difference between these Key/Value pairs and Attributes is that Attributes may have source citations and notes, while Key/Value data may not.

The central part of the window lists all existing Key/Value pairs. The buttons and let you add and remove pairs. To modify the text of Key or Value, first select the desired entry. Then press the button to select the Key, or click in either the Key or Value cell of that entry and type your text. When you are done, click outside the cell to exit editing mode.

###### References

The tab lists all the database records that refer to this source, if any. The list can be ordered by any of its column headings: , , or . Double-clicking an entry allows you to view and edit the record.

{{-}}

## Editing information about repositories

Once you have selected a source, or if you had chosen the or buttons, then the dialog appears.

### New Repository dialog

![[_media/NewRepository-editor-dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} New Repository - editor dialog - example]]

The following fields are shown:

- of the repository (where sources are stored).

- of repository can be physical or virtual structures where genealogical and family history sources are stored:

  - *Album*
  - *Archive*
  - *Bookstore*
  - *Cemetery*
  - *Church*
  - *Collection*
  - **Library** (default)
  - *Safe*
  - *Unknown*
  - *Web site*

-   
  an unique record to identify the repository. Leave empty to be generated by Gramps.

- Lock icon toggle.

- - 

{{-}}

### New Repository tab pages

The tabs represent the following categories of repository data:

#### Addresses

  
The tab lets you view and record the various addresses of the repository.

<!-- -->

  
The bottom part of the window lists all addresses stored in the database. The top part shows the details of the currently selected address in the list (if any). The buttons , , and allow you to correspondingly add, modify, and remove an address record from the database. Note that the and buttons become available only when an address is selected from the list.

#### Internet

  
The tab displays Internet addresses relevant to the repository. (This tab exhibits identical behavior to the [Internet Tab](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Internet) for the Person editor and its [Internet Address Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Internet_Address_Editor) is the same also.)

The bottom part lists all such Internet addresses and accompanying descriptions. The top part shows the details of the currently selected addresses in the list (if any). The buttons , , and let you add, modify, and remove an Internet address. The "Go" button (represented by an icon having a green arrow and yellow circle) opens your web browser and takes you directly to the highlighted page. Note that the , and buttons become available only when an address is selected from the list.

#### Notes

  
The tab provides a place to record notes or comments about the repository. To add a note or modify existing notes simply edit the text in the text entry field.

#### References

  
The tab indicates any database records that refer to a given repository. The list can be ordered according to any of its column headings: , , or . Double-clicking an entry allows you to view and edit the corresponding record.

{{-}}

## Editing information about notes

See also:

- [Notes Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Notes_Category)

### Note editor dialog

![[_media/NewNote-editor-dialog-example-with-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} New Note - editor dialog - default example]]

When creating a new note, or when editing an existing note, the dialog appears. There are two tabs, the **** tab, and the **** tab.

#### Note tab

The tab is the space where text is added. The text can be formatted using many standard text editing tools.

##### Note Toolbar

:\* A toolbar to apply styles (or Font Decorations) to text in your notes. You can select and apply one of the toolbuttons, or set the values as you want and start typing.

::\* : Slants text for emphasis, common in most text editors

::\* : Darkens text for emphasis, common in most text editors

::\* : Draws a line under text, common in most text editors

::\* : draws a line through, commonly used to indicate text to be deleted

::\* : Raises text slightly, commonly used for footnotes (e.g., Wikipedia<sup>2</sup>)

::\* : Lowers text slightly, commonly used in formulas (e.g., H<sub>2</sub>O)

::\* : selection drop down list, a basic font selector showing all fonts installed on your operating system.

::\* : selection drop down list, select the size of the font to use for your text.

::\* : Undoes last action.

::\* : Re-applies last "Undone" action.

::\* : Select the color of your font.

::\* : Adds a background color to the text you enter.

::\* : Opens the allowing you to create an internal link to an item in Gramps, such as a Person, Family, Event, Note, etc. External URL links can also be created.

::\* : Return selected text to plain text. Removes any links made.

##### Textview context menu

:\* Right click on the textview to show the context menu:

::\*  - The most important entry in this context menu is the spell selection. You are offered a selection of installed languages on your system with spell checking enabled. A [spelling checker](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Environment_Settings) is available for *English* and your installed local language (Note in the section enable the option for global English by default or the language your Gramps is run in and the note context menu is per note in the selected Language of your choice)

:::\*  - (default)

:::\*

::\*  - the selected text.

::\*  - the selected text.

::\*  - the previously cut or copied text.

::\*  - the selected text.

<hr>

::\*  - the text in the textview.

::\* -

::\* -

##### Note properties

:\* Some properties of your note

::\* checkbox: Notes in Gramps are considered reflowable to allow the content to conform to the report's page size and formatting for the most harmonious presentation. In the default setting, newlines (linefeeds & carriage returns) and white spaces will be automatically ignored so as to form complete paragraphs, which are defined by an empty line between two textblocks.  
When is checked, Gramps will assume the whitespace and newlines you keyed into the notes are important. Use *Preformatted* for tables, literal transcripts, and so forth. Using a monospace font will help keep preformatting column widths & margins predictable.  
Try not to use preformatted unless absolutely necessary, the reports create will flow more naturally.

::\* Privacy is the same as on the other objects. With one easy click, you can indicate a note should be considered private so Gramps can remove this note from all output created.

::\* a unique ID for the note. If left blank, an automatic ID will be generated according to the settings in the preferences.

<div id="note_type">

::\* (`General` default) The note type. You can add your own [custom Type](wiki:Gramps_Glossary#custom) by keyboarding it in directly. Adding a Note will automatically set the Type to match the object to which it is being added. (e.g. A note added to the Notes tab of the Person Editor will default to *Person Note* Type.)

  
  
{\|class="wikitable"

! style="text-align:left;"\| Type ! Recognized for features in \|- \|*[<primary object>](wiki:Gramps_Glossary#primary_object)* Note \| \|- \|*[<secondary object>](wiki:Gramps_Glossary#secondary_object)* Note \| \|- \|Citation \| \|- \|General \|*(default)* \|- \|Html code \|[Narrated Web Site](wiki:Gramps_6.0_Wiki_Manual_-_Reports#Narrated_Web_Site) report inclusions; export to GEDCOM \|- \|Link \| \|- \|Report \| \|- \|Research \| \|- \|Source text \| \|- \|To Do \|[To Do](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#To_Do) Gramplet, [ToDo Notes Gramplet](wiki:Addon:ToDoNotesGramplet) Addon. *Not to be confused with ToDo tag-based reports.* \|- \|Transcript \| \|- \|Unknown \| \|}

</div>

::\* Select a Tag for the note: Complete, Todo etc... You can add your own Tags by typing it. Reports based on tags include: [Tag Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Tag_Report), [Todo report](wiki:Addon:ToDoReport)

:::\* The button brings up the dialog list that lets you remove or assign existing custom tags. {{-}}

#### References tab

The tab indicates any objects that refer to a given note. The list can be ordered according to any of its column headings: , , or . Selecting or Double-clicking an entry allows you to view and edit the corresponding record.

### Link Editor

![[_media/Note-LinkEditor-dialog-default-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Link Editor - dialog - example]] **A block of Note text must be highlighted for the Link Editor to be active.** There is no visual indicator when the button is inactive. The has the following options:

- specifies the type of link

  - Internet Address ([<abbr title="Uniform Resource Locator, also known as a web address">URL</abbr>](https://en.m.wikipedia.org/wiki/URL))
  - or an item in Gramps, such as an [Event](wiki:Events), Family, Media, Note, Person, [Place](wiki:Places), Repository, [Source](wiki:Sources), or [Citation](wiki:Citations).

-  button : opens the selector dialog for existing items in the category specified in the Link Type. Not applicable for Internet Address selection.

- button : opens a window to create a new item of the specified Gramps item. Successful creation of a new item will autofill the Gramps item box and the Internet Address box with the appropriate data.

- - This box is Auto generated by the selection of the button/ button/ button.

- button : opens the editor dialog for the specified Gramps item. The selected item will autofill the Gramps item box and the Internet Address box with the appropriate data.

- - A Link type = Gramps type will autofill this box but the contents will be greyed out
  - for Link type = Internet Address delete any data left by Gramps and enter the full Internet Address.

![[_media/Note-showing-tooltip-for-link-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Notes Editor - Linking text example]]

See also:

- [Internet Address Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Internet_Address_Editor)
- [Note Link Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Note_Link_Report)

{{-}}

### Note markup and preformat in reports

Markup like **bold**, color, <u>underline</u>, ... can be added to notes. A note can be preformatted or not. It depends on the output type how this markup will appear. Here an overview is given of what you can expect.

- **PDF** and **direct print** (to printer or to file) fully support the markup and the preformatted setting
- **ascii** print removes all markup from the notes for obvious reasons

<!-- -->

- **LaTeX** supports the preformatted setting and partially supports font emphasis stylings and size markup;  
  output does not support font family or colors markup.
- **Narrative Web**. Many people use the Narrative Web report as an easy way to work with their data. This report is trying to respect markup in the notes. This is an interpreted translation, it is not one-to-one.
- **ODF** output does not support markup.
- **RTF** output does not support markup.
- **html** output does not support markup.

{{-}}

[Category:Pt PT:Documentation](wiki:Category:Pt_PT:Documentation)
