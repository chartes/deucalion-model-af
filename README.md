Deucalion Model Ancien Français ENC
===================================

[![Lien Docker](https://img.shields.io/docker/pulls/ponteineptique/deucalion-model-af.svg)](https://cloud.docker.com/repository/docker/ponteineptique/deucalion-model-af)

# Credits

This software is based on Pie by Enrique Manjavacas (@emanjavacas) and Mike Kestemont (@mikekestemont) [![DOI](https://zenodo.org/badge/131014015.svg)](https://zenodo.org/badge/latestdoi/131014015)

The web application and its maintenance is done by Thibault Clérice ( @ponteineptique ). To learn how to cite this repository, go check [our releases](https://github.com/chartes/deucalion-model-af/releases).

# Information about the model

The model is based on  :

- Geste: un corpus de chansons de geste, dir. Jean-Baptiste Camps, avec la collab. d'Elena Albarran, Alice Cochet & Lucence Ing, Paris, 2016, http://github.com/Jean-Baptiste-Camps/Geste.
- Edition nativement numérique du recueil hagiographique "Li Seint Confessor" de Wauchier de Denain d'après le manuscrit 412 de la Bibliothèque nationale de France, Ariane Pinche, Lyon, Encours
	- Only Dialogues and La vie de Saint Martin are used right now. Data are closed source until publication of the PhD thesis.

For more details about the errors, see [CONFUSION.md](CONFUSION.md)


# Install

To run, you'll need to install Docker. Then, you can simply run the following commands :

```shell
docker build -t deucalion-af:latest .
docker run -p 5001:5000 deucalion-af:latest
```

You can replace 5001 with any port you want to run the service on.

Then, simply go to http://127.0.0.1:5001/?data=SOIGNORS,or%20escoutez,que%20D%C3%A9s%20vos%20soit%20amis,.III%20.vers%20de%20bone%20estoire,se%20je%20les%20vos%20devis or post any data to the same URI with `data` parameters containing your plain text.