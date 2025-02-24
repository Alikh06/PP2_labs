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

# 8)
import os
path = input("Please input path of file: ")
if os.path.exists(path):
    os.remove(path)
else:
    print("Path isn't exists")