# word_counter.R
# Chandrachud Malali Gowda and Parth Parth
# This program is an R program to create a word counter in R
# 04 - 15 - 2022

# Program to count the number of each word in a given text file

# Importing the string package
library(stringr)
# Function to count the number of occurences of each word in a text file
word_counter <- function(filename) {

    # Read in the data
    data <- scan(filename, what = "", sep = "\n")

    # Separate elements by one or more whitepace
    words <- strsplit(data, "[[:space:]]+")

    # Extracting the first vector element and setting it tot he lsit
    names(words) <- sapply(words, `[[`, 1)

    # Converting each list element to lower case
    words <- lapply(words, tolower)

    # Looping through each element in the list
    for(i in 1 : length(words)) {
        # Removing punctuation from the string
        words[[i]] <- gsub("[[:punct:]]", "", words[[i]])
    }

    # Finding all the unique elements in the list
    unique_words <- unique(words)

    print(length(words[[1]]))

    # Looping through all the unique elements
    for(unique_word in unique_words[[1]]) {
        count <- 0
        for (word in words[[1]]) {
            ifelse(word == unique_word, count <- count + 1, count)
        }
        # Printing the count of each unique word
        print(paste(unique_word, count, sep = " : "))
    }

}

# Running the word counter function
word_counter("wctest.txt")