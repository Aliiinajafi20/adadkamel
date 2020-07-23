#!/usr/bin/python                                                               

import threading

from numpy.core import long
from pip._vendor.distlib.compat import raw_input


class Number(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        if self.num % 2 == 0:
            print( "%d is even number\n" % self.num)

        else:
            print( "%d is odd number\n" % self.num)



threads = []
while True:
    input = long(raw_input("Number(0 to exit): "))
    if (input == 0):
        break;
    thread = Number(input)
    threads.append(thread)
    thread.start()

for thr in threads:
    thr.join()  