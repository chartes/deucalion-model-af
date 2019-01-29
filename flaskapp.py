"""

This module can be run by install the app requirements (`pip install -r requirements-app.txt`)

The goal here is to be able to have, later, a distributed series of APIs that could be using different version of Pie
and run through containers, unified by a public API such as https://github.com/hipster-philology/deucalion which would
then talk to the different micro-services.

How to run for development :
    PIE_MODEL=/home/thibault/dev/pie/model-lemma-2018_10_23-14_05_19.tar FLASK_ENV=development flask run

    where PIE_MODEL is the path to your model

How to run in production :
    gunicorn --workers 2 app:app --env PIE_MODEL=/home/thibault/dev/pie/model-lemma-2018_10_23-14_05_19.tar

    Probably add to this a --bind

Example URL:
    http://localhost:5000/?data=Ci+gist+saint+Martins+el+sains+de+tours.%20Il%20fut%20bon%20rois.

Example curl :
    curl --data "data=Ci gist saint Martins el sains de tours. Il fut bon rois." http://localhost:5000

Example output :
    token	lemma	morph	pos
    ci	ci	DEGRE=-	ADVgen
    gist	jesir	MODE=ind|TEMPS=pst|PERS.=3|NOMB.=s	VERcjg
    saint	saint	NOMB.=s|GENRE=f|CAS=r	ADJqua
    martins	martin	NOMB.=s|GENRE=m|CAS=r	NOMcom
    el	en1+le	NOMB.=s|GENRE=m|CAS=r	PRE.DETdef
    sains	sain	NOMB.=p|GENRE=m|CAS=r	NOMcom
    de	de	MORPH=empty	PRE
    tours	tor2	NOMB.=p|GENRE=f|CAS=r	NOMcom
    .	.	_	PONfrt
    il	il	PERS.=3|NOMB.=s|GENRE=m|CAS=n	PROper
    fut	estre1	MODE=ind|TEMPS=psp|PERS.=3|NOMB.=s	VERcjg
    bon	bon	NOMB.=s|GENRE=m|CAS=n|DEGRE=p	ADJqua
    rois	roi2	NOMB.=s|GENRE=m|CAS=n	NOMcom
    .	.	_	PONfrt

"""
from webapp import bind, Formatter
from flask import Flask, render_template
import re

app = Flask(__name__, static_folder="./statics", template_folder="./templates")


@app.route("/")
def form():
    return render_template("index.html")


class GlueFormatter(Formatter):
    HEADERS = ["token", "lemma", "POS", "morph"]
    MORPH_PART = ["MODE", "TEMPS", "PERS.", "NOMB.", "GENRE", "CAS", "DEGRE"]
    PONCTU = re.compile("\W")

    def __init__(self, tasks):
        super(GlueFormatter, self).__init__(tasks)
        self.pos_tag = "POS"
        if "POS" not in self.tasks and "pos" in self.tasks:
            self.pos_tag = "pos"

    def format_headers(self):
        return GlueFormatter.HEADERS

    def format_line(self, token, tags):
        tags = list(tags)
        lemma = tags[self.tasks.index("lemma")]
        if GlueFormatter.PONCTU.match(lemma):
            lemma = token

        return [
            token,
            lemma,
            tags[self.tasks.index(self.pos_tag)],
            "|".join(
                "{cat}={tag}".format(
                    cat=morph_part,
                    tag=tags[self.tasks.index(morph_part.replace(".", ""))]
                )
                for morph_part in GlueFormatter.MORPH_PART
                if morph_part.replace(".", "") in self.tasks and
                tags[self.tasks.index(morph_part.replace(".", ""))] != "_"
            ) or "MORPH=empty"
        ]


# Add the lemmatizer routes
bind(app, formatter_class=GlueFormatter, route_path="/api")
