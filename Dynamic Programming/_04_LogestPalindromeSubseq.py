'''
### 최장 회문 부수열 (Longest Palindrome Subsequence) ###
영어 대문자로만 구성된 문자열이 입력으로 주어지면, 입력 문자열의 부수열(subsequence) 중에서 가장 긴 회문(palindrome)의 길이를 출력

- 입력 문자열의 길이는 1이상 2,500 이하이다
- 회문은 왼쪽에서 오른쪽으로 읽거나 반대로 오른쪽에서 왼쪽으로 읽어도 같은 단어를 의미한다. (예: radar, madam 등)
- 회문의 길이는 회문 문자열의 길이이다. (예: radar는 길이가 5인 회문임)
- 한 문자는 길이가 1인 회문이다

힌트: 전형적인 LCS(Longest Common Subsequence) 스타일의 동적계획법으로 접근 가능!
제한시간: 5초
주의: 외부 자료 + 동료 토론 금지 (LCS DP 알고리즘을 따라하면 충분히 혼자 할 수 있음!)
주석: 알고리즘을 간단히 설명하고 수행 시간을 분석하시오
'''

# LCS(Longest Comon Subsequence) 계산하기
def LPS(X, Y):
  n, m = len(X), len(Y)
  # prepare 2d list len and initialization
  A = [
    [None] * n
    for _ in range(n)
  ]
  
  for j in range(0, n):
    A[0][j],A[j][0] = 0, 0
  # filling DP table A
  for i in range(1, n):
    for j in range(1, m):
      if X[i] == Y[j]: # 마지막 두 글자가 같으면
        A[i][j] = A[i-1][j-1] + 1
      else:
        A[i][j] = max(A[i-1][j], A[i][j-1])
  return A[n-1][m-1]
  
  
x = "CHEESECAKE"
y = x[:]
result = LPS(x, y)
print(result)
