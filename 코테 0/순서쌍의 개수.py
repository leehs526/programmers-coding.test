두 숫자의 곱이 n인 자연수 순서쌍의 개수
ex)n= 20 -> 곱이 20인 순서쌍은 (1, 20), (2, 10), (4, 5), (5, 4), (10, 2), (20, 1) 이므로 6을 return

1)
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i==0:
            answer += 1
    return answer
    
2) #출력형태 [(1, 6), (2, 3), (3, 2), (6, 1)]
def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            answer.append((i, n//i))
    return answer