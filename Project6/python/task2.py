# Parth Parth and Chandrachud Gowda
# 04/12/2022
# Python program to demonstrate File I/o

from urllib.request import urlopen

def main():
    # Open file for reading
    infile = open("input.txt", "r")

    # Open file for writing
    outfile = open("output.txt", "a")

    # Read the first line from the file
    line = infile.readline()

    # Print the line to the console
    print(line)

    # Write the first line to the file
    outfile.write(line)

    # Accept user input
    line = input("Enter a line: ")

    # Write the user input to the file
    outfile.write(line)

    # Close the files
    infile.close()
    outfile.close()

    # Read a binary file
    infile = open("task2a", "rb")

    # Write a binary file
    outfile = open("output1.txt", "wb")

    # Read the first byte from the file
    byte = infile.read(1)

    # Print the byte
    print(byte)

    # Write the first byte to the file
    outfile.write(byte)

    # Close the files
    infile.close()
    outfile.close()

    # Open a URL
    infile = urlopen('https://www.stackoverflow.com')

    # Read the lines and print them
    for line in infile:
        print(line)

if __name__ == "__main__":
    main()
