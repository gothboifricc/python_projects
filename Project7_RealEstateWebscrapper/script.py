import requests
from bs4 import BeautifulSoup
import pandas

r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content

soup = BeautifulSoup(c, "html.parser")
#print(soup.prettify())
all = soup.find_all("div", {"class" : "propertyRow"})
#print(all)
#check the len(all), it is 10, i.e it has 10 property elements, and it atcs like a list, hence we access the first element using [0] which has a find_all method
all[0].find("h4", {"class" : "propPrice"}).text.replace("\n", "").replace(" ", "")
l = []

base_url = "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0, 30, 10):
    r = requests.get(base_url + str(page) + ".html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div", {"class" : "propertyRow"})
    for items in all:
        c = {}
        c["Address"] = items.find_all("span", {"class" : "propAddressCollapse"})[0].text
        try:
            c["Locality"] = items.find_all("span", {"class" : "propAddressCollapse"})[1].text
        except:
            c["Locality"] = None
        c["Price"] = items.find("h4", {"class" : "propPrice"}).text.replace("\n", "").replace(" ", "")

        try:
            #print(items.find("span", {"class" : "infoBed"}).text)
            #if u want only number of beds printed out and not text follow below code
            c["Beds"] = items.find("span", {"class" : "infoBed"}).find("b").text
        except:
            c["Beds"] = None
        try:
            c["Area (sq. ft)"] = items.find("span", {"class" : "infoSqFt"}).find("b").text
        except:
            c["Area (sq. ft)"] = None
        try:
            #print(items.find("span", {"class" : "infoValueFullBath"}).text)
            c["Full Baths"] = items.find("span", {"class" : "infoValueFullBath"}).find("b").text
        except:
            c["Full Baths"] = None
        try:
            c["Half Baths"] = items.find("span", {"class" : "infoValueHalfBath"}).find("b").text
        except:
            c["Half Baths"] = None #or pass
        for column_group in items.find_all("div", {"class" : "columnGroup"}):
            #print(column_group)
            for feature_group, feature_name in zip(column_group.find_all("span", {"class" : "featureGroup"}),
            column_group.find_all("span", {"class" : "featureName"})):
                #print(feature_group.text, feature_name.text)
                if "Lot Size" in feature_group.text:
                    c["Lot Size"] = feature_name.text
        l.append(c)
df = pandas.DataFrame(l)
#print(df)
df.to_csv("Output.csv")
