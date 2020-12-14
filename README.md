Deucalion Model Ancien Français ENC
===================================

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2539134.svg)](https://doi.org/10.5281/zenodo.2539134)

## Model files

Because models are large files, only Markdown is kept in this repository. Find the latest model in the [Release tab](https://github.com/chartes/deucalion-model-af/releases/latest)

## Cite As

```bibtex
@software{clerice_thibault_2019_3237455,
  author       = {Camps, Jean-Baptiste and
                  Clérice, Thibault and
                  Pinche, Ariane and
                  Ing, Lucence and
                  Duval, Frédéric and
                  Kanaoka, Naomi},
  title        = {Deucalion, Modèle Ancien Francais (0.3.0)},
  month        = dec,
  year         = 2020,
  publisher    = {Zenodo},
  version      = {v0...0},
  doi          = {10.5281/zenodo.4320487},
  url          = {https://doi.org/10.5281/zenodo.4320487}
}
```

## Credits

This model can be used with [Pie-Extended](https://github.com/hipster-philology/nlp-pie-taggers) and tested on [Deucalion](https://dh.chartes.psl.eu/deucalion/fro).

This mosdel is trained on Pie by Enrique Manjavacas (@emanjavacas) and Mike Kestemont (@mikekestemont) [![DOI](https://zenodo.org/badge/131014015.svg)](https://zenodo.org/badge/latestdoi/131014015).

## Information about the model

### Scores

<!-- Start Scores -->
More details:
- [lemma](lemma-pos.score.md)
- [POS](lemma-pos.score.md)
- [NOMB](morph/nomb.tar.score.md)
- [DEGRE](morph/degre.tar.score.md)
- [GENRE](morph/genre.tar.score.md)
- [CAS](morph/cas.tar.score.md)
- [TEMPS](morph/temps.tar.score.md)
- [PERS](morph/pers.tar.score.md)
- [MODE](morph/mode.tar.score.md)


#### lemma

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9747   | 0.7284    | 0.726  | 73507   |
| known-tokens     | 0.9831   | 0.8969    | 0.8979 | 71726   |
| unknown-tokens   | 0.6367   | 0.4327    | 0.4326 | 1781    |
| ambiguous-tokens | 0.9777   | 0.7723    | 0.7752 | 44987   |
| unknown-targets  | 0.0751   | 0.0408    | 0.0408 | 253     |


#### POS

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9739   | 0.8129    | 0.787  | 73507   |
| known-tokens     | 0.9775   | 0.8325    | 0.8098 | 71726   |
| unknown-tokens   | 0.8293   | 0.528     | 0.5079 | 1781    |
| ambiguous-tokens | 0.9713   | 0.8126    | 0.8007 | 49942   |


#### NOMB

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.966    | 0.9589    | 0.9576 | 28824   |
| known-tokens     | 0.9709   | 0.9635    | 0.9627 | 27536   |
| unknown-tokens   | 0.8626   | 0.8505    | 0.7935 | 1288    |
| ambiguous-tokens | 0.9538   | 0.9473    | 0.9481 | 14032   |


#### DEGRE

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9842   | 0.8266    | 0.7396 | 28824   |
| known-tokens     | 0.9865   | 0.8475    | 0.7554 | 27536   |
| unknown-tokens   | 0.9356   | 0.5693    | 0.4783 | 1288    |
| ambiguous-tokens | 0.9524   | 0.8443    | 0.7695 | 5863    |


#### GENRE

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9608   | 0.9276    | 0.8738 | 28824   |
| known-tokens     | 0.9671   | 0.9332    | 0.8815 | 27536   |
| unknown-tokens   | 0.8245   | 0.6139    | 0.6159 | 1288    |
| ambiguous-tokens | 0.9428   | 0.9156    | 0.863  | 13608   |


#### CAS

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9457   | 0.9057    | 0.9052 | 28824   |
| known-tokens     | 0.9514   | 0.9105    | 0.9106 | 27536   |
| unknown-tokens   | 0.8238   | 0.6096    | 0.605  | 1288    |
| ambiguous-tokens | 0.9301   | 0.9036    | 0.9054 | 16647   |


#### TEMPS

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9854   | 0.945     | 0.9408 | 28824   |
| known-tokens     | 0.9886   | 0.9584    | 0.9585 | 27536   |
| unknown-tokens   | 0.9169   | 0.8372    | 0.8109 | 1288    |
| ambiguous-tokens | 0.9644   | 0.9331    | 0.9527 | 4638    |


#### PERS

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9872   | 0.8732    | 0.7848 | 28824   |
| known-tokens     | 0.9897   | 0.8782    | 0.7906 | 27536   |
| unknown-tokens   | 0.9325   | 0.8832    | 0.8721 | 1288    |
| ambiguous-tokens | 0.9756   | 0.8709    | 0.7839 | 8648    |


#### MODE

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9897   | 0.9086    | 0.8815 | 28824   |
| known-tokens     | 0.9932   | 0.9284    | 0.9066 | 27536   |
| unknown-tokens   | 0.9146   | 0.7783    | 0.7381 | 1288    |
| ambiguous-tokens | 0.9722   | 0.8739    | 0.9003 | 4603    |


<!-- End Scores -->

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
