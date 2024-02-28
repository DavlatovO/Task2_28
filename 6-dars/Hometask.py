#1
# class WeekDays:
    
#     days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#     def __init__(self):
#         self.index = 0

#     def __iter__(self):
#         return self  

#     def __next__(self):
#         if self.index < len(self.days):
#             day = self.days[self.index]
#             self.index += 1
#             return day
#         else: 
#             raise StopIteration('amal yakunlandi')


# week_days = WeekDays()

# for day in week_days:
#     print(day)

#2
# months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# class Months():
    
#     def __init__(self, months_list):
#         self.months_list = months_list
#         self.index = 0

#     def __iter__(self):
#         return self  

#     def __next__(self):
#         if self.index < len(self.months_list):
#             month = self.months_list[self.index]
#             self.index += 1
#             return month
#         else: 
#             raise StopIteration('amal yakunlandi')

# print_months = Months(months_list)

# for month in print_months:
#     print(month)

#3
 
# class User():
#     users = []
#     count = 0

#     def __init__(self, f_name, l_name, email):
#         self.f_name = f_name
#         self.l_name = l_name
#         self.email = email
#         self.users.append(self)

#     def __iter__(self):
#         return self 

#     def __next__(self):
#         if self.count<len(self.users):
#             result = self.users[self.count]
#             self.count +=1
#             return result
#         raise StopIteration
    
# user1 = User('Ahmad', 'Ergashev', 'paxan012@gmail.com')
# user2 = User('Jony', 'Smith', 'Jonsmith12@gmail.com')
# user3 = User('Bahodir', 'Johnson', 'bob.johnson@gmail.com')

# for i in User('Cristiano', 'Messi', 'messiiiiuuu@gmail.com'):
#     print(i)


