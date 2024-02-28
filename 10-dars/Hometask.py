#2

# def index():
#     presses_needed = {} 
#     numbers = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
#     word = input("So'z kiriting:")
#     word = word.lower()  #
#     for i in word:
#         for keys,values in numbers.items():
#             if(i in values):
#                 if keys in presses_needed:
#                     presses_needed[keys] += values.index(i) + 1
#                 else:
#                     presses_needed[keys] = values.index(i) + 1
#     print(presses_needed)

# index()

#3

# def html_tags(html_text):
#     inside_tag = False
#     result = ""
    
#     for char in html_text:
#         if char == "<":
#             inside_tag = True
#         elif char == ">":
#             inside_tag = False
#         elif not inside_tag:
#             result += char

#     return result.strip()

# html_text = "<h1>Salom<b> yaxshimisan? </b></h1>"
# result = html_tags(html_text)
# print(result)

#4

# numbers = [64, 34, 25, 12, 22, 11, 90]
# def selection_sort(num):
#     n = len(num)
    
#     for i in range(n):
#         min_num = i
#         for j in range(i+1, n):
#             if num[j] < num[min_num]:
#                 min_num = j
        
#         num[i], num[min_num] = num[min_num], num[i]
    
#     return num

# sorted_numbers = selection_sort(numbers)
# print("Sorted numbers:", sorted_numbers)

#5

# list = [12, 9, 6, 3]

# def pattern(num):
#     length = len(num)
    
#     for i in range(length-2):
#         if num[i] - num[i+1] != num[i+1] - num[i+2]:
#             return "Pattern is broken"
        
    
#     return "Pattern is not broken"

# print(pattern(list))

#6

# def index(word):
#     vowels = 'AEIOUaeuio'
#     vowel_count = 0
#     for i in word:
#         if (i in vowels):
#             vowel_count +=1
#     return f"Bo'g'inlar soni:{vowel_count}ta"

# result = index(input("So'zni kiriting:"))
# print(result)   

#7

# def is_prime(num):
#     if num <= 1:
#         return False
#     if num == 2:
#         return True
#     if num % 2 == 0:
#         return False
#     #Matematik formuladan foydalanamiz:
#     for i in range(3, int(num ** 0.5) + 1, 2):
#         if num % i == 0:
#             return False
#     return True

# def primes_until(num):
#     for i in range(2, num+1):
#         if is_prime(i):
#             print(i)

# number = 81
# primes_until(number)

#8

# list = [2,3,4,52,34]
# def index(num):
#     max_n = max(list)
#     for i in range(max_n):
#         if(i not in list):
#             print(i)

# result = index(list)
# print(result)

#9

# def index(number):
#     number = str(number)
#     f_numbers = {"1": "O'n", "2": "Yigirma", "3": "O'ttiz", "4": "Qirq", "5": "Ellik", "6": "Oltmish", "7": "Yetmish",
#                  "8": "Sakson", "9": "To'qson"}
#     s_numbers = {"1": "bir", "2": "ikki", "3": "uch", "4": "to'rt", "5": "besh", "6": "olti", "7": "yetti", "8": "sakkiz",
#                  "9": "to'qqiz"}

#     if int(number) > 9:
#         for keys, values in f_numbers.items():
#             if number[0] == keys:
#                 first_one = values
#                 for keys2, values2 in s_numbers.items():
#                     if number[1] == keys2:
#                         second_one = values2
#                         return f"{first_one} {second_one}"  
#     else:
#         for keys2, values2 in s_numbers.items():
#             if number == keys2:
#                 return values2

# result = index(5)
# print(result)

# #10

# def express_as_sum_of_numbers(number):
#     actual_number = number
#     coins = [16, 9, 4, 1]
#     result = []

#     for coin in coins:
#         count = number // coin
#         number -= count * coin
#         if count > 0:
#             result.append(f"{count}*{coin}")

#     return f"{actual_number} is equal to {'+'.join(result)}"

# result = express_as_sum_of_numbers(45)
# print(result)








   






























