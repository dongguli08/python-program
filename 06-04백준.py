# a,b=map(int,input().split())
# a_list=list(map(int,input().split()))

# for i in a_list:
#     if i<b:
#          print(i, end=" ")


numbers=[ ]
for i in range(9):
    i=int(input())
    numbers.append(i)

print(max(numbers))
print(numbers.index(max(numbers))+1) 



