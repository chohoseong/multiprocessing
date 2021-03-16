import multiprocessing
import time
import math

n=1000000

def is_prime(num):
    for i in range(2,int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

def prime_num(n):
    proc = multiprocessing.current_process()
    print(f"prime_num PID: {proc.pid}")
    p_nums = [num for num in range(2,n+1) if is_prime(num) == True]
    return p_nums

if __name__ == "__main__":
    proc = multiprocessing.current_process()
    print(f"main PID: {proc.pid}")

    start_time = time.time()
    p_nums = prime_num(1000000)
    end_time = time.time()

    print(f"time : {end_time-start_time}")

