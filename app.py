from typing import Text
from flask import Flask, render_template, request
import tweepy as tw
from sentilex import Score_sentimento
import spidev
import ws2812

app = Flask(__name__)

@app.route('/')
def index():  # put application's code here

    spi = spidev.SpiDev()
    spi.open(0,0)
    ws2812.write2812(spi, [[0,0,0] * 33])

    #twitter

    consumer_key = "QO61pvhO0VdFaZBIGJLbhRBfG"
    consumer_secret = "vuN4ATiwzf3BenkzkeG3kXr6ISGZ17makoOgEuoyt7Rs3JHGel"
    access_token = "1427399398481399819-hAhAKowuXS7fNFYrSMUpBYiv6Qmm5P"
    access_token_secret = "NMx85GIh4PzVY54PQIcoYfEFSdgSjfSoy1fSVE45UNbdX"
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    public_tweets = api.home_timeline()

    if request.args.get("busca"):
        palavra_busca = request.args.get("busca")
    else:
        palavra_busca = ""

    i = 0
    tweets = {}
    armpol = 0
    for tweet in public_tweets:
        tweets[i] = tweet._json
        tweets[i]["polaridade"] = Score_sentimento(tweets[i]["text"])
        
        if(palavra_busca in str(tweets[i]["text"]) and palavra_busca != ""):
            armpol += int(tweets[i]["polaridade"].split(":")[1])
        elif(palavra_busca == ""):
            armpol += int(tweets[i]["polaridade"].split(":")[1])
        i += 1

    media = 0
    media = armpol / i
    #return tweets
    if(media > 0):
        ws2812.write2812(spi, [[10,0,0] * 33])
    if(media == 0):
        ws2812.write2812(spi, [[8,9 ,0 ] * 33])
    if(media < 0):
        ws2812.write2812(spi, [[0,10,0] * 33])
    
    i = 0
    armpol = 0
    media = 0
    return render_template("Tweets.html", tweets=tweets, busca=palavra_busca)




if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
