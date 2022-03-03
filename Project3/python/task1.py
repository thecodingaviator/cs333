# task1.py
# Chandrachud Malali Gowda And Parth Parth
# This program is a sample in the selected language that demosntrates the ruels for identifier naming, variable declarations, and identifier scoping
# 2022 - 02 - 02

# Class names must be in camel case
class MyTask1:

    # Variable names should be lowercase with words seperated by underscores
    # Cannot start with a digit, can be a combination of letters in lowercase or uppercase or digits or an underscore, keywords cannot be used as identifiers
    my_total = 0 # This is a global variable
 
    # Function definition is here
    def sum(self, my_num1, my_num2):
        # Add both parameters and return them
        my_total = my_num1 + my_num2
        print("Inside the function, the local total: ", my_total)
        return my_total

# Defining the main method
def main():
    task1 = MyTask1()
    task1.sum(10, 20)
    print("Outside the function, the global total: ", task1.my_total)

if __name__ == '__main__':
    main()