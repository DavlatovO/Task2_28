#1

# from collections import namedtuple
# User = namedtuple('User', 'yosh ism familiya')

# user_list = []

# for i in range(2):
#     yosh = int(input('Yoshingizni kiriting:'))
#     ism = input('Ismingnizni kiriting:')
#     familiya = input('Familiyangizni kiriting:')
    
#     user = User(yosh=yosh, ism=ism, familiya=familiya)
#     user_list.append(user)

# result = max(user_list, key=lambda x: x.yosh)
# print(result)

#2

def is_prime(num1:int, num2:int):
    if num1 <= 1:
        yield False
    elif num1 == 2:
        yield True
    elif num1 % 2 == 0:
        yield False
    #Matematik formuladan foydalanamiz:
    for i in range(3, int(num1 ** 0.5) + 1, 2):
        if num1 % i == 0:
            yield False
    yield True
    if num1 <= 1:
        yield False
    elif num1 == 2:
        yield True
    elif num1 % 2 == 0:
        yield False
    for i in range(3, int(num2 ** 0.5) + 1, 2):
        if num2 % i == 0:
            yield False
    yield True

for i in is_prime(34,17):
    print(i)
    