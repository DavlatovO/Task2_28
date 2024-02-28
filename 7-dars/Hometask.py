import funcs
#1
# def some_password(num):
#     count =0
#     while num>count:
#         count +=1
#         yield funcs.create_password()


# for i in some_password(21):
#     print(i)

#2
# inputs_number = int(input("Raqamni kiriting:"))
# def gen_numbers(num):
#     for i in range(num):
#         if i%2==0:
#             yield i 

# even_numbers = gen_numbers(inputs_number)
# for c in even_numbers:
#     print(c)

#3

# inputs_number = int(input("Raqamni kiriting:"))
# def gen_numbers(num):
#     i=0
#     while i<num-1:
#         i=i+1
#         if i%2!=0:
#             yield i 

# even_numbers = gen_numbers(inputs_number)
# for c in even_numbers:
#     print(c)

#4
     
# inputs_number = int(input("Raqamni kiriting:"))

# def gen_numbers(num):
#     i = 0
#     number_of_multipliers = 0
#     while i < num:
#         i += 1
#         if num % i == 0:
#             number_of_multipliers += 1
#     yield number_of_multipliers

# for c in gen_numbers(inputs_number):
#     if c==2:
#         print("Bu tub son")
#     else: 
#         print("Bu tub son emas")    





        