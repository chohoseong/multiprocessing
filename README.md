# multiprocessing
멀티프로세싱을 활용한 소수찾기  
n=1000000 기준으로 소수를 찾아 return

without multiprocessing  
``` python
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
 
 ```
 ```
main PID: 9356
sub PID: 9356
time : 4.877999305725098
 ```  
함수와 main의 pid가 같음  
 
<br>with multiprocessing pool
<br>pool -> process갯수를 지정하고 처리할 값들에 대해 알아서 분산처리
 ```python
 def is_prime(num):
    if num == n:
        proc = multiprocessing.current_process()
        print(f"sub PID: {proc.pid}") #자식 프로세스 1개의 PID

    for i in range(2,int(math.sqrt(num)+1)):
        if not num % i:
            return
    return num

if __name__ == "__main__":
    start_time = time.time()
    proc = multiprocessing.current_process()
    print(f"main PID: {proc.pid}") #부모 PID
    pool = multiprocessing.Pool(processes=4)
    p_nums = list(filter(lambda x: x!=None, pool.map(is_prime, range(2,n+1))))
    pool.close()
    pool.join()

    print(f"time: {time.time()-start_time}")

 ```
 ```
main PID: 15724
sub PID: 23116
time: 2.0064163208007812
 ```
 
<br>with multiprocessing process
<br>process -> 프로세스별로 할당량을 명시적으로 정해줌
``` python
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
```
```
main PID: 9672
sub PID: 1572
sub PID: 20160
sub PID: 17576
sub PID: 12876
2.4130005836486816
```
multiprocessing을 사용한 경우 성능향상을 기대할 수 있음.
