# import time
# import threading


# def smth(a,b):
#     print('func boshlandi')
#     time.sleep(5)
#     print('Func tugadi')
#     print(a+b)

# thread_1 = threading.Thread(target=smth, kwargs={'a':10, 'b':10})    
# thread_2 = threading.Thread(target=smth, args=(11,11))    

# thread_1.start()  
# thread_2.start()

# thread_1.join()
# thread_2.join()


# print('Tasklar tugadi')
import requests

# URL of the image you want to download
image_url = "https://i.natgeofe.com/k/6d4021bf-832e-49f6-b898-27b7fcd7cbf7/eiffel-tower-ground-up_2x1.jpg"


response = requests.get(image_url)


if response.status_code == 200:
    
    with open("downloaded_image.jpg", "wb") as f:
        f.write(response.content)
    print("Image downloaded successfully.")
else:
    print(f"Failed to download image. Status code: {response.status_code}")
