'''
Warming-up: 미로탈출

### n x n 미로 M이 주어진다
1) M[i][j] = 0이면 빈 칸이고, 1이면 장애물이라고 가정
2) 생쥐가 M[0][0]에서 출발하여, M[n-1][n-1]에 도착하면 탈출 성공!
3) 빈 칸만을 방문해야 하고, 오직 오른쪽에 이웃한 빈 칸 또는 아래쪽에 위치한 빈 칸으로만 이동할 수 있다고 가정
4) 문제는 생쥐가 미로 지도를 갖고 있지 않기에 기을 미리 계산할 수 없다는 것이다. 성공적으로 탈출할 수 있는지 결정하는 문제

### 전략
현재 칸이 탈출 칸이라면 : 성공!
아니라면:
  1. 현재 칸이 장애물이라면, 그 전 칸으로 후퇴(Backtracking)!
  2. 현재 칸이 빈 칸이고, 처음 방문한 칸이라면:
    a. 방문했다고 기록
    b. 아래 칸으로 이동(재귀적으로 반복)
    c. 아래 칸으로 이동해서 목적지에 도달하지 못했다면:
      i) 오른쪽 칸으로 이동(재귀적으로 반복)
    d. 오른쪽 칸으로 이동해서도 목적지에 도달하지 못했다면:
      i) 실패 결곽를 가지고 backtrack!
'''

# Pseudo Code
def find_way(x, y):
  if x >= n or y >= n: return False
  if x == n-1 and y == n-1: return True
  if M[x][y] != 1: # 현재 칸이 장애물이 아닌 경우
    try_down = find_way(x+1, y) # 아래 칸으로 이동
    if try_down: return True # 성공했다면!?
    try_east = find_way(x, y+1) # 오른쪽 칸으로 이동
    return try_east
  else:
    return False

n = int(input())
M = [
  list(map(int, input().split()))
  for _ in range(n)
]
print(M)
result = find_way(0,0)
print(result)
