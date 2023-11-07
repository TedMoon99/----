

# 입력 : 왼쪽으로 rotation이동을 한 리스트

def rotateCount(arr):
  m = len(arr) // 2
  if len(arr) < 1 or m == 0: return 0
  if not len(arr) % 2:
    m -= 1
  if arr[m] > arr[m+1]: # 값을 출력
    return len(arr[m+1:])
  elif arr[m] < arr[m+1]:
    return rotateCount(arr[m+1:])
  else: # arr[m] = arr[m+1]
    return rotateCount(arr[m+1:])

while True:
  A = list(map(int, input().split()))
  print(rotateCount(A))
  check = input("계속하시겠습니까?: ")
  if check == 'n':
    break
