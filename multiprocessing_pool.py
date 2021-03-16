import multiprocessing
import time
import math

n=1000000

def is_prime(num):
    if num == n:
        proc = multiprocessing.current_process()
        print(f"sub PID: {proc.pid}") 

    for i in range(2,int(math.sqrt(num)+1)):
        if not num % i:
            return
    return num

if __name__ == "__main__":
    start_time = time.time()
    proc = multiprocessing.current_process()
    print(f"main PID: {proc.pid}") 
    pool = multiprocessing.Pool(processes=4) #4개 프로세스 사용
    p_nums = list(filter(lambda x: x!=None, pool.map(is_prime, range(2,n+1))))
    #mapping 결과에서 none filtering
    pool.close()
    pool.join()

    print(f"time: {time.time()-start_time}")
