from bs4 import BeautifulSoup
import requests

location = input("What is the first part of your Postcode? ")

url = "https://www.bbc.co.uk/weather/%s" % location.lower()

webpage = requests.get(url)

doc = BeautifulSoup(webpage.text, "html.parser")

temps = doc.find_all(class_ = "wr-value--temperature--c")
temps_list = []
temps_list.extend(temps)
temps_list1 = []

print ("Over the next 14 days starting from now, this is the weather forecast in %s:\n" % location)
for item in temps_list:
    temps_list1.append(item.string)
count = 0
for item in temps_list1:
    if count != 14:
        print (item, end = ",")
        count += 1



