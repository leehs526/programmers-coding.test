1)
def solution(n):
    answer = []
    for i in range(1, n+1): #for i in n 안됨!! n이 정수이기때문
        if n % i == 0:
            answer.append(i) # answer += i 안됨!! 리스트에 추가할때는 append 써야함
    return answer

2)
def solution(n):
    answer = [i for i in range(1, n+1) if n % i == 0]
    return answer
