# Garbage collection in Python
# Parth and Chandra
# 4/25/2022

# Import time
import time

def memory():
    # Start timer
    start = time.time()

    # Create a list of 1,000,000 integers 15 times
    for i in range(15):
        local = start
        l = [k for k in range(1000000)]
        start = time.time()
        # Print lapsed time
        print("Time at mk 1 ", i, ": ", start - local)
        start = local

if __name__ == "__main__":
    memory()
    print("\nSecond call:\n")
    memory()
