# @file hello_world.R
# @author Parth Parth and Chandrachud Malali Gowda
# @brief A program that demonstrates the simple synatax and 
# functionality of the R language
# @version 0.1
# @date 2022-02-22

cat("What's your class year?: ");
input <- as.integer(readLines("stdin", n=1));
if(input == 1) {
    print(("Hi Freshman! Welcome to Colby!"));
} else if (input == 2) {
    print("Hi Spohomore! Weclome back to Colby!")
} else if (input == 3) {
    print("Hi Junior! Welcome back to Colby!")
} else if (input == 4) {
    print("Hi Senior! Weclome back to Colby!")
} else {
    print("Invalid Class Year")
}


