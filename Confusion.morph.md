Confusion tables
================

- [Lemma](#lemma)
- [Part-of-Speech](#part-of-speech)
- [Case](#case)
- [Mode](#mode)
- [Degre](#degre)
- [Genre](#genre)
- [Temps](#temps)
- [Nombre](#nombre)
- [Personne](#personne)


# Lemma
```
all:
  accuracy: 0.9398
  precision: 0.6464
  recall: 0.6398
  support: 17751
ambiguous-tokens:
  accuracy: 0.9487
  precision: 0.7247
  recall: 0.7282
  support: 8423
unknown-targets:
  accuracy: 0.6696
  precision: 0.2637
  recall: 0.2549
  support: 911
unknown-tokens:
  accuracy: 0.5941
  precision: 0.3787
  recall: 0.375
  support: 1286
```
  

| Expected        | Total Errors | Predictions     | Predicted times |
|-----------------|--------------|-----------------|-----------------|
| segm            | 44           | le              | 3               |
|                 |              | que4            | 3               |
|                 |              | et              | 2               |
|                 |              | penser          | 1               |
|                 |              | i2              | 1               |
|                 |              | estre1          | 1               |
|                 |              | son4            | 1               |
|                 |              | soi1            | 1               |
|                 |              | enföir1         | 1               |
|                 |              | faistre         | 1               |
|                 |              | verse           | 1               |
|                 |              | destraire       | 1               |
|                 |              | faire           | 1               |
|                 |              | grant           | 1               |
|                 |              | baston          | 1               |
|                 |              | carré           | 1               |
|                 |              | acessement      | 1               |
|                 |              | ton4            | 1               |
|                 |              | mon1            | 1               |
|                 |              | se              | 1               |
|                 |              | denoz           | 1               |
|                 |              | saifonse        | 1               |
|                 |              | jusque          | 1               |
|                 |              | un              | 1               |
|                 |              | en1             | 1               |
|                 |              | en2             | 1               |
|                 |              | avoir           | 1               |
|                 |              | poi             | 1               |
|                 |              | cent            | 1               |
|                 |              | don             | 1               |
|                 |              | de              | 1               |
|                 |              | vilvenir        | 1               |
|                 |              | assentir        | 1               |
|                 |              | encui           | 1               |
|                 |              | bié             | 1               |
|                 |              | croire          | 1               |
|                 |              | vui             | 1               |
|                 |              | parsisis        | 1               |
|                 |              | solier          | 1               |
| ''''            | 31           |                 | 31              |
| que2            | 30           | que4            | 29              |
|                 |              | que1            | 1               |
| que4            | 28           | que2            | 27              |
|                 |              | que1            | 1               |
| que1            | 26           | que4            | 22              |
|                 |              | que2            | 4               |
| il              | 16           | le              | 13              |
|                 |              | el1             | 1               |
|                 |              | lor2            | 1               |
|                 |              | i2              | 1               |
| le              | 13           | il              | 12              |
|                 |              | là              | 1               |
| avoir           | 11           | a3              | 8               |
|                 |              | ost             | 1               |
|                 |              | öir             | 1               |
|                 |              | on              | 1               |
| ne1             | 10           | ne2             | 9               |
|                 |              | segm            | 1               |
| se              | 9            | si              | 7               |
|                 |              | soi1            | 2               |
| estre1          | 9            | ester           | 2               |
|                 |              | ez              | 2               |
|                 |              | saint           | 2               |
|                 |              | estovoir1       | 1               |
|                 |              | jesir           | 1               |
|                 |              | soi1            | 1               |
| savoir          | 8            | estre1          | 3               |
|                 |              | sachier2        | 2               |
|                 |              | sacrer          | 1               |
|                 |              | soi1            | 1               |
|                 |              | sachant         | 1               |
| ne2             | 8            | ne1             | 8               |
| si              | 7            | soi1            | 4               |
|                 |              | se              | 3               |
| a3              | 6            | avoir           | 5               |
|                 |              | nom             | 1               |
| en2             | 6            | en1             | 3               |
|                 |              | on              | 3               |
| traire          | 6            | tref2           | 2               |
|                 |              | träir           | 2               |
|                 |              | trer2           | 1               |
|                 |              | trere           | 1               |
| que3            | 6            | que4            | 5               |
|                 |              | que2            | 1               |
| cel             | 5            | ce2             | 3               |
|                 |              | cest            | 1               |
|                 |              | quel1           | 1               |
| vëoir           | 5            | aler            | 3               |
|                 |              | venir           | 1               |
|                 |              | voir            | 1               |
| auberi          | 5            | aubri           | 5               |
| lou             | 5            | lever           | 2               |
|                 |              | löer1           | 1               |
|                 |              | lovent          | 1               |
|                 |              | lover           | 1               |
| damnedieu       | 5            | damnedeu        | 5               |
| sëoir           | 5            | estre1          | 1               |
|                 |              | seror           | 1               |
|                 |              | si+il           | 1               |
|                 |              | soir            | 1               |
|                 |              | savoir          | 1               |
| saint1          | 4            | saint           | 4               |
| voloir          | 4            | vieil           | 1               |
|                 |              | vos             | 1               |
|                 |              | voler           | 1               |
|                 |              | vëoir           | 1               |
| sachier2        | 4            | savoir          | 2               |
|                 |              | sacher          | 1               |
|                 |              | saumer          | 1               |
| saint           | 4            | saint1          | 4               |
| ici             | 4            | issi            | 3               |
|                 |              | je+il           | 1               |
| veintre         | 4            | vesquerre       | 1               |
|                 |              | ventre1         | 1               |
|                 |              | venir           | 1               |
|                 |              | ventir          | 1               |
| doner           | 4            | durer           | 3               |
|                 |              | donc            | 1               |
| trenchier1      | 4            | trachier2       | 1               |
|                 |              | trenchant       | 1               |
|                 |              | trechant        | 1               |
|                 |              | trechier        | 1               |
| o3              | 4            | où              | 4               |
| soi1            | 4            | son4            | 2               |
|                 |              | se              | 2               |
| de              | 3            | de+le           | 2               |
|                 |              | cle             | 1               |
| metre2          | 3            | movoir          | 2               |
|                 |              | jeter           | 1               |
| desoz           | 3            | desus           | 1               |
|                 |              | seignor         | 1               |
|                 |              | soz             | 1               |
| fort            | 3            | fors1           | 3               |
| chartrier1      | 3            | chartraisier    | 1               |
|                 |              | chartrainier1   | 1               |
|                 |              | chartraistre    | 1               |
| rëont           | 3            | rondre          | 2               |
|                 |              | ronde           | 1               |
| vif             | 3            | vëoir           | 1               |
|                 |              | vie1            | 1               |
|                 |              | vivre1          | 1               |
| je              | 3            | mon1            | 2               |
|                 |              | mi2             | 1               |
| mescroire       | 3            | mescrëant       | 3               |
| cele            | 3            | cel             | 3               |
| mon1            | 3            | je              | 1               |
|                 |              | mi2             | 1               |
|                 |              | metre2          | 1               |
| où              | 3            | o3              | 3               |
| peser           | 3            | pesser          | 1               |
|                 |              | poissant        | 1               |
|                 |              | pessant         | 1               |
| pöoir           | 3            | poissant        | 2               |
|                 |              | porrer          | 1               |
| orfenin         | 3            | orfelin         | 2               |
|                 |              | orfelïon        | 1               |
| privé1          | 3            | priver          | 1               |
|                 |              | priveement      | 1               |
|                 |              | privee          | 1               |
| son4            | 3            | si              | 1               |
|                 |              | soi1            | 1               |
|                 |              | som2            | 1               |
| desfigurer      | 3            | desfirier       | 3               |
| floripas        | 3            | florir          | 2               |
|                 |              | florer          | 1               |
| vaillant        | 3            | valoir          | 3               |
| pesance         | 3            | poissance       | 3               |
| öir             | 3            | avoir           | 3               |
| ce2             | 3            | ce1             | 3               |
| dent2           | 3            | dan2            | 3               |
| en1             | 3            | en2             | 2               |
|                 |              | il              | 1               |
| mont            | 3            | monde1          | 3               |
| durendal        | 3            | durondal        | 2               |
|                 |              | duroner         | 1               |
| feu             | 3            | fuir            | 1               |
|                 |              | falir           | 1               |
|                 |              | estre1          | 1               |
| abé2            | 2            | abé1            | 2               |
| alemaigne       | 2            | alemaine        | 1               |
|                 |              | alemander       | 1               |
| icest           | 2            | segm            | 1               |
|                 |              | ici             | 1               |
| vos             | 2            | vostre          | 2               |
| espargnance     | 2            | esparmance      | 2               |
| bruiant2        | 2            | bruiant         | 2               |
| pechëor         | 2            | pechier         | 2               |
| presenter       | 2            | present2        | 2               |
| ore3            | 2            | ëur             | 2               |
| acostumer       | 2            | acostume        | 2               |
| donc            | 2            | dont            | 2               |
| secrestain      | 2            | secretain       | 2               |
| sore            | 2            | sor2            | 2               |
| lions           | 2            | lïon            | 2               |
| empererriz      | 2            | emperëor        | 2               |
| denis           | 2            | saint-denis     | 2               |
| fils2           | 2            | fil2            | 2               |
| äimant          | 2            | amer1           | 1               |
|                 |              | aime            | 1               |
| chaut           | 2            | chaude          | 2               |
| poil            | 2            | pel2            | 1               |
|                 |              | pöoir           | 1               |
| mïete           | 2            | miete           | 2               |
| baisier         | 2            | bese            | 1               |
|                 |              | baser           | 1               |
| galois          | 2            | gallais         | 2               |
| a3+le           | 2            | en1+le          | 1               |
|                 |              | o4              | 1               |
| per             | 2            | pier            | 1               |
|                 |              | pere            | 1               |
| cor2            | 2            | corne1          | 2               |
| movoir          | 2            | monter          | 1               |
|                 |              | mëuse           | 1               |
| demostrer       | 2            | demorer         | 2               |
| mot             | 2            | mos1            | 2               |
| avenir          | 2            | avanant         | 1               |
|                 |              | avenant         | 1               |
| repairier       | 2            | repartir        | 1               |
|                 |              | repaire         | 1               |
| joëor           | 2            | jöer            | 2               |
| fublëure        | 2            | fasfulëure      | 1               |
|                 |              | asseoir         | 1               |
| entrer          | 2            | enterrer        | 1               |
|                 |              | entreindre      | 1               |
| flame           | 2            | flambe          | 2               |
| umanité         | 2            | utitelotité     | 1               |
|                 |              | utitité         | 1               |
| mener           | 2            | mander          | 1               |
|                 |              | maner           | 1               |
| gent1           | 2            | segm            | 1               |
|                 |              | gent2           | 1               |
| coste2          | 2            | costé           | 2               |
| nés             | 2            | nase            | 2               |
| detriier        | 2            | detrier(e)      | 2               |
| mentir          | 2            | mander          | 1               |
|                 |              | mantier         | 1               |
| öil             | 2            | o3              | 1               |
|                 |              | uil             | 1               |
| ja+mais1        | 2            | jaime           | 1               |
|                 |              | genëir          | 1               |
| vie1            | 2            | voie            | 1               |
|                 |              | viez            | 1               |
| on              | 2            | en2             | 2               |
| ovrir           | 2            | vovoir          | 1               |
|                 |              | ovrer           | 1               |
| vëer            | 2            | vëoir           | 2               |
| fee1            | 2            | fer             | 1               |
|                 |              | fie1            | 1               |
| conoistre       | 2            | conoitne        | 1               |
|                 |              | coing           | 1               |
| apercevoir      | 2            | esperchier      | 1               |
|                 |              | esparcier       | 1               |
| jöer            | 2            | joier           | 2               |
| depecier        | 2            | despechier      | 1               |
|                 |              | despecier       | 1               |
| riuns           | 2            | riun            | 1               |
|                 |              | rire            | 1               |
| autel2          | 2            | autel1          | 2               |
| repondre        | 2            | reposter        | 2               |
| corbeillon      | 2            | corbelon        | 2               |
| bordon1         | 2            | borde           | 1               |
|                 |              | bordon          | 1               |
| e2              | 2            | et              | 1               |
|                 |              | je              | 1               |
| pëor            | 2            | por2            | 1               |
|                 |              | poiersement     | 1               |
| champ           | 2            | chaumpe         | 1               |
|                 |              | chaump          | 1               |
| nos1            | 2            | ne1+il          | 1               |
|                 |              | nul             | 1               |
| sor2            | 2            | sus             | 2               |
| assaut          | 2            | assalir         | 2               |
| braire          | 2            | brait           | 2               |
| bien1           | 2            | bien2           | 1               |
|                 |              | bain            | 1               |
| escharpe        | 2            | eschaper        | 1               |
|                 |              | eschepe         | 1               |
| aler            | 2            | estre1          | 1               |
|                 |              | avoir           | 1               |
| duel            | 2            | doil            | 1               |
|                 |              | deus            | 1               |
| là              | 2            | il              | 1               |
|                 |              | le              | 1               |
| cest            | 2            | ce2             | 2               |
| tant            | 2            | tens            | 1               |
|                 |              | atant           | 1               |
| boivre          | 2            | bever           | 1               |
|                 |              | bui             | 1               |
| manant          | 2            | manand          | 1               |
|                 |              | menar           | 1               |
| mais1           | 2            | mès             | 2               |
| acorre          | 2            | acoire          | 1               |
|                 |              | acorer          | 1               |
| baugi           | 2            | baugin          | 2               |
| nom             | 2            | a3              | 1               |
|                 |              | non             | 1               |
| tinel1          | 2            | tenir1          | 2               |
| prendre         | 2            | pris1           | 1               |
|                 |              | prinier         | 1               |
| en1+le          | 2            | o4              | 1               |
|                 |              | où              | 1               |
| pain            | 2            | peing           | 1               |
|                 |              | pein            | 1               |
| dijon           | 2            | digon           | 1               |
|                 |              | dieu            | 1               |
| salir2          | 2            | salu            | 1               |
|                 |              | sauter          | 1               |
| nul             | 2            | non             | 2               |
| mason           | 2            | masson          | 2               |
| vuidier         | 2            | voloir          | 2               |
| comant          | 2            | comander        | 2               |
| arbre           | 2            | arbe            | 2               |
| atelie          | 2            | hatillie        | 1               |
|                 |              | hatelie         | 1               |
| apartenir       | 1            | apertenir       | 1               |
| lige            | 1            | lege            | 1               |
| arimathie       | 1            | arimate         | 1               |
| despendre1      | 1            | despendre       | 1               |
| galahaz         | 1            | galatas         | 1               |
| hosselice       | 1            | hosselie        | 1               |
| cui             | 1            | coit            | 1               |
| alaschier       | 1            | aler            | 1               |
| ferme1          | 1            | ferme           | 1               |
| gorde           | 1            | gordes          | 1               |
| feste1          | 1            | feste           | 1               |
| paume2          | 1            | paume1          | 1               |
| rendre          | 1            | rëëoir          | 1               |
| crëable         | 1            | chëable         | 1               |
| chalemel        | 1            | chalomier       | 1               |
| verceles        | 1            | vergeles        | 1               |
| pöestëif        | 1            | pöoir           | 1               |
| emprès          | 1            | empres          | 1               |
| asouvenir       | 1            | assovenir       | 1               |
| joces           | 1            | juce2           | 1               |
| caïfas          | 1            | carfais         | 1               |
| granment        | 1            | grant           | 1               |
| afolement       | 1            | afuler1         | 1               |
| ez              | 1            | estre1          | 1               |
| chevetaigne     | 1            | chevaune        | 1               |
| espargnier      | 1            | esparner        | 1               |
| ganor           | 1            | ganoir          | 1               |
| oriande         | 1            | orïendre        | 1               |
| femier          | 1            | fumier          | 1               |
| lor2            | 1            | il              | 1               |
| fait1           | 1            | faire           | 1               |
| merveillos      | 1            | merveille       | 1               |
| aprochier       | 1            | aprocier        | 1               |
| haucier         | 1            | hochier         | 1               |
| carrer          | 1            | carré           | 1               |
| las             | 1            | lassez          | 1               |
| piere           | 1            | pier            | 1               |
| setisme         | 1            | septe           | 1               |
| fuite           | 1            | fuie            | 1               |
| verdor          | 1            | verdoir1        | 1               |
| espenser        | 1            | espanser        | 1               |
| baissier        | 1            | baisier         | 1               |
| charme1         | 1            | charme          | 1               |
| grant           | 1            | gent1           | 1               |
| pois2           | 1            | pois1           | 1               |
| aesmer          | 1            | aimer           | 1               |
| tarse           | 1            | tharsie         | 1               |
| cilicie         | 1            | cilichie        | 1               |
| frein           | 1            | fré             | 1               |
| conte1          | 1            | cant2           | 1               |
| relenquir       | 1            | reliquer        | 1               |
| quinzime        | 1            | quinzement      | 1               |
| fausser         | 1            | faucier         | 1               |
| estendre        | 1            | ester           | 1               |
| riviere         | 1            | river2          | 1               |
| vermendois      | 1            | vermendir       | 1               |
| foler2          | 1            | foller          | 1               |
| seror           | 1            | sorëur          | 1               |
| damoisel        | 1            | danmile         | 1               |
| nëul            | 1            | negues          | 1               |
| ceindre         | 1            | coigne          | 1               |
| depopler        | 1            | depompler       | 1               |
| meciner         | 1            | mescin          | 1               |
| escremir        | 1            | escremiter      | 1               |
| nuef1           | 1            | nüeve           | 1               |
| serrer          | 1            | sarré           | 1               |
| filistien       | 1            | filsune         | 1               |
| ircamien        | 1            | wramien         | 1               |
| escarflaires    | 1            | escarfantre     | 1               |
| flot2           | 1            | flor1           | 1               |
| plaire          | 1            | place           | 1               |
| apovrir         | 1            | apover          | 1               |
| mès             | 1            | mais1           | 1               |
| posnee          | 1            | poinee          | 1               |
| noise           | 1            | noif            | 1               |
| joster          | 1            | joste2          | 1               |
| saintëé         | 1            | saint           | 1               |
| flamboiier      | 1            | flambier        | 1               |
| pöeros          | 1            | porest          | 1               |
| jehui           | 1            | jesir           | 1               |
| plait           | 1            | pler            | 1               |
| bricon1         | 1            | bricon          | 1               |
| changier        | 1            | chanter         | 1               |
| chandoile       | 1            | chaudele        | 1               |
| compagne1       | 1            | compagnie       | 1               |
| replenir        | 1            | resplenir       | 1               |
| vert            | 1            | verde1          | 1               |
| son1            | 1            | son4            | 1               |
| costure         | 1            | couture         | 1               |
| banc            | 1            | ban             | 1               |
| ivorie          | 1            | morir           | 1               |
| enföir1         | 1            | enföir2         | 1               |
| crïee           | 1            | crïer2          | 1               |
| plorer          | 1            | plaiier         | 1               |
| tot             | 1            | tost1           | 1               |
| marchëandise    | 1            | marchëandie     | 1               |
| esperdre        | 1            | espardre        | 1               |
| asseoir         | 1            | estre1          | 1               |
| vaunuble        | 1            | vaunguble       | 1               |
| acointer        | 1            | acointier       | 1               |
| poille          | 1            | puile           | 1               |
| romaigne        | 1            | romagne         | 1               |
| eschif1         | 1            | eschire         | 1               |
| colom           | 1            | colon           | 1               |
| blanc           | 1            | blant           | 1               |
| ester           | 1            | estait          | 1               |
| chanoine        | 1            | cenoine         | 1               |
| entr'acoler     | 1            | entr'escoler    | 1               |
| blé             | 1            | ble             | 1               |
| orri            | 1            | orrir           | 1               |
| bordeaux        | 1            | bordale         | 1               |
| tordre          | 1            | tort2           | 1               |
| tref2           | 1            | tref1           | 1               |
| juene           | 1            | joiant          | 1               |
| lïemier         | 1            | liemer          | 1               |
| i2              | 1            | il              | 1               |
| cerchier        | 1            | cherchier       | 1               |
| remener         | 1            | remanoir        | 1               |
| desert1         | 1            | desert2         | 1               |
| gregois         | 1            | graigois        | 1               |
| mien            | 1            | mon1            | 1               |
| digne           | 1            | dignier         | 1               |
| soslever        | 1            | soler           | 1               |
| laidir          | 1            | laide           | 1               |
| roye            | 1            | roie2           | 1               |
| riule           | 1            | regle           | 1               |
| devenir         | 1            | servir          | 1               |
| cant1           | 1            | cant2           | 1               |
| guilaume        | 1            | guilame         | 1               |
| denz            | 1            | dent2           | 1               |
| se+il           | 1            | si+il           | 1               |
| le+quel1        | 1            | licques         | 1               |
| pevree          | 1            | pevre           | 1               |
| cambrai         | 1            | cembrer2        | 1               |
| joie            | 1            | joi             | 1               |
| flechir         | 1            | fluchier        | 1               |
| douçor          | 1            | dosor           | 1               |
| guerrier        | 1            | guerredoier2    | 1               |
| blanchir        | 1            | blanchoir       | 1               |
| priiere         | 1            | präire          | 1               |
| escordement1    | 1            | escordement     | 1               |
| forment2        | 1            | forment         | 1               |
| tan             | 1            | tant            | 1               |
| an              | 1            | en1             | 1               |
| entre           | 1            | entre2          | 1               |
| come1           | 1            | col             | 1               |
| essillier       | 1            | eschillant      | 1               |
| issère          | 1            | isser           | 1               |
| pesme           | 1            | pief            | 1               |
| grever          | 1            | grevissïon      | 1               |
| sofraite        | 1            | sofrete         | 1               |
| aplanïer        | 1            | aplonier        | 1               |
| resachier       | 1            | reschier1       | 1               |
| voiz            | 1            | voie            | 1               |
| covenant        | 1            | convenir        | 1               |
| jeter           | 1            | jeste2          | 1               |
| autel1          | 1            | autel2          | 1               |
| desfaire        | 1            | desferre        | 1               |
| bort1           | 1            | borc            | 1               |
| malëuros        | 1            | malëuré         | 1               |
| loing           | 1            | loindre         | 1               |
| vostre          | 1            | vos             | 1               |
| fier            | 1            | ferir           | 1               |
| denier          | 1            | denir1          | 1               |
| archier         | 1            | archiers        | 1               |
| saiete          | 1            | saitie          | 1               |
| bretesche       | 1            | bisce           | 1               |
| flum            | 1            | bois            | 1               |
| dit             | 1            | dire            | 1               |
| sospir          | 1            | sopier          | 1               |
| höer            | 1            | horir           | 1               |
| fraisne         | 1            | fraine          | 1               |
| sauvëor         | 1            | sauverue        | 1               |
| jöir            | 1            | joie            | 1               |
| celebrer        | 1            | celer1          | 1               |
| lait2           | 1            | lait1           | 1               |
| mesfaire        | 1            | mesfait         | 1               |
| crever          | 1            | griver          | 1               |
| mont-loon       | 1            | montalon        | 1               |
| prover          | 1            | prever          | 1               |
| cosin           | 1            | cosine          | 1               |
| doon            | 1            | don             | 1               |
| franc           | 1            | franc1          | 1               |
| qui+il          | 1            | que4+il         | 1               |
| cant2           | 1            | cant1           | 1               |
| cuer2           | 1            | querre          | 1               |
| amenaunt        | 1            | amener          | 1               |
| covenir         | 1            | covenant        | 1               |
| encröer         | 1            | encrïer         | 1               |
| naturel         | 1            | natural         | 1               |
| contendre       | 1            | conter          | 1               |
| eschivir        | 1            | eschire         | 1               |
| motir           | 1            | motiersoiier    | 1               |
| encontre1       | 1            | encontre2       | 1               |
| col             | 1            | coup1           | 1               |
| mulot2          | 1            | mulot           | 1               |
| tenir1          | 1            | tendre1         | 1               |
| sevrer          | 1            | segm            | 1               |
| hisdos          | 1            | hieus           | 1               |
| munpoun         | 1            | munporne        | 1               |
| ploiier         | 1            | plaire          | 1               |
| batisement      | 1            | batisment       | 1               |
| guerroiier2     | 1            | garir           | 1               |
| voie            | 1            | vëoir           | 1               |
| crëanter        | 1            | croire          | 1               |
| maistre         | 1            | metre2          | 1               |
| aprendre        | 1            | apendre         | 1               |
| foi             | 1            | foie2           | 1               |
|                 | 1            | ''''            | 1               |
| mëisme          | 1            | maisire         | 1               |
| galles          | 1            | gale            | 1               |
| perles          | 1            | perle           | 1               |
| listenois       | 1            | listansois      | 1               |
| prëer           | 1            | predor          | 1               |
| mois2           | 1            | mois            | 1               |
| sofire          | 1            | soflir          | 1               |
| orbe3           | 1            | orbe            | 1               |
| rüe2            | 1            | rues            | 1               |
| deguerpir       | 1            | destorbire      | 1               |
| abiter          | 1            | abit            | 1               |
| ce1             | 1            | ce2             | 1               |
| reims           | 1            | roinc           | 1               |
| precier         | 1            | prëechier       | 1               |
| planer2         | 1            | plenier2        | 1               |
| hardement       | 1            | hardenen        | 1               |
| adenter         | 1            | adoter          | 1               |
| assaser         | 1            | assasiier       | 1               |
| oïr             | 1            | oir             | 1               |
| seignor         | 1            | sainté          | 1               |
| proiier         | 1            | prometre        | 1               |
| verai           | 1            | vëoir           | 1               |
| mesprison       | 1            | mesproison      | 1               |
| reprendre2      | 1            | reprendre1      | 1               |
| trover          | 1            | trever          | 1               |
| mordre2         | 1            | mordre1         | 1               |
| gent2           | 1            | gent1           | 1               |
| ainsi           | 1            | ainz            | 1               |
| brunir          | 1            | bornir          | 1               |
| lentement       | 1            | lentement2      | 1               |
| corporel        | 1            | corportel       | 1               |
| medecine        | 1            | mëisme          | 1               |
| cliner          | 1            | clinir          | 1               |
| perrier2        | 1            | perrier         | 1               |
| odor            | 1            | ode             | 1               |
| confire2        | 1            | comire2         | 1               |
| souder1         | 1            | soudeer1        | 1               |
| essaiement      | 1            | assaument       | 1               |
| hernaudet       | 1            | hernaut         | 1               |
| mont-martre     | 1            | munt-martre     | 1               |
| apareillier1    | 1            | afeblir         | 1               |
| meque           | 1            | moques          | 1               |
| amant           | 1            | amer1           | 1               |
| mi1             | 1            | mie             | 1               |
| prëechier       | 1            | prendre         | 1               |
| ravine          | 1            | ravine1         | 1               |
| tor5            | 1            | turc            | 1               |
| plevir          | 1            | plaiier         | 1               |
| cöart           | 1            | cort1           | 1               |
| deviser         | 1            | devise          | 1               |
| ame             | 1            | amer1           | 1               |
| manois          | 1            | manois2         | 1               |
| antiquité       | 1            | entitit         | 1               |
| penëancier      | 1            | penëier         | 1               |
| meillor         | 1            | melor           | 1               |
| combatre        | 1            | combatant       | 1               |
| enväir          | 1            | avironer        | 1               |
| aombrer         | 1            | aombrer1        | 1               |
| bolir           | 1            | boisson         | 1               |
| siglas          | 1            | ciclais         | 1               |
| point           | 1            | poing           | 1               |
| canivet         | 1            | conivet         | 1               |
| charrete        | 1            | charte1         | 1               |
| faire           | 1            | fais            | 1               |
| charriier       | 1            | charier         | 1               |
| afeblir         | 1            | esfloibier      | 1               |
| jëuner          | 1            | guener          | 1               |
| gautier         | 1            | gautlier        | 1               |
| tresfiner       | 1            | tresfain        | 1               |
| erepuis         | 1            | erpure          | 1               |
| le_mans         | 1            | mans            | 1               |
| repaire         | 1            | repairier       | 1               |
| conte2          | 1            | conte1          | 1               |
| mescrëant       | 1            | mescroire       | 1               |
| rüele           | 1            | rüel            | 1               |
| cent            | 1            | sentier         | 1               |
| antiaume        | 1            | antaume         | 1               |
| jazerenc        | 1            | jazarez         | 1               |
| bauvere_(porte) | 1            | bauver          | 1               |
| vistement       | 1            | vitement        | 1               |
| edesse          | 1            | asseoir         | 1               |
| laudesse        | 1            | laudes          | 1               |
| helais          | 1            | he_lais         | 1               |
| onoreement      | 1            | onorement       | 1               |
| ars             | 1            | ardre           | 1               |
| doloir          | 1            | dolir           | 1               |
| ardre           | 1            | hardi           | 1               |
| remetre         | 1            | remanoir        | 1               |
| rien            | 1            | reing           | 1               |
| tarder          | 1            | tardir          | 1               |
| mainbornie      | 1            | maisnbiee       | 1               |
| entreprendre    | 1            | entr'eprendre   | 1               |
| osteler         | 1            | osteillier      | 1               |
| äi!             | 1            | ami             | 1               |
| restre          | 1            | refuser         | 1               |
| naïmant         | 1            | naiment         | 1               |
| deça            | 1            | deca            | 1               |
| arme            | 1            | ame             | 1               |
| bovier          | 1            | belier          | 1               |
| tonel           | 1            | toune           | 1               |
| garantir        | 1            | garantin        | 1               |
| depercier       | 1            | depecier        | 1               |
| sacrefise       | 1            | sacrefiinquerre | 1               |
| rober           | 1            | rober1          | 1               |
| poignëiz        | 1            | poindre         | 1               |
| dozime          | 1            | douz            | 1               |
| soutain2        | 1            | sotien          | 1               |
| cordöan         | 1            | cordoias        | 1               |
| la              | 1            | le              | 1               |
| uis             | 1            | us              | 1               |
| coillir         | 1            | cuel            | 1               |
| outreement      | 1            | outrement       | 1               |
| garir           | 1            | garder          | 1               |
| oir             | 1            | er2             | 1               |
| esmiier         | 1            | esmer           | 1               |
| os2             | 1            | ost             | 1               |
| mëoler          | 1            | moller          | 1               |
| o2              | 1            | où              | 1               |
| pale            | 1            | pale1           | 1               |
| mu1             | 1            | müer            | 1               |
| sol1            | 1            | soz             | 1               |
| rupane          | 1            | ropendre        | 1               |
| chiere          | 1            | chier           | 1               |
| entremetre      | 1            | entrement       | 1               |
| o4              | 1            | ove             | 1               |
| reboisier       | 1            | reboissant      | 1               |
| orgoillir       | 1            | orgoillier      | 1               |
| bastre          | 1            | batre           | 1               |
| ostel           | 1            | oste            | 1               |
| hauberc         | 1            | harbe           | 1               |
| regne           | 1            | regner          | 1               |
| mort            | 1            | morir           | 1               |
| israel          | 1            | issaille        | 1               |
| aitre           | 1            | atrie           | 1               |
| tierce          | 1            | tierz           | 1               |
| un              | 1            | i2              | 1               |
| laissier        | 1            | laiier2         | 1               |
| plenier2        | 1            | plenir          | 1               |
| orlëure         | 1            | ostlëure        | 1               |
| moitié          | 1            | mitié           | 1               |
| aigue           | 1            | avoir           | 1               |
| röe             | 1            | roi2            | 1               |
| balesguez       | 1            | balesgëoiz      | 1               |
| charles         | 1            | charlemagne     | 1               |
| sejorner        | 1            | sorjorner       | 1               |
| grevos          | 1            | greves          | 1               |
| errant          | 1            | errer2          | 1               |
| val1            | 1            | valoir          | 1               |
| terrienement    | 1            | terrïenment     | 1               |
| besoing         | 1            | besoigno        | 1               |
| decorir         | 1            | decorter        | 1               |
| clerjon         | 1            | clercon         | 1               |
| engignier1      | 1            | enseignier      | 1               |
| sainteté        | 1            | saint           | 1               |
| nostre          | 1            | nos1            | 1               |
| serein          | 1            | serf            | 1               |
| lumbardie       | 1            | lurbardie       | 1               |
| net2            | 1            | naistre         | 1               |
| garder          | 1            | garir           | 1               |
| pener           | 1            | peine           | 1               |
| issir           | 1            | aler            | 1               |
| escroler        | 1            | escroillier     | 1               |
| or4             | 1            | ore3            | 1               |
| fromund         | 1            | fromurdor       | 1               |
| espanois        | 1            | espanoir        | 1               |
| arcediacne      | 1            | marchëant       | 1               |
| voutiz          | 1            | voloir          | 1               |
| coroner         | 1            | coronee         | 1               |
| folement        | 1            | folement2       | 1               |
| chaloir         | 1            | chaillier1      | 1               |
| recomencier     | 1            | recomance       | 1               |
| reslumer        | 1            | reslomer        | 1               |
| puis            | 1            | plus            | 1               |
| perçoivre       | 1            | percier         | 1               |
| ramage          | 1            | ramager         | 1               |
| cuidier1        | 1            | qui             | 1               |
| gile            | 1            | saint-gilles    | 1               |
| arester         | 1            | arestier        | 1               |
| voir            | 1            | vers2           | 1               |
| cursable        | 1            | curable         | 1               |
| put             | 1            | pute            | 1               |
| ainz            | 1            | ainc            | 1               |
| regarder        | 1            | ergardant       | 1               |
| sivre           | 1            | siror           | 1               |
| chastel         | 1            | chautalier      | 1               |
| voisdos         | 1            | voidos          | 1               |
| atendrir        | 1            | atenir          | 1               |
| nercir          | 1            | merci           | 1               |
| gabriel         | 1            | garber          | 1               |
| prometre        | 1            | premetre        | 1               |
| atente          | 1            | atainte         | 1               |
| muntferant      | 1            | montferant      | 1               |
| resplendissor   | 1            | resplendre      | 1               |
| alumer          | 1            | eslumer         | 1               |
| par             | 1            | pare1           | 1               |
| marois2         | 1            | marais          | 1               |
| valoir          | 1            | vaslet          | 1               |
| veille          | 1            | voloir          | 1               |
| moins           | 1            | mendre          | 1               |
| polissement     | 1            | polisier        | 1               |
| empirier        | 1            | empir           | 1               |
| hontosoment     | 1            | hontevent       | 1               |
| david           | 1            | devin1          | 1               |
| mestier         | 1            | maistre         | 1               |
| entr'ovrir      | 1            | entrover        | 1               |
| loir2           | 1            | loi3            | 1               |
| betlïant        | 1            | belïant         | 1               |
| venir           | 1            | venus           | 1               |
| present1        | 1            | present2        | 1               |
| estovoir1       | 1            | estre1          | 1               |
| vos1            | 1            | vos             | 1               |
| alemele         | 1            | lemele          | 1               |
| porter          | 1            | porte1          | 1               |
| cöarder         | 1            | cöardir         | 1               |
| esperit         | 1            | espirit         | 1               |
| contree         | 1            | contraiee       | 1               |
| qui             | 1            | que4            | 1               |
| resplendir      | 1            | resplendre      | 1               |
| pot             | 1            | pöoir           | 1               |
| puiz            | 1            | puis            | 1               |
| semer2          | 1            | semanoir        | 1               |
| force1          | 1            | force2          | 1               |
| clos            | 1            | clo             | 1               |
| crote1          | 1            | crote           | 1               |
| los1            | 1            | lot1            | 1               |
| anjou           | 1            | angois          | 1               |
| maine           | 1            | maigne          | 1               |
| nil             | 1            | nul             | 1               |
| près            | 1            | priier          | 1               |
| parole          | 1            | parler          | 1               |
| bretaigne       | 1            | bertaine        | 1               |
| estant          | 1            | ester           | 1               |
| saintisme       | 1            | saint           | 1               |
| mier            | 1            | mer             | 1               |
| vengier         | 1            | vent            | 1               |
| renaut          | 1            | renoil          | 1               |
| chevauchiee     | 1            | chevauchier     | 1               |
| ajornee         | 1            | ajorner         | 1               |
| damner          | 1            | danois          | 1               |
| coupable2       | 1            | corpable        | 1               |
| aorser          | 1            | aorer2          | 1               |
| saint-gilles    | 1            | gile            | 1               |
| haire           | 1            | here            | 1               |
| assëurer        | 1            | essëurer        | 1               |
| pon2            | 1            | pont            | 1               |
| monte           | 1            | monter          | 1               |
| ainc            | 1            | ainz            | 1               |
| devëer          | 1            | devoir          | 1               |
| fierement       | 1            | floierement     | 1               |
| salatrés        | 1            | salité          | 1               |
| perdre          | 1            | pordreindre     | 1               |
| ataindre        | 1            | ateindre        | 1               |

# Part-of-Speech

```
all:
  accuracy: 0.9472
  precision: 0.8081
  recall: 0.7416
  support: 17751
ambiguous-tokens:
  accuracy: 0.9416
  precision: 0.7856
  recall: 0.7307
  support: 10299
unknown-tokens:
  accuracy: 0.8258
  precision: 0.5515
  recall: 0.5148
  support: 1286
```
| Expected      | Total Errors | Predictions   | Predicted times |
|---------------|--------------|---------------|-----------------|
| NOMcom        | 147          | ADJqua        | 30              |
|               |              | NOMpro        | 27              |
|               |              | VERcjg        | 25              |
|               |              | VERppe        | 18              |
|               |              | VERinf        | 11              |
|               |              | ADVgen        | 11              |
|               |              | VERppa        | 7               |
|               |              | PROind        | 5               |
|               |              | PRE           | 3               |
|               |              | DETpos        | 2               |
|               |              | PROdem        | 2               |
|               |              | PROper        | 2               |
|               |              | DETcar        | 1               |
|               |              | PROcar        | 1               |
|               |              | ADJord        | 1               |
|               |              | ADVneg        | 1               |
| ADJqua        | 80           | NOMcom        | 43              |
|               |              | VERppe        | 14              |
|               |              | NOMpro        | 7               |
|               |              | ADVgen        | 7               |
|               |              | VERcjg        | 6               |
|               |              | VERppa        | 2               |
|               |              | PRE           | 1               |
| OUT           | 78           | NOMcom        | 14              |
|               |              | VERcjg        | 9               |
|               |              | PROper        | 7               |
|               |              | ADJqua        | 6               |
|               |              | DETdef        | 5               |
|               |              | ADVgen        | 5               |
|               |              | VERppe        | 4               |
|               |              | NOMpro        | 4               |
|               |              | CONsub        | 4               |
|               |              | CONcoo        | 4               |
|               |              | DETpos        | 3               |
|               |              | PRE           | 3               |
|               |              | ADVneg        | 2               |
|               |              | PROcar        | 2               |
|               |              | PROadv        | 1               |
|               |              | VERppa        | 1               |
|               |              | DETndf        | 1               |
|               |              | PROind        | 1               |
|               |              | VERinf        | 1               |
|               |              | DETdem        | 1               |
| ADVgen        | 67           | ADJqua        | 13              |
|               |              | NOMcom        | 11              |
|               |              | PRE           | 8               |
|               |              | PROind        | 6               |
|               |              | CONcoo        | 6               |
|               |              | PROper        | 5               |
|               |              | CONsub        | 4               |
|               |              | DETind        | 4               |
|               |              | VERcjg        | 3               |
|               |              | DETdef        | 3               |
|               |              | NOMpro        | 1               |
|               |              | PROrel        | 1               |
|               |              | ADVneg.PROper | 1               |
|               |              | VERinf        | 1               |
| VERcjg        | 65           | NOMcom        | 25              |
|               |              | VERppe        | 18              |
|               |              | PRE           | 10              |
|               |              | PROper        | 3               |
|               |              | VERppa        | 2               |
|               |              | ADVgen        | 2               |
|               |              | NOMpro        | 1               |
|               |              | PROind        | 1               |
|               |              | PROrel        | 1               |
|               |              | VERinf        | 1               |
|               |              | PRE.DETdef    | 1               |
| PROrel        | 45           | CONsub        | 35              |
|               |              | CONcoo        | 3               |
|               |              | PROint        | 2               |
|               |              | ADVgen        | 2               |
|               |              | NOMcom        | 1               |
|               |              | VERcjg        | 1               |
|               |              | ADVsub        | 1               |
| NOMpro        | 40           | NOMcom        | 22              |
|               |              | ADJqua        | 7               |
|               |              | VERppe        | 4               |
|               |              | VERcjg        | 3               |
|               |              | VERinf        | 2               |
|               |              | CONcoo        | 1               |
|               |              | DETind        | 1               |
| CONsub        | 38           | PROrel        | 28              |
|               |              | ADVgen        | 9               |
|               |              | PROper        | 1               |
| VERppe        | 37           | NOMcom        | 18              |
|               |              | VERcjg        | 9               |
|               |              | ADJqua        | 3               |
|               |              | NOMpro        | 2               |
|               |              | PROper        | 1               |
|               |              | PROrel        | 1               |
|               |              | ADVneg        | 1               |
|               |              | PROdem        | 1               |
|               |              | ADVgen.PROper | 1               |
| PROper        | 29           | DETdef        | 15              |
|               |              | NOMpro        | 3               |
|               |              | DETpos        | 3               |
|               |              | PROimp        | 2               |
|               |              | CONsub        | 2               |
|               |              | PRE.DETdef    | 1               |
|               |              | PROadv        | 1               |
|               |              | PROind        | 1               |
|               |              | NOMcom        | 1               |
| PROind        | 28           | DETind        | 8               |
|               |              | ADVgen        | 5               |
|               |              | NOMcom        | 4               |
|               |              | DETndf        | 3               |
|               |              | PROadv        | 3               |
|               |              | NOMpro        | 2               |
|               |              | ADJind        | 2               |
|               |              | ADVneg        | 1               |
| CONcoo        | 27           | ADVneg        | 11              |
|               |              | PRE           | 7               |
|               |              | ADVgen        | 4               |
|               |              | PRE.DETdef    | 2               |
|               |              | PROrel        | 2               |
|               |              | CONsub        | 1               |
| PRE           | 24           | VERcjg        | 9               |
|               |              | ADVgen        | 7               |
|               |              | NOMcom        | 3               |
|               |              | PROadv        | 3               |
|               |              | PRE.DETdef    | 1               |
|               |              | DETdem        | 1               |
| DETdef        | 21           | PROper        | 19              |
|               |              | OUT           | 2               |
| ADJpos        | 19           | DETpos        | 15              |
|               |              | PROper        | 1               |
|               |              | OUT           | 1               |
|               |              | ADJqua        | 1               |
|               |              | NOMcom        | 1               |
| PROimp        | 18           | PROper        | 18              |
| PROcar        | 15           | DETcar        | 5               |
|               |              | NOMcom        | 3               |
|               |              | ADJcar        | 2               |
|               |              | PROind        | 2               |
|               |              | DETndf        | 1               |
|               |              | PROper        | 1               |
|               |              | VERcjg        | 1               |
| VERinf        | 15           | NOMcom        | 12              |
|               |              | VERppe        | 2               |
|               |              | NOMpro        | 1               |
| DETcar        | 15           | DETndf        | 9               |
|               |              | NOMcom        | 2               |
|               |              | ADJcar        | 2               |
|               |              | PROcar        | 1               |
|               |              | VERppe        | 1               |
| ADVneg        | 14           | CONcoo        | 10              |
|               |              | NOMcom        | 2               |
|               |              | PROind        | 2               |
| PROint        | 13           | PROrel        | 8               |
|               |              | CONsub        | 2               |
|               |              | NOMcom        | 1               |
|               |              | NOMpro        | 1               |
|               |              | DETint        | 1               |
| DETpos        | 11           | PROper        | 6               |
|               |              | NOMcom        | 2               |
|               |              | CONsub        | 1               |
|               |              | ADVgen        | 1               |
|               |              | VERppe        | 1               |
| VERppa        | 11           | ADJqua        | 5               |
|               |              | NOMcom        | 4               |
|               |              | ADVgen        | 1               |
|               |              | VERcjg        | 1               |
| DETind        | 10           | ADVgen        | 3               |
|               |              | PROind        | 3               |
|               |              | ADJind        | 2               |
|               |              | ADJqua        | 1               |
|               |              | NOMcom        | 1               |
| ADJind        | 9            | DETind        | 7               |
|               |              | PROind        | 1               |
|               |              | NOMcom        | 1               |
| ADJcar        | 9            | DETcar        | 4               |
|               |              | PROcar        | 3               |
|               |              | DETndf        | 1               |
|               |              | VERcjg        | 1               |
| PROadv        | 7            | PRE           | 5               |
|               |              | PROper        | 1               |
|               |              | PROind        | 1               |
| ADJord        | 6            | NOMcom        | 4               |
|               |              | ADJqua        | 1               |
|               |              | PROord        | 1               |
| PROdem        | 5            | ADVgen        | 2               |
|               |              | DETdem        | 2               |
|               |              | VERcjg        | 1               |
| PROord        | 5            | NOMcom        | 3               |
|               |              | NOMpro        | 1               |
|               |              | ADJord        | 1               |
| DETndf        | 5            | DETcar        | 2               |
|               |              | PROper        | 1               |
|               |              | PROind        | 1               |
|               |              | PROadv        | 1               |
| ADVint        | 5            | CONsub        | 3               |
|               |              | CONcoo        | 1               |
|               |              | ADVsub        | 1               |
| PRE.DETdef    | 4            | PRE           | 2               |
|               |              | VERcjg        | 1               |
|               |              | PROrel        | 1               |
| DETdem        | 4            | PROdem        | 3               |
|               |              | NOMcom        | 1               |
| PROpos        | 3            | ADJpos        | 2               |
|               |              | NOMcom        | 1               |
| INJ           | 3            | CONcoo        | 1               |
|               |              | PROcar        | 1               |
|               |              | ADVint        | 1               |
| DETrel        | 2            | DETint        | 2               |
| CONsub.PROper | 1            | ADVgen.PROper | 1               |
| PROrel.PROper | 1            | PROint        | 1               |
| DETint        | 1            | PROrel        | 1               |

# Case

```
all:
  accuracy: 0.9338
  precision: 0.9079
  recall: 0.9037
  support: 17751
ambiguous-tokens:
  accuracy: 0.9164
  precision: 0.907
  recall: 0.9062
  support: 9953
unknown-tokens:
  accuracy: 0.8515
  precision: 0.8808
  recall: 0.8793
  support: 1286
```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| r        | 454          | n           | 265             |
|          |              | _           | 136             |
|          |              | i           | 48              |
|          |              | x           | 5               |
| n        | 447          | r           | 388             |
|          |              | _           | 44              |
|          |              | x           | 8               |
|          |              | i           | 7               |
| _        | 184          | r           | 136             |
|          |              | n           | 38              |
|          |              | x           | 5               |
|          |              | i           | 5               |
| i        | 79           | r           | 53              |
|          |              | n           | 17              |
|          |              | _           | 9               |
| x        | 12           | r           | 8               |
|          |              | _           | 3               |
|          |              | n           | 1               |

# Mode

```
all:
  accuracy: 0.9874
  precision: 0.8975
  recall: 0.8655
  support: 17751
ambiguous-tokens:
  accuracy: 0.959
  precision: 0.9135
  recall: 0.9083
  support: 2367
unknown-tokens:
  accuracy: 0.9401
  precision: 0.8435
  recall: 0.7618
  support: 1286
```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| ind      | 107          | _           | 63              |
|          |              | sub         | 30              |
|          |              | imp         | 11              |
|          |              | con         | 3               |
| _        | 51           | ind         | 45              |
|          |              | sub         | 3               |
|          |              | imp         | 3               |
| sub      | 37           | ind         | 29              |
|          |              | _           | 6               |
|          |              | imp         | 2               |
| imp      | 23           | ind         | 15              |
|          |              | _           | 7               |
|          |              | sub         | 1               |
| con      | 6            | ind         | 5               |
|          |              | _           | 1               |

# Degre

```
all:
  accuracy: 0.9826
  precision: 0.8529
  recall: 0.7672
  support: 17751
ambiguous-tokens:
  accuracy: 0.9502
  precision: 0.8221
  recall: 0.7648
  support: 3774
unknown-tokens:
  accuracy: 0.9432
  precision: 0.906
  recall: 0.6289
  support: 1286
```
| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| p        | 97           | _           | 80              |
|          |              | -           | 15              |
|          |              | s           | 2               |
| -        | 95           | _           | 74              |
|          |              | p           | 13              |
|          |              | s           | 6               |
|          |              | c           | 2               |
| _        | 95           | -           | 51              |
|          |              | p           | 44              |
| s        | 15           | -           | 9               |
|          |              | p           | 3               |
|          |              | _           | 3               |
| c        | 7            | -           | 4               |
|          |              | p           | 3               |

# Genre

```
all:
  accuracy: 0.9518
  precision: 0.9152
  recall: 0.8535
  support: 17751
ambiguous-tokens:
  accuracy: 0.9324
  precision: 0.9102
  recall: 0.8572
  support: 8308
unknown-tokens:
  accuracy: 0.8491
  precision: 0.8591
  recall: 0.6911
  support: 1286
```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| f        | 262          | m           | 220             |
|          |              | _           | 34              |
|          |              | x           | 5               |
|          |              | n           | 3               |
| m        | 253          | _           | 120             |
|          |              | f           | 99              |
|          |              | n           | 19              |
|          |              | x           | 15              |
| _        | 183          | m           | 132             |
|          |              | f           | 38              |
|          |              | n           | 8               |
|          |              | x           | 5               |
| n        | 125          | m           | 83              |
|          |              | _           | 36              |
|          |              | f           | 6               |
| x        | 32           | m           | 20              |
|          |              | f           | 7               |
|          |              | _           | 5               |


# Temps

```
all:
  accuracy: 0.9855
  precision: 0.9435
  recall: 0.9356
  support: 17751
ambiguous-tokens:
  accuracy: 0.9577
  precision: 0.9079
  recall: 0.9178
  support: 2459
unknown-tokens:
  accuracy: 0.9277
  precision: 0.8606
  recall: 0.7921
  support: 1286
```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| pst      | 97           | _           | 62              |
|          |              | psp         | 23              |
|          |              | ipf         | 10              |
|          |              | fut         | 2               |
| _        | 67           | pst         | 51              |
|          |              | psp         | 9               |
|          |              | fut         | 6               |
|          |              | ipf         | 1               |
| psp      | 47           | pst         | 18              |
|          |              | _           | 15              |
|          |              | ipf         | 13              |
|          |              | fut         | 1               |
| ipf      | 31           | _           | 11              |
|          |              | psp         | 7               |
|          |              | pst         | 7               |
|          |              | fut         | 6               |
| fut      | 16           | _           | 11              |
|          |              | pst         | 2               |
|          |              | psp         | 2               |
|          |              | ipf         | 1               |


# Nombre

```
all:
  accuracy: 0.9586
  precision: 0.94
  recall: 0.9366
  support: 17751
ambiguous-tokens:
  accuracy: 0.9429
  precision: 0.932
  recall: 0.9326
  support: 8700
unknown-tokens:
  accuracy: 0.8997
  precision: 0.8844
  recall: 0.8592
  support: 1286
```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| s        | 323          | p           | 183             |
|          |              | _           | 130             |
|          |              | x           | 10              |
| p        | 239          | s           | 212             |
|          |              | _           | 22              |
|          |              | x           | 5               |
| _        | 155          | s           | 132             |
|          |              | p           | 21              |
|          |              | x           | 2               |
| x        | 18           | s           | 13              |
|          |              | _           | 4               |
|          |              | p           | 1               |

# Personne

```
all:
  accuracy: 0.9786
  precision: 0.8593
  recall: 0.7747
  support: 17751
ambiguous-tokens:
  accuracy: 0.9599
  precision: 0.8549
  recall: 0.7799
  support: 5736
unknown-tokens:
  accuracy: 0.9362
  precision: 0.8728
  recall: 0.8226
  support: 1286
```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| 3        | 142          | _           | 93              |
|          |              | 1           | 42              |
|          |              | 2           | 5               |
|          |              | 0           | 2               |
| _        | 107          | 3           | 83              |
|          |              | 2           | 13              |
|          |              | 1           | 11              |
| 1        | 73           | 3           | 42              |
|          |              | _           | 21              |
|          |              | 2           | 10              |
| 2        | 41           | _           | 21              |
|          |              | 3           | 11              |
|          |              | 1           | 9               |
| 0        | 16           | 3           | 16              |
