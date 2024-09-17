import random
flag = ""
random_flag = random.randint(1,2)
if random_flag == 1:
    flag = "norte"
else:
    flag = "sur"


print(flag)
print(type(flag))