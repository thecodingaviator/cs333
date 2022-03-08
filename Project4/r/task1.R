# task1.R
# Chandrachud Malali Gowda And Parth Parth
# This program is a sample R program that demonstrates
# the control flow statements in the language,
# variable declarations, and identifier scoping
# 03 - 10 - 2022

# if, else if, and else control statements
grade <- function(x) {
    if (x > 90) {
        return("A")
    } else if (x > 80) {
        return("B")
    } else if (x > 70) {
        return("C")
    } else if (x > 60) {
        return("D")
    } else {
        return("F")
    }
}

# switch control statements
option_choice <- function(x) {
    switch(x,
    a = "option 1",
    b = "option 2",
    c = "option 3",
    stop("Invalid `x` value")
    )
}

# Loop control statements
loop_example <- function() {
    for (i in 1:10) {
        if (i < 3) {
            next
        }

        print(i)

        if (i >= 5) {
            break
        }
    }
}

# Testing the functions
print(grade("A"))
print(option_choice("c"))
loop_example()