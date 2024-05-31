# from itertools import combinations

# a,b=map(int,input("숫자의 갯수와 합 입력:").split())
# c=list(map(int,input("숫자%d개 입력:" %a).split()))
# biggest_sum=0


# for i in combinations(c,3):
#         list_sum=sum(i)
#         if biggest_sum<list_sum<=b:
#          biggest_sum=list_sum
# print(biggest_sum)

# while(True):
#     a,b=map(int,input().split())
#     if input == 0:
#         break
#     else:
#         print(a+b)

# a=list(map(int,input().split()))
# print(a)
# a.sort(reverse=False)
# print(a)

# n = int(input())
# a = []
# for _ in range(n):
#     number = int(input())
#     a.append(number)
# a.sort() 오름차순으로 정렬
# for number in a:
#     print(number)

# a = list(map(int,input().split()))
# print(a[0])

# a=list(input().split())
# print(a[0]+a[1])
# print(a[0:2])

# a,b=map(int,input().split())
# a_list=list(map(int,input().split()))
# for i in a_list:
#     if(i<b):
#         print(i ,end=" ")

# num=[i for i in range(1,31)]

# for i in range(28):
#     n=int(input())
#     num.remove(n)
#     num.sort()
#     for i in range(len(num)):
#         print(num[i])


students = [i for i in range(1, 31)]

for _ in range(28):
    n = int(input())
    students.remove(n)

students.sort()

for student in students:
    print(student)


