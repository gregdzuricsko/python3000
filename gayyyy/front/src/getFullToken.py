import requests
import fbkeys

params = {'grant_type':'fb_exchange_token','client_id':fbkeys.APP_ID, 'client_secret':fbkeys.SECRET,'fb_exchange_token':fbkeys.SHORT_TERM_TOKEN}


r = requests.get("https://graph.facebook.com/oauth/access_token?", params=params)
print(r)
print(r.text)
#python code for changing a file. I did it manually.
