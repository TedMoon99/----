def max_sum(A, left, right):
  if left == right: return A[left]
  m = (left + right) // 2 # 5
  
  L = max_sum(A, left, m)
  R = max_sum(A, m+1, right)
  # M 계산
  # 왼쪽 최대 구간합 a
  a = max_sum(A, m - m // 2, m)
  # 오른쪽 최대 구간합 b
  b = max_sum(A, m+1, m + m // 2)
  M = a + b
  return max(L, R, M)

A = [
  int(x)
  for x in input().split()
  ]
sol = max_sum(A, 0, len(A)-1) # a = 0, b = len(A) - 1
print(sol)


'''
분할정복방법은 A의 값을 반으로 분할하면, 최대 구간 합은 다음 세 가지 중 하나이다
A﻿의 왼쪽 반 구간에 존재하는 경우
A의 오른쪽 반 구간에 존재하는 경우
A의 양쪽에 모두 걸치는 경우
1번과 2번 경우에는 재귀적으로 해결하고, 3번의 경우엔 A[m]에서 끝나는 왼쪽의 최대 구간과 A[m+1]로 시작하는 오른쪽의 최대 구간의 합을 구하면 된다. (여기서 m = (left+right)//2)
최종 답은 1, 2, 3번의 경우 중 합이 최대인 구간이 된다
'''
  
    