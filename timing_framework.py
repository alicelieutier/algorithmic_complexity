import time

start_time = time.time_ns()

#  run some code

end_time = time.time_ns()
duration_ns = end_time - start_time
print(duration_ns)