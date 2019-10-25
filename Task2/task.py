from bs4 import BeautifulSoup
import requests




def get_products_from_page(url):

    source = requests.get(url) # get url items
    soup = BeautifulSoup(source.text, 'lxml') # make soup object

    items_list = [] # list for adding items in dictionaries

    for items in soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3'): # find all cols
        dict = {}

        # item_title
        try:
            # item_title = items.find('h3').text
            dict["name"] = items.find('h3').text
        except Exception:
            dict["name"] = 'None'

        # item_price
        try:
            # item_price = items.find('p', class_='price_color').text
            dict["price"] = items.find('p', class_='price_color').text
        except Exception:
            dict["price"] = 'None'

        # item_link
        try:
            item_link = items.find('img', class_='thumbnail')['src']
            dict["image"] = "http://books.toscrape.com/{}".format(item_link)
        except Exception:
            dict["image"] = 'None'
        # print("http://books.toscrape.com/{}".format(item_link))

        # item_rating
        try:

            rating_dict = {"One": 1,
                           "Two": 2,
                           "Three": 3,
                           "Four": 4,
                           "Five": 5}

            item = items.find_all('p')

            for p in item:
                rating = (rating_dict[p['class'][1]])
                dict["rating"] = rating

        except Exception:
            dict["rating"] = 'None'


        # item_availability
        try:
            item_availability = items.find('p', class_='instock availability').text

            if item_availability.strip() == "In stock":
                dict["Is_tock"] = True
            else:
                dict["Is_tock"] = False

        except Exception:
            dict["Is_tock"] = False



        items_list.append(dict) # append dictionary in list


    return items_list


#print(len(get_products_from_page('http://books.toscrape.com/index.html')))