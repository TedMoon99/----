'''
2 x 1 (또는 1 x 2) 도미노 여러개를 이용해 2 x n 타일을 빈틈없이 메우는 경우의 수는?
A[n] = 2 x 1 도미노 여러개를 이용해 2 x n 타일을 빈틈 없이 메우는 경우의 수로 정의

A[n] = A[n-1] + A[n-2]

A[n-1] : 가장 오른쪽 열을 타일 하나로 채우는 경우(세로)
A[n-2] : 가장 오른쪽 열을 타일 2개로 채우는 경우(가로) 
'''

def tiling_domino(n):
  # A[n] = A[n-1] + A[n-2]
  F = [0,1]
  for k in range(2,n+1): # 1 ~ n
    F.append(F[k-1] + F[k-2])
  return F[n]

n = int(input("2 x n의 타일을 채울 것인지 정하시오 :"))
result = tiling_domino(n)
print(f"2 x {n}의 타일을 채우는 경우의 수는 {result}입니다.")
