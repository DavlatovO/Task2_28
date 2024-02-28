# class WeekDay:
#     days = [1,2,3,4,5,6,7]
#     count = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#        if self.count < len(self.days):
#          result = self.days[self.count]
#          self.count += 1
#          return result
#        raise StopIteration

# for i in WeekDay():
#     print(i)


# class User:
#     users = []
#     count = 0

#     def __init__(self, user, password):
#         self.user = user
#         self.password = password
#         self.users.append(self)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.count < len(self.users):  
#             result = self.users[self.count]
#             self.count +=1 
#             return result
#         raise StopIteration

# User('ahmadillo', 'verz12e')
# User('siuuu', '12313hfs')


# for i in User('d','d'):
#     print(i)


class User:
    users = []
    count = 0

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.users.append(self)

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < len(self.users):  
            result = self.users[self.count]
            self.count +=1 
            return result
        raise StopIteration

a = User('ahmadillos', 'verz12e')
b = User('siuuu', '12313hfs')
c = User('Sasdsfasf', 'dwd2312')


result = filter(lambda x:len(x.user)>8, User('as',))
print(result)



    