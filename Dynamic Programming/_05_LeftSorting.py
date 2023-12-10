def leftSort(wl, w):
  # wl = 문장을 이루는 단어의 개수
  # w = 폭의 길이
  DP = [w ** 3] * (wl+1)
  DP[0] = 0
  for i in range(1, wl+1):
    length, temp = 0, ""
    for j in range(i, 0, -1):
      temp += words[j-1] + " "
      length = len(temp.strip())
      if length > w: break
      penalty = (w - length) ** 3
      DP[i] = min(DP[i], DP[j-1] + penalty)
  return DP[wl]

W = int(input("문장의 폭을 입력하세요: "))
words = input("문서에 작성할 문장을 입력하세요").split()
# code below
wl = len(words)
result = leftSort(wl, W)
print(result)