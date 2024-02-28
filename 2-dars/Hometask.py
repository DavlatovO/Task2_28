
# list1 = [1, 3, 7, 9, 11]
# def interval(data:int):
#     largest_gap = 0
#     start_point = 0
#     end_point = 0


#     for i in range(len(data) - 1):
#      current_gap = data[i + 1] - data[i]
#      if current_gap > largest_gap:
#         largest_gap = current_gap
#         start_point = data[i]
#         end_point = data[i + 1]
#     return f"{largest_gap} is between {start_point} and {end_point}"   

# result = interval(list1)
# print(result)

#2
# list1 = [1, 3, 7, 9, 11]
# def interval(data:float):
#     smallest_gap = float('inf')
#     start_point = 0
#     end_point = 0


#     for i in range(len(data) - 1):
#      current_gap = data[i + 1] - data[i]
#      if current_gap < smallest_gap:
#         smallest_gap = current_gap
#         start_point = data[i]
#         end_point = data[i + 1]
#     return f"{smallest_gap} is between {start_point} and {end_point}"   

# result = interval(list1)
# print(result)

#3
# P2 = ['2','3','4', '-', '1']
# P1 = ['1', '1', '+', '2', '2']
# new_list = []
# result = 0
# operation = '+' 

# for i in P2:
#     if not i.isdigit():
#         if new_list:  
#             numbers = int(''.join(new_list))
#             if operation == '+':
#                 result += numbers
#             elif operation == '-':
#                 result -= numbers
#             new_list = [] 
#             operation = i  
#     else:
#         new_list.append(i)


# if new_list:
#     numbers = int(''.join(new_list))
#     if operation == '+':
#         result += numbers
#     elif operation == '-':
#         result -= numbers

# print(result)

#4
 
# def text(data:str):
#     data_s = data.split()
#     length = len(data_s)
    
#     for i in range(length-1):
#         reversed = data_s[::-1]
#         return reversed
       
    
# result = text('Ronaldo did Siuuu celebration last night')
# print(result)    

#5

# list1 = ['Shuhrat0', 'aka', 'dasd@gmail.com','adasd@', 'ahmad78@mail.ru', 'jambo11@yandex.ru']    
# def index(data:list):
#     new_list = []
#     symbol = '@'
#     for i in data:
#         if (i.endswith('.com') or i.endswith('.ru') and (symbol in i)):
#             new_list.append(i)
#     return new_list        


# result = index(list1)
# print(result)

#6
# num_people = int(input("How many people do you want to enter data for? "))
# new_list = []
# for i in range(num_people):
#     age = input('How old are you:')
#     date_of_birth = input("Type your born year:")
#     date_of_month = input("Type your born month:")
#     date_of_day = input("Type your born day:")


#     user_data = {

#     'age': age,
#     'date_of_birth': date_of_birth,
#     'date_of_month': date_of_month,
#     'date_of_day': date_of_day
# }
#     new_list.append(user_data)
# oldest_person = max(new_list, key=lambda x: x['age'])
# youngest_person = min(new_list, key=lambda x: x['age'])
# print(f"Oldest: {oldest_person}")
# print(f"Youngest: {youngest_person}")








