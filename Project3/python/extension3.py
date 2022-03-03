# extension_3.py
# Chandrachud Malali Gowda And Parth Parth
# This program demostrates that functions are a basic data type in Python and that a variable can hold an arbitrary
# function
# 2022 - 02 - 02

class Extension3:

    # Function to convert text to uppercase
    def to_upper(self, text):
        return text.upper()

    # Function to convert text to lowercase
    def to_lower(self, text):
        return text.lower()

    # Function to test if a function can be passed as a variable
    def test_function(self, func):
        # Storing the function in a variable
        func_var = func("I am generated from a function passed as an argument (i.e. datatype)")
        print("Function variable: ", func_var)

# Defining the main method
def main():
    ext3 = Extension3()
    ext3.test_function(ext3.to_lower)
    ext3.test_function(ext3.to_upper)

if __name__ == '__main__':
    main()