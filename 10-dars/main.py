import threading
import multiprocessing

import time

# return_datas = []
 
# def salom_ber(num):
#     print(f"Assalomu alaykum{num}")
#     global return_datas
#     return_datas.append({salom_ber.__name__:10})

# datas = []

# if __name__ == "__main__":
#    for  i  in range(10):
    
#     protcess = multiprocessing.Process(target = salom_ber, args=(i,))
#     protcess.start()
#     datas.append(protcess)
#    for i in datas:
#     i.join()
#    print(return_datas)      

# data_collection = []




# return_datas = []

# def salom_ber(num):
#     start_time = time.time()
#     print(f"Assalomu alaykum {num}")

#     stop_time = time.time()
#     execution_time = stop_time - start_time

#     global return_datas
#     return_datas.append({f"{salom_ber.__name__}_{num}": execution_time})

# if __name__ == "__main__":
#     processes = []

#     for i in range(10):
#         process = multiprocessing.Process(target=salom_ber, args=(i,))
#         process.start()
#         processes.append(process)

#     for process in processes:
#         process.join()

#     print(return_datas)








    
