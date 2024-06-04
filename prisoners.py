from random import shuffle

def find_num():
    # 죄수 번호가 들어갈 박스
    boxes = {}

    # 셔플한 수 저장할 배열
    nums = []
    # 2
    # 셔플된 죄수 번호를 하나씩 뽑아 박스에 넣는다.
    for i, num in enumerate(nums):
        boxes[i + 1] = num