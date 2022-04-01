# task1.R
# Chandrachud Malali Gowda and Parth Parth
# This program is a sample R program that implements a linked list in R
# 2022 - 03 - 31

# Importing the required libraries
library(methods)

# Creating the node class
node <- setRefClass("node", fields = list(data = "ANY", next_node = "ANY"))

# Creating the linked list class
linked_list <- setRefClass("linked_list", 
                fields = list(head = "ANY", tail = "ANY", size = "numeric"))

# Function to clear the linked list
clear <- function(l) {
    l$head <- NULL
    l$tail <- NULL
    l$size <- 0
}
 # Function to return the size of the list
size <- function(l) {
    return(l$size)
}

# Function to add a node to the end of the list
append <- function(l, new_item) {
    new_node <- node(data = new_item, next_node = NULL)
    if (l$size == 0) {
        l$head <- new_node
        l$tail <- new_node
    } else {
        l$tail$next_node <- new_node
        l$tail <- new_node
    }
    l$size <- l$size + 1
}

# Function to add a node to the beginning of the list
push <- function(l, new_item) {
    new_node <- node(data = new_item, next_node = NULL)
    if (l$size == 0) {
        l$head <- new_node
        l$tail <- new_node
    } else {
        new_node$next_node <- l$head
        l$head <- new_node
    }
    l$size <- l$size + 1
}
        
# Function to remove a node from the front of the list
pop <- function(l) {
    if (l$size == 0) {
        print("List is empty")
        return(NULL)
    }
    temp <- l$head
    l$head <- l$head$next_node
    l$size <- l$size - 1
    if (l$size == 0) {
        l$tail <- NULL
    }
    return(temp$data)
}

# Function to remove the first node in the list
# whose data matches the target with a specified comparison function
remove <- function(l, target, f) {
    if (l$size == 0) {
        print("List is empty")
        return(NULL)
    }

    prev <- NULL
    curr <- l$head
    while (!is.null(curr)) {
        if (curr$data == target) {
            if (prev == NULL) {
                l$head <- curr$next_node
            } else {
                prev$next_node <- curr$next_node
            }
            l$size <- l$size - 1
            return(curr$data)
        }
        curr <- curr$next_node
    }
    return(NULL)
}

# Function to remove a node at a particualr position of the list
remove_at <- function(l, pos) {
    if (l$size > 0) {
        prev <- NULL
        curr <- l$head

        counter <- 0

        while (counter < pos) {
            prev <- curr
            curr <- curr$next_node
            counter <- counter + 1
        }

        if (counter == 0) {
            l$head <- curr$next_node
        } else if (counter == l$size - 1) {
            l$tail <- prev
            prev$next_node <- NULL
        } else {
            prev$next_node <- curr$next_node
        }

        l$size <- l$size - 1
        return(curr$data)
    }
    return(NULL)
}
        
# Function to map a function to the list
map <- function(l, f) {
    if (l$size == 0) {
        print("List is empty")
        cat("\n")
        return(NULL)
    } else {
        curr <- l$head
        while (!is.null(curr)) {
            curr$data <- f(curr)
            curr <- curr$next_node
        }
    }
    cat("\n")
}

# Function to print an integer
print_data <- function(node) {
    print(node$data)
}

# Function that squares an integer
square <- function(node) {
    return(node$data * node$data)
}

# Test function for the various linked list functions (Integer data type)
test_function_int <- function() {

    # Creating a linked list
    linked_list <- linked_list(head = NULL, tail = NULL, size = 0)

    # Pushing data into the list
    for (i in 1:10) {
        push(linked_list, i)
    }

    # Printing the list
    print("After initialization:")
    cat("\n")
    map(linked_list, print_data)

    # Testing the map function
    print("After squaring")
    map(linked_list, square)
    map(linked_list, print_data)

    # Testing the remove function
    print("After removing the number 7:")
    cat("\n")
    remove(linked_list, 7)
    map(linked_list, print_data)

    # Testing the removeAt function
    print("After removing the number at position 3:")
    cat("\n")
    remove_at(linked_list, 3)
    map(linked_list, print_data)

    # Testing the append function
    print("After appending the number 11:")
    cat("\n")
    append(linked_list, 11)
    map(linked_list, print_data)

    # Testing the pop function
    print("After popping the first element:")
    cat("\n")
    pop(linked_list)
    map(linked_list, print_data)

    # Testing the size function
    print("The size of the list: ")
    cat("\n")
    print(size(linked_list))
    cat("\n")

    # Testing the clear function
    print("After clearing the list:")
    cat("\n")
    clear(linked_list)
    map(linked_list, print_data)

    # Testing the size function
    print("The size of the list: ")
    cat("\n")
    print(size(linked_list))
    cat("\n")

}

# Test function for the various linked list functions (String data type)
test_function_str <- function() {

    # Creating a linked list
    linked_list <- linked_list(head = NULL, tail = NULL, size = 0)

    # Pushing data into the list
    for (i in 65:90) {
        push(linked_list, intToUtf8(i))
    }

    # Printing the list
    print("After initialization:")
    cat("\n")
    map(linked_list, print_data)

    # Testing the remove function
    print("After removing the element 'c'':")
    cat("\n")
    remove(linked_list, "c")
    map(linked_list, print_data)

    # Testing the removeAt function
    print("After removing the element at position 3:")
    cat("\n")
    remove_at(linked_list, 3)
    map(linked_list, print_data)

    # Testing the append function
    print("After appending dollar sign ($):")
    cat("\n")
    append(linked_list, "$")
    map(linked_list, print_data)

    # Testing the pop function
    print("After popping the first element:")
    cat("\n")
    pop(linked_list)
    map(linked_list, print_data)

    # Testing the size function
    print("The size of the list: ")
    cat("\n")
    print(size(linked_list))
    cat("\n")

    # Testing the clear function
    print("After clearing the list:")
    cat("\n")
    clear(linked_list)
    map(linked_list, print_data)

    # Testing the size function
    print("The size of the list: ")
    cat("\n")
    print(size(linked_list))
    cat("\n")

}

# Calling the test function for integer data
test_function_int()

# Calling the test function for string data
test_function_str()
