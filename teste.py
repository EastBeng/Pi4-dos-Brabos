import tweepy as tw


consumer_key = "QO61pvhO0VdFaZBIGJLbhRBfG"
consumer_secret = "vuN4ATiwzf3BenkzkeG3kXr6ISGZ17makoOgEuoyt7Rs3JHGel"
access_token = "1427399398481399819-hAhAKowuXS7fNFYrSMUpBYiv6Qmm5P"
access_token_secret = "NMx85GIh4PzVY54PQIcoYfEFSdgSjfSoy1fSVE45UNbdX"

auth = tw.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth,wait_on_rate_limit=True)

public_tweets = api.home_timeline()



for tweet in public_tweets:
    print(tweet.text)



    {
        "contributors": null,
        "coordinates": null,
        "created_at": "Sat Mar 27 20:50:16 +0000 2021",
        "entities": {
            "hashtags": [
                {
                    "indices": [
                        35,
                        42
                    ],
                    "text": "Gopain"
                }
            ],
            "symbols": [

            ],
            "urls": [

            ],
            "user_mentions": [

            ]
        },
        "favorite_count": 0,
        "favorited": false,
        "geo": null,
        "id": 1375913081738510338,
        "id_str": "1375913081738510338",
        "in_reply_to_screen_name": null,
        "in_reply_to_status_id": null,
        "in_reply_to_status_id_str": null,
        "in_reply_to_user_id": null,
        "in_reply_to_user_id_str": null,
        "is_quote_status": false,
        "lang": "pt",
        "place": null,
        "retweet_count": 0,
        "retweeted": false,
        "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
        "text": "Caralho pain TATAKAE caralho !!!! \n#Gopain",
        "truncated": false,
        "user": {
            "contributors_enabled": false,
            "created_at": "Mon Apr 27 02:14:19 +0000 2020",
            "default_profile": true,
            "default_profile_image": false,
            "description": "Engenharia de Dados- grupo Banestes 📚",
            "entities": {
                "description": {
                    "urls": [

                    ]
                }
            },
            "favourites_count": 1439,
            "follow_request_sent": false,
            "followers_count": 48,
            "following": true,
            "friends_count": 730,
            "geo_enabled": false,
            "has_extended_profile": false,
            "id": 1254594654676320257,
            "id_str": "1254594654676320257",
            "is_translation_enabled": false,
            "is_translator": false,
            "lang": null,
            "listed_count": 0,
            "location": "",
            "name": "Caio Souza",
            "notifications": false,
            "profile_background_color": "F5F8FA",
            "profile_background_image_url": null,
            "profile_background_image_url_https": null,
            "profile_background_tile": false,
            "profile_banner_url": "https://pbs.twimg.com/profile_banners/1254594654676320257/1588005106",
            "profile_image_url": "http://pbs.twimg.com/profile_images/1254594844485451776/5GfovdT0_normal.jpg",
            "profile_image_url_https": "https://pbs.twimg.com/profile_images/1254594844485451776/5GfovdT0_normal.jpg",
            "profile_link_color": "1DA1F2",
            "profile_sidebar_border_color": "C0DEED",
            "profile_sidebar_fill_color": "DDEEF6",
            "profile_text_color": "333333",
            "profile_use_background_image": true,
            "protected": false,
            "screen_name": "caio_rkira",
            "statuses_count": 1090,
            "time_zone": null,
            "translator_type": "none",
            "url": null,
            "utc_offset": null,
            "verified": false,
            "withheld_in_countries": [

            ]
        }
    }

