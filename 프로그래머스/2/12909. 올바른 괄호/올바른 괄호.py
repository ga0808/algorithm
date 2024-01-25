#스택으로 구현해보자

#( ) - 쌍이 잘 맞아서 모두 없어졌을때 -> return T
#) , ( - 남아버렸다 -> return False

def solution(s):
    stack = []
    #( 여는 괄호를 stack에 넣은다음에, )이 나올때마다 삭제해줌 
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack ==[]: 
                return False
            else:
                stack.pop()
    if stack != []: #for문 다 돌았는데, 여전히 여는 괄호가 남아있다면
        return False
    
    return True