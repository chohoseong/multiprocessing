import multiprocessing
import time
import math

n=1000000

def is_prime(num):
    for i in range(2,int(math.sqrt(num)+1)):
        if not num % i:
            return False
    return True

def prime_num(s,e,conn):
    proc = multiprocessing.current_process()
    print(f"sub PID: {proc.pid}")
    for i in range(s,e):
        if is_prime(i) == True:
            #conn.send(i)
            i           

if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()
    proc = multiprocessing.current_process()
    print(f"main PID: {proc.pid}")
    start_time = time.time()

    p_nums=[]
    procs=[]
    num_list = [2, n//4, n//2, n//4*3, n+1]
    
    for i in range(len(num_list)-1):
        p = multiprocessing.Process(target=prime_num, args=(num_list[i], num_list[i+1], child_conn))
        procs.append(p)
        p.start()
    
    for p in procs:
        p.join()

    #print(parent_conn.recv())    
    print(time.time()-start_time)
