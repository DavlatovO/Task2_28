# import threading
# import os

# def count_vowels(file_path):
#     vowels = "aeiouAEIOU"
#     with open(file_path, 'r') as file:
#         content = file.read()
#         vowel_count = sum(1 for i in content if i in vowels)
#         print(f"File: {file_path}, Number vowels: {vowel_count}")

# def main():
#     script_path = os.path.dirname(os.path.abspath(__file__))

#     text_files = [file for file in os.listdir(script_path) if file.endswith('.txt')]

    
#     threads = []
#     for file in text_files:
#         file_path = os.path.join(script_path, file)
#         thread = threading.Thread(target=count_vowels, args=(file_path,))
#         thread.start()
#         threads.append(thread)

  
#     for thread in threads:
#         thread.join()

# main()

