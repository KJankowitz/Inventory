# === Import Modules ===
from tabulate import tabulate

#========The beginning of the class==========
class Shoe:
    '''Class representing one shoe product'''


    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity


    def get_cost(self):
        '''Returns cost of shoe product'''
        return self.cost


    def get_quantity(self):
        '''Returns quantity of shoe product'''
        return self.quantity


    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"


#=============Shoe list===========
# List of Shoe objects
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    '''
    Reads data from inventory.txt (skipping header line) and creates new Shoe 
    objects from data in each line.
    Appends each Shoe object to shoe_list.
    '''
    with open("inventory.txt", "r", encoding="utf-8") as i_file:
        next(i_file) #skip header line
        for line in i_file:
            one_line = line.strip()
            one_line = one_line.split(",")
           # Create Shoes object
            one_shoe = Shoe(
                one_line[0],
                one_line[1],
                one_line[2],
                one_line[3],
                one_line[4]
               )
            shoe_list.append(one_shoe)


def capture_shoes():
    '''
    Allows a user to capture data about a shoe and use this data to create 
    a Shoe object and append this object inside the shoe_list.
    '''
    new_country = input("Enter country of product:\n").capitalize()
    new_code = input("Enter product code:\n") #starting with SKU?
    new_product = input("Enter product name:\n")
    new_cost = int(input("Enter product cost as whole number:\n"))
    new_quantity = int(input("Enter quantity of pruduct:\n"))

    new_shoe = Shoe(new_country, new_code, new_product, new_cost, new_quantity)
    shoe_list.append(new_shoe)
    return "Product data captured"

def view_all():
    '''
    Iterates over the shoes_list and prints the details of the shoes returned 
    from the __str__ function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    product_list = [["Country","Code","Product","Cost","Quantity"]]
    
    for product in shoe_list:
        product = str(product)
        product = product.split(",")
        #print(product)
        product_list.append(product)
    
    #print(product_list)
    print(tabulate(product_list, headers="firstrow"))

def re_stock():
    pass
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

def seach_shoe():
    pass
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    pass
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

def highest_qty():
    pass
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''


# To avoid unnecessarily calling the dunder method itself, use the built-in
# function that calls them (str() calls __str__() method implemented in class object)
#print(str(shoe1))

read_shoes_data()
view_all()
