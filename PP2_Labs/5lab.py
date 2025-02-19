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

# 7)
import re

def toCamelCase(text):
    pattern = r"_\w+"
    x = str(re.findall(pattern, text))
    for i in range(len(x) - 1):
        if x[i] == "_":
            x[i].removeprefix()
            x[i+1].upper()
            return x
text = {"hello_world", "hi_john"}
for i in text:
    print(toCamelCase(i))