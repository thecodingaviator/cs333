# Parth Parth and Chandrachud Gowda
# 04/12/2022
# Python program to demonstrate error handling

def main():
  try:
    # Read a file
    fd = open("testerr.txt", "r")
    # Read a string from the file
    data = fd.read()
    # Convert the string to integer
    number = int(data)
    print(number)
    # Close the file
    fd.close()
  except IOError:
    print("File not found")
  except ValueError:
    print("Invalid data")
  except:
    print("Unknown error")

  # Errors can be intentionally thrown by programmer using raise
  raise NameError("Hi")

if __name__ == "__main__":
  main()
