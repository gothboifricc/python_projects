#Importing the required libs
import requests
from bs4 import BeautifulSoup

#using the requests lib to get the source code of the webpage
r = requests.get("http://www.pyclass.com/example.html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

#grabbing the content of the requests
c = r.content

#using beautifulsoup to make it pretty
soup = BeautifulSoup(c, "html.parser")

##print(soup.prettify()) makes it visually attractive

#extract all data from the div that has a common class
all = soup.find_all("div", {"class" : "cities"})
##print(all)

#further extracting data from this is by using indexing; video ref 244
##print(all[0].find_all("h2")[0].text)

#iterating thru each item of the all list using for loop
for items in all:
    print(items.find_all("h2")[0].text)
    print(items.find_all("p")[0].text)
