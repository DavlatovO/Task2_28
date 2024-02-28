""" sequence, closures """
from decorators import chek_admin, chek_sth
import time
# 
# ism = 'Abdulaziz'
# ism[1]
# start,stop,step
# ism[1:5:2]

# """
# sequence types
# 1) str
# 2) list
# 3) tuple
# 4) range
# """

# ism[5:]
# print(ism[1:3])
# print(ism[3:])
# print(ism[:3])
# print(ism[:])

# print(ism[1:5:2])

# class WeekDays:
#     items = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

#     def __getitem__(self, index):
#         print(index)
#         return self.items[index]


# print(WeekDays()[::-1])

# admn, staff, user

# @chek_admin()
# def get_staff(a,b,c): #admin, staff
#     print('Func ishladi')
    # if user.status == 'admin' or user.status == 'staff':
    # ...

# @chek_admin
# def update_staff(): # admin, staff
    # if user.status == 'admin' or user.status == 'staff':
    # ...
    # ...

# def delete_staff(): # admin
    # if user.status == 'admin':
    # ...
    # ...


# def create_staff(): # admin
    # if user.status == 'admin':
    # ...
    # ...

# @chek_sth
# def salom_ber(ism):
#     time.sleep(2)
#     return f"Assalomu alaykum {ism}"


# @chek_sth
# def familiya_salo_ber(familiya):
#     return f"Assalomu alaykum {familiya}"

# print(salom_ber(ism='Muhammadaziz'))



# a = 10


# def my_fun():
#     b = 10
#     def wrapper():
        # global a
        # print(a)
        # a +=5
        # nonlocal b
        # print(b)
        # b+=5
        # print(b)
    # return wrapper()


# my_fun()
# print(a)