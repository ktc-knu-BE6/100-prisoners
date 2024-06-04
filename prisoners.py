from random import shuffle

def find_num():
    # 죄수 번호가 들어갈 박스
    boxes = {}
    #3
    # 각 죄수가 방에 들어가 자신의 번호가 매겨진 박스부터 열어본다.
    for prisoner in range(1, 101):
        # 만약 앞 죄수가 열어본 박스에 본인 번호가 있다면 열 필요가 없다. 
        # 프로그램의 검색 속도를 높이기 위함. 결과에 영향을 주지 않음.  
        if prisoner in visited:
            continue
        open_num = prisoner
        for _ in range(50):
            visited.add(open_num)
            open_num = boxes[open_num]
            if open_num == prisoner:
                # print(i, '번호를 찾았다')
                break
        else:
            # 파이썬의 for문에는 else가 있습니다.
            # break가 걸리지 않았으면 실행되는 구문입니다.
            # print('못 찾았다')
            return 0
    return 1
