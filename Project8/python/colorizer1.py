# Parth and Chandra
# Colorizer with 1 thread
# 5/06/2022

import sys
import threading
import time
import math


class PPM:

    def __init__(self, filename=None):
        self.rows = 0
        self.cols = 0
        self.colors = 255
        self.data = []
        self.source = filename

        if filename != None:
            self.read(filename)

    def read(self, filename):

        try:
            fp = open(filename, "rb")  # open the file as a binary file

            s = ""
            c = fp.read(1)
            while c != b"\n":
                s += str(c)
                c = fp.read(1)

            if s == b'P'b'6':
                print("PPM Magic number")

            c = fp.read(1)
            while c == b"#":
                while c != b"\n":
                    c = fp.read(1)
                c = fp.read(1)

            s = ""
            while c != b"\n":
                s += c.decode("utf-8")
                c = fp.read(1)

            words = s.split()
            self.cols = int(words[0])
            self.rows = int(words[1])
            # self.colors = int(words[2])

            print("Rows %d  Cols %d  Colors %d" %
                  (self.rows, self.cols, self.colors))
            self.data = bytearray(fp.read())  # read the rest of it

            fp.close()

        except:
            print("Unable to process file %s" % (filename))
            return None

    def write(self, filename):
        fp = open(filename, "wb")
        s = "P6\n%d %d %d\n" % (self.cols, self.rows, self.colors)
        fp.write(bytearray(s, encoding='utf-8'))
        fp.write(self.data)
        fp.close()

    def get(self, row, col):
        index = 3 * (row * self.cols + col)
        return [self.data[index+0], self.data[index+1], self.data[index+2]]

    def set(self, row, col, r, g, b):
        index = 3 * (row * self.cols + col)
        self.data[index+0] = r
        self.data[index+1] = g
        self.data[index+2] = b


def t_pixel(ppm, start_row, end_row):
    for i in range(start_row, end_row):
        # print("row", i)
        for j in range(0, ppm.cols):
            # print("col", j)
            index = 3 * (i*ppm.cols + j)
            for k in range(0, 3):
                if ppm.data[index+k] > 128:
                    ppm.data[index+k] = math.floor((220+ppm.data[index+k])/2)
                else:
                    ppm.data[index+k] = math.floor((30+ppm.data[index+k])/2)


def main(argv):
    if len(argv) < 2:
        print("Usage: python3 <image filename>")
        exit()

    print("Reading image", argv[1])
    ppm = PPM(argv[1])
    print("Setting values")
    rows = ppm.rows

    t1 = threading.Thread(target=t_pixel, args=(ppm, 0, math.floor(rows/2)))
    time1 = time.time()
    t1.start()
    t1.join()
    time2 = time.time()
    print("Writing mod.ppm")
    ppm.write("mod.ppm")
    print("Time:", time2-time1)
    print("Terminating")


if __name__ == "__main__":
    main(sys.argv)
