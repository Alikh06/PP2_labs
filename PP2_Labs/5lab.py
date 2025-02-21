# RegEx
# # 1)
# import re
# def checking(text):
#     pattern = r"^a?b*0*"
#     if re.fullmatch(pattern, text):
#         return True
#     else:
#         return False
# text = {"a", "ab", "a0", "abd", "asb", "abb", "abbb0", "a000", "abbbb"}
# for i in text:
#     print(f"{i}: {checking(i)}")

# # 2)
# import re
# def checking(text):
#     pattern = r"ab{2,3}"
#     res = re.search(pattern, text)
#     print(res)
#     if res:
#         return True
#     else:
#         return False
# text = {"assdabb", "abbb", "dsabbb", "dsabbbb", "dsabbbds"}
# for i in text:
#     print(f"{i}: {checking(i)}")

# # 3)
# import re
# def checking(text):
#     pattern = r"[a-z]+_[a-z]+"
#     if re.search(pattern, text):
#         return True
#     else:
#         return False
# text = {"hello_world", "test_case", "valid_string", "Invalid_String", "no_underscore", "_underscore"}
# for i in text:
#     print(f"{i}: {checking(i)}")

# # 4)
# import re
# def checking(text):
#     pattern = r"[A-Z][a-z]+"
#     if re.search(pattern, text):
#         return True
#     else:
#         return False
# text = {"hello_world", "test_case", "valid_string", "Invalid_String", "no_underscore", "_underscore"}
# for i in text:
#     print(f"{i}: {checking(i)}")

# # 5)
# import re
# def checking(text):
#     pattern = r"a[a-z]+b$"
#     if re.search(pattern, text):
#         return True
#     else:
#         return False
# text = {"acgcdycb", "dsabdchbdjb", "ssdakndashcbhbc"}
# for i in text:
#     print(f"{i}: {checking(i)}")

# # 6)
# import re
# def replace(text):
#     pattern = r"[ ,.]"
#     for i in text:
#         print(re.sub(pattern, ":", i))
        
# text = ["Hello,world.This is a test", "Python is fun, isn't it?", "Replace spaces, commas. And dots!"]
# replace(text)

# # 7)
# import re

# text_to_match = "some_snake_case"

# res = re.split(r'_', text_to_match)

# print(res)

# ans = ''

# for word in res:
#     ans += word.capitalize()

# res = ''
# res += ans[0].lower() + ans[1:]

# print(res)

# # 8)
# import re
# text = "helloJohnMyNameIsAlikhan"
# spl = re.findall(r'[A-Z][^A-Z]*', text)
# print(spl)

# # 9)
# import re 
# text = "helloJohnMyNameIsAlikhan"
# x = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
# print(x)

# 10)
import re 
text = "someCamelCase"
res = re.sub(r'([a-z])([A-Z])', r'\1_\2', text)
des = re.split(r'_', res)
x = ''
for i in des:
    if i == des[-1]:
        x += i.lower()
        break
    else: 
        x += i.lower() + "_"
print(x)