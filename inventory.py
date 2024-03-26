
#========The beginning of the class==========
class Shoe:


    def __init__(self, country, code, product, cost, quantity):
       self.country = country
       self.code = code
       self.product = product
       self.cost = cost
       self.quantity = quantity


    def get_cost(self):
      return self.cost


    def get_quantity(self):
        return self.quantity


    def __str__(self):
        return f'''
        Country: {self.country}
        Code: {self.code}
        Product: {self.product}
        Cost: {self.cost}
        Quantity: {self.quantity}
    '''


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
   
   with open("inventory.txt", "r", encoding="utf-8") as i_file:
       next(i_file) #skip header line
       for line in i_file:
           one_line = line.strip()
           one_line = one_line.split(",")
           print(one_line)
            

def capture_shoes():
    pass
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

def view_all():
    pass
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

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

shoe1 = Shoe("RSA",  123, "Tekkie", 200, 30)

# To avoid unnecessarily calling the dunder method itself, use the built-in
# function that calls them (str() calls __str__() method implemented in class object)
#print(str(shoe1))

read_shoes_data()