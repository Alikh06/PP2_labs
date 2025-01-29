# #function1
# # 1)
# def to_ounces(grams):
#     ounces = 28.3495231 * grams
#     print(ounces)
# grams = float(input())
# to_ounces(grams)

# # 2)
# def conversion_to_C(F):
#     C = (5 / 9) * (F - 32)
#     print(f"{F}F = {C}C")
# F = float(input())
# conversion_to_C(F)

# # 3)
# def solve(numheads, numlegs):
#     chicken = int((4 * numheads - numlegs) / 2)
#     rabbit  = int(numheads - chicken)
#     print(f"chickens = {chicken}, rabbits = {rabbit}")
# numheads = 35
# numlegs = 94
# solve(numheads, numlegs)

# # 4)
# def find_prime_num(numbers):
#     for i in numbers:
#         if(i > 1):
#             flag = False
#             for j in range(2, i - 1):
#                 if (i % j) == 0:
#                     flag = True
#                     break
#             if not flag:
#                 print(f"Prime number = {i}")

# n = int(input())
# numbers = [n]
# for i in range(n):
#     numbers.append(int(input()))
# find_prime_num(numbers)

# # 5)
# from itertools import permutations

# def print_permutations(input_string):
#     perms = permutations(input_string)
#     for perm in perms:
#         print(''.join(perm))

# user_input = input("Input the string: ")
# print_permutations(user_input)

# 6)
def reverse_words(text):
    words = text.split(" ")
    words.reverse()
    reversed_str = " ".join(words)
    print(reversed_str)

text = input("Input the string: ")
reverse_words(text)

# 7)
