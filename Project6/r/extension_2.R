# extension_2.R
# Chandrachud Malali Gowda
# This program is a R program that demonstrates how R handles strings 
# through various examples
# 04 - 15 - 2022

# Built-in string operations in R

# nchar() - Function that takes a character vector as the input and 
# returns a vector which contains the sizes of all the elements inside
# the character vector
print("nchar() : ")
string <- "Hello My Name Is Chandrachud"
nchar(string)
strvec <- c(string, "hi", "hey", "haha")
nchar(strvec)

# toupper() - Function that turns the input character vector to upper case
print("toupper() : ")
toupper(string)
toupper(strvec)

# tolower() - Function that turns the input character vector to lowercase
print("tolower() : ")
tolower(string)
tolower(strvec)

# substr() - Function that extracts and returns a part of a given input string
print("substr() : ")
substr(string, 5, 20)

# grep() - Function that searches for a patttern inside a given string and 
# returns the number of instances a match is found
print("grep() : ")
grep("Chandra", string)

# paste() - Function that converts objects into characters and concatenates them
print("paste() : ")
paste("hello", "goodbye", string, sep = "-")

# strsplit() - Function that splits the given input string into substrings 
# according to the given split argument
print("strsplit() : ")
strsplit(string, "a")

# sprintf() - Function that prints strings with variables in them
counter <- 1000L
name <- "Chandrachud"
place <- "wallet"
print("sprintf() : ")
sprintf("There are %d dollars in %s's %s", counter, name, place)

# cat() - Function that combines all input objects into a single
#  character vector
print("cat() : ")
cat("hello", "this", "is", "chandrachud", sep = "-")

# sub() - Function that replaces the first occurence of a substring in a 
# string with another substring
print("sub() : ")
sub("My Name Is", "I Am", string)

# A string in R is a collection of character variables i.e. it is a
# one-dimensional array of characters

# R's equivalent of Java's toString() function
MyClass <- R6::R6Class(
    "MyClass",
    list(i = 0)
)

toString.MyClass <- function(x, ...) {
    paste("i is", x$i)
}

my_object <- MyClass$new()
toString(my_object)
my_object$i <- 1
toString(my_object)
