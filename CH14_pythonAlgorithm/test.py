import time

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

test_value = 500
iterations = 10000  # 실행 횟수 증가

start_time = time.perf_counter()
for _ in range(iterations):
    factorial(test_value)
end_time = time.perf_counter()

avg_time = (end_time - start_time) / iterations
print(f"Average Execution Time: {avg_time:.10f} seconds")
