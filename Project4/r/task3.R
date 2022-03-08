# task3.R
# Chandrachud Malali Gowda And Parth Parth
# This program is a sample R program that demonstrates
# a general sort algorithm (here insertion sort) that can be used for
# any type and can be used to obtain any desired order
# variable declarations, and identifier scoping
# 03 - 10 - 2022

# Writing the insertion sort function
insertion_sort <- function(x, ascending = TRUE) {
    # Initialize a variable to store the sorted list
    sorted_list <- list()
    # Loop through the input list
    for (i in 1:length(x)) {
        # Initialize the current value
        current_value <- x[i]
        # Initialize the index
        index <- i
        # Loop through the sorted list and swap based on the order
        if (ascending) {
            while (index > 1 && current_value < sorted_list[[index - 1]]) {
                sorted_list[[index]] <- sorted_list[[index - 1]]
                index <- index - 1
            }
        } else {
            while (index > 1 && current_value > sorted_list[[index - 1]]) {
                sorted_list[[index]] <- sorted_list[[index - 1]]
                index <- index - 1
            }
        }
        # Add the current value to the sorted list
        sorted_list[[index]] <- current_value
    }
    # Return the sorted list
    sorted_list
}

# Testing the function to make sure it works on all generic types
test_list_1 <- c(5, 2, 7, 4, 6, 1, 3)
test_list_2 <- c(5.75, 2.5, 7.5, 4.5, 6.5, 1.5, 3.5)
test_list_3 <- c("a", "b", "c", "d", "e", "f", "g")

# Printing results for List 1
print("List 1:")

# Sorting List 1 in ascending order
result_1 <- insertion_sort(test_list_1, TRUE)

# Printing the result 1
print(paste("Result 1:", result_1))

# Sorting List 1 in descending order
result_2 <- insertion_sort(test_list_1, FALSE)

# Printing the result 2
print(paste("Result 2:", result_2))

# Printing results for List 2
print("List 2:")

# Sorting List 2 in ascending order
result_3 <- insertion_sort(test_list_2, TRUE)

# Printing the result 3
print(paste("Result 3:", result_3))

# Sorting List 2 in descending order
result_4 <- insertion_sort(test_list_2, FALSE)

# Printing the result 4
print(paste("Result 4:", result_4))

# Printing results for List 3
print("List 3:")

# Sorting List 3 in ascending order
result_5 <- insertion_sort(test_list_3, TRUE)

# Printing the result 5
print(paste("Result 5:", result_5))

# Sorting List 3 in descending order
result_6 <- insertion_sort(test_list_3, FALSE)

# Printing the result 6
print(paste("Result 6:", result_6))
