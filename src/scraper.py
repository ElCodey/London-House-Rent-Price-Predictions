import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


def get_soup(url):
    request = requests.get(url)
    soup = bs(request.content, "lxml")
    return soup

def scraper():
    price = []
    bedrooms = []
    location = []
    counter = 2
    for i in range(1000):
        try:
            soup = get_soup("https://www.zoopla.co.uk/to-rent/property/london/?price_frequency=per_month&q=London&results_sort=newest_listings&search_source=to-rent&pn={}".format(counter))
            counter += 1
            for i in soup.find("div", {"class":"css-1anhqz4-ListingsContainer earci3d2"}):
                bedrooms.append(i.find("p", {"class": "css-r8a2xt-Text eczcs4p0"}).text.strip())
                location.append(i.find("p", {"class": "css-nwapgq-Text eczcs4p0"}).text.strip())
                price.append(i.div.p.text.strip())
        except:
            pass

    df = pd.DataFrame({"price": price, "number_bedrooms": bedrooms, "postcode": location})
    df.to_csv(df.to_csv("zoopla_rentals.csv"))
