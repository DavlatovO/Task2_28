from contextlib import contextmanager

# class MyDataBase:
#     def __init__(self):
#         self.connection = False

#     def __enter__ (self):
#         self.connection = True
#         return self

#     def __exit__(self, error_type, error_body, traceback):
#         self.connection = False
#         if error_type:
#             print(error_type)
#             print(error_body)
#             print(traceback)

#     def do_sommething(self):
#         print('DB is working') 

# with MyDataBase() as db:
#     db.do_sommething()
                


# @contextmanager
# def my_context_manager(*args):
#     try:
#         print('Context manager started')
#         yield [1, 2, 3, 4, 5, 6]
#     except Exception as e:
#         print(f'An error occurred: {e}')
#     finally:
#         print('Context manager finished')

# # Using the context manager
# with my_context_manager() as cm:
#     print(cm)



# @contextmanager
# def add_to_list_manager(my_list, number):
#     try:
#         my_list.append(number)
#         yield my_list
#     except Exception as e:
#         print(f'Error occurred: {e}.')
#         my_list.clear()
#     finally:
#         print(f'Current list: {my_list}')
# my_list = [] 
# my_list2 = add_to_list_manager(my_list, result)



 
