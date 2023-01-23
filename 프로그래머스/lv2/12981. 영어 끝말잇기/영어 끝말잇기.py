def solution(n, words):
    answer = []
    #n= 참여자 수
    #words = 끝말잇기 단어들 순서대로 담겨져 있는 lst
    copy_words=[]
    cnt=1 #몇번째 사람이 말하는지
    cnt_talk=1  #몇번 턴이 돌았는지
    for w in range(len(words)):
        if cnt==n+1 and (len(words)!=(len(copy_words)+1)):
            cnt=1
            cnt_talk+=1
            
#         if len(words[w]) ==1:
#             answer.append(cnt)
#             answer.append(cnt_talk)
#             break
            
        if words[w] in copy_words:
            answer.append(cnt)
            answer.append(cnt_talk)  
            break
        
        if w != 0 and words[w][0] != words[w-1][-1]:
            answer.append(cnt)
            answer.append(cnt_talk)
            break
            
        copy_words.append(words[w])
        cnt+=1
        
        if len(words) == len(copy_words):
            answer = [0,0]
    return answer