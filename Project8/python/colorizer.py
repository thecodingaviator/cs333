import threading

def cube(num):
    print("Cube: ", num * num * num)


def square(num):
    print("Square: ", num * num)


if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=square, args=(10,))
    t2 = threading.Thread(target=cube, args=(10,))

    # start thread 1
    t1.start()
    # start thread 2
    t2.start()

    # wait for thread 1 to complete
    t1.join()
    # wait for thread 2 to complete
    t2.join()

    # when both threads are completely executed
    print("Done!")

