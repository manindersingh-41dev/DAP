# f = open('test.txt')

# # for i in f.read(5):
# #     print(i)

# # for i in f.readline():
# #     print(i)

# # line = f.readline()
# # print(line)

# print(f.readlines())

# # print("\n\n")

# # for i in f.readlines():
# #     print(i)

# f.close()

with open("test.txt",'r') as f:
    print(f.readlines())
#     for i in f.readlines():
#         print(i)


# with open("new.txt", 'w') as f:
#     f.write("This is file")
#     f.write("This another line")