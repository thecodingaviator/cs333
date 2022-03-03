# task3.py
# Chandrachud Malali Gowda and Parth Parth
# This program is a sample in the selected language that demonstrates the rules for identifier naming, variable declarations, 
# and identifier scoping
# 2022 - 02 - 02

class MyTask3:

    # Constructor
    def __init__(self, name, age, height, weight):
        self.name = name # String data type
        self.age = age # Integer data type
        self.height = height # Float data type
        self.weight = weight # Float data type

    # Getter method for the name
    def get_name(self):
        return self.name

    # Setter method for the name
    def set_name(self, name):
        self.name = name

    # Getter method for the age
    def get_age(self):
        return self.age

    # Setter method for the age
    def set_age(self, age):
        self.age = age

    # Getter method for the height
    def get_height(self):
        return self.height

    # Setter method for the height
    def set_height(self, height):
        self.height = height

    # Getter method for the weight
    def get_weight(self):
        return self.weight

    # Setter method for the weight
    def set_weight(self, weight):
        self.weight = weight

    # Function to calculate and print the BMI
    def calculate_bmi(self):
        bmi = self.weight / (self.height * self.height)
        print("BMI is: ", bmi)

    # Function to reverse the age
    def reverse_age(self):
        rev = 0
        while(self.age > 0):
            rev = rev * 10 + self.age % 10
            self.age = self.age // 10 # // --> Floor division in python
        print("Reverse age is: ", rev)

    # Function to print the details of the person
    def print_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Height: ", self.height)
        print("Weight: ", self.weight)

# Defining the main method
def main():
    task3 = MyTask3("Chandrachud", 22, 5.11, 70.5)
    task3.print_details()
    task3.calculate_bmi()
    task3.reverse_age()

if __name__ == '__main__':
    main()