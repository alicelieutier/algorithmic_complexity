import timing_framework as tm
import random

def linear_search(args):
  arr, target = args
  for el in arr:
    if el == target:
      return True
  return False

def binary_search(args):
  arr, target = args
  if len(arr) == 0:
    return False
  def aux(arr, start, end):
    if end <= start + 1:
      return arr[start] == target
    else:
      middle = arr[(end + start)//2]
      if middle == target:
        return True
      if middle > target:
        return aux(arr, start, (end + start)//2)
      return aux(arr, (end + start)//2, end)
  return aux(arr, 0, len(arr))

# search arguments generator
def gen_args_for_search(min, max, step, target):
  while min < max:
    for _ in range(15):
      yield (sorted([int(random.random()* random.random() * 1_000_000) for i in range(min)]), target)
    yield None
    min += step

args = gen_args_for_search(50000, 500001, 50000, 2000_6500)
tm.get_durations(linear_search, args, tm.average_no_outliers)
args = gen_args_for_search(50000, 500001, 50000, 2000_0890)
tm.get_durations(binary_search, args, tm.average_no_outliers)

if __name__ == "__main__":
  assert(binary_search(([1,2,3,4,5,6,7,8], 3)) == True)
  assert(binary_search(([1,2,4,5,6,7,8], 3)) == False)
  assert(binary_search(([1,2,4,5,6,7,8], 1)) == True)
  assert(binary_search(([1,2,4,5,6,7,8], 8)) == True)
  assert(binary_search(([8], 8)) == True)
  assert(binary_search(([8], 2)) == False)
  assert(binary_search(([], 2)) == False)
