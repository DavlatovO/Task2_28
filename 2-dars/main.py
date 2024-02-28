# def index(data: str) -> list:
#     a = '('
#     b = ')'
    

#     for x, y in enumerate(data):
#         if y not in (a, b):
#             return False
#         else:
            
            

    

# result = index(input('Qavslarni kiriting:'))
# print(result)

# def index(data: str) -> bool:
#     balance = 0
#     a = '('
#     b = ')'
    

#     for i in data:
#         if i not in (a, b):
#             return False

#     for char in data:
#         if char == '(':
#             balance += 1
#         elif char == ')':
#             balance -= 1
           

        
#         if balance < 0:
#             return False

    
#     return balance == 0

# result = index(input('Qavslarni kiriting:'))
# print(result)

   


    
    

        





list1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, ]]

# def matrix(data):
    
#     if not all(len(sublist) == len(data[0]) for sublist in data):
#         raise ValueError("Sublists must have the same length")

#     new_list = []
#     columns = len(data)
#     col_numbers = len(data[0])


#     new_list.extend(data[0])

    
#     for row in data[1:-1]:
#         new_list.append(row[-1])

    
#     new_list.extend(data[-1][::-1])

    
#     for row in data[1:-1][::-1]:
#         new_list.append(row[0])

#     return new_list

# try:
#     result = matrix(list1)
#     print(','.join(map(str, result)))
# except ValueError as e:
#     print(f"Error: {e}")









