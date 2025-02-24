#dir-and-files
# # 1)
# import os
# path = input("Please input path of file: ") #C:\Users\Victus\Desktop\Ali\PP1
# only_directories = []
# only_files = []
# all_files_directories = os.listdir(path)
# for i in all_files_directories:
#     if os.path.isdir(i):
#         only_directories.append(i)
#     else:
#         only_files.append(i)
# print(f"Only directories: {only_directories}")
# print(f"only files: {only_files}")

# # 2)
# import os
# path = input("Please input path of file: ") #C:\Users\Victus\Desktop\Ali\PP1\PP2_Labs\d.txt
# print(f"Existence: {os.path.exists(path)}")
# print(f"Readability: {os.access(path, os.R_OK)}")
# print(f"Writability: {os.access(path, os.W_OK)}")
# print(f"Executablity: {os.access(path, os.X_OK)}")

# # 3)
# import os
# path = input("Please input path of file: ") #C:\Users\Victus\Desktop\Ali\PP1\PP2_Labs\d.txt
# if os.path.exists(path):
#     print(f"File name: {os.path.basename(path)}")
#     print(f"Directory: {os.path.dirname(path)}")
# else:
#     print("This path don't exists")

# # 4)
# import os
# f = open("d.txt")
# countt = 0
# for i in f:
#     countt += 1
# print(countt)

# # 5)
# import os
# f = open("d.txt", "w")
# list = [1, 2, 3, 4]
# for i in list:
#     if i == list[0]:
#         f.write("[")
#     if i != list[-1]:
#         f.write(f"{str(i)}, ")
#     if i == list[-1]:
#         f.write(f"{str(i)}]")
# f.close()
# f = open("d.txt")
# print(f.read())

# # 6)
# import string
# for i in string.ascii_uppercase:
#     file = f"{i}.txt"
#     open(file, "x")

# # 7)
# file = open("d.txt")
# copy = open("copy.txt", "w")
# for i in file:
#     copy.write(i)

# # 8)
# import os
# path = input("Please input path of file: ")
# if os.path.exists(path):
#     os.remove(path)
# else:
#     print("Path isn't exists")

# # built-in-functions
# # 1)
# from functools import reduce
# def multiply(numbers):
#     result = reduce(lambda x, y: x*y, numbers)
#     return result
# numbers = [1, 2, 3, 4]
# print(f"Product of all num = {multiply(numbers)}")

# # 2)
# def count_case_letters(string):
#     upper_count = sum(1 for char in string if char.isupper())
#     lower_count = sum(1 for char in string if char.islower())
#     print(f"Upper case letters = {upper_count}")
#     print(f"Lower case letters = {lower_count}")
# string = "Hello World!"
# count_case_letters(string)

# # 3)
# def is_palindrome(string):
#     if "".join(reversed(string)) == string:
#         return True
#     else:
#         return False
# string = "kazak"
# print(is_palindrome(string))

# # 4)
# import time
# def square(n, m):
#     n_square = pow(n, 1/2)
#     m = float(m / 1000)
#     time.sleep(m)
#     return f"Square root of {n} after {int(m*1000)} miliseconds is {n_square}"
# n = 25100
# m = 2123
# print(square(n, m))

# 5)
def checking_true(tuple):
    our_list = list(tuple)
    b = False
    for i in our_list:
        if bool(i):
            b = True
        else: 
            b = False
            print("All el in our tuple is not true")
            return
    if b:
        print("All el in our tuple is true")
tuple = ("a", 1, "A", "B", 5, -1)
checking_true(tuple)