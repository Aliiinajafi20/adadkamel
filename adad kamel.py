import math
import queue
import threading
import time
import timeit

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q

   def run(self):
      print ("Starting " + self.name)
      process_data(self.name, self.q)
      print ("Exiting " + self.name)

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

def process_data(threadName, q):
   while not exitFlag:
      queueLock.acquire()
      if not workQueue.empty():
         data = q.get()
         queueLock.release()
         print ("%s processing %s" % (threadName, data))
      else:
         queueLock.release()
         time.sleep(1)

n = int(input("please enter number: "))
Thread = int(input("please enter thread: "))

for j in range(n):
    if (adad_kamel(j)):
        print(j)
lentgh = int(n / Thread)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["lentgh One", "lentgh Two", "lentgh Three", "lentgh Four", "lentgh Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = [lentgh]
threadID = 1

# Create new threads
for tName in threadList:
   thread = myThread(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
   workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
   pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")




