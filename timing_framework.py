import time
import random

def gen_arrays(min, max, step):
  while min < max:
    for i in range(20):
      yield [random.random()* 100000 for i in range(min)]
    yield None
    min += step


def duration(fun, arg):
  start_time = time.time_ns()
  fun(arg)
  end_time = time.time_ns()
  duration_ns = end_time - start_time
  return duration_ns

def median(arr):
  return sorted(arr)[len(arr)//2]

def get_durations(fun, arg_gen):
  arrays = gen_arrays(5_000, 50_001, 5_000)
  durations, size = [], 0, 
  for array in arrays:
    if array == None:
      print("{}\t{}".format(size, median(durations)))
      durations, size = [], 0
    else:
      size = len(array)
      durations.append(duration(fun, array))

get_durations(max, gen_arrays)