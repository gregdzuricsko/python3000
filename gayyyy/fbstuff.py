import requests

import fbkeys

GROUND_ZERO_ID = '162965219745'
URL_BASE = 'https://graph.facebook.com/'


print( fbkeys.AUTH_TOKEN, fbkeys.APP_ID, fbkeys.SECRET)
accessTokenSuffix = 'access_token=' + fbkeys.AUTH_TOKEN
r = requests.get(URL_BASE + GROUND_ZERO_ID + "/" + "feed" + "?" + accessTokenSuffix)

print(r)
print(r.json())
