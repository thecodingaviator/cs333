# task2.R
# Chandrachud Malali Gowda And Parth Parth
# This program is a sample R program that demonstrates
# that functions can be treated as a datatype,
# variable declarations, and identifier scoping
# 03 - 10 - 2022

# Writing a sample function
sum <- function(x, y) {
    x + y
}

# Assigning a function to a variable
sum_var <- sum(7, 7)

# Printing out the result of the function
print(sum_var)

# Passing a function as an argument to another function
print_func <- function(x) {
    print(paste("The input for this function was", x))
}

sample_run_func <- function(f, x) {
    f(x)
}

sample_run_func(print_func, "Hello World")

# You don't ahve to name a function and can directly
# define the function in the argument slot
sample_run_func(function(x) {
    print(paste("The input for this function was", x))
}, "Hello World")
