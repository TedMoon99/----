def find_k(p1, p2):
  # K가 Matrix 안에 존재하지 않는 경우
  if A[0][0] > K or A[n-1][n-1] < K: return -1, -1
  # pivot을 포함하는 2 x 2에 존재하는 경우
  if A[p2][p1] == K: return p2, p1
  elif A[p1][p2] == K: return p1, p2
  elif A[p1][p1] == K: return p1, p1
  elif A[p2][p2] == K: return p2, p2 

  if (p1, p2) == (0,1) and A[0][0] != K: return -1, -1 # (0, 0)
  if (p1, p2) == (n-2, 1) and A[n-1][0] != K: return -1, -1 # (n-1, 0)
  if (p1, p2) == (0, n-1) and A[0][n-1] != K: return -1, -1 # (0, n-1)
  if (p1, p2) == (n-2, n-1) and A[n-1][n-1] != K: return -1, -1 # (n-1, n-1)
  tempX_1, tempX_2, tempX_3, tempY_1, tempY_2, tempY_3 = 0, 0, 0, 0, 0, 0
  moveSize = p2 // 2
  # pivot을 기준으로 사분면을 나눠서 이동하는 경우
  if A[p1][p1] > K: # 제 4사분면에는 존재하지 않는다 => 제 1, 2, 3 사분면에 존재한다.
    tempX_2, tempY_2 = find_k(p1 - moveSize, moveSize) # 제 2사분면으로 이동
    if (tempX_2, tempY_2) == (-1, -1):
      tempX_1, tempY_1 = find_k(moveSize, p2 + moveSize) # 제 1사분면으로 이동
    else:
      return tempX_2, tempY_2
    if (tempX_1, tempY_1) == (-1, -1): # 제 3사분면으로 이동
      return find_k(p1 + moveSize, moveSize)
    else:
      return tempX_1, tempY_1

       
  elif A[p2][p2] < K : # 제 2사분면에는 존재하지 않는다. => 제 1, 3, 4 사분면에 존재한다.
    # 제 1사분면으로 이동
    tempX_1, tempY_1 = find_k(moveSize, p2 + moveSize)
    if (tempX_1, tempY_1) == (-1, -1):
      # 제 3사분면으로 이동
      tempX_3, tempY_3 = find_k(p1 + moveSize, moveSize)
    else:
      return tempX_1, tempY_1
    if (tempX_3, tempY_3) == (-1, -1): # 제 4사분면으로 이동
      return find_k(p1 + moveSize, p2 + moveSize)
      
  else: # 제 2, 4사분면에 존재하지 않는다. => 제 1, 3사분면에 존재한다.
    temp1, temp2 = find_k(moveSize, p2 + moveSize) # 제 1사분면으로 이동
    if (temp1, temp2) == (-1, -1):# 제 1사분면에서 원하는 k를 못 찾은 경우
      return find_k(p1 + moveSize, moveSize) # 제 3사분면으로 이동
    return temp1, temp2 # 제 1사분면에 존재한 경우




# 첫 줄 입력 받아오기
n, K = map(int, input().split())
# 행의 값을 받아와서 행렬 만들기
A = [
	list(map(int, input().split()))
	for _ in range(n)
]
i, j = find_k(n // 2 -1, n // 2)
print(f"({i}, {j})")
# 행마다 열마다 오름차순으로 나열되어 있다.

