# task3.R
# Chandrachud Malali Gowda And Parth Parth
# This program is a sample python program that demosntrates all the
# built-in types and how to construct aggregate types, variable declarations,
# and identifier scoping
# 2022 - 02 - 02

library(methods)

# Creating the task3 reference class
my_task3 <- setRefClass("my_task3",
    fields = list(name = "character", age = "numeric", height = "numeric",
    weight = "numeric", alive = "logical"),
    methods = list(
    calculate_bmi = function(weight, height) {
        bmi <- 0
        bmi <- weight / (height * height)
        print(paste("The bmi is ", bmi))
    },
    reverse_age = function(age) {
        rev <- 0
        while (age > 0) {
            rev <- rev * 10 + age %% 10
            age <- floor(age / 10)
        }
        print(paste("The reversed age is ", rev))

    },
    print_details = function() {
        print(paste("Name: ", name))
        print(paste("Age: ", age))
        print(paste("Height: ", height))
        print(paste("Weight: ", weight))
        print(paste("Alive status: ", alive))
    }
))

task3 <- my_task3(name = "Chandrachud", age = 23, height = 1.75, weight = 65,
alive = TRUE)
task3$print_details()
task3$calculate_bmi(task3$weight, task3$height)
task3$reverse_age(task3$age)
