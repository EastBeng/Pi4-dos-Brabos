import json

from flask import Flask, render_template, request
import tweepy as tw

app = Flask(__name__)


#@app.route('/')
#def index():  # put application's code here
#    return render_template('PaginaWeb.html')

#@app.route('/tweets')
#def tweets():
@app.route('/')
def index():  # put application's code here
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

    for tweet in public_tweets:
        tweets[i] = tweet._json
        i += 1

    return render_template("Tweets.html", tweets=tweets, busca=palavra_busca)

@app.route('/buscar_tweets')
def buscar_tweets():

    buscar = request.args.get("pesquisa")
    tipo_tweet = request.args.get("tipo_tweet")

    if tipo_tweet=="Meus Tweets":
        template_lista_tweets = "UserTweets.html"
    else:
        template_lista_tweets = "TimeLineTweets.html"

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

    return render_template(template_lista_tweets, timeline=aux, busca=buscar)

@app.route('/user_tweets')
def user_tweets():

    buscar_user = request.args.get("pesquisa")

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

    return render_template("UserTweets.html", timeline=aux, busca=buscar_user)

@app.route('/timeline_tweets')
def timeline_tweets():

    buscar_timeline = request.args.get("pesquisa")

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

    return render_template("TimeLineTweets.html", timeline=aux, busca=buscar_timeline)

if __name__ == '__main__':
    app.run(debug=True, port=80)