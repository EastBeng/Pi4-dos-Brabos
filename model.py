import json
from sentilex import Score_sentimento
import tweepy as tw


def novos_tweets():
    consumer_key = "QO61pvhO0VdFaZBIGJLbhRBfG"
    consumer_secret = "vuN4ATiwzf3BenkzkeG3kXr6ISGZ17makoOgEuoyt7Rs3JHGel"
    access_token = "1427399398481399819-hAhAKowuXS7fNFYrSMUpBYiv6Qmm5P"
    access_token_secret = "NMx85GIh4PzVY54PQIcoYfEFSdgSjfSoy1fSVE45UNbdX"
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    # tweets
    public_tweets = api.home_timeline()

    i = 0
    tweets = {}

    # faz o score dos sentimentos
    for tweet in public_tweets:
        tweets[i] = tweet._json
        tweets[i]["polaridade"] = Score_sentimento(tweets[i]["text"])
        i += 1

    grava_arquivo(dados=tweets)

    return tweets


def abre_arquivo(arquivo='./tweets.json'):
    arquivo = arquivo
    arq     = open(arquivo, mode='r')
    dados   = json.load(arq)
    arq.close()

    # se o arquivo estiver vazio, busca por novos tweets
    if not dados:
        dados = novos_tweets()

    return dados


def grava_arquivo(arquivo='./tweets.json', dados=''):
    arq     = open(arquivo, mode='w')
    arq.write(json.dumps(dados))
    arq.close()

    return True
