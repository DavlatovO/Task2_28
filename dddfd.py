# class WeekDay:
#     days = [1,2,3,4,5,6,7]
#     count = 0

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.count < len(self.days):
#             result = self.days[self.count]
#             self.count +=1
#             return result
#         raise StopIteration
    
# for i in WeekDay():
#     print(i)




from ewqewq import create_password
passwords = [create_password for _ in range(10)]
print(passwords)