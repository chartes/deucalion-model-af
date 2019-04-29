import re

from flask import Flask, render_template

from flask_pie import PieController
from flask_pie.utils import Formatter, DataIterator


app = Flask(__name__, static_folder="./statics", template_folder="./templates")


@app.route("/")
def form():
    return render_template("index.html")


# Uppercase regexp
uppercase = re.compile("^[A-Z]$")


class GlueFormatter(Formatter):
    HEADERS = ["form", "lemma", "POS", "morph"]
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


controller = PieController(
    model_file="<morph.tar,MODE,TEMPS,PERS,NOMB,GENRE,CAS,DEGRE><lemma-pos.tar,lemma,pos>",
    headers={"X-Accel-Buffering": "no"},
    formatter_class=GlueFormatter, batch_size=16
)
controller.init_app(app)


if __name__ == "__main__":
    app.run(debug=True)
