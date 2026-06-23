# n = int(input().strip())
    
# if (n%2!=0):
#     print("Weird")
# else:
#     if n in range(2,5):
#         print("Not Weird")
#     elif n in range(6,20):
#         print("Weird")
#     elif n>20:
#         print("Not Weird")


# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# out = [(i,j,k) for i in range(2) for j in range(2) for k in range(3) if i+j+k!=3]
# print(out)

# for i,j,k in (1,2,3):
#     print(f"{i}-{j}-{k}")



arr = map(int, input().split())
arr = sorted(arr,reverse=True)
for i in arr:
    print(i)



