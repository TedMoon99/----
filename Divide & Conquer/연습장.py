def insertion_sort(A, n):
  for i in range(1, n): # 1 ~ n
    j = i - 1
    while j >= 0 and A[j] > A[j+1]:
      A[j], A[j+1] = A[j+1], A[j]
      j = j - 1
def quick_midle_sort(A,first, last):
  global Qc2, Qs2, K
  if len(A[first:last]) < K // 2: return
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
      right += 1
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
  # print(len(A))
  return insertion_sort(A, n)
 
A = [ 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
K = 6
 
quick_sort2(A)
 
def check_sort(A):
    for i in range(n):
        if A[i] > A[i+1]:
            return False
    return True
assert(check_sort(A))