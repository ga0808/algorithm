def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else: # i == ')'인 경우
            if stack == []: 
            return False
            else:
                stack.pop()
    return stack == []