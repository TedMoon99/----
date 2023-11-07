import random, timeit

def insertion_sort1(A, n):
  global Qc1, Qs1
  for i in range(1, n): # 1 ~ n
    j = i - 1
    while j >= 0 and A[j] > A[j+1]:
      A[j], A[j+1] = A[j+1], A[j]
      j = j - 1
      Qc1 += 1
      Qs1 += 1

def insertion_sort2(A, n):
  global Qc2, Qs2
  for i in range(1, n): # 1 ~ n
    j = i - 1
    while j >= 0 and A[j] > A[j+1]:
      A[j], A[j+1] = A[j+1], A[j]
      j = j - 1
      Qc2 += 1
      Qs2 += 1

def quick_sort(A, first, last): # A[first] ... A[last]까지 quick sort하는 함수
  global Qc, Qs
  # A[first] ... A[last]로 quick sort!
  if first >= last: return # 정렬할 값이 1개 이하이므로 그냥 리턴
  # first < last인 경우는 quick selection과 유사하게 pivot을 정해서 나눔
  left, right = first+1, last
  pivot = A[first] 
  while left <= right: # 정렬할 값이 1개 이하가 될 때까지 나누어라 / pivot보다 작은 값은 왼쪽에, 큰 값은 오른쪽으로 재배치
    while left <= last and A[left] < pivot: # pivot보다 작은 경우 -> 더 오른쪽 값을 확인 -> pivot보다 크거나 같은 값을 찾아서 바꾸니까
      Qc += 1
      Qs += 1
      left += 1
    while right > first and A[right] > pivot: # pivot보다 큰 경우 -> 더 왼쪽 값을 확인 -> pivot보다 작거나 같은 값을 찾아서 바꾸니까
      Qc += 1
      Qs += 1
      right -= 1
    if left <= right: # swap A[left] and A[right]
      A[left], A[right] = A[right], A[left] # 현재 A[left]는 pivot보다 크거나 같은 값, A[right]는 pivot보다 작거나 같은 값 => 둘이 바꿔줌
      Qs += 1
      left += 1
      right -= 1
  A[first], A[right] = A[right], A[first] # A[right]가 pivot보다 작거나 같으므로 pivot이랑 바꿔준다
  Qs += 1
  quick_sort(A, first, right-1) # pivot의 왼쪽에 대해서 재귀적으로 적용
  quick_sort(A, right+1, last) # pivot의 오른쪽에 대해서 재귀적으로 적용

def quick_sort1(A, first, last, K):
  global Qc1, Qs1
  '''
  굳이 하나가 남을 때까지 분할할 필요는 없습니다. 경우에 따라서는 10과 40 사이의 상수 K에 대해서,
  K개 이하가 되면 분할을 멈추고 insertion sort로 정렬을 하면 더 빠를지도 모릅니다.
  이 방법을 구현해 비교해 보세요
  '''
  if first >= last: return
  if len(A[first:last+1]) > K: 
    left, right = first+1, last
    pivot = A[first]
    while left <= right:
      while left <= last and A[left] < pivot: # left의 element가 pivot보다 큰 경우
        left += 1
        Qc1 += 1
      while right > first and A[right] > pivot: # <-
        right -= 1
        Qc1 += 1
      if left <= right: # swap A[left] and A[right]
        A[left], A[right] = A[right], A[left]
        Qs1 += 1
        left += 1
        right -= 1
    A[first], A[right] = A[right], A[first]
    Qs1 += 1
    quick_sort(A, first, right-1)
    quick_sort(A, right+1, last)
  else:
    insertion_sort1(A,len(A[first:last])+1)
    
def quick_midle_sort(A, first, last):
  global Qc2, Qs2, K
  if first >= last or len(A[first:last]) <= K: return
  p = A[first]
  left, right = first+1, last
  while left <= right:
    while left <= last and A[left] < p:
      left += 1
    while right > first and A[right] > p:
      right -= 1
    if left <= right:
      A[left], A[right] = A[right], A[left]
      left += 1
      right -= 1
  A[first], A[right] = A[right], A[first]
  quick_midle_sort(A, first, right-1)
  quick_midle_sort(A, left, last)

def quick_sort2(A):
  global Qc2, Qs2, K
  '''
  적당한 K개가 남을 때까지만 분할한 후, 따로 insertion sort 등으로 정렬을 하지 않는다면,
  전체 값이 완전히 정렬이 되지는 않지만 대부분 정렬이 된 상태가 됩니다.
  완전히 정렬하기 위해, 전체 값들을 대상을 insertion sort를 적용할 수도 있습니다.
  이 방법을 구현해 비교해 보세요
  '''
  quick_midle_sort(A,0, len(A)-1)
  return insertion_sort2(A, n)
  
    
    
  
  

def merge_two_sorted_lists(A, first, last):
  global Mc, Ms
  m = (first + last) // 2
  i, j = first, m+1
  B = []
  # A의 리스트를 L, R로 나누고 L의 element를 하나씩 읽어가면서 R의 리스트와 비교해서 둘 중 큰 놈을 넣으면 된다.
  while i <= m and j <= last:
    if A[i] <= A[j]: # R의 element가 더 큰 경우 -> R의 ELEMENT를 B에 추가
      B.append(A[i])
      i += 1
    else:            # L의 element가 더 큰 경우 -> L의 ELEMENT를 B에 추가
      B.append(A[j])
      j += 1
    Mc += 1
    Ms += 1
  
  # 위의 2개의 for문은 둘 중 하나만 실행된다 <= while문이 빠져나오려면 i가 m인 경우 or j가 last인 경우 둘 중 하나이기 때문
  for k in range(i, m+1): # j == last이기에 while문을 빠져나온경우
    Ms += 1
    B.append(A[k])
  for k in range(j, last+1): # i == m이기에 while문을 빠져나온 경우
    Ms += 1
    B.append(A[k])
  for i in range(first, last+1): # A <- B
    Ms += 1
    A[i] = B[i - first]

def merge_sort(A, first, last): # A[first] ... A[last]까지 merge sort하는 함수
  global Mc, Ms
  if first >= last: return
  m = (first + last) // 2
  merge_sort(A, first, m)
  merge_sort(A, m+1, last)
  merge_two_sorted_lists(A, first, last)

def merge_sort2(A, first, last):
  global Mc2, Ms2
  if first >= last: return
  m1 = (last - first) // 3
  m2 = 2 * m1
  merge_sort2(A, first, first+m1)
  merge_sort2(A, first+m1+1, first+m2)
  merge_sort2(A, first+m2+1, last)
  B = []
  i, j, k = first, first+m1+1, first+m2+1
  while i <= first+m1 and j <= first+m2 or k <= last and j <= first+m2 or k <= last and i <= first+m1:
    if k == last+1:
      if A[i] <= A[j] and i <= first+m1:
        B.append(A[i])
        i += 1
        Mc2, Ms2 =Mc2 + 1, Ms2 + 1
      elif A[j] <= A[i] and j <= first+m2:
        B.append(A[j])
        j += 1
        Mc2, Ms2 =Mc2 + 1, Ms2 + 1
    elif j == first+m2 +1:
      if A[i] <= A[k] and i <= first+m1:
        B.append(A[i])
        i += 1
        Mc2, Ms2 =Mc2 + 1, Ms2 + 1
      elif A[k] <= A[i]  and k <= last:
        B.append(A[k])
        k += 1
        Mc2, Ms2 =Mc2 + 1, Ms2 + 1
    elif i == first+m1 +1:
      if A[j] <= A[k]  and j <= first+m2:
        B.append(A[j])
        j += 1
        Mc2, Ms2 =Mc2 + 1, Ms2 + 1
      elif A[k] <= A[j]  and k <= last:
        B.append(A[k])
        k += 1
        Mc2, Ms2 =Mc2 + 1, Ms2 + 1
    else:
      if A[i] <= A[j] and A[i] <= A[k] and i <= first+m1:
        B.append(A[i])
        i += 1
        Mc2, Ms2 =Mc2 + 2, Ms2 + 1
      elif A[j] <= A[i] and A[j] <= A[k]  and j <= first+m2:
        B.append(A[j])
        j += 1
        Mc2, Ms2 =Mc2 + 2, Ms2 + 1
      elif A[k] <= A[i] and A[k] <= A[j]  and k <= last:
        B.append(A[k])
        k += 1
        Mc2, Ms2 =Mc2 + 2, Ms2 + 1
  for i in range(i, first+m1+1): 
    B.append(A[i])
    Ms2 += 1
  for j in range(j, first+m2+1): 
    B.append(A[j])
    Ms2 += 1
  for k in range(k, last+1): 
    B.append(A[k])
    Ms2 += 1
  for z in range(first, last+1): 
    A[z] = B[z-first]	
    Ms2 += 1
  


  

def heapify_down(A, k, size):
  global Hc, Hs
  while 2*k+1 < size:
    L, R = 2*k+1, 2*k+2
    Hs += 1
    if L < size and A[L] > A[k]:
      m = L
    else:
      m = k
    Hc += 1
    if R < size and A[R] > A[m]:
      Hc += 1
      m = R
    if m != k:
      A[k], A[m] = A[m], A[k]
      Hs += 1
      k = m
    else: break
  return

def make_heap(A):
  n = len(A)
  for i in range(n-1, -1, -1):
    heapify_down(A, i, n)
  return
     
def heap_sort(A):
  global Hc, Hs
  n = len(A)
  make_heap(A)
  for i in range(len(A)-1, -1, -1):
    A[0], A[i] = A[i], A[0]
    Hs += 1
    n = n - 1
    heapify_down(A, 0,n)
  return

def tim_sort(A):
  A.sort()
  

# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#

def check_sorted(A):
	for i in range(n-1): # 오름차순으로 정렬해라
		if A[i] > A[i+1]: return False
	return True

# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
Qc, Qs, Mc, Ms, Hc, Hs, Qc1, Qs1, Qc2, Qs2, Mc2, Ms2  = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

n = int(input("삽입할 데이터의 개수를 입력하세요 : "))
K = int(input("추가 점수 코드에서의 K를 몇으로 할 지 입력하세요 : "))
random.seed()
A = []
for i in range(n):
  A.append(random.randint(-1000,1000))
B = A[:] 
C = A[:] 
D = A[:]
E = A[:]
F = A[:]
G = A[:]
print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))


print("Quick sort1:")
print("time =", timeit.timeit("quick_sort1(D, 0, n-1, K)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc1, Qs1))


print("Quick sort2:")
print("time =", timeit.timeit("quick_sort2(E)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc2, Qs2))

print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))


print("Merge sort2:")
print("time =", timeit.timeit("merge_sort2(F, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc2, Ms2))


print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

print("Tim sort:")
print("time=", timeit.timeit("tim_sort(G)", globals=globals(), number=1))

# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))
assert(check_sorted(D))
assert(check_sorted(E))
assert(check_sorted(F))
assert(check_sorted(G))