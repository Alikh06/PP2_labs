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

# # 6)
# def reverse_words(text):
#     words = text.split(" ")
#     words.reverse()
#     reversed_str = " ".join(words)
#     print(reversed_str)

# text = input("Input the string: ")
# reverse_words(text)

# # 7)
# def has_33(nums, n):
#     for i in range(n - 1):
#         its = False
#         if(nums[i] == 3 and nums[i+1] == 3):
#             its = True
#             break
#         else:
#             its = False
#     if(its):
#         print("True")
#     else:
#         print("False")

# n = int(input("How many symbols we are have: "))
# nums = []
# for x in range(n):
#     i = int(input())
#     nums.append(i)
# has_33(nums, n)

# # 8)
# def spy_game(nums, n):
#     new_list = []
#     our_list = [0, 0, 7]
#     for i in range(n):
#         if(nums[i] == 0):
#             new_list.append(nums[i])
#         if(nums[i] == 7):
#             new_list.append(nums[i])
#     if(new_list == our_list):
#         print("True")
#     else:
#         print("False")

# n = int(input("How many symbols we are have: "))
# nums = []
# for x in range(n):
#     i = int(input())
#     nums.append(i)
# spy_game(nums, n)

# # 9)
# import math 
# def v_of_sphere(r):
#     v = float((4/3) * math.pi * math.pow(r, 3))
#     print(f"Volume of sphere = {v}")
# r = int(input("Radius of sphere: "))
# v_of_sphere(r)

# # 10)
# def unique_elements(input_list):
#     unique_list = []
#     for element in input_list:
#         if element not in unique_list:
#             unique_list.append(element)
#     return unique_list

# input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
# result = unique_elements(input_list)
# print(result)

# # 11)
# def is_palindrome(s):
#     s = ''.join(char.lower() for char in s if char.isalnum())
#     return s == s[::-1]

# print(is_palindrome("madam"))
# print(is_palindrome("hello"))

# # 12)
# def histogram(nums):
#     a = ""
#     for i in nums:
#         for j in range(i):
#             a += '*'
#         print(a)
#         a = ""

# n = int(input("How many symbols we are have: "))
# nums = []
# for x in range(n):
#     i = int(input())
#     nums.append(i)
# histogram(nums)

# # 13)
# from random import randint
# def guess(num, name):
#     count = 0
#     print(f"Well, {name}, I am thinking of a number between 1 and 20.")
#     num_input = 0
#     while num_input != num:
#         count += 1
#         print('Take a guess.')
#         num_input = int(input())
#         if(num_input < num):
#             print('Your guess is too low.')
#         if(num_input > num):
#             print("Your guess is too more.")
#         if(num_input == num):
#             print(f"Good job, {name}! You guessed my number in {count} guesses!")
# num = randint(1, 20)
# print("Hello what is your name? ")
# name = input()
# guess(num, name)


# #function2
# movies = [
# {
# "name": "Usual Suspects", 
# "imdb": 7.0,
# "category": "Thriller"
# },
# {
# "name": "Hitman",
# "imdb": 6.3,
# "category": "Action"
# },
# {
# "name": "Dark Knight",
# "imdb": 9.0,
# "category": "Adventure"
# },
# {
# "name": "The Help",
# "imdb": 8.0,
# "category": "Drama"
# },
# {
# "name": "The Choice",
# "imdb": 6.2,
# "category": "Romance"
# },
# {
# "name": "Colonia",
# "imdb": 7.4,
# "category": "Romance"
# },
# {
# "name": "Love",
# "imdb": 6.0,
# "category": "Romance"
# },
# {
# "name": "Bride Wars",
# "imdb": 5.4,
# "category": "Romance"
# },
# {
# "name": "AlphaJet",
# "imdb": 3.2,
# "category": "War"
# },
# {
# "name": "Ringing Crime",
# "imdb": 4.0,
# "category": "Crime"
# },
# {
# "name": "Joking muck",
# "imdb": 7.2,
# "category": "Comedy"
# },
# {
# "name": "What is the name",
# "imdb": 9.2,
# "category": "Suspense"
# },
# {
# "name": "Detective",
# "imdb": 7.0,
# "category": "Suspense"
# },
# {
# "name": "Exam",
# "imdb": 4.2,
# "category": "Thriller"
# },
# {
# "name": "We Two",
# "imdb": 7.2,
# "category": "Romance"
# }
# ]

# # 1)
# def is_above_5_5(movie):
#     return movie["imdb"] > 5.5
# print(is_above_5_5(movies[0]))

# # 2)
# def get_high_rated_movies(movies):
#     return [movie for movie in movies if is_above_5_5(movie)]
# print(get_high_rated_movies(movies))

# # 3)
# def get_movies_by_category(movies, category):
#     return [movie for movie in movies if movie["category"].lower() == category.lower()]
# print(get_movies_by_category(movies, "Romance"))

# # 4)
# def average_imdb_score(movies):
#     return sum(movie["imdb"] for movie in movies) / len(movies)
# print(average_imdb_score(movies))

# # 5)
# def average_imdb_by_category(movies, category):
#     category_movies = get_movies_by_category(movies, category)
#     return average_imdb_score(category_movies)
# print(average_imdb_by_category(movies, "Romance"))



# classes

# # 1)
# class two_func():
#     def getString(self, name, age):
#         self.name = name
#         self.age = age
#     def printString(slef):
#         return f"My name is {name}, and I'm {age}"

# c1 = two_func()
# name = input()
# age = int(input())
# c1.getString(name, age)
# print(c1.printString())

# # 2)
# class Shape:
#     def area(self):
#         return 0


# class Square(Shape):
#     def __init__(self, length):
#         self.length = length

#     def area(self):
#         return self.length ** 2

# shape = Shape()
# print("Area of Shape:", shape.area())
# square = Square(5)
# print("Area of Square:", square.area())

# # 3)
# class Rectangle(Shape):
#     def __init__(self, length, weigth):
#         self.length = length
#         self.weigth = weigth
#     def area(self):
#         return self.length * self.weigth

# c2 = Rectangle(2, 5)
# print(c2.area())

# # 4)
# import math
# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def show(self):
#         return f"x = {self.x}, y = {self.y}"
    
#     def move(self1, new_x, new_y):
#         self1.x = new_x
#         self1.y = new_y
    
#     def dist(self, self1):
#         return math.sqrt((self.x - self1.x) ** 2 + (self.y - self1.y) ** 2)

# point1 = Point(2, 3)
# point2 = Point(5, 7)
# print(f"coordinate of point1: {point1.show()}")
# print(f"coordinate of point2: {point2.show()}")
# point1.move(8, 10)
# distance = point1.dist(point2)
# print(f"distance of two points = {distance}")

# # 5)
# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited ${amount}. New balance: ${self.balance}")
#     def withdraw(self, amount):
#         if amount > 0:
#             if amount <= self.balance:
#                 self.balance -= amount
#                 print(f"Withdrew ${amount}. New balance: ${self.balance}")
#     def __str__(self):
#         return f"Account owner: {self.owner}, Our balance = ${self.balance}"
# c5 = Account("Alikhan", 0)
# c5.deposit(47000)
# c5.withdraw(14800)
# c5.deposit(10000)
# c5.withdraw(15000)
# print(c5)

# 6)
import math
def isp(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n > 2:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0: return False
            else: return True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

prime_numbers = list(filter(lambda x: isp(x), numbers))
print(prime_numbers)
