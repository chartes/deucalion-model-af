Confusion tables
================

- [Lemma](#lemma)
- [POS ](#pos-)

# Lemma

```
all:
  accuracy: 0.9638
  precision: 0.7123
  recall: 0.7089
  support: 48317
ambiguous-tokens:
  accuracy: 0.9665
  precision: 0.7585
  recall: 0.7643
  support: 27844
unknown-targets:
  accuracy: 0.729
  precision: 0.2685
  recall: 0.2603
  support: 1236
unknown-tokens:
  accuracy: 0.6429
  precision: 0.429
  recall: 0.4249
  support: 1792
  ```

| Expected         | Total Errors | Predictions   | Predicted times |
|------------------|--------------|---------------|-----------------|
| que2             | 86           | que4          | 79              |
|                  |              | que3          | 4               |
|                  |              | que1          | 2               |
|                  |              | qui           | 1               |
| que4             | 64           | que2          | 56              |
|                  |              | que1          | 5               |
|                  |              | que3          | 3               |
| segm             | 49           | ne2           | 2               |
|                  |              | sen2          | 2               |
|                  |              | loi3          | 2               |
|                  |              | legier2       | 2               |
|                  |              | son4          | 2               |
|                  |              | contreval     | 1               |
|                  |              | il            | 1               |
|                  |              | agrant        | 1               |
|                  |              | nuire         | 1               |
|                  |              | ore3          | 1               |
|                  |              | logros        | 1               |
|                  |              | enchantement  | 1               |
|                  |              | le+eschëur    | 1               |
|                  |              | lacier        | 1               |
|                  |              | negraise      | 1               |
|                  |              | que_que       | 1               |
|                  |              | pendre        | 1               |
|                  |              | principal     | 1               |
|                  |              | a3            | 1               |
|                  |              | val1          | 1               |
|                  |              | girbert       | 1               |
|                  |              | cest          | 1               |
|                  |              | ça            | 1               |
|                  |              | lorgueil      | 1               |
|                  |              | charles       | 1               |
|                  |              | avoir         | 1               |
|                  |              | estre1        | 1               |
|                  |              | ome           | 1               |
|                  |              | enragier      | 1               |
|                  |              | lencron       | 1               |
|                  |              | nen1          | 1               |
|                  |              | negraiment    | 1               |
|                  |              | entracoit     | 1               |
|                  |              | leschis       | 1               |
|                  |              | secrir        | 1               |
|                  |              | loglëor       | 1               |
|                  |              | eschaper      | 1               |
|                  |              | mauaire       | 1               |
|                  |              | monois        | 1               |
|                  |              | emperëor      | 1               |
|                  |              | saisir        | 1               |
|                  |              | dorm          | 1               |
|                  |              | lesu1         | 1               |
|                  |              | ne1           | 1               |
| avoir            | 41           | a3            | 23              |
|                  |              | öir           | 6               |
|                  |              | a3+le         | 4               |
|                  |              | häir          | 3               |
|                  |              | avuec         | 2               |
|                  |              | aucai         | 2               |
|                  |              | estre1        | 1               |
| il               | 35           | le            | 26              |
|                  |              | là            | 4               |
|                  |              | je            | 2               |
|                  |              | lors          | 1               |
|                  |              | aler          | 1               |
|                  |              | i2            | 1               |
| que1             | 34           | que4          | 33              |
|                  |              | que2          | 1               |
| ne2              | 27           | ne1           | 27              |
| le               | 24           | il            | 20              |
|                  |              | là            | 3               |
|                  |              | lez           | 1               |
| se               | 22           | si            | 12              |
|                  |              | soi1          | 6               |
|                  |              | ce1           | 2               |
|                  |              | segm          | 1               |
|                  |              | son4          | 1               |
| ne1              | 20           | ne2           | 20              |
| si               | 16           | soi1          | 8               |
|                  |              | se            | 6               |
|                  |              | son4          | 1               |
|                  |              | si+il         | 1               |
| a3               | 14           | avoir         | 14              |
| donc             | 13           | dont          | 12              |
|                  |              | don           | 1               |
| öir              | 13           | avoir         | 9               |
|                  |              | oir           | 3               |
|                  |              | olir          | 1               |
| vivre1           | 12           | vëoir         | 9               |
|                  |              | vif           | 1               |
|                  |              | vire1         | 1               |
|                  |              | vis1          | 1               |
| ''''             | 11           |               | 11              |
| o3               | 10           | où            | 7               |
|                  |              | en1+le        | 2               |
|                  |              | avoir         | 1               |
| que3             | 10           | que4          | 6               |
|                  |              | que2          | 4               |
| en1              | 9            | en2           | 6               |
|                  |              | on            | 2               |
|                  |              | an            | 1               |
| estre1           | 9            | avoir         | 3               |
|                  |              | ester         | 1               |
|                  |              | segm          | 1               |
|                  |              | vëoir         | 1               |
|                  |              | savoir        | 1               |
|                  |              | estovoir1     | 1               |
|                  |              | sus           | 1               |
| prodome          | 9            | pro           | 9               |
| ainz             | 9            | ainc          | 9               |
| soi1             | 9            | se            | 5               |
|                  |              | si            | 2               |
|                  |              | son4          | 2               |
| ester            | 9            | estre1        | 5               |
|                  |              | estovoir1     | 3               |
|                  |              | esté1         | 1               |
| en2              | 9            | en1           | 5               |
|                  |              | on            | 3               |
|                  |              | segm          | 1               |
| entre            | 9            | entre2        | 9               |
| savoir           | 8            | suen          | 2               |
|                  |              | sachier2      | 1               |
|                  |              | sacrer        | 1               |
|                  |              | sec           | 1               |
|                  |              | sëu           | 1               |
|                  |              | sot           | 1               |
|                  |              | set           | 1               |
| qui              | 8            | que4          | 4               |
|                  |              | que2          | 3               |
|                  |              | cui           | 1               |
| vëoir            | 8            | aler          | 3               |
|                  |              | vair1         | 1               |
|                  |              | avoir         | 1               |
|                  |              | voloir        | 1               |
|                  |              | venir         | 1               |
|                  |              | vos           | 1               |
| sëel2            | 7            | sëel1         | 6               |
|                  |              | saiel         | 1               |
| où               | 7            | o3            | 7               |
| saint1           | 7            | saint         | 7               |
| là               | 7            | le            | 4               |
|                  |              | il            | 3               |
|                  | 7            | ''''          | 6               |
|                  |              | ascamnit      | 1               |
| bien2            | 6            | bien1         | 6               |
| vos              | 6            | vostre        | 3               |
|                  |              | il            | 1               |
|                  |              | ost           | 1               |
|                  |              | oste          | 1               |
| avenir           | 6            | avenant       | 6               |
| en1+le           | 6            | o3            | 2               |
|                  |              | il            | 1               |
|                  |              | où            | 1               |
|                  |              | estre1        | 1               |
|                  |              | o4            | 1               |
| ce1              | 6            | se            | 3               |
|                  |              | ce2           | 3               |
| ce2              | 5            | ce1           | 3               |
|                  |              | son4          | 1               |
|                  |              | se            | 1               |
| vif              | 5            | vis1          | 2               |
|                  |              | vil           | 1               |
|                  |              | uis           | 1               |
|                  |              | vëoir         | 1               |
| conte1           | 5            | conte2        | 3               |
|                  |              | conter        | 2               |
| son4             | 5            | si            | 3               |
|                  |              | sui           | 1               |
|                  |              | lor2          | 1               |
| mort             | 5            | morir         | 4               |
|                  |              | mors1         | 1               |
| cest             | 4            | ce2           | 3               |
|                  |              | cel           | 1               |
| bruire           | 4            | bruiant2      | 2               |
|                  |              | bruit         | 1               |
|                  |              | brisier       | 1               |
| once2            | 4            | onque         | 2               |
|                  |              | oncevoir      | 1               |
|                  |              | onceve        | 1               |
| chevrueil        | 4            | chevrel       | 4               |
| aidier           | 4            | äie           | 2               |
|                  |              | avoir         | 2               |
| non              | 4            | nom           | 3               |
|                  |              | num           | 1               |
| aler             | 4            | avoir         | 1               |
|                  |              | ire           | 1               |
|                  |              | vëoir         | 1               |
|                  |              | eslire        | 1               |
| plaire           | 4            | plait         | 3               |
|                  |              | plaisir       | 1               |
| char1            | 4            | char2         | 4               |
| dieu             | 4            | deus          | 2               |
|                  |              | devoir        | 2               |
| laissier         | 4            | vëoir         | 1               |
|                  |              | laiier2       | 1               |
|                  |              | le            | 1               |
|                  |              | lais          | 1               |
| tref1            | 4            | tref2         | 4               |
| ferir            | 3            | faire         | 2               |
|                  |              | fief          | 1               |
| lez              | 3            | le            | 1               |
|                  |              | il            | 1               |
|                  |              | lever         | 1               |
| pel1             | 3            | pel2          | 2               |
|                  |              | pue           | 1               |
| pöoir            | 3            | poissant      | 2               |
|                  |              | puis          | 1               |
| warochier        | 3            | warchëoir     | 3               |
| tant             | 3            | atant         | 1               |
|                  |              | tens          | 1               |
|                  |              | tendre1       | 1               |
| sëoir            | 3            | savoir        | 1               |
|                  |              | saisir        | 1               |
|                  |              | estre1        | 1               |
| arbre            | 3            | arbe          | 2               |
|                  |              | erbe          | 1               |
| afaire1          | 3            | afaire2       | 3               |
| revenir          | 3            | röeir2        | 1               |
|                  |              | reuvoir1      | 1               |
|                  |              | reuvrer       | 1               |
| nos1             | 3            | nul           | 2               |
|                  |              | nostre        | 1               |
| on               | 3            | en2           | 2               |
|                  |              | en1           | 1               |
| entaschier       | 3            | entachier     | 3               |
| tendre1          | 3            | tendre2       | 2               |
|                  |              | tenir1        | 1               |
| vostre           | 3            | vos           | 3               |
| feste            | 3            | feste1        | 3               |
| devoir           | 3            | duire         | 1               |
|                  |              | douz          | 1               |
|                  |              | doi           | 1               |
| pesance          | 3            | poissance     | 3               |
| seignier         | 3            | saignier      | 3               |
| sor2             | 3            | sus           | 3               |
| cuire            | 3            | cuidier1      | 3               |
| cort2            | 3            | corir         | 1               |
|                  |              | cort1         | 1               |
|                  |              | cortois       | 1               |
| servir           | 3            | serorir       | 1               |
|                  |              | seror         | 1               |
|                  |              | seroriu       | 1               |
| je               | 3            | i2            | 2               |
|                  |              | mi2           | 1               |
| cui              | 3            | qui           | 3               |
| perdre           | 3            | pardoner      | 1               |
|                  |              | pordrir       | 1               |
|                  |              | por2          | 1               |
| peser            | 3            | paistre       | 2               |
|                  |              | poissant      | 1               |
| o4               | 3            | o3            | 2               |
|                  |              | où            | 1               |
| tor2             | 3            | tort2         | 2               |
|                  |              | tor5          | 1               |
| icest            | 3            | icel          | 1               |
|                  |              | cel           | 1               |
|                  |              | ice2          | 1               |
| moillier1        | 3            | moillier2     | 3               |
| pere             | 3            | pere1         | 3               |
| salir1           | 3            | salir2        | 3               |
| ez               | 3            | et            | 1               |
|                  |              | ester         | 1               |
|                  |              | estre1        | 1               |
| cel              | 3            | cil           | 2               |
|                  |              | quel1         | 1               |
| traire           | 3            | träir         | 3               |
| avant            | 3            | autant        | 3               |
| nu1              | 3            | nul           | 2               |
|                  |              | nüe           | 1               |
| alier            | 3            | aliier        | 2               |
|                  |              | alix          | 1               |
| porsëoir2        | 3            | porsener      | 2               |
|                  |              | porsenor      | 1               |
| venir            | 3            | venüe         | 1               |
|                  |              | uenir         | 1               |
|                  |              | vain          | 1               |
| forsenerie       | 3            | forcoine      | 1               |
|                  |              | forfoidiere   | 1               |
|                  |              | forcenie      | 1               |
| sor1             | 2            | sort2         | 1               |
|                  |              | sor2          | 1               |
| tenir1           | 2            | tendre1       | 2               |
| complaindre      | 2            | complamner    | 1               |
|                  |              | comploiier    | 1               |
| theoniste        | 2            | theodoise     | 1               |
|                  |              | thenois       | 1               |
| culvert          | 2            | cuir          | 1               |
|                  |              | guivret       | 1               |
| autel2           | 2            | autel1        | 2               |
| pris1            | 2            | prendre       | 2               |
| garir            | 2            | garder        | 2               |
| jesir            | 2            | jeter         | 2               |
| coper            | 2            | çoper         | 1               |
|                  |              | cope1         | 1               |
| essaucier        | 2            | eshaucier     | 2               |
| apercevoir       | 2            | espardre      | 1               |
|                  |              | esparchier    | 1               |
| soudre           | 2            | soillier      | 1               |
|                  |              | soloir        | 1               |
| encontre2        | 2            | encontre1     | 2               |
| doze+mil1        | 2            | trente+mil1   | 1               |
|                  |              | trois+mil1    | 1               |
| seignor          | 2            | sainté        | 1               |
|                  |              | saintëé       | 1               |
| plenierement     | 2            | plenier1      | 2               |
| desesperer       | 2            | dessevrer     | 2               |
| dunemarche       | 2            | ducarne       | 1               |
|                  |              | ducarn        | 1               |
| pur              | 2            | por2          | 2               |
| mon1             | 2            | je            | 1               |
|                  |              | mais1         | 1               |
| césar            | 2            | cesar         | 2               |
| forment          | 2            | forment2      | 2               |
| suen             | 2            | son4          | 2               |
| bëer             | 2            | baillier      | 2               |
| maxime           | 2            | maumetre      | 1               |
|                  |              | maximien      | 1               |
| denis            | 2            | saint-denis   | 1               |
|                  |              | dinis         | 1               |
| crüauté          | 2            | crüaleté      | 2               |
| parrain          | 2            | parein        | 1               |
|                  |              | parin         | 1               |
| mil1             | 2            | metre2        | 1               |
|                  |              | milieu        | 1               |
| suscription      | 2            | sosprocier    | 1               |
|                  |              | sochier       | 1               |
| metre2           | 2            | mëisme        | 1               |
|                  |              | jeter         | 1               |
| mais1            | 2            | mon1          | 2               |
| i2               | 2            | un            | 2               |
| longement2       | 2            | longement     | 2               |
| jeter            | 2            | geter         | 1               |
|                  |              | gaitier       | 1               |
| prevost          | 2            | prevoste      | 2               |
| sivre            | 2            | savoir        | 2               |
| martel           | 2            | martois       | 1               |
|                  |              | martire2      | 1               |
| comporter        | 2            | comparer2     | 2               |
| vers2            | 2            | ventre1       | 2               |
| espiet           | 2            | espee         | 1               |
|                  |              | espie3        | 1               |
| ha!              | 2            | häir          | 2               |
| brice            | 2            | briciton      | 1               |
|                  |              | bricet        | 1               |
| depecier         | 2            | despechier    | 2               |
| jöir             | 2            | jöer          | 2               |
| saint            | 2            | sentir        | 1               |
|                  |              | sans          | 1               |
| don              | 2            | dont          | 1               |
|                  |              | donc          | 1               |
| foi              | 2            | foiz          | 2               |
| poiz             | 2            | poing         | 2               |
| an               | 2            | en2           | 1               |
|                  |              | on            | 1               |
| feindre          | 2            | fendre        | 1               |
|                  |              | feinte        | 1               |
| pon2             | 2            | pont          | 2               |
| sen2             | 2            | sanc          | 2               |
| lé               | 2            | lez           | 1               |
|                  |              | lait1         | 1               |
| cri              | 2            | mois          | 2               |
| secorer          | 2            | secors        | 1               |
|                  |              | secorre1      | 1               |
| vile             | 2            | uile          | 2               |
| reims            | 2            | roint1        | 1               |
|                  |              | raim          | 1               |
| gent2            | 2            | gent1         | 2               |
| covenant         | 2            | conoistre     | 1               |
|                  |              | covenancier1  | 1               |
| chierir          | 2            | chëoir        | 1               |
|                  |              | chier         | 1               |
| vendre           | 2            | venir         | 2               |
| tesmoignage      | 2            | tesmoigne     | 2               |
| tinel1           | 2            | tinte         | 2               |
| cheval           | 2            | chevel        | 1               |
|                  |              | chievre       | 1               |
| porsivre         | 2            | porsentir     | 1               |
|                  |              | porsevoir     | 1               |
| vëer             | 2            | vëoir         | 2               |
| gent1            | 2            | gant          | 1               |
|                  |              | gent2         | 1               |
| besoignier       | 2            | besoigne      | 2               |
| quinze           | 2            | quint         | 2               |
| veintre          | 2            | vestir        | 1               |
|                  |              | vivre1        | 1               |
| par              | 2            | por2          | 2               |
| consirer         | 2            | conseignier   | 1               |
|                  |              | consirrer     | 1               |
| di               | 2            | dis1          | 2               |
| charnel2         | 2            | charnel       | 2               |
| escrïer          | 2            | encröer       | 1               |
|                  |              | escrire       | 1               |
| or4              | 2            | ore3          | 1               |
|                  |              | or1           | 1               |
| mauvaisement     | 2            | mauvais       | 2               |
| sachier2         | 2            | savoir        | 2               |
| cuidier1         | 2            | quiter        | 2               |
| veraiement       | 2            | iroiament     | 1               |
|                  |              | verai         | 1               |
| mëur             | 2            | maubre        | 1               |
|                  |              | movoir        | 1               |
| tot              | 2            | tost1         | 2               |
| veillier2        | 2            | voloir        | 2               |
| ore3             | 2            | or4           | 2               |
| durer            | 2            | dur           | 2               |
| lieue            | 2            | lié1          | 1               |
|                  |              | lieu          | 1               |
| solement         | 2            | solement2     | 2               |
| privé1           | 2            | priveement    | 1               |
|                  |              | priver        | 1               |
| repondre         | 2            | repost        | 2               |
| espargnance      | 2            | espargatie    | 1               |
|                  |              | espartance    | 1               |
| partir           | 2            | part1         | 1               |
|                  |              | partie        | 1               |
| pere1            | 2            | pere          | 2               |
| paistre          | 2            | peser         | 2               |
| près             | 2            | près+que      | 2               |
| conter           | 2            | conte1        | 2               |
| tolir            | 2            | tot           | 2               |
| tens             | 2            | tant          | 2               |
| defendre         | 2            | ceinture      | 1               |
|                  |              | defendëor     | 1               |
| intencïon        | 2            | entencïon     | 2               |
| plate            | 2            | plat          | 2               |
| comunaument      | 2            | comunement    | 1               |
|                  |              | comunement2   | 1               |
| laidengier       | 2            | landigïon     | 1               |
|                  |              | landeviner    | 1               |
| pais             | 2            | poi           | 1               |
|                  |              | päis          | 1               |
| lumbardie        | 2            | lamberie      | 1               |
|                  |              | lonbardie     | 1               |
| comunauté        | 2            | comunité      | 1               |
|                  |              | comuniter     | 1               |
| afoler1          | 2            | afoler2       | 2               |
| bofu             | 2            | bouz          | 2               |
| estrangier2      | 2            | estragier     | 2               |
| dotance          | 2            | de+le         | 1               |
|                  |              | tence         | 1               |
| changier         | 2            | chargier      | 1               |
|                  |              | chancier1     | 1               |
| entrer           | 2            | entre2        | 1               |
|                  |              | entree        | 1               |
| cors1            | 2            | cort1         | 2               |
| faim             | 2            | fein          | 1               |
|                  |              | feindre       | 1               |
| chiere           | 2            | chier         | 2               |
| morel1           | 2            | moral         | 1               |
|                  |              | morsel        | 1               |
| dis1             | 2            | dit           | 1               |
|                  |              | di            | 1               |
| a3+le            | 2            | il            | 1               |
|                  |              | o3            | 1               |
| rachater         | 1            | recanter      | 1               |
| turnevent        | 1            | torner        | 1               |
| enui             | 1            | enoiier       | 1               |
| boban            | 1            | boner         | 1               |
| vigne1           | 1            | venir         | 1               |
| baillie          | 1            | balais2       | 1               |
| agencir          | 1            | agenoillier   | 1               |
| depopler         | 1            | depeler       | 1               |
| chargier         | 1            | changier      | 1               |
| essuier          | 1            | essuiier      | 1               |
| respasser        | 1            | repasser      | 1               |
| montee           | 1            | monter        | 1               |
| espondre         | 1            | espostire2    | 1               |
| graine           | 1            | grenain       | 1               |
| flote3           | 1            | flot2         | 1               |
| vassal           | 1            | vassel        | 1               |
| ost              | 1            | avoir         | 1               |
| sengler          | 1            | cengler       | 1               |
| mostrer          | 1            | montre        | 1               |
| ne1+il           | 1            | nos1          | 1               |
| boivre           | 1            | boisier2      | 1               |
| sis2             | 1            | vëoir         | 1               |
| verser1          | 1            | aversier      | 1               |
| amaigrir         | 1            | amener        | 1               |
| ovrer            | 1            | ovrir         | 1               |
| nom              | 1            | non           | 1               |
| heaume           | 1            | ame           | 1               |
| alemaigne        | 1            | alemant       | 1               |
| efrené           | 1            | esfrëer       | 1               |
| häir             | 1            | häi!          | 1               |
| jöe              | 1            | joie          | 1               |
| joier            | 1            | jovier        | 1               |
| es2              | 1            | estre1        | 1               |
| erepuis          | 1            | arpumius      | 1               |
| le_mans          | 1            | manc1         | 1               |
| vistece          | 1            | vistice       | 1               |
| löer2            | 1            | loiier        | 1               |
| voutiz           | 1            | volter        | 1               |
| amertume         | 1            | amer1         | 1               |
| partot           | 1            | tort1         | 1               |
| deus             | 1            | dieu          | 1               |
| assez            | 1            | essez         | 1               |
| toute            | 1            | toste1        | 1               |
| reconjöir        | 1            | reconoistre   | 1               |
| parthenie        | 1            | partir        | 1               |
| establer1        | 1            | estable1      | 1               |
| cremetos         | 1            | crever        | 1               |
| covoitos         | 1            | covoitier     | 1               |
| guerredoner      | 1            | guerdir       | 1               |
| eschignier       | 1            | eschiner      | 1               |
| regne            | 1            | ragent        | 1               |
| font1            | 1            | fonz          | 1               |
| mulot2           | 1            | mol           | 1               |
| ambler           | 1            | embler        | 1               |
| repairier        | 1            | repaire       | 1               |
| vint             | 1            | venir         | 1               |
| milier           | 1            | milien        | 1               |
| issir            | 1            | espoir2       | 1               |
| nercir           | 1            | mercïer       | 1               |
| bret             | 1            | brief         | 1               |
| taillëor         | 1            | taillier1     | 1               |
| regenerer        | 1            | regnerrer     | 1               |
| benefice         | 1            | benivor       | 1               |
| sidre            | 1            | sivre         | 1               |
| tornement        | 1            | tornoiement   | 1               |
| penser           | 1            | pensé         | 1               |
| garlain          | 1            | garlan        | 1               |
| aive             | 1            | avoir         | 1               |
| mordrir          | 1            | morir         | 1               |
| encens           | 1            | ancessor      | 1               |
| mirre            | 1            | mire1         | 1               |
| alöé             | 1            | alöer1        | 1               |
| entr'acoler      | 1            | entreconder   | 1               |
| soie3            | 1            | soie2         | 1               |
| former           | 1            | fermer        | 1               |
| piz              | 1            | pis1          | 1               |
| justin           | 1            | justicin      | 1               |
| tu               | 1            | ton4          | 1               |
| demincier        | 1            | demencier     | 1               |
| lait1            | 1            | laidengier    | 1               |
| quel1            | 1            | conte1        | 1               |
| ardoise          | 1            | atoise        | 1               |
| fauz             | 1            | faus          | 1               |
| vair1            | 1            | vair2         | 1               |
| lïemier          | 1            | liemier       | 1               |
| errer1           | 1            | errer2        | 1               |
| desmembrer       | 1            | demener       | 1               |
| tarse            | 1            | therrain      | 1               |
| cilicie          | 1            | clices        | 1               |
| arme             | 1            | ame           | 1               |
| esteler2         | 1            | estele2       | 1               |
| nef2             | 1            | nés           | 1               |
| barbé            | 1            | berbert       | 1               |
| noise            | 1            | noiz          | 1               |
| retronçoner      | 1            | retrover      | 1               |
| entr'avenir      | 1            | entrevenir    | 1               |
| fil2             | 1            | fi2           | 1               |
| sorcuidier       | 1            | sordoiier     | 1               |
| soissons         | 1            | saison        | 1               |
| iretier1         | 1            | ireté         | 1               |
| tor5             | 1            | tor2          | 1               |
| desireter        | 1            | desirrir      | 1               |
| roincevaux       | 1            | rocelut       | 1               |
| arcevesque       | 1            | escrevesque   | 1               |
| öil              | 1            | o3            | 1               |
| chose            | 1            | cause         | 1               |
| corir            | 1            | cort1         | 1               |
| uef              | 1            | ost           | 1               |
| desclore         | 1            | desclöer      | 1               |
| essaiement       | 1            | assasiier     | 1               |
| alemele          | 1            | lame          | 1               |
| combatëor        | 1            | combatre      | 1               |
| chaser           | 1            | chacier       | 1               |
| pré              | 1            | prè           | 1               |
| florir           | 1            | forir         | 1               |
| ice2             | 1            | ice1          | 1               |
| autel1           | 1            | autel2        | 1               |
| desfaire         | 1            | desferrer     | 1               |
| trüant           | 1            | träin         | 1               |
| enz              | 1            | an            | 1               |
| esperit          | 1            | espirter      | 1               |
| omage            | 1            | umage         | 1               |
| prisier          | 1            | premier       | 1               |
| esforcement2     | 1            | esforcement1  | 1               |
| livrer           | 1            | lire1         | 1               |
| cendal           | 1            | cender        | 1               |
| perrin           | 1            | parin         | 1               |
| prïor            | 1            | priier        | 1               |
| esclavon         | 1            | esclavont     | 1               |
| apert            | 1            | apert1        | 1               |
| mès              | 1            | mais1         | 1               |
| envers2          | 1            | envers1       | 1               |
| pel2             | 1            | pel1          | 1               |
| veine1           | 1            | voine1        | 1               |
| un               | 1            | i2            | 1               |
| curçuse          | 1            | curcevauche   | 1               |
| esperdre         | 1            | espardre      | 1               |
| ja               | 1            | je            | 1               |
| vergoignier      | 1            | vergonder     | 1               |
| dïemaine         | 1            | dïamence      | 1               |
| paste            | 1            | pasté         | 1               |
| mäaille          | 1            | maille        | 1               |
| ail              | 1            | aigue         | 1               |
| mier             | 1            | mer           | 1               |
| comant           | 1            | comander      | 1               |
| destruire        | 1            | destruit      | 1               |
| aorer2           | 1            | avoir         | 1               |
| delivrer         | 1            | delivre1      | 1               |
| cartage          | 1            | carthage      | 1               |
| desäerdre        | 1            | desaraierder  | 1               |
| covenir          | 1            | cevenir       | 1               |
| marrir           | 1            | morir         | 1               |
| gironville       | 1            | girondelon    | 1               |
| escïent          | 1            | icïant        | 1               |
| chevelu          | 1            | chevel        | 1               |
| venjance         | 1            | voingne       | 1               |
| douz             | 1            | doze          | 1               |
| soigle           | 1            | soille        | 1               |
| aspremont        | 1            | asprement     | 1               |
| oriflor          | 1            | orfrois       | 1               |
| iseut            | 1            | ysout         | 1               |
| si+en2           | 1            | signe         | 1               |
| cant2            | 1            | cantque       | 1               |
| recevoir         | 1            | recu          | 1               |
| sire2            | 1            | serrer        | 1               |
| franchiser       | 1            | franchir      | 1               |
| juene            | 1            | joble         | 1               |
| desrompre        | 1            | despromer     | 1               |
| vengier          | 1            | veignier      | 1               |
| fein             | 1            | faim          | 1               |
| fuerre1          | 1            | fuerre2       | 1               |
| ametre           | 1            | ami           | 1               |
| empreu           | 1            | emprès        | 1               |
| loing            | 1            | loint         | 1               |
| code             | 1            | cote1         | 1               |
| faire            | 1            | ferir         | 1               |
| moller           | 1            | moudre1       | 1               |
| plaidier1        | 1            | plaidier2     | 1               |
| duel             | 1            | duc2          | 1               |
| ui               | 1            | öir           | 1               |
| buire1           | 1            | buir          | 1               |
| barné            | 1            | berne         | 1               |
| viron1           | 1            | viron         | 1               |
| sautier2         | 1            | saitier       | 1               |
| conduire         | 1            | conduit       | 1               |
| vivus            | 1            | vilus         | 1               |
| cercler          | 1            | cercle        | 1               |
| chöe             | 1            | chose         | 1               |
| devenir          | 1            | servir        | 1               |
| governëor        | 1            | governaire    | 1               |
| sel1             | 1            | si+il         | 1               |
| jugement         | 1            | ivelment      | 1               |
| desfïer          | 1            | defiser       | 1               |
| comprendre       | 1            | comparer2     | 1               |
| torbe1           | 1            | torbe2        | 1               |
| despaner         | 1            | depentir      | 1               |
| retrover         | 1            | retrois       | 1               |
| celer1           | 1            | cel           | 1               |
| papegai          | 1            | papeliant     | 1               |
| chatel           | 1            | chater        | 1               |
| apartenir        | 1            | apertenir     | 1               |
| avesprer         | 1            | avespre       | 1               |
| refaire1         | 1            | refaire2      | 1               |
| deguerpir        | 1            | degreier      | 1               |
| comander         | 1            | coment1       | 1               |
| ancïenement      | 1            | encïent       | 1               |
| anciien          | 1            | escïent       | 1               |
| mieus            | 1            | mel           | 1               |
| cervel           | 1            | cors1         | 1               |
| haut             | 1            | hater2        | 1               |
| enfer            | 1            | enfant        | 1               |
| empoindre        | 1            | empoignier    | 1               |
| desjoinccïon     | 1            | discidance    | 1               |
| uit              | 1            | set           | 1               |
| nuef1            | 1            | il            | 1               |
| plesence         | 1            | plaisence     | 1               |
| respit           | 1            | repïet        | 1               |
| nomement         | 1            | noment        | 1               |
| sospendre        | 1            | sospire       | 1               |
| toit             | 1            | tot           | 1               |
| sain             | 1            | saignier      | 1               |
| catre            | 1            | cot           | 1               |
| limors           | 1            | limoges       | 1               |
| losengier2       | 1            | losengier1    | 1               |
| entrecontrariier | 1            | entrecombatre | 1               |
| mie1             | 1            | mie           | 1               |
| despire          | 1            | despite       | 1               |
| dozime           | 1            | doner         | 1               |
| nesun            | 1            | nesus         | 1               |
| crïer2           | 1            | criembre      | 1               |
| departir         | 1            | deporter      | 1               |
| prendre          | 1            | pendre        | 1               |
| esfrëer          | 1            | esfrïer       | 1               |
| encenser2        | 1            | encener       | 1               |
| recorir          | 1            | recorder      | 1               |
| müel             | 1            | mu1           | 1               |
| oir              | 1            | hoir          | 1               |
| reperdre         | 1            | reprendre1    | 1               |
| ohi              | 1            | öir           | 1               |
| plaisance        | 1            | plaissance    | 1               |
| oïr              | 1            | oir           | 1               |
| proiier          | 1            | prometre      | 1               |
| pleige           | 1            | ploige        | 1               |
| deplaindre       | 1            | departir      | 1               |
| remener          | 1            | remanoir      | 1               |
| autrui           | 1            | nature        | 1               |
| malapris         | 1            | malapré       | 1               |
| escuser2         | 1            | escuser1      | 1               |
| damage           | 1            | domacier      | 1               |
| enchasser        | 1            | enchacier     | 1               |
| esböeler         | 1            | esböener      | 1               |
| peindre1         | 1            | point         | 1               |
| sauver           | 1            | savoir        | 1               |
| cembel1er        | 1            | chamberler    | 1               |
| saler            | 1            | salir2        | 1               |
| pointurie        | 1            | pointuret     | 1               |
| mëismement       | 1            | mïemement     | 1               |
| dis2             | 1            | dit           | 1               |
| reproche         | 1            | reprochier1   | 1               |
| prover           | 1            | proisier      | 1               |
| present1         | 1            | present2      | 1               |
| molin            | 1            | moillien1     | 1               |
| moudre1          | 1            | movoir        | 1               |
| for              | 1            | fort          | 1               |
| vair2            | 1            | vair1         | 1               |
| manoir1          | 1            | mener         | 1               |
| puis             | 1            | plus          | 1               |
| sentir           | 1            | estre1        | 1               |
| cant1            | 1            | cant2         | 1               |
| abatëiz          | 1            | abatre        | 1               |
| sëur2            | 1            | sor2          | 1               |
| pëor             | 1            | por2          | 1               |
| rompre           | 1            | ros3          | 1               |
| nape             | 1            | napert        | 1               |
| sembler          | 1            | sebile        | 1               |
| coral2           | 1            | corail        | 1               |
| ajornal          | 1            | ajorner       | 1               |
| sainteté         | 1            | saint         | 1               |
| nul              | 1            | nos1          | 1               |
| elainne          | 1            | eleine        | 1               |
| espee            | 1            | sepe          | 1               |
| mont             | 1            | monde1        | 1               |
| chaloir          | 1            | chëoir        | 1               |
| forsené          | 1            | forsener      | 1               |
| delivre2         | 1            | delivre1      | 1               |
| argone           | 1            | argonde       | 1               |
| pois2            | 1            | pois1         | 1               |
| tinianus         | 1            | tinitanc      | 1               |
| trejanus         | 1            | trengale      | 1               |
| sevoir           | 1            | savoir        | 1               |
| coment1          | 1            | comencier     | 1               |
| avoutire1        | 1            | avoitre       | 1               |
| ensivre2         | 1            | ensivre1      | 1               |
| secrestain       | 1            | secretain     | 1               |
| desiretement     | 1            | desertinement | 1               |
| es3              | 1            | en1+le        | 1               |
| noroison         | 1            | norion        | 1               |
| parrastre        | 1            | pareras       | 1               |
| enclume          | 1            | enclumer      | 1               |
| armaire          | 1            | onor          | 1               |
| arborius         | 1            | priier        | 1               |
| brunet           | 1            | brunir        | 1               |
| entr'ueil        | 1            | entr'avol     | 1               |
| merveillier      | 1            | merveillos    | 1               |
| fort             | 1            | fors1         | 1               |
| saisir           | 1            | secorre1      | 1               |
| coi2             | 1            | qui           | 1               |
| crever           | 1            | griver        | 1               |
| voirement        | 1            | ivorment      | 1               |
| definement       | 1            | definerie     | 1               |
| oier             | 1            | oir           | 1               |
| anee             | 1            | anene2        | 1               |
| boiste           | 1            | bote2         | 1               |
| atendre          | 1            | atant         | 1               |
| lor2             | 1            | il            | 1               |
| estanchier       | 1            | estenceler    | 1               |
| enfançon         | 1            | enfance       | 1               |
| baril            | 1            | barrable      | 1               |
| paien            | 1            | paiier        | 1               |
| glatir           | 1            | glatent       | 1               |
| arinant          | 1            | ariene        | 1               |
| evesque          | 1            | viece         | 1               |
| dont             | 1            | donc          | 1               |
| celebrer         | 1            | celer1        | 1               |
| fragilité        | 1            | freiglait     | 1               |
| taster           | 1            | taire         | 1               |
| plain            | 1            | plein         | 1               |
| maintenant       | 1            | maintenir     | 1               |
| neporuec         | 1            | neporcaut     | 1               |
| faunoiier        | 1            | faudernement  | 1               |
| tolede           | 1            | tolete        | 1               |
| candie           | 1            | chandie       | 1               |
| esclat           | 1            | escla         | 1               |
| froiier          | 1            | fraindre      | 1               |
| recouper         | 1            | recoper       | 1               |
| tronçoner        | 1            | trenchier1    | 1               |
| es1              | 1            | ais           | 1               |
| estrosseement    | 1            | estrossement  | 1               |
| pers             | 1            | per           | 1               |
| cort1            | 1            | cuer2         | 1               |
| deugié           | 1            | doloir        | 1               |
| paroir           | 1            | perdre        | 1               |
| nüe              | 1            | nu1           | 1               |
| lïement          | 1            | lieement      | 1               |
| tartarun         | 1            | tartart       | 1               |
| obëir            | 1            | obesïoigne    | 1               |
| poing            | 1            | pui           | 1               |
| nerve            | 1            | nevre         | 1               |
| forclore         | 1            | fors1         | 1               |
| soverain         | 1            | sovenaire     | 1               |
| logier           | 1            | loignier      | 1               |
| paumier2         | 1            | pamier        | 1               |
| träitor          | 1            | traitier      | 1               |
| degaster         | 1            | degahater     | 1               |
| lié1             | 1            | lé            | 1               |
| mestorner        | 1            | mestirer      | 1               |
| retarder         | 1            | retenir       | 1               |
| maillier2        | 1            | maillier1     | 1               |
| babilonie        | 1            | babiloine     | 1               |
| guerroiier2      | 1            | guerrier      | 1               |
| quitëé           | 1            | quite         | 1               |
| chamoiz          | 1            | camois        | 1               |
| floripas         | 1            | florïant      | 1               |
| rëont            | 1            | rëon          | 1               |
| sauf             | 1            | son4          | 1               |
| noé              | 1            | nol           | 1               |
| arche2           | 1            | arche         | 1               |
| oindre           | 1            | oidre         | 1               |
| crïee            | 1            | crïer2        | 1               |
| voiz             | 1            | voie          | 1               |
| marc1            | 1            | marz          | 1               |
| crïator          | 1            | crïature      | 1               |
| main1            | 1            | main2         | 1               |
| assignier        | 1            | assenir       | 1               |
| reconoistre      | 1            | requerre      | 1               |
| mescrëant        | 1            | mescroire     | 1               |
| content2         | 1            | conter        | 1               |
| reboter          | 1            | reboter1      | 1               |
| entre2           | 1            | entre         | 1               |
| engignier1       | 1            | enseignier    | 1               |
| amant            | 1            | amer1         | 1               |
| croire           | 1            | croistre      | 1               |
| demostrer        | 1            | demorer       | 1               |
| roidement        | 1            | redement      | 1               |
| riule            | 1            | roigle        | 1               |
| mençogne         | 1            | mongage       | 1               |
| flore            | 1            | floovant      | 1               |
| trenchier1       | 1            | trenchant     | 1               |
| atorner          | 1            | ateler        | 1               |
| consiree         | 1            | consivre      | 1               |
| aparmain         | 1            | aparement     | 1               |
| dido             | 1            | didi          | 1               |
| gorge            | 1            | gage          | 1               |
| felix            | 1            | felon         | 1               |
| merveillos       | 1            | merveille     | 1               |
| après            | 1            | aspre         | 1               |
| oriande          | 1            | orïent        | 1               |
| blanchoiier      | 1            | blanchir      | 1               |
| sëure            | 1            | sore          | 1               |
| höer             | 1            | hoire         | 1               |
| poil             | 1            | pel1          | 1               |
| clerjon          | 1            | clerc         | 1               |
| yuliuz           | 1            | hilus         | 1               |
| depercier        | 1            | depecier      | 1               |
| face             | 1            | faire         | 1               |
| planter          | 1            | plenté        | 1               |
| remanoir         | 1            | remander      | 1               |
| estrangement     | 1            | estrange      | 1               |
| recoillir        | 1            | reculer       | 1               |
| celer2           | 1            | celer1        | 1               |
| apareillier1     | 1            | afebliier     | 1               |
| errer2           | 1            | erre1         | 1               |
| vengement        | 1            | venir         | 1               |
| deduit           | 1            | deduire       | 1               |
| jurer            | 1            | jesir         | 1               |
| endementieres    | 1            | endemain      | 1               |
| autant           | 1            | atant         | 1               |
| grece            | 1            | griche        | 1               |
| aiuel            | 1            | avoir         | 1               |
| jarlein          | 1            | maugalien     | 1               |
| larriz           | 1            | lorir         | 1               |
| gloton           | 1            | florc         | 1               |
| noveleté         | 1            | novité        | 1               |
| paulus           | 1            | paulon        | 1               |
| artilian         | 1            | artian        | 1               |
| enforcier1       | 1            | endormir      | 1               |
| huchier1         | 1            | hochier       | 1               |
| demaine1         | 1            | demener       | 1               |
| corroz           | 1            | culue2        | 1               |
| reforsener       | 1            | reforser2     | 1               |
| röeler           | 1            | roler         | 1               |
| secorre1         | 1            | secor         | 1               |
| estre4           | 1            | estre1        | 1               |
| monëer           | 1            | mener         | 1               |
| foiz             | 1            | foi           | 1               |
| nigremance       | 1            | nigerece      | 1               |
| jart1            | 1            | jart          | 1               |
| nöer2            | 1            | no11          | 1               |
| mener            | 1            | moine1        | 1               |
| avancir          | 1            | avenant       | 1               |
| cambrai          | 1            | charmir       | 1               |
| lacier           | 1            | laschier      | 1               |
| ligne2           | 1            | ligniee       | 1               |
| avorter          | 1            | avoir         | 1               |
| redementer       | 1            | redemander    | 1               |
| pomier           | 1            | pamier        | 1               |
| penëant          | 1            | penëir        | 1               |
| sostenement      | 1            | sostement     | 1               |
| toivre           | 1            | tibre         | 1               |
| gerir            | 1            | garir         | 1               |
| empeler          | 1            | emparlir      | 1               |
| chëable          | 1            | crëable       | 1               |
| afeblir          | 1            | esfloitier    | 1               |
| colorir          | 1            | convoir       | 1               |
| sol1             | 1            | soz           | 1               |
| pesme            | 1            | pieme         | 1               |
| jornee           | 1            | jorner        | 1               |
| plein            | 1            | pleinement    | 1               |
| douce-joie       | 1            | doucier       | 1               |
| marguerite       | 1            | marchëarie    | 1               |
| porter           | 1            | port2         | 1               |
| eschivement      | 1            | eschiement    | 1               |
| baillir          | 1            | baillier      | 1               |
| escorser         | 1            | escorre1      | 1               |
| covent1          | 1            | conoistre     | 1               |
| eschëoir         | 1            | eschifier     | 1               |
| oblïance         | 1            | oblice        | 1               |
| margerie         | 1            | magier        | 1               |
| serrer           | 1            | sarrer        | 1               |
| silence          | 1            | siglence      | 1               |
| marche1          | 1            | marche2       | 1               |
| asseoir          | 1            | asne          | 1               |
| boter1           | 1            | buitier       | 1               |
| reprendre2       | 1            | reprendre1    | 1               |
| malëure          | 1            | malëur        | 1               |
| durement         | 1            | durement2     | 1               |
| tarir            | 1            | taire         | 1               |
| privee           | 1            | privé1        | 1               |
| gerin            | 1            | garin         | 1               |
| vis1             | 1            | uis           | 1               |
| tiran            | 1            | tirer         | 1               |
| doucement        | 1            | douz          | 1               |
| messie           | 1            | maisniee      | 1               |
| ci               | 1            | si            | 1               |
| äi!              | 1            | hai!          | 1               |
| desonorer        | 1            | desofrir      | 1               |
| orer2            | 1            | öir           | 1               |
| enubler          | 1            | anobler       | 1               |
| sanses           | 1            | samsun        | 1               |
| maistre          | 1            | metre2        | 1               |
| aprendre         | 1            | apercenoir    | 1               |
| passemervoille   | 1            | passemsele    | 1               |
| tortüe           | 1            | tort1         | 1               |
| serpent          | 1            | saprent       | 1               |
| compagnie        | 1            | compagne1     | 1               |
| cors2            | 1            | cors1         | 1               |
| sofrir           | 1            | assourer      | 1               |
| puiz             | 1            | poi           | 1               |
| envoiier         | 1            | envoie        | 1               |
| vent             | 1            | vendre        | 1               |
| flair            | 1            | floisir       | 1               |
| rose             | 1            | ros3          | 1               |
| encraissier      | 1            | engresser     | 1               |
| port2            | 1            | porter        | 1               |
| serreement       | 1            | sarrasinement | 1               |
| ceseire          | 1            | cesar         | 1               |
| esche            | 1            | aiguece       | 1               |
| entaillëure      | 1            | antiel        | 1               |
| ponpinius        | 1            | ponpinien     | 1               |
| ponponius        | 1            | ponpoing      | 1               |
| sëeler           | 1            | salir2        | 1               |
| durandart        | 1            | durendal      | 1               |
| meillor          | 1            | mesler        | 1               |
| membré1          | 1            | membré2       | 1               |
| sacrefise        | 1            | sacrefiier    | 1               |
| mescroire        | 1            | mescrëant     | 1               |
| morir            | 1            | mort          | 1               |
| relenquir        | 1            | relever       | 1               |
| remetre          | 1            | remanoir      | 1               |
| ordure           | 1            | ordre         | 1               |
| aceindre         | 1            | acener        | 1               |
| forclose         | 1            | forsel        | 1               |
| teindre          | 1            | toindre       | 1               |
| broche           | 1            | broche1       | 1               |
| ardre            | 1            | hardir        | 1               |
| université       | 1            | unevrité      | 1               |
| pardonable       | 1            | pardunal      | 1               |
| desarmer         | 1            | deserment     | 1               |
| ospinel          | 1            | opinïon       | 1               |
| laver            | 1            | lever         | 1               |
| soillier         | 1            | soille        | 1               |
| samsoinie        | 1            | samsonie      | 1               |
| muntbrant        | 1            | muntram       | 1               |
| joiant           | 1            | vëoir         | 1               |
| maucuidant       | 1            | maudire       | 1               |
| loigne1          | 1            | lonc          | 1               |
| anmarri          | 1            | enraisri      | 1               |
| tente4           | 1            | tant          | 1               |
| miche            | 1            | miche1        | 1               |
| ostesse          | 1            | oster2        | 1               |
| aprentiz         | 1            | aprendre      | 1               |
| corëor           | 1            | coroier       | 1               |
| baston           | 1            | batre         | 1               |
| angoissier       | 1            | angoisse      | 1               |
| sëu              | 1            | savoir        | 1               |
| cosin            | 1            | cuisine       | 1               |
| ateindre         | 1            | ataindre      | 1               |
| embel1ir         | 1            | embelie       | 1               |
| seror            | 1            | süer          | 1               |
| especïaument     | 1            | espusicement  | 1               |
| manant           | 1            | mener         | 1               |
| alegier1         | 1            | alige         | 1               |
| assoagier        | 1            | assauge       | 1               |
| espuisier        | 1            | espoisier     | 1               |
| mesfait          | 1            | mesfaire      | 1               |
| delaiance        | 1            | delaie        | 1               |
| pute+gent1       | 1            | poindre       | 1               |
| demoree          | 1            | demorer       | 1               |
| süer             | 1            | suen          | 1               |
| som3             | 1            | som2          | 1               |
| estorbeillon     | 1            | estoble1      | 1               |
| part1            | 1            | partir        | 1               |
| voloir           | 1            | viel          | 1               |
| amenistracion    | 1            | amistion      | 1               |
| mu1              | 1            | mul3          | 1               |
| letré1           | 1            | letré         | 1               |
| mangier          | 1            | maigre        | 1               |
| orteil           | 1            | artu          | 1               |
| loier            | 1            | loiier        | 1               |
| apolin           | 1            | apolir        | 1               |
| piramus          | 1            | pirampor      | 1               |
| melancolie       | 1            | melealon      | 1               |
| apointier2       | 1            | apoindre      | 1               |
| ossenefort       | 1            | oblase        | 1               |
| chastel          | 1            | chautel       | 1               |
| que2+il          | 1            | que4          | 1               |
| escachier        | 1            | eschaucier    | 1               |
| desassembler     | 1            | dessaucier    | 1               |
| fonz             | 1            | font1         | 1               |
| lambegues        | 1            | lamberlenc    | 1               |
| uevre            | 1            | ovrir         | 1               |
| fin1             | 1            | fin2          | 1               |
| mail             | 1            | mal1          | 1               |
| piler2           | 1            | pilet2        | 1               |
| ravoiier         | 1            | ravoir2       | 1               |
| garder           | 1            | garde         | 1               |
| vinçant          | 1            | saint-vincent | 1               |
| guerredon        | 1            | gironde       | 1               |
| gremoarz         | 1            | gremarain     | 1               |
| muntdisoier      | 1            | montidier     | 1               |
| edesse           | 1            | deseut        | 1               |
| laudesse         | 1            | laudunet      | 1               |
| forsen           | 1            | forsener      | 1               |
| paliz            | 1            | palir         | 1               |
| devise           | 1            | deviser       | 1               |
| raconter         | 1            | reconter      | 1               |
| chandoile        | 1            | chaudel       | 1               |
| soner            | 1            | sovenir       | 1               |
| brabançon        | 1            | brebican      | 1               |
| jesu             | 1            | jhesu         | 1               |
| precier          | 1            | prëechier     | 1               |
| ole              | 1            | il            | 1               |
| mëismes          | 1            | mëisme        | 1               |
| mors1            | 1            | mur           | 1               |
| mal              | 1            | mal1          | 1               |
| priscillien      | 1            | prisicle      | 1               |
| noinz            | 1            | nom           | 1               |
| soute            | 1            | soter2        | 1               |
| prison           | 1            | dragon        | 1               |
| fors1            | 1            | fort          | 1               |
| despendëor2      | 1            | despendëor    | 1               |
| porreture        | 1            | porte1        | 1               |
| porpoindre       | 1            | porpensé1     | 1               |
| enföir1          | 1            | enföir2       | 1               |
| noçoiier         | 1            | nocier        | 1               |
| paumoiier        | 1            | paumie2       | 1               |
| regarder         | 1            | ergaragnier   | 1               |
| oripont          | 1            | orïent        | 1               |
| fossé            | 1            | fosse         | 1               |
| carriere         | 1            | craisdre      | 1               |
| renge2           | 1            | resne2        | 1               |
| desserrer        | 1            | descirier     | 1               |
| crïacïon         | 1            | crïator       | 1               |
| el1              | 1            | en1+le        | 1               |
| fontaine         | 1            | fontene       | 1               |
| fé               | 1            | faire         | 1               |
| comé             | 1            | comer1        | 1               |
| aloigne          | 1            | aleigne       | 1               |
| eschevir3        | 1            | excevin       | 1               |
| sorargenter      | 1            | sorage        | 1               |
| radoter          | 1            | radoter1      | 1               |
| de+il            | 1            | de+le         | 1               |
| ressuier         | 1            | resuscire     | 1               |
| costure          | 1            | coutree       | 1               |
| damagier         | 1            | damagne       | 1               |
| amer1            | 1            | amasser       | 1               |
| araisne          | 1            | areine        | 1               |
| oreillier3       | 1            | oreillier1    | 1               |
| quarrois         | 1            | carrois       | 1               |
| carduel          | 1            | karadusal     | 1               |
| devisëor         | 1            | devisïon      | 1               |
| däerrain         | 1            | derrenier     | 1               |
| engrant          | 1            | emgrant       | 1               |
| antiaume         | 1            | entencïos     | 1               |
| tesmoignement    | 1            | tesmoignier   | 1               |
| ancïeneté        | 1            | anciien       | 1               |
| eslaissier       | 1            | eslacier      | 1               |
| templier2        | 1            | templir       | 1               |
| jus1             | 1            | ius           | 1               |
| que2/            | 1            | que2          | 1               |
| livre3           | 1            | livre1        | 1               |

# POS 

```
all:
  accuracy: 0.9613
  precision: 0.7828
  recall: 0.7572
  support: 48317
ambiguous-tokens:
  accuracy: 0.9549
  precision: 0.7888
  recall: 0.753
  support: 32232
unknown-tokens:
  accuracy: 0.8677
  precision: 0.5959
  recall: 0.5918
  support: 1792
```

| Expected      | Total Errors | Predictions   | Predicted times |
|---------------|--------------|---------------|-----------------|
| NOMcom        | 247          | ADJqua        | 76              |
|               |              | ADVgen        | 32              |
|               |              | VERcjg        | 29              |
|               |              | VERppe        | 28              |
|               |              | NOMpro        | 22              |
|               |              | VERinf        | 22              |
|               |              | PROind        | 12              |
|               |              | VERppa        | 6               |
|               |              | ADVneg        | 4               |
|               |              | OUT           | 4               |
|               |              | PRE           | 3               |
|               |              | PROcar        | 2               |
|               |              | PROrel        | 1               |
|               |              | PROadv        | 1               |
|               |              | ADVsub        | 1               |
|               |              | PROper        | 1               |
|               |              | ADJcar        | 1               |
|               |              | PRE.DETdef    | 1               |
|               |              | DETind        | 1               |
| CONsub        | 146          | PROrel        | 62              |
|               |              | CONcoo        | 52              |
|               |              | ADVgen        | 15              |
|               |              | PROper        | 7               |
|               |              | ADVint        | 4               |
|               |              | PROint        | 2               |
|               |              | PROdem        | 2               |
|               |              | ADVsub        | 1               |
|               |              | DETpos        | 1               |
| ADVgen        | 144          | NOMcom        | 25              |
|               |              | PRE           | 21              |
|               |              | PROind        | 18              |
|               |              | CONsub        | 13              |
|               |              | PROper        | 12              |
|               |              | ADJqua        | 10              |
|               |              | CONcoo        | 8               |
|               |              | DETind        | 7               |
|               |              | VERcjg        | 6               |
|               |              | DETdef        | 5               |
|               |              | PROrel        | 4               |
|               |              | VERinf        | 2               |
|               |              | ADJind        | 2               |
|               |              | NOMpro        | 2               |
|               |              | DETpos        | 1               |
|               |              | VERppe        | 1               |
|               |              | PROord        | 1               |
|               |              | ADVsub        | 1               |
|               |              | ADVgen.PROper | 1               |
|               |              | PROadv        | 1               |
|               |              |               | 1               |
|               |              | ADVneg        | 1               |
|               |              | PROint        | 1               |
| ADJqua        | 131          | NOMcom        | 68              |
|               |              | VERppe        | 17              |
|               |              | ADVgen        | 13              |
|               |              | VERcjg        | 9               |
|               |              | VERppa        | 6               |
|               |              | OUT           | 4               |
|               |              | NOMpro        | 4               |
|               |              | PRE           | 3               |
|               |              | PROind        | 2               |
|               |              | PROper        | 1               |
|               |              | DETcar        | 1               |
|               |              | ADJpos        | 1               |
|               |              | VERinf        | 1               |
|               |              | ADJind        | 1               |
| CONcoo        | 129          | CONsub        | 75              |
|               |              | ADVneg        | 29              |
|               |              | PROrel        | 13              |
|               |              | ADVgen        | 9               |
|               |              | VERcjg        | 1               |
|               |              | DETpos        | 1               |
|               |              | PRE.DETdef    | 1               |
| VERcjg        | 114          | NOMcom        | 35              |
|               |              | VERppe        | 32              |
|               |              | PRE           | 29              |
|               |              | ADJqua        | 6               |
|               |              | ADVgen        | 4               |
|               |              | PRE.DETdef    | 3               |
|               |              | VERinf        | 3               |
|               |              | ADJind        | 1               |
|               |              | PROper        | 1               |
| PROrel        | 102          | CONsub        | 77              |
|               |              | PROint        | 8               |
|               |              | CONcoo        | 7               |
|               |              | ADVgen        | 6               |
|               |              | DETrel        | 3               |
|               |              | NOMcom        | 1               |
| VERppe        | 82           | VERcjg        | 33              |
|               |              | NOMcom        | 30              |
|               |              | ADJqua        | 12              |
|               |              | ADJpos        | 2               |
|               |              | VERinf        | 1               |
|               |              | OUT           | 1               |
|               |              | VERppa        | 1               |
|               |              | ADVgen        | 1               |
|               |              | PROper        | 1               |
| PROper        | 74           | DETdef        | 27              |
|               |              | PROimp        | 18              |
|               |              | ADVgen        | 8               |
|               |              | PROind        | 7               |
|               |              | DETpos        | 6               |
|               |              | PROadv        | 3               |
|               |              | CONsub        | 3               |
|               |              | PROpos        | 1               |
|               |              | NOMcom        | 1               |
| PROimp        | 72           | PROper        | 72              |
| PRE           | 70           | ADVgen        | 29              |
|               |              | VERcjg        | 16              |
|               |              | PROadv        | 9               |
|               |              | NOMcom        | 4               |
|               |              | PROind        | 4               |
|               |              | CONcoo        | 3               |
|               |              | ADJqua        | 2               |
|               |              | NOMpro        | 1               |
|               |              | PROint        | 1               |
|               |              | VERinf        | 1               |
| OUT           | 65           | NOMcom        | 19              |
|               |              | ADJqua        | 9               |
|               |              | VERcjg        | 6               |
|               |              | ADVgen        | 5               |
|               |              | NOMpro        | 5               |
|               |              | VERppe        | 5               |
|               |              | ADVneg        | 3               |
|               |              | DETpos        | 3               |
|               |              | CONcoo        | 1               |
|               |              | PROper        | 1               |
|               |              | VERppa        | 1               |
|               |              | PROdem        | 1               |
|               |              | VERinf        | 1               |
|               |              | PROrel        | 1               |
|               |              | PRE           | 1               |
|               |              | DETdem        | 1               |
|               |              | PROint        | 1               |
|               |              | DETdef        | 1               |
| PROind        | 61           | ADVgen        | 17              |
|               |              | DETind        | 13              |
|               |              | NOMcom        | 12              |
|               |              | ADJind        | 7               |
|               |              | DETndf        | 4               |
|               |              | PROadv        | 2               |
|               |              | PROper        | 2               |
|               |              | PRE           | 1               |
|               |              | ADJqua        | 1               |
|               |              | VERcjg        | 1               |
|               |              | PRE.DETdef    | 1               |
| NOMpro        | 45           | NOMcom        | 24              |
|               |              | VERinf        | 6               |
|               |              | VERcjg        | 4               |
|               |              | ADVgen        | 3               |
|               |              | ADJqua        | 2               |
|               |              | VERppe        | 2               |
|               |              | DETind        | 1               |
|               |              | CONcoo        | 1               |
|               |              | VERppa        | 1               |
|               |              | DETcar        | 1               |
| DETind        | 36           | PROind        | 15              |
|               |              | ADVgen        | 9               |
|               |              | ADJind        | 5               |
|               |              | ADJqua        | 4               |
|               |              | NOMcom        | 1               |
|               |              | DETndf        | 1               |
|               |              | PROdem        | 1               |
| DETcar        | 30           | DETndf        | 17              |
|               |              | ADJcar        | 4               |
|               |              | PROcar        | 3               |
|               |              | NOMcom        | 2               |
|               |              | VERcjg        | 1               |
|               |              | ADJord        | 1               |
|               |              | NOMpro        | 1               |
|               |              | PROind        | 1               |
| VERinf        | 30           | NOMcom        | 25              |
|               |              | VERcjg        | 2               |
|               |              | ADJqua        | 2               |
|               |              | NOMpro        | 1               |
| PROcar        | 27           | ADJcar        | 9               |
|               |              | DETcar        | 8               |
|               |              | PROind        | 4               |
|               |              | VERppe        | 1               |
|               |              | NOMpro        | 1               |
|               |              | DETndf        | 1               |
|               |              | PROper        | 1               |
|               |              | NOMcom        | 1               |
|               |              | CONsub        | 1               |
| ADVneg        | 26           | CONcoo        | 20              |
|               |              | NOMcom        | 4               |
|               |              | ADVgen        | 1               |
|               |              | PROind        | 1               |
| DETpos        | 25           | ADJpos        | 9               |
|               |              | PROper        | 9               |
|               |              | ADVgen        | 5               |
|               |              | OUT           | 1               |
|               |              | PROpos        | 1               |
| DETdef        | 21           | PROper        | 19              |
|               |              | ADVgen        | 2               |
| PROdem        | 20           | DETdem        | 13              |
|               |              | VERcjg        | 3               |
|               |              | CONsub        | 2               |
|               |              | NOMcom        | 1               |
|               |              | ADVgen        | 1               |
| PROint        | 19           | PROrel        | 14              |
|               |              | DETrel        | 1               |
|               |              | NOMcom        | 1               |
|               |              | NOMpro        | 1               |
|               |              | DETdem        | 1               |
|               |              | ADVgen        | 1               |
| VERppa        | 16           | ADJqua        | 10              |
|               |              | NOMpro        | 2               |
|               |              | VERcjg        | 2               |
|               |              | NOMcom        | 2               |
| ADJind        | 16           | PROind        | 7               |
|               |              | DETind        | 4               |
|               |              | ADJqua        | 3               |
|               |              | VERcjg        | 1               |
|               |              | ADVgen        | 1               |
| ADVsub        | 16           | CONsub        | 10              |
|               |              | ADVgen        | 3               |
|               |              | ADVint        | 3               |
| ADJpos        | 13           | DETpos        | 10              |
|               |              | PROpos        | 3               |
| PROadv        | 11           | PRE           | 5               |
|               |              | PROind        | 4               |
|               |              | DETndf        | 1               |
|               |              | PROrel        | 1               |
| ADVint        | 11           | CONsub        | 10              |
|               |              | ADVsub        | 1               |
| DETdem        | 9            | PROdem        | 8               |
|               |              | DETpos        | 1               |
| DETndf        | 9            | DETcar        | 5               |
|               |              | PROind        | 2               |
|               |              | PROadv        | 1               |
|               |              | PROcar        | 1               |
| PRE.DETdef    | 8            | CONcoo        | 3               |
|               |              | PROper        | 2               |
|               |              | PROrel        | 1               |
|               |              | VERcjg        | 1               |
|               |              | PRE           | 1               |
| ADJcar        | 7            | DETcar        | 5               |
|               |              | PROcar        | 1               |
|               |              | ADJord        | 1               |
|               | 7            | ADJqua        | 1               |
|               |              | PROper        | 1               |
|               |              | VERinf        | 1               |
|               |              | DETdef        | 1               |
|               |              | PROadv        | 1               |
|               |              | PRE           | 1               |
|               |              | CONcoo        | 1               |
| DETrel        | 6            | PROrel        | 3               |
|               |              | DETint        | 3               |
| PROpos        | 5            | ADJpos        | 5               |
| DETint        | 4            | DETrel        | 4               |
| PROord        | 4            | ADJord        | 3               |
|               |              | VERcjg        | 1               |
| INJ           | 3            | VERcjg        | 3               |
| PRE.PROper    | 2            | PRE.DETdef    | 1               |
|               |              | CONcoo        | 1               |
| ADVneg.PROper | 1            | PROper        | 1               |
| CONsubs       | 1            | CONsub        | 1               |
| ADVgen.PROadv | 1            | ADVgen        | 1               |
| DETord        | 1            | ADJqua        | 1               |
| PROrel.PROper | 1            | CONsub        | 1               |
