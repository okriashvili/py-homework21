print("Home Work 21")

import time
import threading
from concurrent.futures import ThreadPoolExecutor
import math

def is_prime(n):
    if n <= 1:
        return "1 in neither prime nor composite number"
    if n <= 3:
        return "a prime number"
    if n % 2 == 0 or n % 3 == 0:
        return "Not a prime number"
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return "composite number"
        i += 6
    return "prime number"


t1 = time.perf_counter()

num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51]

def check_prime(num):
    return f"{num} is {is_prime(num)}"

with ThreadPoolExecutor(max_workers=5) as executor:
    executor.submit(is_prime, num_list)
    # result = list(executor.map(check_prime, num_list))


t2 = time.perf_counter()

print(f"function took {t2 - t1} seconds")



