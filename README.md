Deucalion Model Ancien Français ENC
===================================

## Cite As

```bibtex
@software{clerice_thibault_2019_3237455,
  author       = {Clérice, Thibault and
                  Camps, Jean-Baptiste and
                  Pinche, Ariane},
  title        = {Deucalion, Modèle Ancien Francais (0.2.0)},
  month        = jun,
  year         = 2019,
  publisher    = {Zenodo},
  version      = {v0.2.0},
  doi          = {10.5281/zenodo.3237455},
  url          = {https://doi.org/10.5281/zenodo.3237455}
}
```

## Credits

This model can be used with [Pie-Extended](https://github.com/hipster-philology/nlp-pie-taggers) and tested on [Deucalion](https://dh.chartes.psl.eu/deucalion/fro).

This mosdel is trained on Pie by Enrique Manjavacas (@emanjavacas) and Mike Kestemont (@mikekestemont) [![DOI](https://zenodo.org/badge/131014015.svg)](https://zenodo.org/badge/latestdoi/131014015).

## Information about the model

### Corpora

The model was trained on the following corpora :

- _Geste: un corpus de chansons de geste_, dir. Jean-Baptiste Camps, avec la collab. d'Elena Albarran, Alice Cochet & Lucence Ing, Paris, 2016-…, http://github.com/Jean-Baptiste-Camps/Geste.
- _Édition nativement numérique du recueil hagiographique "Li Seint Confessor" de Wauchier de Denain d'après le manuscrit 412 de la Bibliothèque nationale de France_, éd. Ariane Pinche, Lyon, en cours (only _Dialogues_ and La vie de Saint Martin are used right now. Data are closed source until publication of the PhD thesis)
- _Les Institutes de Justinien en français_, éd. F. Olivier-Martin (1935), éd. revue par F. Duval, lemmatisée par F. Duval et L. Ing. Paris, 2018.
- _Chrétien de Troyes: Cligès, Erec, Lancelot, Perceval, Yvain -- Manuscrit P (BnF Fr. 794)_, éd. P. Kunstmann (2009), annotation revue par J.B. Camps et L. Ing (2017).


### Annotations

The **annotations** are made according to the following reference lists:

- **lemma:** Adolf Tobler et Erhard Friedrich Lommatzsch, _Altfranzösisches Wörterbuch: édition électronique_, éd. Peter Blumenthal et Achim Stein, Stuttgart, F. Steiner, 2002.
- **POS and morph:** Sophie Prévost, Céline Guillot, Alexei Lavrentiev et Serge Heiden, _Jeu d’étiquettes morphosyntaxiques  CATTEX2009-max_, Lyon, 2013, http://bfm.ens-lyon.fr/IMG/pdf/Cattex2009_2.0.pdf.

More information on the annotation practice can be found in the wiki of the _Geste_ corpus: [https://github.com/Jean-Baptiste-Camps/Geste/wiki](https://github.com/Jean-Baptiste-Camps/Geste/wiki).

## Sample

Sample from annotation:

<<<<<<< HEAD
```tsv
form	lemma	POS	morph
G'	je	PROper	PERS.=1|NOMB.=s|GENRE=m|CAS=n
irai	aler	VERcjg	MODE=ind|TEMPS=fut|PERS.=1|NOMB.=s
sor	sor2	PRE	MORPH=empty
eus	il	PROper	PERS.=3|NOMB.=p|GENRE=m|CAS=i
por	por2	PRE	MORPH=empty
lor	lor2	DETpos	PERS.=3|NOMB.=p|GENRE=f|CAS=r
terres	terre	NOMcom	NOMB.=p|GENRE=f|CAS=r
saisir	saisir	VERinf	MORPH=empty
```
