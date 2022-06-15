'''
takes top 50 shopify apps in csv, sorts items and displays in a mock app store for purchase
'''
import csv
from distutils.util import subst_vars

class Cart(list):
    def subtotal(self):
        sub = 0
        for item in self:
            item_price = App.get_price(item)
            sub += float(item_price)
        return sub
    

class App(object):
    '''App class defines an app item
    available in store. App object saved in
    category_dict per category
    and rating_dict per rating and price_dict per price '''
    category_dict = {}
    rating_dict = {}
    price_dict = {}

    def __init__(self, ID, name, developer, description, price, rating, review_count, category):
        '''Initialization method'''
        self.__id = ID
        self.__name = name
        self.__developer = developer
        self.__description = description
        self.__price = price
        self.__rating = rating
        self.__review_count = review_count
        self.__category = category

        if self.__category in App.category_dict.keys():
            App.category_dict[self.__category].append(self)

        else:
            App.category_dict[self.__category] = [self]

        #rating_dict key = rating value as whole number
        # for example an app of 4.9 rating will be saved under key 4 and values = list of objects for
        #that rating

        if (int(float(self.__rating))) in App.rating_dict.keys():
            fixedr = int(float(self.__rating))
            App.rating_dict[fixedr].append(self)

        else:
            fixedr = int(float(self.__rating))
            App.rating_dict[fixedr] = [self]
        #price_dict is be similar as rating except key is price,
        #all the apps between 1.00$-1.99 will be under key 1.00$
        if self.__price == "Free":
            self.__price = 0
        if (int(float(self.__price))) in App.price_dict.keys():
            fixedp = int(float(self.__price))
            App.price_dict[fixedp].append(self)
        
        else:
            fixedp = int(float(self.__price))
            App.price_dict[fixedp] = [self]

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name

    def get_developer(self):
        return self.__developer

    def get_description(self):
        return self.__description

    def get_price(self):
        return self.__price

    def get_rating(self):
        return self.__rating

    def get_category(self):
        return self.__category

#process file
filename = 'Top50ShopifyApps.csv' #path doesnt have to be fully typed on any other computer
with open(filename) as fin:
    #uses csv reader to read the file info
    #skips the header
    #itereates over each line
    #separates the ID, name, developer, description, price, rating, review_count, category
    #creates an object
    read_file = csv.reader(fin, delimiter = ',')  
    next(read_file, None)
    for line in read_file:
        ID, name, developer, description, price, rating, review_count, category = line
        a = App(ID, name, developer, description, price, rating, review_count, category)



'''Testing code to check object creating Items'''
'''
for k,v in App.category_dict.items(): #v is a list of all objects
    print(k, [(obj.get_name(), obj.get_rating()) for obj in v ])
print('++++++++++')

for k,v in App.rating_dict.items(): #v is a list of all objects
    print(k, [obj.get_rating() for obj in v ])
print('++++++++++')

for k,v in App.price_dict.items(): #v is a list of all objects
    print(k, [obj.get_price() for obj in v ])
print('++++++++++')
'''




          

