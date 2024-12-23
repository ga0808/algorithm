def solution(phone_book):
    phone_book = sorted(phone_book, key= lambda x : (x,len(x)) )
    
    for idx, num in enumerate(phone_book):
        if len(phone_book)-1 == idx:
            return True
        if num == phone_book[idx+1][:len(num)] :
            return False
    
    # for idx, number in enumerate(phone_book):
    #     if idx == len(phone_book)-1:
    #         break
    #     for next in phone_book[idx+1:]:
    #         n_len = len(number)
    #         if number[0] != next[0]:
    #             continue
    #         if number == next[:n_len]:
    #             return False

