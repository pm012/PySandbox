import concurrent.futures
import math
import os
import time

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    sqrt_n = int(math.sqrt(n))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def benchmark_process_pool(workers):
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(workers) as executor:
        list(executor.map(is_prime, PRIMES))
    return time.time() - start_time

if __name__ == '__main__':
    fixed_workers = 4
    cpu_workers = os.cpu_count()
    cpu_workers_div2 = max(2, os.cpu_count() // 2) # if many cores divide them by 2 to save resources
    
    print(f"Benchmarking with {fixed_workers} workers...")
    time_fixed = benchmark_process_pool(fixed_workers)
    print(f"Time taken with {fixed_workers} workers: {time_fixed:.4f} seconds")
    
    print(f"\nBenchmarking with {cpu_workers} workers...")
    time_cpu = benchmark_process_pool(cpu_workers)
    print(f"Time taken with {cpu_workers} workers: {time_cpu:.4f} seconds")
    
    print(f"\nBenchmarking with {cpu_workers_div2} workers...")
    time_cpu_div2 = benchmark_process_pool(cpu_workers_div2)
    print(f"Time taken with {cpu_workers_div2} workers: {time_cpu_div2:.4f} seconds")
    
    print(f"\nPerformance improvement: {100 * (time_fixed - time_cpu) / time_fixed:.2f}%")
    print(f"\nPerformance improvement: {100 * (time_fixed - time_cpu_div2) / time_fixed:.2f}%")
