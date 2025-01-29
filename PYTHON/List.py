numbers = [4, 5, True, "Hello", 1.05]
print(numbers)

numbers[3] = 0

numbers.append(100)
print(numbers)

numbers.insert(1, False)
print(numbers)

numbers.extend([1, 2, 3])
print(numbers)

b = [4, 5, 6]
numbers.extend(b)
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers.pop()
print(numbers)

numbers.pop(0)
print(numbers)

numbers.remove(0)
print(numbers)

print(numbers.count(5))
print(len(numbers))
print(numbers.clear())

n = int(input())
user_list = []
i = 0
while i < n:
    user_list.append(input())
    i += 1
print(user_list)    