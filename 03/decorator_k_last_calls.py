import time
import math

def timer(k):
    def _timer(func):
        count = 0
        arr = []
        def wrapper(*args, **kwargs): 
            nonlocal arr, count
            count += 1
            start_ts = time.time()
            res = func(*args, **kwargs)
            end_ts = time.time()
            print(f"Число вызовов функции {func.__name__} =", count)
            mean_time = 0
            if count <= k:
                arr.append(end_ts - start_ts)
                mean_time = sum(arr)/len(arr)
                print(f"Время работы за {len(arr)} вызовов равно: {mean_time:.5f} cекунд")
            else:
                arr[((count % k) or k) - 1] = end_ts - start_ts
                mean_time = sum(arr)/k
                print(f"Время работы за {k} последних вызовов равно: {mean_time:.5f} cекунд")
            print("Время последних вызовов: ")
            for i in range(len(arr)):
                print(f"{arr[i]:.5f}", end=', ')
            print('\n')
            return round(mean_time, 5)
        return wrapper
    return _timer


k = 5
@timer(k)
def foo(arg1, delay):
    time.sleep(delay)
    pass


@timer(10)
def boo(arg1, delay):
    time.sleep(delay)
    pass


dct = dict()
for i in range(10):
    dct[i+1] = foo("Walter", 0.2)
    assert math.isclose(dct[i+1], 0.2, rel_tol = 0.1) == True

print('------------\n')
    
dct.clear()
for i in range(30):
    dct[i+1] = boo("Walter", 0.5)
    assert math.isclose(dct[i+1], 0.5, rel_tol = 0.06) == True