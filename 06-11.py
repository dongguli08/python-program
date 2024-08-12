# str = input()

# for i in str:
#     if i.isupper() == True:
#         print(i.lower(), end="")
#     else:
#         print(i.upper(), end="") is upper는 대문자를 찾는 함수 islower은 소문자를 찾는 함수

# str = input()

# for i in str:
#     if i.islower() == True:
#         print(i.upper(), end="")
#     else:
#         print(i.lower(), end="")

# print('!@#$%^&*(\\\'\"<>?:;')

# a, b = map(int, input().strip().split(' '))
# c=a+b
# print(a,"+",b ,"=", c) 
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
    if n in students:
        students.remove(n)
    else:
        print("다시입력")

students.sort()

for student in students:
    print(student)
