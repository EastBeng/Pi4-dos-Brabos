from flask import Flask, render_template, request, redirect, url_for
from model import novos_tweets, abre_arquivo

app = Flask(__name__)


@app.route('/')
def index():
    if request.args.get("novos_tweets")=="buscar": # novos tweets
        novos_tweets()
        return redirect(url_for('index'))
    else: # tweets já armazenados
        tweets = abre_arquivo()

    if request.args.get("busca"): # termo buscado entre os tweets
        palavra_busca = request.args.get("busca")
    else:
        palavra_busca = ""

    return render_template("Tweets.html", tweets=tweets, busca=palavra_busca)


if __name__ == '__main__':
    app.run(debug=True, port=80)