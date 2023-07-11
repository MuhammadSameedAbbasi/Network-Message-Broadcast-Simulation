import random

init_list = []

def init_generator():
    for i in range(0, 3):
        init_list.append((random.randint(2, 49), random.randint(2, 49)))


init_generator()
print(init_list)