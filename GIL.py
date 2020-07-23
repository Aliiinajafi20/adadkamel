from multiprocessing import pool
import time

CONT = 500000000
def contdown(n):
    while n>0:
        n -= 1



if __name__=='__main':
    pool = pool(processes=2)
    start = time.time()
    r1 = pool.applay_asnc(contdown,[CONT//2])
    r2 = pool.applay_asnc(contdown,[CONT//2])
    pool.close()
    pool.join()
    end = time.time()
    print('time taken in second-', end - start)
