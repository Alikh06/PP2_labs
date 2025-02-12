# # generators
# # 1)
# def square_gen(presition):
#     n = 1
#     while True:
#         yield round(n**2, presition)
#         n += 1
# presition = 3
# gen = square_gen(presition)
# for i in range(10):
#     print(next(gen))

# # 2)
# def even_gen(n):
#     num = 0
#     while num <= n:
#         yield num
#         num += 2
# n = 100
# gen = even_gen(n)
# for i in range((n // 2) + 1):
#     print(next(gen), end=", " if i < n // 2 else "")

# # 3)
# def div(n):
#     num = 0
#     for num in range(n):
#         if num % 3 == 0 and num % 4 == 0:
#             yield num
# n = 100
# gen = div(n)
# for i in gen:
#     print(i)

# # 4)
# import math
# def squares(a, b):
#     for i in range(a, b):
#         yield math.sqrt(i)
# a = int(input())
# b = int(input())
# gen = squares(a, b)
# print(*gen, sep=", ")

# # 5)
# def all(n):
#     num = n
#     while num >= 0:
#         yield num
#         num -= 1
# n = int(input())
# gen = all(n)
# for i in gen:
#     print(i)

# # math
# # 1)
# import math

# def degree_to_radian(degree):
#     return round(degree * (math.pi / 180), 6)
# degree = 15
# radian = degree_to_radian(degree)
# print(f"Input degree: {degree}")
# print(f"Output radian: {radian}")

# # 2)
# import math

# def trapezoid_area(height, base1, base2):
#     return 0.5 * (base1 + base2) * height

# height = 5
# base1 = 5
# base2 = 6
# area = trapezoid_area(height, base1, base2)
# print(area)

# # 3)
# import math

# def regular_polygon_area(sides, length):
#     return (sides * length ** 2) / (4 * math.tan(math.pi / sides))

# sides = 4
# length = 25
# area = regular_polygon_area(sides, length)
# print(f"The area of the polygon is: {area:.2f}")

# # 4)
# import math

# def parallelogram_area(base, height):
#     return base * height
# base = 5
# height = 6
# area = parallelogram_area(base, height)
# print(f"Expected Output: {area:.1f}")

# # date 
# # 1)
# from datetime import datetime, timedelta

# now_date = datetime.now()
# new_date = now_date - timedelta(days=5)
# print("Текущая дата:", now_date.strftime("%Y-%m-%d"))
# print("Дата 5 дней назад:", new_date.strftime("%Y-%m-%d"))

# # 2)
# from datetime import datetime, timedelta
# today = datetime.now()
# yesterday = today - timedelta(days=1)
# tomorrow = today + timedelta(days=1)

# print("Вчера: ", yesterday.strftime("%Y-%m-%d"))
# print("Сегодня: ", today.strftime("%Y-%m-%d"))
# print("Завтра: ", tomorrow.strftime("%Y-%m-%d"))

# # 3)
# from datetime import datetime, timedelta
# now = datetime.now()
# noww = now.replace(microsecond=0)
# print(noww)

# # 4)
# from datetime import datetime, timedelta
# current_datetime = datetime.now()
# past_datetime = current_datetime - timedelta(days=1)
# difference_in_seconds = (current_datetime - past_datetime).total_seconds()
# print("Текущая дата и время:", current_datetime)
# print("Дата и время 1 дней назад:", past_datetime)
# print("Разница в секундах:", difference_in_seconds)

# JSON
import json
with open(r'C:\Users\Victus\Desktop\Ali\PP1\sample-data.json') as file:
    data = json.load(file)
    
print("Interface Status")
print("=" * 73)
print(f"DN{' '* 45} Description{' ' * 7} Speed{' ' * 3} MTU{' ' * 6}")
print(f"{'-' * 45} {'-' * 20} {'-' * 6} {'-' * 6}")

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes["descr"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print(f"{dn} {' ' *19} {description} {' ' *1} {speed} {' '*1} {mtu} {' '*6}")