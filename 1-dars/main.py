# 1
# def index(data:str):
#     split_data = data.split()
#     l_w = split_data[-1]  
#     length = len(l_w)
#     return l_w, length        
              
# result = index('Ronaldo said Siuuuu')
# print(result)    

#2
# def index(data:str):
#     split_data = data.split()
#     length = len(split_data)
#     return length
    
             
              
# result = index('Ronaldo said Siuuuu')
# print(result) 

#3
# new_list = ['Ronny', 'Siuuu', 'hehehe', 'Iyaa']

# def reverse_word(word_list):
#     result_list = []
#     for index, word in enumerate(word_list):
#         if index % 2 == 1:  
#             result_list.append(word[::-1])
#         else:
#             result_list.append(word)
#     return result_list

# result = reverse_word(new_list)
# print(result)

#4
# def index(data:str)-> bool:
#     ss =''.join(data.split())
#     return ss == ss[::-1]

    
             
              
# result = index('on no')
# print(result) 

#5
# def only_stnu(input_info):
#     result = ''.join(i for i in input_info if i.isalnum())
#     return result

# input_str = " C*risti&no Ro)na&ldo Si!!!iiiuuu"
# result_str = only_stnu(input_str)
# print(result_str)