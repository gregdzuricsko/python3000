import requests
import dateutil.parser as dateparser
import fbkeys


GROUND_ZERO_ID = '162965219745'
URL_BASE = 'https://graph.facebook.com/'

def get_shared_event_ids(data):
    eventIDs = []
    for x in data:
        if 'message' in x and "/events/" in x['message']:
            # print(x['message'])
            message = x['message']
            n = message.index('/events/') +  8
            eventIDs.append(message[n:message.index('/',n)])
    return eventIDs

def get_shared_event_jsons(pageID):
    # print( fbkeys.AUTH_TOKEN, fbkeys.APP_ID, fbkeys.SECRET)
    accessTokenSuffix = 'access_token=' + fbkeys.AUTH_TOKEN
    r = requests.get(URL_BASE + pageID + "/" + "feed" + "?" + accessTokenSuffix)

    json = r.json()
    data = json['data']
    print(r)

    sharedEventIDs = get_shared_event_ids(data)
    sharedEventJsons = {}
    for eventID in sharedEventIDs:
        r = requests.get(URL_BASE + eventID + "?" + accessTokenSuffix)#get unix time format
        sharedEventJson = r.json()
        d = dateparser.parse(sharedEventJson['start_time'])
        day = d.strftime('%a, %d, %B')
        sharedEventJson['parsed_start_time'] = d.strftime('%X')
        sharedEventJsons[day] = sharedEventJson
    return sharedEventJsons

def get_ground_zero_events():
    groundZeroEvents = get_shared_event_jsons(GROUND_ZERO_ID)
    return groundZeroEvents
