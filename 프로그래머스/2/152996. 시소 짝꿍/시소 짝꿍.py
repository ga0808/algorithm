from itertools import combinations
def solution(weights):

    # 균형 = 시소짝꿍 -> (탑승 무게 * 시소축 * 좌석간 거리) 가 양쪽 같으면 시소짝꿍
    
    #같은 수 몇개 있는지 알 수 있는 딕셔너리
    cnt_dict = {}
    
    #같은 애들 찾은 만큼 조합 횟수    
    for w in weights:
        if w not in cnt_dict:
            cnt_dict[w] = 1
        else :
            cnt_dict[w] += 1
    
    
       
    ans = 0
    #같은 수 애들끼리 조합 수 찾기
    for w in cnt_dict:
        ans += cnt_dict[w] * (cnt_dict[w]-1) // 2
    
    if len(cnt_dict) == 1:
        return ans
    
    distance_2 = [ 2*w for w in cnt_dict]
    distance_3 = [ 3*w for w in cnt_dict]
    distance_4 = [ 4*w for w in cnt_dict]
    
    print(distance_2)
    print(distance_3)
    print(distance_4)
        
    for i in distance_2:
        if i in distance_3:
            ans += cnt_dict[i//2] * cnt_dict[i//3]
        if i in distance_4:
            ans += cnt_dict[i//2] * cnt_dict[i//4]
            
    for j in distance_3:
        if j in distance_4:
            ans += cnt_dict[j//3] * cnt_dict[j//4]

    return ans