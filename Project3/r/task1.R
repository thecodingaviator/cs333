# task1.R
# Chandrachud Malali Gowda And Parth Parth
# This program is a sample python program that demonstrates
# the rules for identifier naming,
# variable declarations, and identifier scoping
# 2022 - 02 - 02

library(methods)

# Creating the task1 reference class
my_task1 <- setRefClass("MyTask1", 
    fields = list(name = "character", my_total = "numeric"), methods = list(
    sum = function(num1, num2) {
        my_total <<- num1 + num2
        print("The sum is ", my_total)
    }
))

task1 <- my_task1(name = "Task 1", my_total = 046545)

# Print the value of the total
print(task1$my_total)

# Run the sum function
task1$sum(1, 2)

# Print the value of the total
print(task1$my_total)