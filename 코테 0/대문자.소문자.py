대문자->소문자, 소문자->대문자

1)
def solution(my_string):
    return my_string.swapcase()

2)
def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else:
            answer += i.upper()
    return answer
