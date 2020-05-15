import time
import random

def gen_arrays(min, max, step):
  while min < max:
    for _ in range(20):
      yield [random.random()* 100000 for i in range(min)]
    yield None
    min += step

def gen_sorted_arrays(min, max, step):
  while min < max:
    for _ in range(20):
      yield sorted([random.random()* 100000 for i in range(min)])
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
  print(fun.__name__)
  durations = []
  for arg in arg_gen:
    if arg == None:
      print(median(durations))
      durations = []
    else:
      durations.append(duration(fun, arg))


if __name__ == "__main__":
  arrays = gen_arrays(5_000, 50_001, 5_000)
  get_durations(lambda arr: arr[-1], arrays)
  arrays = gen_arrays(5_000, 50_001, 5_000)
  get_durations(max, arrays)