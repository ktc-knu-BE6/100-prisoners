from random import shuffle

def find_num():
    # 죄수 번호가 들어갈 박스
    boxes = {}


#4
success = 0
for _ in range(10000):
    success += find_num()
print(success / 10000)
