def solution(record):
    answer = []
    #입장 : Enter 유저id 닉네임
    #퇴장 : Leave 유저id
    #변경  : Change 유저id 닉네임
    # record_dict = {유저id : 닉네임}
    record_dict = {}
    for rec in record:
        rec = rec.split()
        # print(rec)
        user_id = rec[1]
        if len(rec)==3: #입장 또는 변경
            if rec[0] == "Enter":
                record_dict[user_id] = rec[2]
                answer.append([user_id,"님이 들어왔습니다."])
            else : #닉네임 변경
                record_dict[user_id] = rec[2]
        else: #퇴장
            # del record_dict[user_id]
            answer.append([user_id,"님이 나갔습니다."])
    
    final_answer = []
    for user_id, state in answer:
        user_id = record_dict[user_id]
        final_answer.append(user_id + state)
        
    return  final_answer