def prisoner_strategy(prisoner_number, boxes): #2번째 함수 정의
    attempts = 50 
    current_box = prisoner_number
    for _ in range(attempts):
        if boxes[current_box -1] == prisoner_number:
            return True
        current_box = boxed[current_box - 1]
    return False
