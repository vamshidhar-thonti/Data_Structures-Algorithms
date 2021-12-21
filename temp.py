# def one(a, b=None):
#     print(a, b)

# def two(a=None, b=None):
#     print(a, b)

# print(two(5, 7))

# elem = [2, 3, 3, 2, 4, 3]
# window_size = 3

# output = [] 
# #2,3,3 -> 2
# #3, 3, 2 -> 2

# pointer = 0
# val = []
# loop = 1
# while (loop <= 4):

#     output.append(len(set(elem[pointer:pointer+window_size])))

#     # for i in range(pointer, pointer+window_size):
#     #     val.append(elem[i])
#     #     vals = list(set(val))

#     # count = 0
#     # for v in vals:
#     #     count += 1

#     loop += 1
#     pointer += 1
#     # output.append(count)

# print(output)
from datetime import datetime

# def time_dec(X):
#     def func():
#         print(datetime.now())
#     return func

# @time_dec
# def hello():
#     print("Hello")

dict_1 = {
    "a": 1,
    "b": 2,
}

temp = dict_1["a"]
del dict_1["a"]
dict_1["c"] = temp
print(dict_1)
# print("New")
