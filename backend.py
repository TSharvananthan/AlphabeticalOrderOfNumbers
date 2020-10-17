import flask
from utils import *
import os

app = flask.Flask(__name__)

@app.route("/")
def home():
    return flask.render_template("index.html")

@app.route("/ordered/", methods=["POST"])
def ordered():
    form = dict(flask.request.form)
    max_num = int(form["number"])

    words = sort_number_words(list(range(1, max_num + 1)))
    return flask.render_template("ordered.html", words=words)

'remove cache'
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return flask.url_for(endpoint, **values)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
