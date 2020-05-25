import random
import timing_framework as tm

def selection_sort(arr):
  def _index_min(start):
    if len(arr) < start + 1:
      raise "No"
    current_index_min = start
    i = start
    while i < len(arr):
      current_minimum = arr[current_index_min]
      if arr[i] < current_minimum:
        current_index_min = i
      i += 1
    return current_index_min
  i = 0
  while i < len(arr):
    min_i = _index_min(i)
    arr[i], arr[min_i] = arr[min_i], arr[i]
    i += 1
  return arr

def insertion_sort(arr):
  i = 1
  while i < len(arr):
    # print("i:{},arr:{}".format(i, arr))
    value = arr[i]
    j = 0
    while j < i:
      if arr[i] < arr[j]:
        arr.insert(j, value)
        arr.pop(i+1)
      j+=1
    i+= 1
  return arr

def _merge(arr1, arr2):
  # if len(arr1) < len(arr2):
  #   arr1, arr2 = arr2, arr1
  c1 = 0
  c2 = 0
  result = []
  while c1 < len(arr1) and c2 < len(arr2):
    if arr1[c1] < arr2[c2]:
      result.append(arr1[c1])
      c1 += 1
    else:
      result.append(arr2[c2])
      c2 += 1
  while c2 < len(arr2):
    result.append(arr2[c2])
    c2 += 1
  while c1 < len(arr1):
    result.append(arr1[c1])
    c1 += 1
  return result

def mergesort(arr):
  if len(arr) < 2:
    return arr
  left, right = arr[:len(arr) // 2], arr[len(arr) // 2:]
  sol1 = mergesort(left)
  sol2 = mergesort(right)
  return _merge(sol1, sol2)



def quicksort(arr):
  # random.shuffle(arr)
  def aux(start, end):
    if end - start < 1:
      return
    pivot = arr[start]
    pi = start
    li = start + 1
    ri = end
    while li <= ri:
      # print("li:{}, pi:{}, ri:{}, arr:{}, pivot:{}".format(li, pi, ri, arr, pivot))
      if arr[li] <= pivot:
        arr[li], arr[pi] = arr[pi], arr[li]
        pi += 1
        li += 1
      else:
        arr[li], arr[ri] = arr[ri], arr[li]
        ri -= 1
    aux(start, pi - 1)
    aux(pi + 1, end)
  aux(0, len(arr) - 1)
  return arr

def gen_arrays(min, max, step):
  while min < max:
    for _ in range(15):
      yield [int(random.random()*random.random()* 1_000_000) for i in range(min)]
    yield None
    min += step

arrays = gen_arrays(50, 501, 50)
tm.get_durations(mergesort, arrays, tm.average_no_outliers)
arrays = gen_arrays(50, 501, 50)
tm.get_durations(selection_sort, arrays, tm.average_no_outliers)
arrays = gen_arrays(50, 501, 50)
tm.get_durations(quicksort, arrays, tm.average_no_outliers)
arrays = gen_arrays(50, 501, 50)
tm.get_durations(insertion_sort, arrays, tm.average_no_outliers)
# # arrays = gen_arrays(5000, 50_001, 5000)
# # tm.get_durations(quicksort, arrays)

if __name__ == "__main__":
  assert(selection_sort([2,3,4,3,2,1]) == [1,2,2,3,3,4])
  assert(selection_sort([1,1,1,1,1]) == [1,1,1,1,1])
  assert(selection_sort([0]) == [0])
  assert(selection_sort([9,2,3,7,7]) == [2,3,7,7,9])
  assert(selection_sort([]) == [])

  assert(insertion_sort([2,3,4,3,2,1]) == [1,2,2,3,3,4])
  assert(insertion_sort([1,1,1,1,1]) == [1,1,1,1,1])
  assert(insertion_sort([0]) == [0])
  assert(insertion_sort([9,2,3,7,7]) == [2,3,7,7,9])
  assert(insertion_sort([9,2,3]) == [2,3,9])
  assert(insertion_sort([]) == [])
  assert(insertion_sort([4,5]) == [4,5])
  assert(insertion_sort([10,5]) == [5,10])

  assert(quicksort([2,3,4,3,2,1]) == [1,2,2,3,3,4])
  assert(quicksort([1,1,1,1,1]) == [1,1,1,1,1])
  assert(quicksort([0]) == [0])
  assert(quicksort([9,2,3,7,7]) == [2,3,7,7,9])
  assert(quicksort([9,2,3]) == [2,3,9])
  assert(quicksort([]) == [])
  assert(quicksort([4,5]) == [4,5])
  assert(quicksort([10,5]) == [5,10])


  assert(mergesort([2,3,4,3,2,1]) == [1,2,2,3,3,4])
  assert(mergesort([1,1,1,1,1]) == [1,1,1,1,1])
  assert(mergesort([0]) == [0])
  assert(mergesort([9,2,3,7,7]) == [2,3,7,7,9])
  assert(mergesort([9,2,3]) == [2,3,9])
  assert(mergesort([]) == [])
  assert(mergesort([4,5]) == [4,5])
  assert(mergesort([10,5]) == [5,10])