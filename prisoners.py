from random import shuffle

def find_num():
    # 죄수 번호가 들어갈 박스
    boxes = {}
    
    # 죄수 번호(1~100)를 셔플.
    nums = [i for i in range(1, 101)]
    shuffle(nums)

    # 앞 죄수가 열어본 박스
    visited = set()


#4
success = 0
for _ in range(10000):
    success += find_num()
print(success / 10000)

    

