from bs4 import BeautifulSoup
from urllib import request
import unicodedata
import json
import re



from EventO import EventO

EAGLE_BOLT_URL = "http://eagleboltbar.com/daily_specials.html"
EAGLE_BOLT_SPECIAL_URL = "http://eagleboltbar.com/special_events.html"
SALOON_URL = "http://saloonmn.com/calendar-of-events"
DAY_MAPPING = {0: 'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}

#taken from scrapeTutorial exercise, returns beautifulsoup
def get_soup(url):
	html = request.urlopen(url).read()
	soup = BeautifulSoup(html, "html5lib")
	return soup

#want saloon from day to day, eventually as json
def get_saloon_daily_special():
	soup = get_soup(SALOON_URL)
	allEvents = soup.findAll("div","cover-container") #types in python!
	eventOList = []

	for cover in allEvents:
		eventTitle = cover.find("h4","day")
		eventDescription = cover.find("div","event-description")
		eventDay = print_coded_thing(eventTitle).decode('utf-8')
		#eventDayNumber = get_day_number(eventDay)
		eventDescription = print_coded_thing(eventDescription).decode('utf-8')

		indexAfterAge = eventDescription.find("\n",eventDescription.find("\n",eventDescription.find("\n")+1)+1)
		eventAge = eventDescription[(indexAfterAge-3):indexAfterAge]

		indexAfterCover = eventDescription.find("\n",indexAfterAge+1)
		eventCover = eventDescription[indexAfterAge:indexAfterCover].strip()
		eventHours = eventDescription[indexAfterCover:].strip()
		eventDescription = eventDescription[:eventDescription.find("\n")]
		eventOList.append(EventO("n/a", eventDescription, eventDay, eventHours, eventCover, eventAge))

	return eventOList

def print_coded_thing(coverMaybe):
	text = ''.join(coverMaybe.findAll(text=True))
	data = text.strip()
	nkfd_form = unicodedata.normalize('NFKD', data)
	only_ascii = nkfd_form.encode('ASCII', 'ignore')
#	print("printing uncoded",only_ascii)
	return only_ascii

# def print_Encoded_Text(text):
# 	data = text.strip()
# 	nkfd_form = unicodedata.normalize('NFKD', data)
# 	only_ascii = nkfd_form.encode('ASCII', 'ignore')
# 	print("printing uncoded",only_ascii)
# 	return only_ascii

# def get_day_number(dayAsString):
# 	lowerCaseDayAsString = str(dayAsString).lower()
# 	if 'monday' in lowerCaseDayAsString:
# 		return 0
# 	elif 'tuesday' in lowerCaseDayAsString:
# 		return 1
# 	elif 'wednesday' in lowerCaseDayAsString:
# 		return 2
# 	elif 'thursday' in lowerCaseDayAsString:
# 		return 3
# 	elif 'friday'in lowerCaseDayAsString:
# 		return 4
# 	elif 'saturday' in lowerCaseDayAsString:
# 		return 5
# 	elif 'sunday' in lowerCaseDayAsString:
# 		return 6

# def get_current_day(currentDay=None):
# 	if currentDay == None:
# 		dayNumber = datetime.datetime.today().weekday() #from datetime, get current day as int from monday = 0
# 		print(dayNumber)
# 		currentDay = DAY_MAPPING[dayNumber]

#def convert_to_whatever_code(SALOON_MAPPINGS):
#	for key in SALOON_MAPPINGS:#== for key in dict.keys
#		text = SALOON_MAPPINGS[key]
#		SALOON_MAPPINGS[key] = print_coded_thing(text).decode('utf-8')


def get_eagle_special_events():
	eagleSpecialMappings = {}
	soup = get_soup(EAGLE_BOLT_SPECIAL_URL)
	allDays = soup.findAll("span","style34") #types in python!
	for day in allDays:
		if day.text is '':
			continue
		eventDescription = day.find_next("blockquote")
		eagleSpecialMappings[day.text] = re.sub(r'\s+',' ',print_coded_thing(eventDescription).decode('utf-8'))
	return eagleSpecialMappings

def get_eagle_daily_specials():
	dailyMappings = {}
	soup = get_soup(EAGLE_BOLT_URL)
	r = re.compile('[a-zA-Z]+day')
	assert r.match('sunday')
	assert r.match('SUNday')
	allDays = soup.findAll(is_a_and_name_ends_with_day)
	for day in allDays:
		greatGrandparent = day.parent.parent.parent
		activities = greatGrandparent.next_sibling.next_sibling
		if activities is None:
			activities = greatGrandparent.parent.next_sibling.next_sibling
		activity = ""
		for string in activities.stripped_strings:
			activity = activity + string + "\n"
		#print(activity)
		dailyMappings[day['name']] = activity

	print("leaving specials")
	#print(dailyMappings)
	return dailyMappings

def is_a_and_name_ends_with_day(tag):
	return tag.has_attr("name") and re.compile('[a-zA-Z]+day').match(tag['name'])


#empties a a file
def delete_content(pfile):
	pfile.seek(0)
	pfile.truncate()

def log_it(stuffToBeWritten, fileName):
	with open(fileName, "a") as log:
		delete_content(log)
		log.write(stuffToBeWritten)
		log.close()

def encode_eventO(obj):
	if isinstance(obj,EventO):
		return obj.__dict__
	return obj

##1. get eagle events
eagle_special_mappings = get_eagle_special_events()
eagle_special_string = json.dumps(eagle_special_mappings)
log_it(eagle_special_string, "front/src/json/EagleSpecials.txt")

#2. get eagle daily_specials
eagle_daily_mappings = get_eagle_daily_specials()
eagle_daily_string = json.dumps(eagle_daily_mappings)
log_it(eagle_daily_string, "front/src/json/EagleHappyHour.txt")

# 3 Saloon stuff
SALOON_MAPPINGS = {}
saloon_list = get_saloon_daily_special()#saloonList is now a list of events
saloon_json_string = json.dumps(saloon_list, default=encode_eventO)#wow, that was way easier than i thought it would be
log_it(saloon_json_string,"front/src/json/SaloonHappyHour.txt")
