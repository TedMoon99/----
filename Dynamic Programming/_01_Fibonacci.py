import timeit
# Fibonacci 수 계산하기

def fibo1(n): # n번째 피보나치 수 리턴
  if n <= 1: return n
  return fibo1(n-1) + fibo1(n-2)
'''
재귀를 이용한 fibo1 함수는 아주 비효율적이다.
문제점 : fibo1(5) -> fibo1(4) + fibo1(3) -> fibo1(3) + fibo1(2), fibo1(2) + fibo1(1)처럼
같은 값을 여러번 (재귀적으로) 중복 호출되어 매우 느리게 실행됨
'''

# 기록 + 재사용 재귀 알고리즘 : Memorization 방법
def fibo2(n):
  # memo = {} -> memo는 dict로 global 선언되어 있다고 가젖ㅇ
  # memo[k] = F_k 형식으로 저장되는 dict
  memo = {}
  if n in memo.keys(): # F_n이 이미 memo에 기록이 있어 재사용
    return memo[n]
  
  # 전에 계산된 값이 아니라면
  if n <=1:
    f = n
  else:
    f = fibo2(n-1) + fibo2(n-2)
  memo[n] = f
  return f

def fibo3(n): # 기록 + 재사용 비재귀 알고리즘 2
  '''
  위의 재귀 알고리즘1에서는 재귀호출하면서 memo에 값을 처음에만 기록하고 그 이후엔 재사용한다. 이 방식은 기록한 후 재사용하는 재귀호출 방법이지만 재귀호출하지 않고도 리스트를 사용하여 직관적이고 간단하게 구현 가능
  '''
  F = [0, 1]
  if k in range(2, n+1): # 2 ~ n
    F.append(F[k-1] + F[k])
  return F[n]
# What is k?


# 실행창
n= int(input("구하고 싶으면 fibonacci 수를 입력하세요 :"))

print("")
fibo_time1 = timeit.timeit("fibo1(n)",globals=globals(), number=1)
print(fibo_time1)

fibo_time2 = timeit.timeit("fibo2(n)",globals=globals(), number=1)
print(fibo_time2)

fibo_time3 = timeit.timeit("fibo3(n)",globals=globals(), number=1)
print(fibo_time3)