'''
빌딩의 스카이라인은 빌딩들의 위쪽 경계를 의미한다. 여러 분은 스카이라인 밑의 가장 (면적이) 큰 직사각형을 찾아 그 면적을 출력하라
입력:
첫 줄: n  # 빌딩 수, 1 <= n <= 100,000
두 번째 줄: 가장 왼쪽 빌딩부터 높이가 차례로 주어진다 (가장 왼쪽 빌딩의 왼쪽 아래 꼭지점은 (0, 0)에 위치하고, 빌딩의 높이는 1 이상의 자연수이다)
출력: 스카이라인 아래에 있는 가장 큰 직사각형의 면적
'''
n = int(input())
lh = list(map(int, input().split())) # lh = List of the Height
'''
# 연속적으로 커지는 것만 KEEP한다
# 높이가 계속 증가하는 빌딩들만 KEEP한다
# 사용자료구조 : Stack? or dequeue
# DEQUEUE에 증가하는 것들을 계속 push 감소하는 것들은 pop 
'''
# Stack에 들어갈 것 : Stack에 저장된 빌딩 중에 최고의 높이보다 높은 빌딩의 index를 저장 / Stack이 Empty라면? => 일단 0번쨰 정보 저장
# index란? : lh에 저장된 bulding들의 Height를 지칭하는 정보 즉, lh[index]는 index번째 빌딩의 높이를 의미함
def maxAreaOfBuilding(lh): # lh : List of Height
  stack, maxArea, index = [], 0, 0
  # 가장 왼쪽부터 오른쪽까지 정보를 모두 읽어간다.
  while index < len(lh):
    # Stack에 저장되어있는 높이들 중에 가장 큰 높이(lh[stack[-1])보다 현재 빌딩의 높이(lh[index])가 더 크면 Stack에 현재 빌딩의 index를 저장
    while stack != None and lh[stack[-1]] > lh[index]:
      tos = stack.pop()
      if stack == None:
        width = index
      else:
        width = index - stack[-1] - 1
      maxArea = max(maxArea, lh[tos] * width)
    stack.append(index)
    index += 1
  
  while stack != None:
    tos = stack.pop()
    if stack == None:
      width = index
    else:
      width = index - stack[-1] - 1
    maxArea = max(maxArea, lh[tos] * width)
    
  return maxArea

result = maxAreaOfBuilding(lh)
print(result)