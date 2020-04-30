import time

start_time = time.time_ns()

# compare
# (i*i-2 for i in range(10000000)) # 3000 ns
# and
# [i*i-2 for i in range(10000000)] # 1663136000 ns


end_time = time.time_ns()
duration_ns = end_time - start_time
print(duration_ns)