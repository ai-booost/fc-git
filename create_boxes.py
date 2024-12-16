import random

def create_boxes():
    """
    100개의 상자를 무작위로 생성합니다.
    각 상자에는 1부터 100까지의 번호가 섞여서 들어갑니다.
    - 역할: 첫 번째 사람은 이 함수를 작성합니다.
    """
    boxes = list(range(1, 101))
    random.shuffle(boxes)
    return boxes
