import time

def measure_run_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        a=5
        result = func(a)
        end = time.time()

        print(f"function running time : {end - start}")
        return result
    return wrapper

@measure_run_time
def worker(delay_time):
    time.sleep(delay_time)
    return 

worker(5)

# 결과값
# function running time : 5.004865884780884