# Parth Parth 
# 03/02/2022
# Demonstrate Binary Search in Python but obfuscate the code (Extension 1)

"""Does Searching for a value in a list using Binary Search"""
class Search:
    # The docstring can go on multiple lines. It makes it harder to read if not done properly
    """C
    lass to define and perform binary search 
    on a list
    
    """
    def __init__(self, data):

        self.data = data
        self.length = len(
            # I will put so many new lines here to obfuscate the code
            data
        
        
        # I am putting a comment in the code to make it even harder to read
        # This will still work though
        
        )

    def binary_search(self, value):
        """Does Binary Search for value in the list"""
        # Initialize left and right pointers
        low = 0
        high = self.length - 1
        while low <= high:






            # These unnecessary lines breaks should also make it harder to read the code


            mid = (low + high) // 2
            if self.data[mid] == value:
                return mid
            if self.data[mid] > value:
                high = mid - 1
            else:
                low = mid + 1







        # If I put more line breks here, the code will still work

        # If value not found
        return -1

def main():
    """Main function"""
    # I can do what I did below and still have it be a valid list
    # Create a list of 15 numbers
    data = [
        1
        ,
         2
         ,
          3
          ,
 4,
  5,
 6, 
 7, 
                    8,
                     9, 
                     10, 
                                    11, 
        12, 
13, 
                                                            14, 
15]

    # Create an object of Search class
    search = Search(data)

    # Search for the value 8
    print("Searching for 8: ", 
    search.
    binary_search(
        8
        )
                                                                                           )   

    # Search for the value 16
    print("Searching for 16: ", search.binary_search(16))

if __name__ == '__main__':
    main()
