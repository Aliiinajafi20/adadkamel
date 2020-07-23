#!/usr/bin/python3

import _thread
import math
import time

def adad_kamel(n):
    sum = 1


    for i in range(2, (int)(math.sqrt(n)) + 1):
        if (n % i == 0):
            sum += i
            if (i != (n / i)):
                sum += n / i
        i += 1

    if (sum == n):
        return True
    return False

# Create two threads as follows
try:
   _thread.start_new_thread( adad_kamel, ("Thread-1", 2, ) )
   _thread.start_new_thread( adad_kamel, ("Thread-2", 4, ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass