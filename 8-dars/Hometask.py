#1

# class Manager:
#     def __init__(self):
#         self.data = []

#     def append(self, detail):
#         self.data.append(detail)

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type is not None:
#             print(f"An error occurred: {exc_type} - {exc_value}")
            
            
#             self.data.clear()


# with Manager() as appender:
#     try:
#         appender.append(23/0)
#         appender.append(0)
        
        
       

#     except Exception as e:
#         print(f"Error during process: {e}")





