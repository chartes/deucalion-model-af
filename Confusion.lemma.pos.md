Confusion tables
================

- [Lemma](#lemma)
- [POS ](#pos)

# Lemma


all:
  accuracy: 0.9696
  precision: 0.7547
  recall: 0.7558
  support: 50379
ambiguous-tokens:
  accuracy: 0.9665
  precision: 0.8003
  recall: 0.8011
  support: 26217
unknown-targets:
  accuracy: 0.7576
  precision: 0.3295
  recall: 0.3295
  support: 1242
unknown-tokens:
  accuracy: 0.6921
  precision: 0.4912
  recall: 0.4966
  support: 1627

| Expected         | Total Errors | Predictions       | Predicted times |
|------------------|--------------|-------------------|-----------------|
| que4             | 85           | que2              | 79              |
|                  |              | que1              | 4               |
|                  |              | qui               | 1               |
|                  |              | quel1             | 1               |
| que2             | 80           | que4              | 67              |
|                  |              | que3              | 6               |
|                  |              | qui               | 3               |
|                  |              | que1              | 2               |
|                  |              | cui               | 2               |
| que1             | 35           | que4              | 28              |
|                  |              | que2              | 5               |
|                  |              | cent              | 2               |
| avoir            | 29           | a3                | 22              |
|                  |              | öir               | 2               |
|                  |              | aidier            | 2               |
|                  |              | araire            | 1               |
|                  |              | un                | 1               |
|                  |              | et                | 1               |
| le               | 29           | il                | 28              |
|                  |              | se+le             | 1               |
| ne2              | 24           | ne1               | 24              |
| il               | 24           | le                | 21              |
|                  |              | là                | 2               |
|                  |              | el1               | 1               |
| ne1              | 16           | ne2               | 15              |
|                  |              | il                | 1               |
| que3             | 15           | que4              | 9               |
|                  |              | que2              | 6               |
| se               | 14           | soi1              | 7               |
|                  |              | si                | 5               |
|                  |              | ce1               | 2               |
| öir              | 12           | avoir             | 9               |
|                  |              | oir               | 3               |
| a3               | 12           | avoir             | 12              |
| si               | 11           | soi1              | 6               |
|                  |              | se                | 4               |
|                  |              | son4              | 1               |
| en1+le           | 9            | o3                | 6               |
|                  |              | il                | 2               |
|                  |              | estre1            | 1               |
| estre1           | 9            | ester             | 3               |
|                  |              | savoir            | 2               |
|                  |              | soi2              | 1               |
|                  |              | ez                | 1               |
|                  |              | avoir             | 1               |
|                  |              | etre              | 1               |
| cel              | 8            | cil               | 4               |
|                  |              | celer1            | 2               |
|                  |              | quel1             | 1               |
|                  |              | ce2               | 1               |
| on               | 8            | en1               | 4               |
|                  |              | en2               | 3               |
|                  |              | un                | 1               |
| en1              | 8            | en2               | 6               |
|                  |              | on                | 2               |
| en2              | 7            | en1               | 6               |
|                  |              | on                | 1               |
| ‘                | 7            | ''''              | 6               |
|                  |              |                   | 1               |
| ce2              | 7            | ce1               | 6               |
|                  |              | son4              | 1               |
| soi1             | 7            | se                | 5               |
|                  |              | si                | 2               |
| savoir           | 7            | estre1            | 4               |
|                  |              | sivre             | 2               |
|                  |              | sachier2          | 1               |
| ''''             | 6            | ‘                 | 6               |
| entre            | 6            | entre2            | 5               |
|                  |              | entrer            | 1               |
| donc             | 6            | dont              | 4               |
|                  |              | don               | 2               |
| conte1           | 6            | conter            | 3               |
|                  |              | conte2            | 3               |
| où               | 6            | o3                | 5               |
|                  |              | en1+le            | 1               |
| saint            | 6            | saint1            | 5               |
|                  |              | saintisme         | 1               |
| livre2           | 6            | livre3            | 6               |
| par              | 6            | por2              | 6               |
| cui              | 6            | qui               | 5               |
|                  |              | que2              | 1               |
| là               | 6            | il                | 4               |
|                  |              | le                | 2               |
| bien2            | 6            | bien1             | 6               |
| ainz             | 6            | ainc              | 5               |
|                  |              | enz               | 1               |
| corir            | 5            | cort1             | 1               |
|                  |              | cort2             | 1               |
|                  |              | acorre            | 1               |
|                  |              | querre            | 1               |
|                  |              | cure              | 1               |
| nos1             | 5            | nostre            | 4               |
|                  |              | nul               | 1               |
| vivre1           | 5            | vëoir             | 4               |
|                  |              | vif               | 1               |
| jesu             | 5            | jhesu             | 5               |
| tant             | 5            | atant             | 3               |
|                  |              | tens              | 1               |
|                  |              | tendre1           | 1               |
| nom              | 4            | non               | 4               |
| ainc             | 4            | ainz              | 4               |
| suen             | 4            | savoir            | 2               |
|                  |              | si                | 1               |
|                  |              | sëoir             | 1               |
| cant2            | 4            | cant1             | 2               |
|                  |              | cantque           | 2               |
| mort             | 4            | morir             | 4               |
| o3               | 4            | où                | 3               |
|                  |              | en1+le            | 1               |
| son4             | 4            | soz               | 1               |
|                  |              | si+il             | 1               |
|                  |              | si                | 1               |
|                  |              | soi1              | 1               |
| entre2           | 4            | entre             | 4               |
| dan2             | 4            | damnedeu          | 4               |
| ester            | 4            | estre1            | 3               |
|                  |              | estovoir1         | 1               |
| vostre           | 4            | vos               | 4               |
| cest             | 4            | ce2               | 4               |
| maint            | 3            | moins             | 1               |
|                  |              | mente_comunaument | 1               |
|                  |              | ment              | 1               |
| ticius           | 3            | tyces             | 3               |
| däerrain         | 3            | desraison         | 1               |
|                  |              | desrine           | 1               |
|                  |              | derrenier         | 1               |
| dont             | 3            | donc              | 3               |
| vos              | 3            | vostre            | 3               |
| oir              | 3            | öir               | 3               |
| tendre1          | 3            | tendre2           | 3               |
| ome              | 3            | heaume            | 1               |
|                  |              | on                | 1               |
|                  |              | enemi             | 1               |
| laissier         | 3            | laiier2           | 1               |
|                  |              | là                | 1               |
|                  |              | lait2             | 1               |
| trieves          | 3            | trieue            | 3               |
| qui              | 3            | cui               | 1               |
|                  |              | qui+il            | 1               |
|                  |              | que4              | 1               |
| prendre          | 3            | priier            | 1               |
|                  |              | prest1            | 1               |
|                  |              | pendre            | 1               |
| fuir             | 3            | estre1            | 3               |
| plein            | 3            | plenier2          | 1               |
|                  |              | plain             | 1               |
|                  |              | plaigne           | 1               |
| plain            | 3            | plein             | 3               |
| hericier         | 3            | errecier          | 2               |
|                  |              | hercier           | 1               |
| ore3             | 3            | ëur               | 2               |
|                  |              | or4               | 1               |
| repaire          | 3            | repairier         | 3               |
| mais1            | 3            | mon1              | 2               |
|                  |              | mes4              | 1               |
| paroir           | 3            | perdre            | 2               |
|                  |              | parent            | 1               |
| oïr              | 3            | oir               | 3               |
| issir            | 3            | user              | 2               |
|                  |              | estre1            | 1               |
| faire            | 3            | ferir             | 1               |
|                  |              | fait1             | 1               |
|                  |              | fachier           | 1               |
| avoiier          | 3            | avoir             | 2               |
|                  |              | avenant           | 1               |
| si+il            | 3            | son4              | 2               |
|                  |              | sauf              | 1               |
| bien1            | 3            | bien2             | 3               |
| sen2             | 3            | sanc              | 3               |
| non              | 3            | nom               | 3               |
| ainsi            | 3            | ainz              | 1               |
|                  |              | ainsier           | 1               |
|                  |              | ainçois           | 1               |
| pro              | 3            | prodome           | 3               |
| pris1            | 3            | prendre           | 2               |
|                  |              | prisier           | 1               |
| gent2            | 3            | gent1             | 3               |
| mon1             | 3            | mais1             | 2               |
|                  |              | je                | 1               |
| vëoir            | 3            | aler              | 1               |
|                  |              | vendre            | 1               |
|                  |              | voloir            | 1               |
| liier3           | 2            | lié1              | 2               |
| mesfaire         | 2            | mesfait           | 2               |
| maine            | 2            | main2             | 2               |
| sire2            | 2            | seignor           | 2               |
| pur              | 2            | por2              | 2               |
| mossu            | 2            | mosdre1           | 1               |
|                  |              | mosder2           | 1               |
| conte2           | 2            | conte1            | 2               |
| sor1             | 2            | sort2             | 1               |
|                  |              | sore              | 1               |
| changier         | 2            | chargier          | 1               |
|                  |              | changois          | 1               |
| flambe           | 2            | flame             | 2               |
| entrer           | 2            | entree            | 1               |
|                  |              | entre             | 1               |
| laiier2          | 2            | laissier          | 2               |
| löer2            | 2            | löer1             | 2               |
| emperëor         | 2            | emperir           | 1               |
|                  |              | empererriz        | 1               |
| douz             | 2            | dote              | 1               |
|                  |              | doze              | 1               |
| sëoir            | 2            | soiier            | 1               |
|                  |              | si+il             | 1               |
| valoir           | 2            | vëoir             | 1               |
|                  |              | vaillant          | 1               |
| legier2          | 2            | legierement       | 2               |
| esprisier        | 2            | esprendre2        | 1               |
|                  |              | espresser         | 1               |
| escharpe         | 2            | eschaper          | 2               |
| guimer           | 2            | guirmart          | 1               |
|                  |              | gui               | 1               |
| deus             | 2            | dieu              | 1               |
|                  |              | devoir            | 1               |
| metre2           | 2            | mais1             | 1               |
|                  |              | mon1              | 1               |
| forclore         | 2            | forsencler        | 1               |
|                  |              | forcler2          | 1               |
| morir            | 2            | mort              | 2               |
| estovoir1        | 2            | ester             | 1               |
|                  |              | estout            | 1               |
| devëer           | 2            | desver            | 1               |
|                  |              | desvoiier1        | 1               |
| sain             | 2            | saint             | 2               |
| present1         | 2            | present2          | 2               |
| charretier       | 2            | charriere         | 2               |
| fil1             | 2            | fil2              | 2               |
| desesperer       | 2            | dessevrer         | 2               |
| encontre1        | 2            | encontre2         | 1               |
|                  |              | encontrer         | 1               |
| encensier        | 2            | ancensier         | 1               |
|                  |              | encenser2         | 1               |
| tot              | 2            | tost1             | 2               |
| despire          | 2            | desrompre         | 1               |
|                  |              | despit            | 1               |
| foie2            | 2            | foiiee            | 2               |
| lieue            | 2            | lieu              | 1               |
|                  |              | lit1              | 1               |
| sauver           | 2            | salir2            | 2               |
| lieu             | 2            | il                | 1               |
|                  |              | le                | 1               |
| amer1            | 2            | belamer           | 1               |
|                  |              | ainc              | 1               |
| ez               | 2            | ester             | 1               |
|                  |              | estre1            | 1               |
| sor2             | 2            | sore              | 1               |
|                  |              | sol1              | 1               |
| prevoste         | 2            | prevost           | 2               |
| raconter         | 2            | reconter          | 2               |
| tor5             | 2            | tornoi            | 1               |
|                  |              | tor2              | 1               |
| rejeter          | 2            | regner            | 1               |
|                  |              | rejehir           | 1               |
| häir             | 2            | aler              | 1               |
|                  |              | errer2            | 1               |
| aler             | 2            | ageler            | 1               |
|                  |              | alöer2            | 1               |
| clore            | 2            | clos              | 2               |
| fil2             | 2            | fiel              | 2               |
| seignier         | 2            | saignier          | 2               |
| errant           | 2            | errer2            | 2               |
| desus            | 2            | desoz             | 2               |
| fief             | 2            | fier              | 1               |
|                  |              | fil2              | 1               |
| forment          | 2            | forment2          | 2               |
| col              | 2            | come1             | 1               |
|                  |              | coup1             | 1               |
| quiter           | 2            | cuidier1          | 1               |
|                  |              | quite             | 1               |
| chëoir           | 2            | chaufer           | 1               |
|                  |              | chaitier          | 1               |
| complie          | 2            | complir           | 2               |
| avenant          | 2            | avenir            | 2               |
| nuef1            | 2            | deus              | 1               |
|                  |              | il                | 1               |
| durer            | 2            | devoir            | 2               |
| anjou            | 2            | anjon             | 1               |
|                  |              | angonc            | 1               |
| çoper            | 2            | coper             | 1               |
|                  |              | cöaper            | 1               |
| a3+le            | 2            | où                | 1               |
|                  |              | il                | 1               |
| aidier           | 2            | äie               | 1               |
|                  |              | avoir             | 1               |
| plovoir          | 2            | plaire            | 1               |
|                  |              | plus              | 1               |
| jaques           | 2            | saint-jaques      | 1               |
|                  |              | saint-jacques     | 1               |
| avenir           | 2            | avenant           | 2               |
| soir             | 2            | serf              | 1               |
|                  |              | seignor           | 1               |
| gant             | 2            | gent1             | 2               |
| enföir1          | 2            | arle              | 1               |
|                  |              | enföir2           | 1               |
| priier           | 2            | prendre           | 1               |
|                  |              | priant            | 1               |
| monseignor       | 2            | seignor           | 2               |
| some3            | 2            | some2             | 2               |
| verai            | 2            | veraiement        | 2               |
| devoir           | 2            | doter2            | 1               |
|                  |              | doi               | 1               |
| logier           | 2            | loge              | 1               |
|                  |              | loere             | 1               |
| veinquëor        | 2            | veinqure          | 1               |
|                  |              | veinque           | 1               |
| oser             | 2            | oster2            | 1               |
|                  |              | os2               | 1               |
| un               | 2            | i2                | 2               |
| autel2           | 2            | autel1            | 2               |
| ersoir           | 2            | arison            | 2               |
| voloir           | 2            | vos               | 2               |
| refaire2         | 2            | refaire1          | 1               |
|                  |              | referaistre       | 1               |
| lé               | 2            | lez               | 1               |
|                  |              | lait1             | 1               |
| cuidier1         | 2            | quiti(s           | 1               |
|                  |              | querre            | 1               |
| decisïon         | 2            | desciti-ïon       | 1               |
|                  |              | decissïon         | 1               |
| tel              | 1            | atelie            | 1               |
| morsel           | 1            | mors1             | 1               |
| apercevoir       | 1            | esperchier        | 1               |
| invasïon         | 1            | jevancier2        | 1               |
| tierce           | 1            | tierz             | 1               |
| geste1           | 1            | geste2            | 1               |
| cote1            | 1            | cote2             | 1               |
| emparler         | 1            | emparlé           | 1               |
| tost1            | 1            | tot               | 1               |
| jöir             | 1            | jöer              | 1               |
| celebrer         | 1            | celer1            | 1               |
| tandis           | 1            | tendre1           | 1               |
| a3+il            | 1            | a3+le             | 1               |
| resmaiier        | 1            | remanoir          | 1               |
| vëer             | 1            | vëoir             | 1               |
| colëiz           | 1            | colede            | 1               |
| gramairiien      | 1            | gramain           | 1               |
| retoriien        | 1            | retorin           | 1               |
| müer             | 1            | mu1               | 1               |
| agnies           | 1            | agnigier          | 1               |
| cecile           | 1            | chaille           | 1               |
| madelaine        | 1            | madelagne         | 1               |
| raisnier         | 1            | resenerir         | 1               |
| puiz             | 1            | puis              | 1               |
| gatanie          | 1            | gante             | 1               |
| chevelet         | 1            | chevel            | 1               |
| grece            | 1            | griec             | 1               |
| prometre         | 1            | premerain         | 1               |
| ademander        | 1            | adementer         | 1               |
| desvoiier1       | 1            | devoir            | 1               |
| amende1          | 1            | amender           | 1               |
| auvergne         | 1            | avigne            | 1               |
| noé              | 1            | noeus             | 1               |
| arche2           | 1            | arche             | 1               |
| röer2            | 1            | röer1             | 1               |
| voiage           | 1            | venjance          | 1               |
| tor4             | 1            | tor2              | 1               |
| entrespargnier   | 1            | entrespagrer      | 1               |
| jangle           | 1            | gengele           | 1               |
| craisse          | 1            | graisse           | 1               |
| celer1           | 1            | cel               | 1               |
| plait            | 1            | plaire            | 1               |
| atendre          | 1            | ataindre          | 1               |
| maleoit          | 1            | malëir            | 1               |
| aluec            | 1            | alus              | 1               |
| mëur             | 1            | mor1              | 1               |
| puille           | 1            | puile             | 1               |
| sicile           | 1            | seillise          | 1               |
| apareillier1     | 1            | aparoir           | 1               |
| taire            | 1            | ton4              | 1               |
| si+en2           | 1            | si                | 1               |
| ramponos         | 1            | ramponer          | 1               |
| questain         | 1            | coistain          | 1               |
| danois           | 1            | denois            | 1               |
| pervers          | 1            | perver            | 1               |
| ravoir2          | 1            | raler             | 1               |
| encombrier       | 1            | encombrer         | 1               |
| engignier1       | 1            | engendrer1        | 1               |
| guichet          | 1            | guinchet          | 1               |
| coster1          | 1            | cosdre            | 1               |
| perche2          | 1            | perche1           | 1               |
| don              | 1            | donc              | 1               |
| par2             | 1            | por2              | 1               |
| constance        | 1            | costantinos       | 1               |
| envoiier         | 1            | enjoindre         | 1               |
| reson            | 1            | raison            | 1               |
| mëismes          | 1            | mëisme            | 1               |
| montant          | 1            | montaigne         | 1               |
| liier1           | 1            | liier3            | 1               |
| cinquisme        | 1            | cinquise          | 1               |
| bienëuré         | 1            | benëir            | 1               |
| cele             | 1            | ciel              | 1               |
| duchoise1        | 1            | docoistre         | 1               |
| priiere          | 1            | präerie           | 1               |
| escordement1     | 1            | escordement       | 1               |
| renomer          | 1            | renomee           | 1               |
| waraingle        | 1            | valoir            | 1               |
| deça             | 1            | dece              | 1               |
| dela             | 1            | delaiier1         | 1               |
| justien          | 1            | justinien         | 1               |
| enteimes         | 1            | entente           | 1               |
| carante          | 1            | il                | 1               |
| vanter           | 1            | vendre            | 1               |
| desenseignier    | 1            | dessener          | 1               |
| escüele          | 1            | escuel            | 1               |
| a2               | 1            | ha                | 1               |
| inocent          | 1            | inneci            | 1               |
| remener          | 1            | remanoir          | 1               |
| esveil           | 1            | esveille          | 1               |
| entressaiier     | 1            | entresaitier      | 1               |
| sarge            | 1            | sargres           | 1               |
| erumprez         | 1            | ordremore         | 1               |
| mulot2           | 1            | mulet3            | 1               |
| ambler           | 1            | embler            | 1               |
| oncle            | 1            | oncler            | 1               |
| esforz1          | 1            | efroire           | 1               |
| o4               | 1            | o3                | 1               |
| intencïon        | 1            | entencïon         | 1               |
| refuse           | 1            | refuser           | 1               |
| boise2           | 1            | bois              | 1               |
| rementevoir      | 1            | ramentevoir       | 1               |
| brusler          | 1            | bruillier         | 1               |
| espaignol        | 1            | espagne           | 1               |
| manee            | 1            | mener             | 1               |
| cordes           | 1            | corde             | 1               |
| gemé             | 1            | gamer             | 1               |
| tenir1           | 1            | tendre1           | 1               |
| targier2         | 1            | targe1            | 1               |
| ceinture         | 1            | chaitine          | 1               |
| prinseignier     | 1            | prendre           | 1               |
| doner            | 1            | durer             | 1               |
| vivre2           | 1            | vivre1            | 1               |
| vestement        | 1            | vestiment         | 1               |
| estable          | 1            | estable1          | 1               |
| desirrer         | 1            | descirier         | 1               |
| forcele          | 1            | forcele1          | 1               |
| coree            | 1            | corir             | 1               |
| present2         | 1            | present1          | 1               |
| vaillant         | 1            | valoir            | 1               |
| tüel             | 1            | toille            | 1               |
| esblöir          | 1            | embler            | 1               |
| ensemble         | 1            | ensemel           | 1               |
| dent2            | 1            | dan2              | 1               |
| moiuel1          | 1            | möel              | 1               |
| peinture         | 1            | pointure          | 1               |
| porpre1          | 1            | propre            | 1               |
| cincante         | 1            | le                | 1               |
| arapater         | 1            | araparer          | 1               |
| vantance         | 1            | maisoncele        | 1               |
| claudas          | 1            | claudie           | 1               |
| voirre           | 1            | voir              | 1               |
| aveuc            | 1            | avuec             | 1               |
| trenchier1       | 1            | tranter           | 1               |
| paumeton         | 1            | paument           | 1               |
| obëir            | 1            | oblie             | 1               |
| tabriol          | 1            | carduel           | 1               |
| membre           | 1            | membrer2          | 1               |
| trinité          | 1            | trinite           | 1               |
| porsivre         | 1            | porsëoir2         | 1               |
| reguignier       | 1            | rejuginer         | 1               |
| chevelu          | 1            | chevel            | 1               |
| chauf            | 1            | chaufe            | 1               |
| brachant         | 1            | brachier          | 1               |
| coute            | 1            | coste2            | 1               |
| roster1          | 1            | resover           | 1               |
| sainteté         | 1            | sainter           | 1               |
| texte            | 1            | titre             | 1               |
| rencomencier     | 1            | rencomancier      | 1               |
| basme            | 1            | baume             | 1               |
| e2               | 1            | et                | 1               |
| comant           | 1            | comandement       | 1               |
| ivel             | 1            | oleme             | 1               |
| tai              | 1            | taire             | 1               |
| lointain         | 1            | loingïe           | 1               |
| guerrer          | 1            | guerroiier2       | 1               |
| turcople         | 1            | turchier          | 1               |
| chargier         | 1            | carchié           | 1               |
| après            | 1            | emprès            | 1               |
| delivre2         | 1            | delivre1          | 1               |
| voir             | 1            | vair1             | 1               |
| termes           | 1            | terme             | 1               |
| ier              | 1            | erz               | 1               |
| mors1            | 1            | mort              | 1               |
| come1            | 1            | que4              | 1               |
| alerïon          | 1            | alerin            | 1               |
| saint-omer       | 1            | saintemoin        | 1               |
| bolir            | 1            | boter1            | 1               |
| ferir            | 1            | fier              | 1               |
| acolite          | 1            | acoillir          | 1               |
| charles          | 1            | charlemagne       | 1               |
| testiere         | 1            | teste             | 1               |
| ote              | 1            | otinel            | 1               |
| arrement         | 1            | arment            | 1               |
| pereços          | 1            | perece            | 1               |
| covenant         | 1            | covenir           | 1               |
| amenistreor      | 1            | amenistrer        | 1               |
| francagel        | 1            | françois          | 1               |
| sauvagine        | 1            | sauvage           | 1               |
| renoncier        | 1            | renomer           | 1               |
| repöoir          | 1            | reposer           | 1               |
| lïon             | 1            | lon               | 1               |
| serpent          | 1            | serpir            | 1               |
| pierre           | 1            | pere              | 1               |
| acorionde        | 1            | acorder           | 1               |
| esche            | 1            | asche2            | 1               |
| fole             | 1            | fol3              | 1               |
| frere            | 1            | fraire            | 1               |
| fëon             | 1            | fais              | 1               |
| alfamie          | 1            | alfanie           | 1               |
| comandëor        | 1            | comander          | 1               |
| herbergement     | 1            | herbergerement    | 1               |
| felon            | 1            | felonie           | 1               |
| livrer           | 1            | livre2            | 1               |
| doter1           | 1            | doter2            | 1               |
| valüe            | 1            | valee             | 1               |
| mentir           | 1            | mente             | 1               |
| naïmant          | 1            | naimes            | 1               |
| espiet           | 1            | espiier1          | 1               |
| tarir            | 1            | targier2          | 1               |
| traire           | 1            | trover            | 1               |
| despendre1       | 1            | despendre2        | 1               |
| eschëoite        | 1            | eschaiement       | 1               |
| ueil             | 1            | ol1               | 1               |
| coche1           | 1            | couchier          | 1               |
| vis2             | 1            | vif               | 1               |
| corjon           | 1            | corin             | 1               |
| catre            | 1            | trois             | 1               |
| entr'acompagnier | 1            | entracompagnier   | 1               |
| tref2            | 1            | tref1             | 1               |
| luitier          | 1            | luite             | 1               |
| losengier2       | 1            | losenge2          | 1               |
| renluminer       | 1            | renumer           | 1               |
| aparmain         | 1            | aparoin           | 1               |
| cant1            | 1            | cant2             | 1               |
| doiz             | 1            | doi               | 1               |
| dïaspre          | 1            | desdëart          | 1               |
| livre1           | 1            | livre3            | 1               |
| lombardie        | 1            | lumbardie         | 1               |
| orlëure          | 1            | olorir            | 1               |
| perece           | 1            | parestie          | 1               |
| seur             | 1            | sor2              | 1               |
| lez              | 1            | lé                | 1               |
| hai!             | 1            | e2                | 1               |
| bot1             | 1            | bot4              | 1               |
| uisseüre         | 1            | fuerëor           | 1               |
| deporter         | 1            | emporter2         | 1               |
| gondri           | 1            | gondip            | 1               |
| soshaucier       | 1            | sostenir          | 1               |
| sidoine          | 1            | sidon             | 1               |
| noradin          | 1            | loradrain         | 1               |
| ane              | 1            | asne              | 1               |
| pestilence       | 1            | pesticele         | 1               |
| astrenomie       | 1            | astrencement      | 1               |
| carthage         | 1            | cartage           | 1               |
| rëondement       | 1            | romprement        | 1               |
| laiton           | 1            | latin             | 1               |
| estraim          | 1            | estrain           | 1               |
| denis            | 1            | saint-denis       | 1               |
| tozjors          | 1            | torjor            | 1               |
| tresfiner        | 1            | trenfigier        | 1               |
| set              | 1            | savoir            | 1               |
| vis1             | 1            | vif               | 1               |
| fier             | 1            | fer               | 1               |
| chastel          | 1            | chatel            | 1               |
| croistre         | 1            | croire            | 1               |
| esloissier       | 1            | esloisir          | 1               |
| joseph           | 1            | josepez           | 1               |
| justicier2       | 1            | justice           | 1               |
| ici              | 1            | issir             | 1               |
| acomparagier     | 1            | acompagnier       | 1               |
| saint1           | 1            | saint             | 1               |
| maudit           | 1            | maudire           | 1               |
| forsenage        | 1            | forsenerie        | 1               |
| no1              | 1            | nos               | 1               |
| aprentiz         | 1            | aprendre          | 1               |
| bigot            | 1            | bigue             | 1               |
| atant            | 1            | il                | 1               |
| devaler          | 1            | desvaler          | 1               |
| marbri           | 1            | marbrir           | 1               |
| arester          | 1            | reravaire         | 1               |
| repromissïon     | 1            | reponcïon         | 1               |
| lidorius         | 1            | lydorie           | 1               |
| baril            | 1            | barrie            | 1               |
| esclados         | 1            | esclat            | 1               |
| verdor           | 1            | verdëor           | 1               |
| escrever         | 1            | escrire           | 1               |
| message1         | 1            | message2          | 1               |
| pel1             | 1            | pal               | 1               |
| trois+cent       | 1            | cent              | 1               |
| fauz             | 1            | faus              | 1               |
| deversité        | 1            | diverseté         | 1               |
| mil1             | 1            | je                | 1               |
| fais             | 1            | faire             | 1               |
| pers             | 1            | per               | 1               |
| mont             | 1            | monde1            | 1               |
| saint-michel     | 1            | michiel           | 1               |
| je+le            | 1            | je+il             | 1               |
| traitier         | 1            | traire            | 1               |
| namur            | 1            | nazmor            | 1               |
| some2            | 1            | some3             | 1               |
| secorer          | 1            | secorre1          | 1               |
| ardor            | 1            | ardre             | 1               |
| flore            | 1            | flaviz            | 1               |
| lait2            | 1            | lait3             | 1               |
| penser           | 1            | paistre           | 1               |
| mongiu           | 1            | mongilon          | 1               |
| temple3          | 1            | temple1           | 1               |
| salomon          | 1            | salemon           | 1               |
| äimant           | 1            | amien             | 1               |
| keu              | 1            | que2+il           | 1               |
| alener           | 1            | aleine            | 1               |
| comune           | 1            | comun             | 1               |
| hostilius        | 1            | oviles            | 1               |
| pëor             | 1            | pöoir             | 1               |
| hernaut          | 1            | herant            | 1               |
| acier            | 1            | achier            | 1               |
| dragoncel        | 1            | dragoncle         | 1               |
| saner            | 1            | saignier          | 1               |
| asservir         | 1            | asseoir           | 1               |
| precier          | 1            | prëechier         | 1               |
| pié              | 1            | poi               | 1               |
| lait1            | 1            | lé                | 1               |
| covir            | 1            | covenir           | 1               |
| sulïant          | 1            | sivre             | 1               |
| bastir           | 1            | batre             | 1               |
| repaiier         | 1            | repairier         | 1               |
| demore           | 1            | demorer           | 1               |
| secorre1         | 1            | secors            | 1               |
| oiance           | 1            | oigne             | 1               |
| dent1            | 1            | adens             | 1               |
| chainsil         | 1            | chaillon          | 1               |
| paistre          | 1            | postre            | 1               |
| fun              | 1            | fum               | 1               |
| lober            | 1            | lobier            | 1               |
| setme            | 1            | semer1            | 1               |
| ardre            | 1            | hardi             | 1               |
| deluge           | 1            | diligent          | 1               |
| parfaire         | 1            | parfait           | 1               |
| gaster           | 1            | gast1             | 1               |
| tolir            | 1            | tot               | 1               |
| percier          | 1            | porcier2          | 1               |
| piscenie         | 1            | pisence           | 1               |
| devin2           | 1            | devin1            | 1               |
| tort2            | 1            | tours             | 1               |
| oier             | 1            | oir               | 1               |
| ferement         | 1            | ferrement         | 1               |
| entier           | 1            | entir             | 1               |
| armaire          | 1            | amor              | 1               |
| mes4             | 1            | mon1              | 1               |
| las              | 1            | he_las            | 1               |
| öil              | 1            | onc               | 1               |
| enchapeler       | 1            | enchaper          | 1               |
| mes3             | 1            | mon1              | 1               |
| atenir           | 1            | atendre           | 1               |
| catorzime        | 1            | catorne)          | 1               |
| fëel             | 1            | felon             | 1               |
| faille1          | 1            | faille3           | 1               |
| ensancmesler     | 1            | ensembler         | 1               |
| chiere           | 1            | chier             | 1               |
| cesaire          | 1            | cesar             | 1               |
| chenir           | 1            | chëoir            | 1               |
| alöer1           | 1            | alöer2            | 1               |
| tire1            | 1            | tire2             | 1               |
| aele             | 1            | aiuele            | 1               |
| pöoir            | 1            | poissant          | 1               |
| oisos            | 1            | oisel             | 1               |
| croiz            | 1            | crucefiier        | 1               |
| nef2             | 1            | nés               | 1               |
| paisible         | 1            | parmanable        | 1               |
| or1              | 1            | ors               | 1               |
| ancessor         | 1            | anceor            | 1               |
| patronage        | 1            | patremoine        | 1               |
| haitement        | 1            | haitieement       | 1               |
| feste            | 1            | feste1            | 1               |
| son3             | 1            | son1              | 1               |
| lié1             | 1            | lé                | 1               |
| salatrés         | 1            | salirater         | 1               |
| fouchier         | 1            | forchier          | 1               |
| arc              | 1            | ardre             | 1               |
| enföir2          | 1            | enfuser           | 1               |
| envenimëor       | 1            | envolier          | 1               |
| mescrëant        | 1            | mescroire         | 1               |
| atorner          | 1            | ateler            | 1               |
| os2              | 1            | ost               | 1               |
| somer            | 1            | somenir           | 1               |
| laver            | 1            | lever             | 1               |
| voler            | 1            | voloir            | 1               |
| jante1           | 1            | gent2             | 1               |
| resortir         | 1            | restre            | 1               |
| cinc             | 1            | cent              | 1               |
| forfait          | 1            | forfaire          | 1               |
| umble            | 1            | honble            | 1               |
| servïable        | 1            | serviable         | 1               |
| deschaitiver     | 1            | decheiefier       | 1               |
| sanc             | 1            | sens              | 1               |
| grieu            | 1            | grec              | 1               |
| guenes           | 1            | ganelon           | 1               |
| foillu           | 1            | folos             | 1               |
| sauvëor          | 1            | sauver            | 1               |
| garantissëor     | 1            | garantisorie      | 1               |
| poing            | 1            | puis              | 1               |
| coper            | 1            | cope1             | 1               |
| roidement        | 1            | redement          | 1               |
| roit1            | 1            | redoter1          | 1               |
| grëer            | 1            | gras              | 1               |
| frois2           | 1            | frois1            | 1               |
| alentir          | 1            | eslantier         | 1               |
| sospite          | 1            | sospiter          | 1               |
| affricant        | 1            | afrique           | 1               |
| sovin            | 1            | solivent          | 1               |
| tisteresce       | 1            | tristece          | 1               |
| chaille          | 1            | ciel              | 1               |
| chalende         | 1            | kalende           | 1               |
| levre            | 1            | lievre            | 1               |
| joier            | 1            | jöer              | 1               |
| monde2           | 1            | monde1            | 1               |
| nüe              | 1            | nu1               | 1               |
| rentiz           | 1            | rentir            | 1               |
| rose             | 1            | ros3              | 1               |
| lais             | 1            | lez               | 1               |
| renge2           | 1            | renge1            | 1               |
| los1             | 1            | lou               | 1               |
| resoignier       | 1            | ressoignier       | 1               |
| mahumet          | 1            | mohom             | 1               |
| raison           | 1            | restre            | 1               |
| voisdie          | 1            | voistois          | 1               |
| veillerie        | 1            | veillier2         | 1               |
| cors2            | 1            | cuer2             | 1               |
| massi            | 1            | massiz            | 1               |
| trone            | 1            | tronse            | 1               |
| prodome          | 1            | pro               | 1               |
| conter           | 1            | conte1            | 1               |
| longement        | 1            | longement2        | 1               |
| gracien          | 1            | gracin            | 1               |
| despit           | 1            | despire           | 1               |
| sëur2            | 1            | sor1              | 1               |
| guingomar        | 1            | guinganbresil     | 1               |
| onestement       | 1            | oneste            | 1               |
| vigile           | 1            | vigele            | 1               |
| trait            | 1            | traire            | 1               |
| mener            | 1            | moine1            | 1               |
| vezïé            | 1            | vëoir             | 1               |
| perpetuus        | 1            | valentinien       | 1               |
| ferrant          | 1            | ferir             | 1               |
| ferëiz           | 1            | ferir             | 1               |
| esteindre        | 1            | ester             | 1               |
| flamesche        | 1            | flame             | 1               |
| antiene          | 1            | entevel           | 1               |
| comé             | 1            | comencier         | 1               |
| föir             | 1            | fuir              | 1               |
| deseur(e)        | 1            | desor             | 1               |
| pardonement      | 1            | pordement         | 1               |
| resconser        | 1            | rescorre          | 1               |
| reflamboiier     | 1            | reflambir         | 1               |
| esploitier       | 1            | eslaistre         | 1               |
| movoir           | 1            | müir2             | 1               |
| respondre1       | 1            | response          | 1               |
| descochier1      | 1            | descochier        | 1               |
| euvagius         | 1            | evagu             | 1               |
| contendre        | 1            | contenir          | 1               |
| nés              | 1            | nëis              | 1               |
| singe            | 1            | signe1            | 1               |
| destrosser       | 1            | destroistre       | 1               |
| enamer           | 1            | enmaner           | 1               |
| crïator          | 1            | crïature          | 1               |
| esforcier2       | 1            | esforcier1        | 1               |
| boniface         | 1            | bonefauté         | 1               |
| mivoie           | 1            | mivüe             | 1               |
| assemblee        | 1            | assembler         | 1               |
| evesque          | 1            | veinque           | 1               |
| terrion          | 1            | terrïon           | 1               |
| descovrir        | 1            | descorder1        | 1               |
| trebace          | 1            | trebelliant       | 1               |
| manche2          | 1            | mace              | 1               |
| arcediacne       | 1            | marchëant         | 1               |
| laurante         | 1            | laure             | 1               |
| lumbardie        | 1            | lombardie         | 1               |
| fein             | 1            | faim              | 1               |
| resplenir        | 1            | replenier         | 1               |
| seneficacïon     | 1            | sentisïon         | 1               |
| eusebius         | 1            | evois             | 1               |
| remander         | 1            | remanoir          | 1               |
| ameor            | 1            | amer2             | 1               |
| uit              | 1            | set               | 1               |
| coutre           | 1            | coutré            | 1               |
| juene            | 1            | jombe2            | 1               |
| emplir           | 1            | amplir            | 1               |
| desert2          | 1            | desert1           | 1               |
| pic2             | 1            | piz               | 1               |
| racheminer       | 1            | rachier2          | 1               |
| porparler        | 1            | porperlaire       | 1               |
| alaitier         | 1            | aler              | 1               |
| arimathie        | 1            | arimatie          | 1               |
| chemin           | 1            | chäeine           | 1               |
| quel1            | 1            | que2+il           | 1               |
| tendre2          | 1            | tendre1           | 1               |
| culvert          | 1            | covrier           | 1               |
| fermeté          | 1            | formeté           | 1               |
| ostel            | 1            | oster2            | 1               |
| pentecoste1      | 1            | pentecoste        | 1               |
| hupe             | 1            | huepe             | 1               |
| samsun           | 1            | sanses            | 1               |
| bone             | 1            | bon               | 1               |
| soie2            | 1            | soi1              | 1               |
| doloir           | 1            | dolent            | 1               |
| tantalis         | 1            | tantalin          | 1               |
| detenement       | 1            | deteniere         | 1               |
| vivant           | 1            | vivre1            | 1               |
| ventrail         | 1            | ventre1           | 1               |
| excepcïon        | 1            | escepcïon         | 1               |
| ente             | 1            | hanste            | 1               |
| concevement      | 1            | conseil           | 1               |
| alegement        | 1            | alegant           | 1               |
| des2             | 1            | de+le             | 1               |
| faissel          | 1            | faillier1         | 1               |
| arragon          | 1            | aragon            | 1               |
| estrange         | 1            | estrangier2       | 1               |
| bucie            | 1            | burie             | 1               |
| risoaudus        | 1            | ruspit            | 1               |
| eucherius        | 1            | euchion           | 1               |
| celsus           | 1            | clasun            | 1               |
| devenir          | 1            | deviser           | 1               |
| air1             | 1            | air2              | 1               |
| or4              | 1            | or1               | 1               |
| nëel1            | 1            | noil              | 1               |
| fabur            | 1            | faurbre           | 1               |
| ogre             | 1            | orgene            | 1               |
| ars              | 1            | ardre             | 1               |
| conquester       | 1            | conquerre         | 1               |
| sorcot           | 1            | sorcuier          | 1               |
| sens             | 1            | serf              | 1               |
| introduire       | 1            | entredout         | 1               |
| pardoner         | 1            | pordin            | 1               |
| larmoiier        | 1            | larmer            | 1               |
| fils2            | 1            | fil2              | 1               |
| vers1            | 1            | vers2             | 1               |
| doible           | 1            | dïable            | 1               |
| benëir           | 1            | beneoit           | 1               |
| deraisnier       | 1            | desraisnier       | 1               |
| rescosse         | 1            | recusse           | 1               |
| dusque           | 1            | donc              | 1               |
| mi2              | 1            | mie               | 1               |
| dure             | 1            | dur               | 1               |
| mercure          | 1            | mercurie          | 1               |
| pui              | 1            | puiz              | 1               |
| blasmer          | 1            | blasme            | 1               |
| guischart        | 1            | guistance         | 1               |
| aclarir          | 1            | aclareillier      | 1               |
| cincante+mil1    | 1            | le                | 1               |
| garlandesche     | 1            | garlement         | 1               |
| rurtius          | 1            | rufustuis         | 1               |
| taborois         | 1            | tabort            | 1               |
| aboser           | 1            | abaissier         | 1               |
| mari             | 1            | marrir            | 1               |
| celerier         | 1            | celeriers         | 1               |
| eve              | 1            | aigue             | 1               |
| mïete            | 1            | metier            | 1               |
| lou              | 1            | love              | 1               |
| estraier3        | 1            | estraier1         | 1               |
| regarder         | 1            | reposer           | 1               |
| damnedeu         | 1            | damnedieu         | 1               |
| plaindre         | 1            | plein             | 1               |
| gent1            | 1            | gent2             | 1               |
| afit2            | 1            | afi2              | 1               |
| cotoatre         | 1            | couter            | 1               |
| crëant           | 1            | croire            | 1               |
| essaiement       | 1            | assagement        | 1               |
| profetisier      | 1            | porfhatier        | 1               |
| onor             | 1            | henor             | 1               |
| voier            | 1            | voiier1           | 1               |
| foi              | 1            | foiz              | 1               |
| paille           | 1            | paile             | 1               |
| nate2            | 1            | nate              | 1               |
| deshait          | 1            | dehé              | 1               |
| träitor          | 1            | traite            | 1               |
| trois            | 1            | très              | 1               |
| cor2             | 1            | cort1             | 1               |
| faus             | 1            | fausser           | 1               |
| pieç'a           | 1            | piece             | 1               |
| resne2           | 1            | rede              | 1               |
| hiraut           | 1            | harmer            | 1               |
| i2               | 1            | un                | 1               |
| enganer          | 1            | engandre          | 1               |
| faussement       | 1            | fauvement         | 1               |
| troias           | 1            | troian            | 1               |
| planer2          | 1            | plenier1          | 1               |
| ëur              | 1            | ore3              | 1               |
| lance            | 1            | lancier3          | 1               |
| jëuner           | 1            | grieté            | 1               |
| flor1            | 1            | flot1             | 1               |
| porprendre       | 1            | porpendre         | 1               |
| embler           | 1            | enfler            | 1               |
| bon              | 1            | meillor           | 1               |
| pener            | 1            | peine             | 1               |
| vif              | 1            | vis1              | 1               |
| röeler           | 1            | röeillier         | 1               |
| duit             | 1            | doi               | 1               |
| jeter            | 1            | metre2            | 1               |
| por2+cant2       | 1            | porcant           | 1               |
| buison           | 1            | flum              | 1               |
| landuc           | 1            | landon            | 1               |
| eschaitiver      | 1            | eschevir3         | 1               |
| an               | 1            | enz               | 1               |
| justicier1       | 1            | justicier2        | 1               |
| thebes           | 1            | thiebaus          | 1               |
| descouper        | 1            | decoper           | 1               |
| arrogacion       | 1            | arracïon          | 1               |
| volenté          | 1            | venté             | 1               |
| près             | 1            | prest1            | 1               |
| rongier2         | 1            | rombant           | 1               |
| avers1           | 1            | avers2            | 1               |
| arme             | 1            | harme             | 1               |
| orle             | 1            | oler              | 1               |
| oraille          | 1            | oreille           | 1               |
| meule            | 1            | mol               | 1               |
| antif            | 1            | entier            | 1               |
| ling2            | 1            | lin               | 1               |
| fondre           | 1            | fonder2           | 1               |
| boivre           | 1            | boire             | 1               |
| räoncler         | 1            | röeillier         | 1               |
| octembre         | 1            | omecite           | 1               |
| magine           | 1            | margine           | 1               |
| travers          | 1            | traverser         | 1               |
| etiope           | 1            | etephien          | 1               |
| orribleté        | 1            | orfenité          | 1               |
| desjoinccïon     | 1            | distincïon        | 1               |
| empirier         | 1            | empire            | 1               |
| lois             | 1            | loi3              | 1               |
| sosprendre       | 1            | sofrir            | 1               |
| batisier         | 1            | pitié             | 1               |
| escarflaires     | 1            | escarfales        | 1               |
| flot2            | 1            | flot1             | 1               |
| plaire           | 1            | plait             | 1               |
| por2             | 1            | porcant           | 1               |
| ressaucier       | 1            | ressalir          | 1               |
| jugier           | 1            | jeher             | 1               |
| cordöan          | 1            | cordande          | 1               |
| muse4            | 1            | mu1               | 1               |
| estive1          | 1            | estieu            | 1               |
| lige             | 1            | lege              | 1               |
| ytace            | 1            | isaut             | 1               |
| compagne1        | 1            | compagnie         | 1               |
| ortiier2         | 1            | ortir             | 1               |
| vieillart        | 1            | vieillar          | 1               |
| moiste           | 1            | moitier           | 1               |
| soudee           | 1            | soudoiier1        | 1               |
| corporel         | 1            | corporer2         | 1               |
| boistos          | 1            | boivre            | 1               |
| enfleüre         | 1            | enflëure          | 1               |
| partir           | 1            | part1             | 1               |
| hertald          | 1            | hetrelant         | 1               |
| siglaton         | 1            | siglas            | 1               |
| defense          | 1            | sembre            | 1               |
| a1               | 1            | a3+le             | 1               |
| derrenier        | 1            | däerrain          | 1               |
| aüste            | 1            | chaste            | 1               |
| plesence         | 1            | plance            | 1               |
| melan            | 1            | mesler            | 1               |
| coutiver         | 1            | couriver          | 1               |
| hardement        | 1            | ardement          | 1               |
| engolé           | 1            | engoler           | 1               |
| saint-gilles     | 1            | gile              | 1               |

# POS

```
all:
  accuracy: 0.9659
  precision: 0.7668
  recall: 0.7493
  support: 50379
ambiguous-tokens:
  accuracy: 0.9577
  precision: 0.7644
  recall: 0.7614
  support: 32318
unknown-tokens:
  accuracy: 0.8851
  precision: 0.6107
  recall: 0.6509
  support: 1627
```

| Expected      | Total Errors | Predictions   | Predicted times |
|---------------|--------------|---------------|-----------------|
| NOMcom        | 260          | ADJqua        | 75              |
|               |              | ADVgen        | 36              |
|               |              | VERcjg        | 34              |
|               |              | VERinf        | 29              |
|               |              | NOMpro        | 26              |
|               |              | VERppe        | 25              |
|               |              | PROind        | 11              |
|               |              | ADVneg        | 9               |
|               |              | PROper        | 3               |
|               |              | PRE           | 2               |
|               |              | VERppa        | 2               |
|               |              | DETpos        | 2               |
|               |              | PROord        | 1               |
|               |              | CONcoo        | 1               |
|               |              | ADJcar        | 1               |
|               |              | PROrel        | 1               |
|               |              | DETrel        | 1               |
|               |              | DETdef        | 1               |
| CONsub        | 165          | PROrel        | 81              |
|               |              | CONcoo        | 63              |
|               |              | PROper        | 7               |
|               |              | ADVgen        | 5               |
|               |              | ADVint        | 4               |
|               |              | ADVsub        | 2               |
|               |              | PROdem        | 2               |
|               |              | DETcar        | 1               |
| ADVgen        | 139          | NOMcom        | 29              |
|               |              | PRE           | 25              |
|               |              | PROind        | 16              |
|               |              | ADJqua        | 13              |
|               |              | PROper        | 12              |
|               |              | CONcoo        | 9               |
|               |              | CONsub        | 6               |
|               |              | DETind        | 6               |
|               |              | VERcjg        | 5               |
|               |              | PROrel        | 3               |
|               |              | ADVneg.PROper | 2               |
|               |              | VERppa        | 2               |
|               |              | DETdef        | 2               |
|               |              | DETpos        | 2               |
|               |              | VERppe        | 1               |
|               |              | PROord        | 1               |
|               |              | VERinf        | 1               |
|               |              | DETdem        | 1               |
|               |              | NOMpro        | 1               |
|               |              | PROint        | 1               |
|               |              | ADJind        | 1               |
| CONcoo        | 113          | CONsub        | 67              |
|               |              | ADVneg        | 27              |
|               |              | ADVgen        | 10              |
|               |              | PROrel        | 7               |
|               |              | DETpos        | 1               |
|               |              | PRE.DETdef    | 1               |
| ADJqua        | 108          | NOMcom        | 61              |
|               |              | VERppe        | 17              |
|               |              | ADVgen        | 8               |
|               |              | NOMpro        | 7               |
|               |              | VERppa        | 5               |
|               |              | VERcjg        | 3               |
|               |              | PRE           | 2               |
|               |              | DETcar        | 2               |
|               |              | PROind        | 2               |
|               |              | DETind        | 1               |
| VERcjg        | 104          | VERppe        | 31              |
|               |              | NOMcom        | 26              |
|               |              | PRE           | 20              |
|               |              | ADJqua        | 10              |
|               |              | VERinf        | 5               |
|               |              | ADVgen        | 4               |
|               |              | CONcoo        | 2               |
|               |              | DETpos        | 1               |
|               |              | DETind        | 1               |
|               |              | DETndf        | 1               |
|               |              | PROper        | 1               |
|               |              | PROpos        | 1               |
|               |              | VERppa        | 1               |
| PROrel        | 89           | CONsub        | 65              |
|               |              | CONcoo        | 10              |
|               |              | PROint        | 7               |
|               |              | DETrel        | 4               |
|               |              | PRE.DETdef    | 1               |
|               |              | PROrel.PROper | 1               |
|               |              | ADVint        | 1               |
| PROper        | 79           | PROimp        | 33              |
|               |              | DETdef        | 26              |
|               |              | DETpos        | 5               |
|               |              | ADVgen        | 4               |
|               |              | CONsub        | 4               |
|               |              | PROind        | 3               |
|               |              | NOMcom        | 2               |
|               |              | DETind        | 1               |
|               |              | ADVneg        | 1               |
| PROind        | 75           | ADVgen        | 22              |
|               |              | DETind        | 18              |
|               |              | ADJind        | 11              |
|               |              | PRE           | 5               |
|               |              | NOMcom        | 5               |
|               |              | PROadv        | 4               |
|               |              | DETndf        | 4               |
|               |              | PROper        | 3               |
|               |              | VERcjg        | 1               |
|               |              | PROrel        | 1               |
|               |              | ADVneg        | 1               |
| VERppe        | 71           | VERcjg        | 40              |
|               |              | NOMcom        | 17              |
|               |              | ADJqua        | 10              |
|               |              | PROdem        | 1               |
|               |              | DETpos        | 1               |
|               |              | ADVgen        | 1               |
|               |              | NOMpro        | 1               |
| NOMpro        | 50           | NOMcom        | 35              |
|               |              | ADJqua        | 4               |
|               |              | VERcjg        | 3               |
|               |              | VERppe        | 3               |
|               |              | VERinf        | 2               |
|               |              | VERppa        | 2               |
|               |              | PRE           | 1               |
| PRE           | 48           | ADVgen        | 23              |
|               |              | VERcjg        | 15              |
|               |              | ADJqua        | 3               |
|               |              | PROadv        | 3               |
|               |              | CONcoo        | 1               |
|               |              | PROind        | 1               |
|               |              | NOMcom        | 1               |
|               |              | PRE.DETdef    | 1               |
| PROimp        | 36           | PROper        | 34              |
|               |              | PROadv        | 2               |
| DETind        | 28           | PROind        | 10              |
|               |              | ADVgen        | 8               |
|               |              | ADJind        | 6               |
|               |              | ADJqua        | 2               |
|               |              | NOMcom        | 1               |
|               |              | DETrel        | 1               |
| DETcar        | 28           | DETndf        | 16              |
|               |              | PROcar        | 7               |
|               |              | ADJcar        | 3               |
|               |              | DETdef        | 1               |
|               |              | ADVgen        | 1               |
| ADJind        | 27           | PROind        | 13              |
|               |              | DETind        | 12              |
|               |              | PROper        | 1               |
|               |              | ADJqua        | 1               |
| ADVneg        | 26           | CONcoo        | 17              |
|               |              | NOMcom        | 5               |
|               |              | ADVgen        | 3               |
|               |              | PROind        | 1               |
| DETdef        | 24           | PROper        | 20              |
|               |              | OUT           | 2               |
|               |              | DETdem        | 1               |
|               |              | ADVgen        | 1               |
| ADJpos        | 22           | DETpos        | 15              |
|               |              | PROpos        | 5               |
|               |              | VERppe        | 2               |
| VERinf        | 22           | NOMcom        | 16              |
|               |              | VERcjg        | 3               |
|               |              | ADJqua        | 1               |
|               |              | NOMpro        | 1               |
|               |              | VERppe        | 1               |
| DETpos        | 22           | ADJpos        | 8               |
|               |              | PROper        | 7               |
|               |              | ADVgen        | 5               |
|               |              | PRE           | 1               |
|               |              | CONcoo        | 1               |
| PROcar        | 19           | DETcar        | 5               |
|               |              | ADJcar        | 4               |
|               |              | PROper        | 3               |
|               |              | PROind        | 3               |
|               |              | DETndf        | 1               |
|               |              | ADVgen        | 1               |
|               |              | NOMcom        | 1               |
|               |              | DETdef        | 1               |
| PROint        | 18           | PROrel        | 14              |
|               |              | CONsub        | 2               |
|               |              | PROdem        | 1               |
|               |              | CONcoo        | 1               |
| PROdem        | 17           | DETdem        | 15              |
|               |              | NOMcom        | 1               |
|               |              | VERcjg        | 1               |
| ADVint        | 15           | CONsub        | 8               |
|               |              | ADVsub        | 4               |
|               |              | ADVgen        | 2               |
|               |              | PROint        | 1               |
| PROadv        | 13           | PRE           | 7               |
|               |              | DETndf        | 2               |
|               |              | PROrel        | 2               |
|               |              | ADVgen        | 1               |
|               |              | CONsub        | 1               |
| DETdem        | 13           | PROdem        | 12              |
|               |              | DETpos        | 1               |
| VERppa        | 12           | ADJqua        | 6               |
|               |              | NOMcom        | 2               |
|               |              | VERppe        | 2               |
|               |              | NOMpro        | 1               |
|               |              | VERcjg        | 1               |
| DETndf        | 10           | DETcar        | 7               |
|               |              | PROind        | 2               |
|               |              | PROadv        | 1               |
| PRE.DETdef    | 9            | CONcoo        | 8               |
|               |              | VERcjg        | 1               |
| ADJcar        | 9            | PROcar        | 4               |
|               |              | DETcar        | 2               |
|               |              | PROord        | 1               |
|               |              | NOMcom        | 1               |
|               |              | VERcjg        | 1               |
| PROord        | 8            | NOMcom        | 4               |
|               |              | ADJord        | 2               |
|               |              | VERcjg        | 1               |
|               |              | ADJqua        | 1               |
| OUT           | 7            | DETdef        | 2               |
|               |              | PROper        | 2               |
|               |              | VERppe        | 1               |
|               |              | PROadv        | 1               |
|               |              | NOMcom        | 1               |
| ADVsub        | 7            | CONsub        | 4               |
|               |              | ADVint        | 3               |
| ADJord        | 6            | PROord        | 4               |
|               |              | ADJqua        | 2               |
| DETint        | 4            | DETrel        | 4               |
|               | 2            | PRE.DETdef    | 2               |
| PROpos        | 2            | ADJpos        | 2               |
| INJ           | 2            | NOMcom        | 1               |
|               |              | CONcoo        | 1               |
| DETrel        | 2            | DETint        | 1               |
|               |              | PROrel.PROper | 1               |
| PRE.PROper    | 1            | PRE.DETdef    | 1               |
| ADVgen.PROadv | 1            | ADVgen        | 1               |
| VERcj         | 1            | NOMcom        | 1               |
| RED           | 1            | CONsub        | 1               |
| PRE.PROind    | 1            | ADVgen        | 1               |
