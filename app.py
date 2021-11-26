from flask import Flask, render_template, request, redirect, url_for
from model import novos_tweets, abre_arquivo
# LED
import spidev
import ws2812

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here

    # LED
    spi = spidev.SpiDev()
    spi.open(0, 0)
    ws2812.write2812(spi, [[0, 0, 0] * 33])

    if request.args.get("novos_tweets")=="buscar": # novos tweets
        novos_tweets()
        return redirect(url_for('index'))
    else: # tweets já armazenados
        public_tweets = abre_arquivo()

    if request.args.get("busca"):
        palavra_busca = request.args.get("busca")
    else:
        palavra_busca = ""

    i = 0
    armpol = 0
    for tweet in public_tweets.values():
        if (palavra_busca in str(tweet["text"]) and palavra_busca != ""):
            armpol += int(tweet["polaridade"].split(":")[1])
        elif (palavra_busca == ""):
            armpol += int(tweet["polaridade"].split(":")[1])
        i = i+1

    # LED
    media = armpol / i
    if (media > 0):
        ws2812.write2812(spi, [[10, 0, 0] * 33])
    if (media == 0):
        ws2812.write2812(spi, [[8, 9, 0] * 33])
    if (media < 0):
        ws2812.write2812(spi, [[0, 10, 0] * 33])

    return render_template("Tweets.html", tweets=public_tweets, busca=palavra_busca)


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')