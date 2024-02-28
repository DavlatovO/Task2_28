import time

# def check_admin(func):
#     def wrapper(*args, **kwargs):
#         if 10==10:
#             func(*args, **kwargs)
#         else:
#             print("Xatolik decorator validatsiya bilan yuz berdi")
#     return wrapper

#1
# def check_age(func):
#     def wrapper(*args, **kwargs):
#         age = int(input('Yoshingizni kiriting:'))
        
#         if age >= 18:
#             nationality = input("Fuqaroligingizni kiriting:").lower()
            
#             if nationality == "o'zbek":
             
        
#              return func(*args, **kwargs)
    
#     return wrapper

# #2
# def check_age(func):
#     def wrapper(*args, **kwargs):
#         age = int(input('Yoshingizni kiriting:'))
        
#         if age >= 18:
#             nationality = input("Fuqaroligingizni kiriting:").lower()
            
#             if nationality == "o'zbek":
#                 return func(*args, **kwargs)
#             else:
#                 raise ValueError('Not uzbek')
#         else:
#             raise ValueError('Kut')
    
#     return wrapper

#3
# import time

# def check_admin(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         stop = time.time()
#         print(f"Function started at: {start}")
#         print(f"Function stopped at: {stop}")
#         return result  
    
#     return wrapper

#3

# def check_time(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         stop = time.time()
#         print(f"Interval: {round(stop-start)}")
#         return result  
    
#     return wrapper

