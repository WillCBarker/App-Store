'''
GUI for CLASS.py file
'''
#imports App and Cart class from CLASS file
from tkinter import *
from CLASS import App, Cart 
from functools import partial
import random, string

class MyFrame(Frame):
    def __init__(self, root):
        '''Constructor method'''
        Frame.__init__(self, root) #
        self.init_container() 
        self.cart = Cart() 
        self.welcome() 
        self.data = StringVar(self, 'Subtotal: 0.0') 

        
    def init_container(self):
        '''Initialize widget containers'''
        self.states = [] #holds state if selected/not i-th list item holds selection for i-th item
 
    def clear_frame(self): 
        '''Clears the previous frame'''
        for widget in self.winfo_children():
            widget.destroy()

    def exit_application(self):
        '''Exits the program'''
        root.destroy()

 
    def welcome(self):
        '''Welcome window - refer spec file for details'''
        self.clear_frame()
        Label(self, text = '****Welcome to AppsCart!****', background="gray70").pack(side = TOP)

        category = Button(self, text = "Select by category", command = self.shop_by_apps_category)
        category.pack()

        ratings = Button(self, text = "Select by ratings", command = self.shop_by_apps_ratings)
        ratings.pack()

        price = Button(self, text = "Select by price", command = self.shop_by_apps_price)
        price.pack()


        exit = Button(self, text = "Exit Application", command = self.exit_application)
        exit.pack()
        

    def shop_by_apps_category(self):
        '''2. Widget to display different category of apps - refer spec file for details'''
        self.clear_frame()
        self.init_container()

        self.app_cat_label = Label(self, text="Choose Apps by Category")
        self.app_cat_label.grid(row = 0, column = 0)

        count = 0
        for i in App.category_dict.keys():
            count +=1
            self.i = Button(self, text = i, command=partial(self.start, App.category_dict[i]))
            self.i.grid(row = count, column = 0)

        self.go_back = Button(self, text = "Go Back", command=self.welcome)
        self.go_back.grid(row = count + 1, column = 0)

    def shop_by_apps_ratings(self):
        self.clear_frame()
        self.init_container()
        self.app_rat_label = Label(self, text="Choose Apps by Rating")
        self.app_rat_label.grid(row = 0, column = 0)

        count = 0
        for i in sorted(App.rating_dict.keys()):
            count +=1
            t = str(i) + " stars & up"
            self.i = Button(self, text = i, command=partial(self.start, App.rating_dict[i]))
            self.i.grid(row = count, column = 0)

        self.go_back = Button(self, text = "Go Back", command=self.welcome)
        self.go_back.grid(row = count + 1, column = 0)


    def shop_by_apps_price(self):
        self.clear_frame()
        self.init_container()
        self.app_pri_label = Label(self, text="Choose Apps by Price")
        self.app_pri_label.grid(row = 0, column = 0)

        count = 0
        for i in sorted(App.price_dict.keys()):
            count +=1
            t = "$" + str(i) + ".00"
            self.i = Button(self, text = t, command=partial(self.start, App.price_dict[i]))
            self.i.grid(row = count, column = 0)

        self.go_back = Button(self, text = "Go Back", command=self.welcome)
        self.go_back.grid(row = count + 1, column = 0)
        
    def start(self, current_items):
        ''''3. Start ordering from selected category,
        list passed by command will be used as current_items'''
        self.clear_frame()
        self.init_container()
        
        #creating widgets for items using a for loop
        #iterative over each item of current apps and
        #create that many checkbuttons, price, ID, rating and category labels
        row = 0#########
        count = 0
        for item in current_items:
            self.states.append(IntVar()) #keeps track if an item is selected
            checkbutton = Checkbutton(self, text=item.get_name(), variable=self.states[count])#create check buttons
            checkbutton.grid(row = count, column = 0)

            self.price_label = Label(self, text="$" + str(item.get_price()))
            self.price_label.grid(row = count, column = 1)

            self.id_label = Label(self, text=item.get_id())
            self.id_label.grid(row = count, column = 2)

            self.rating_label = Label(self, text=item.get_rating())
            self.rating_label.grid(row = count, column = 3)

            self.cat_label = Label(self, text=item.get_category())
            self.cat_label.grid(row = count, column = 4)
            count +=1
        

        self.subtotal_label = Label(self, textvariable = self.data)
        self.subtotal_label.grid(row = count + 1, column = 0)

        self.mm_button = Button(self, text="Main Menu", command = self.welcome)
        self.mm_button.grid(row = count + 1, column = 1)

        self.add_to_cart_button = Button(self, text="Add to Cart", command = partial(self.add_to_cart, current_items))
        self.add_to_cart_button.grid(row = count + 1, column = 2)

        self.checkout_button = Button(self, text="Checkout", command = self.checkout)
        self.checkout_button.grid(row = count + 1, column = 3)

    def add_to_cart(self, current_items):
        '''3. Added to cart, displays subtotal - see spec file for details layout'''
        for i in range(len(current_items)):

            val = self.states[i].get() 
            if val == 1:
                self.cart.append(current_items[i])


        self.data.set('Subtotal: ${:.2f}'.format(self.cart.subtotal()))

        
    def get_receipt_number(self):
        '''Generate random receipt number'''
        return  ''.join(random.choices(string.ascii_letters.upper() + string.digits, k=4))

    def checkout(self):
        '''4. Check out window '''
        self.clear_frame()

        self.eorder_label = Label(self, text="Your e-order")
        self.eorder_label.grid(row = 0, column = 1, columnspan=2)

        self.eorder_num_label = Label(self, text=self.get_receipt_number())
        self.eorder_num_label.grid(row = 1, column = 1, columnspan=2)

        self.line_break = Label(self, text="*************************")
        self.line_break.grid(row = 2, column = 1, columnspan=2)

        self.name_label = Label(self, text="Name")
        self.name_label.grid(row = 3, column = 0)

        self.price_label = Label(self, text="Price")
        self.price_label.grid(row = 3, column = 1)

        self.rating_label = Label(self, text="rating")
        self.rating_label.grid(row = 3, column = 2)

        self.Category_label = Label(self, text="Category")
        self.Category_label.grid(row = 3, column = 3)
        #    Iterates over apps items from cart list
        #	   Genrates labels of 	name, price, rating, category and layout

        line = 3
        for i in self.cart:
            line +=1
            self.i_name = Label(self, text=App.get_name(i))
            self.i_name.grid(row = line, column = 0)

            self.i_price = Label(self, text=App.get_price(i))
            self.i_price.grid(row = line, column = 1)

            self.i_rating = Label(self, text=App.get_rating(i))
            self.i_rating.grid(row = line, column = 2)

            self.i_category = Label(self, text=App.get_category(i))
            self.i_category.grid(row = line, column = 3)

        self.line_break = Label(self, text="*************************")
        self.line_break.grid(row = line + 1, column = 1, columnspan=2)

        self.s_total = Label(self, text="Subtotal: ${:.2f}".format(self.cart.subtotal()))
        self.s_total.grid(row = line + 2, column = 1, columnspan=2)

        self.tax = Label(self, text="Tax: 4.30%")
        self.tax.grid(row = line + 3, column = 1, columnspan=2)

        self.total = Label(self, text="Subtotal: ${:.2f}".format(self.cart.subtotal() + (0.0430 * self.cart.subtotal())))
        self.total.grid(row = line + 4, column = 1, columnspan=2)
        '''
        self.sub = Label(self, text="Subtotal: ", )
        self.sub.grid(line + 1, column = 0)
        '''

        self.thanks = Label(self, text="Thank You!")
        self.thanks.grid(row = line + 5, column = 1, columnspan=2)

        self.exit_button = Button(self, text="Exit Application", command = self.exit_application)
        self.exit_button.grid(row = line + 6, column = 1, columnspan=2)

        
root = Tk()
root.title("Apps Cart")
frame = MyFrame(root)
frame.pack()
root.mainloop()