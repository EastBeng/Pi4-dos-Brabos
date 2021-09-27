from flask import Flask, render_template, request
import tweepy as tw
from sentilex import Score_sentimento

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here

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

    for tweet in public_tweets:
        tweets[i] = tweet._json
        tweets[i]["polaridade"] = Score_sentimento(tweets[i]["text"])
        i += 1

    #return tweets
    return render_template("Tweets.html", tweets=tweets, busca=palavra_busca)


if __name__ == '__main__':
    app.run(debug=True, port=80)