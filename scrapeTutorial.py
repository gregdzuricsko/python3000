from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://www.chicagoreader.com"
#section_url like Food and Drink's link
def get_links_from_category(section_url):
	soup = get_soup(section_url)
	boccat = soup.find("dl", "boccat") #finds the element labeled boccat
	category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
	return category_links

def get_category_winner(category_url):
	soup = get_soup(category_url)
	category = soup.find("h1", "headline").string #types in python!
	winner = [h2.string for h2 in soup.findAll("h2", "boc1")]
	runners_up = [h2.string for h2 in soup.findAll("h2", "boc2")]
	return {"category": category,
		"category_url": category_url,
		"winners": winner,
		"runners_up": runners_up} #return dictionary of data

def get_soup(url):
	html = urlopen(url).read()
	soup = BeautifulSoup(html, "lxml")
	return soup

x = get_links_from_category("http://www.chicagoreader.com/chicago/best-of-chicago-2011-goods-and-services/BestOf?oid=4106022")
print x
for link in x:
	print get_category_winner(link)

