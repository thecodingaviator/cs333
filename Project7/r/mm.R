# Chandrachud Malali Gowda and Parth Parth
# This program is an R program that demonstrates memory management in R
# 04 - 28 - 2022

# install.packages("plyr", repos = "http://cran.us.r-project.org")
# install.packages("pryr", repos = "http://cran.us.r-project.org")
library(plyr)
library(pryr)

# Class to store the details of a employee
setClass("employee", slots=list(name="character", id="numeric", age="numeric", email="character"))
chandra <- new('employee', name="Chandra", id=7, age=18, email="cmgowd25@colby.edu")

# Object size

# Printing the object size of the employee
chandra_size <- object.size(chandra)
print("Size of chandra object: ")
print(chandra_size)

# Printing the object size of the employee name
chandra_name_size <- object.size(chandra@name)
print("Size of chandra name object: ")
print(chandra_name_size)

# Printing the object size of the employee id
chandra_id_size <- object.size(chandra@id)
print("Size of chandra id object: ")
print(chandra_id_size)

# Printing the object size of the employee age
chandra_age_size <- object.size(chandra@age)
print("Size of chandra age object: ")
print(chandra_age_size)

# Printing the object size of the employee email
chandra_email_size <- object.size(chandra@email)
print("Size of chandra email object: ")
print(chandra_email_size)

# The rm function is used to delete any object from R and releases some memory
rm(chandra)

# Memory usage and garbage collection
print("Total size of all objects in memory: ")
print(mem_used())

# Seeing how memoru changes during code execution
print(mem_change(a <- 1 : 1e6))
# Seeing how we get memory back when we delete an object
print(mem_change(rm(a)))

# Showing that even operations that do virtually do nothing still use up minute amounts of memory
print(mem_change(NULL))

# Showing memory change through modification in place of an object
x <- 1:10
print("Printing out the variable's location in memory and telling us how many names point to that location")
print("x variable address and references: ")
print(c(address(x), refs(x)))

y <- x
print("y variable address and references: ")
print(c(address(y), refs(y)))

# Printing the current memory location of an object
print("Current memory location of x :")
print(tracemem(x))
print("Current memory location of y :")
print(tracemem(y))

rm(x)
rm(y)