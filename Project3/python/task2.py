# Parth Parth and Chandrachud Gowda
# 03/02/2022
# Demonstrate Binary Search in Python

"""Does Searching for a value in a list using Binary Search"""
class Search:
    """Class to define and perform binary search on a list"""
    def __init__(self, data):
        self.data = data
        self.length = len(data)

    def binary_search(self, value):
        """Does Binary Search for value in the list"""
        # Initialize left and right pointers
        low = 0
        high = self.length - 1
        while low <= high:
            mid = (low + high) // 2
            if self.data[mid] == value:
                return mid
            if self.data[mid] > value:
                high = mid - 1
            else:
                low = mid + 1
        # If value not found
        return -1

def main():
    """Main function"""
    # Create a list of 15 numbers
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    # Create an object of Search class
    search = Search(data)

    # Search for the value 8
    print("Searching for 8: ", search.binary_search(8))

    # Search for the value 16
    print("Searching for 16: ", search.binary_search(16))

if __name__ == '__main__':
    main()
