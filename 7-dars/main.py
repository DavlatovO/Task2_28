import funcs

# def my_gen():
#     yield 1
#     print('a')
#     yield 2
#     print('b')
#     yield 3
#     print('c')

# a = iter(my_gen())
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# passwords = [funcs.create_password() for _ in range(100000000)]
# passwords_gen = (funcs.create_password() for _ in range(1000000))

# for i, element in enumerate(passwords):
#     if i<10:
#         print(element)
#     else: break    
# for i, element in enumerate(passwords):
#     if i<10:
#         print(element)
#     else: break      
 


# def some_password(num):
#     count =0
#     while num>count:
#         count +=1
#         yield funcs.create_password()

# for i in some_password(21):
#     print(i)
        
# numbers_list = []

# with open('raqamlar.txt', 'r') as open_file:
#     read_file = open_file.read()
#     numbers = map(int, read_file.split())

#     for i in numbers:
#         if i % 2 == 0:
#             numbers_list.append(i)

# print(numbers_list)

open_f = open('raqamlar.txt', 'r')
read_f = open_f.read()
# numbers=[int(num) for num in read_f.split()]
numbers = (int(num) for num in read_f.split())
print(numbers)
      
              

