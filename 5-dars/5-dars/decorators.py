import time



def chek_admin(func):
    def wrapper(*args, **kwargs):
        if 10 == 100:
            func(*args, **kwargs) # fun ishga tushdi
        else:
            print("Xatolik decorator validatsiyadan o'tkazmadi")
    return wrapper


def chek_sth(func):
    def wrapper(*args, **kwargs):
        if True:
            start = time.time()
            result =  func(*args, **kwargs)
            stop = time.time()
            print(f"Result {round(stop-start)}")
            if round(stop-start) < 5:
                return result
    return wrapper
