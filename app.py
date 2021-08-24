import json

from flask import Flask, render_template, request
import tweepy as tw

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('PaginaWeb.html')


@app.route('/user_tweets')
def user_tweets():

    #buscar = request.arg.get("buscar")

    consumer_key = "QO61pvhO0VdFaZBIGJLbhRBfG"
    consumer_secret = "vuN4ATiwzf3BenkzkeG3kXr6ISGZ17makoOgEuoyt7Rs3JHGel"
    access_token = "1427399398481399819-hAhAKowuXS7fNFYrSMUpBYiv6Qmm5P"
    access_token_secret = "NMx85GIh4PzVY54PQIcoYfEFSdgSjfSoy1fSVE45UNbdX"

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tw.API(auth, wait_on_rate_limit=True)

    #public_tweets = api.home_timeline()
    public_tweets = api.user_timeline()

    i = 0

    dicionario = {}

    for tweet in public_tweets:
        dicionario[i] = tweet.text
        i+=1

    #return json.dumps(dicionario)
    #return str(tweet._json)

    aux = dicionario

    return render_template("UserTweets.html", timeline=aux)

@app.route('/timeline_tweets')
def timeline_tweets():

    consumer_key = "QO61pvhO0VdFaZBIGJLbhRBfG"
    consumer_secret = "vuN4ATiwzf3BenkzkeG3kXr6ISGZ17makoOgEuoyt7Rs3JHGel"
    access_token = "1427399398481399819-hAhAKowuXS7fNFYrSMUpBYiv6Qmm5P"
    access_token_secret = "NMx85GIh4PzVY54PQIcoYfEFSdgSjfSoy1fSVE45UNbdX"

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tw.API(auth, wait_on_rate_limit=True)

    public_tweets = api.home_timeline()
    #public_tweets = api.user_timeline()

    i = 0
    dicionario = {}

    for tweet in public_tweets:
        dicionario[i] = tweet.text
        i += 1

    #return json.dumps(dicionario)
    aux = dicionario

    return render_template("TimeLineTweets.html", timeline=aux)

if __name__ == '__main__':
    app.run(debug=True, port=80)
