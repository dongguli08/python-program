#a,b,c=map(int,input().split())
#print(a+b+c)


#a = {'name': 'pey'}
#a[2]='나'#딕셔너리에 2라는 키 와 '나'라는 value선언
#a['lg']='무적'#== a={'neme':'pey', 2:'나', 'lg':'무적'}

#print(a['lg'])
#print(a.get('nokey', 'foo'))
#print('name' in a)
#print('email' in a)

#s2 = set("Hello")
#print(s2)

#a,b=input().split()
#print(int(a)+int(b))
#print(int(a)-int(b))
#print(int(a)*int(b))
#print(int(a)//int(b))
#print(int(a)%int(b))

#s1 = set([1, 2, 3])
#l1 = list(s1)
#print(l1)
#print(l1[0])

#t1 = tuple(s1)
#print(t1)
#print(t1[0])


#money =int (input())
#if money >= 3000:
     #print("택시를 타고 가라")
#else:
     #print("걸어가라")

# add = 0 
# for i in range(1, 11): 
#      add = add + i 
 
# print(add)


# for i in range(2,10):        # 1번 for문
#     for j in range(1, 10):   # 2번 for문
#           print(i*j, end=" ") 
#     print('') 

# add = 0 
# for i in range(1, 11): 
#      add = add + i 
 
# print(add)

# a=[   ]

# for i in range(9):#range9==1부터8까지 for문으로 하나씩 반복

#      a.append(i)#a에 append로 추가하다

#      print(a)

# marks3.py

# marks = [90, 25, 67, 45, 80]
# for number in range(len(marks)):
#     if marks[number] < 60: 
#         continue
#     print("%d번 학생 축하합니다. 합격입니다." % (number+1))

# for i in range(2,10):        # 1번 for문
#      for j in range(1, 10):   # 2번 for문
#          print(i*j, end=" 재민선배") 
#      print('') 


# def add(a, b):
#      return a+b#add함수를 지정 

# a = 3
# b = 4
# c = add(a, b)  # add(3, 4)의 리턴값을 c에 대입
# print(c)


# calculator.py
# result = 0

# def add(num):
#     global result
#     result += num  # 결괏값(result)에 입력값(num) 더하기
#     return result  # 결괏값 리턴

# print(add(3))
# print(result)
# print(add(4))

# a,b=map(int,input().split())
# print(a*b)

# a,b=map(int,input().split())
# print(a/b)

# a,b=map(int,input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)

# a=input()
# print(a+"??!")

# a=int(input())
# print(a-543)

# a,b,c=map(int,input().split())
# print((a+b)%c)
# print(((a%c)+(b%c))%c)
# print((a*b)%c)
# print(((a%c)*(b%c))%c)

# a,b=map(int,input().split()) 한줄로 입력받기
# print(a*(b%10))
# print(a*(b%100//10))
# print(a*(b//100))
# print(a*b)

# a,b=map(int,input().split())

# if a<b:
#     print("<")
 
# elif a>b:
#      print(">")
# else:
#      print("==")

# a=int(input())

# if a>=90 and a<=100:
#     print('A')
# elif a>=80 and a<=89:
#     print('B')
# elif a>=70 and a<79:
#     print('C')
# elif a>=60 and a<=69:
#     print('D')
# else:
#     print('F') 

# a =list(map(str,input().split()))
# print(a)

# a=int(input())
# if a%4==0 and a%100!=0 or a%400==0:
#     print('1')
# else:
#     print('0')
    

# n = int(input())

# for i in range(1,10):  # 1~9
#     print(n, '*', i, '=', n*i) 구구단


# a=int(input()) #a를 입력받고
# answer=0 #answer변수를 선언
# for i in range(1,a+1): #반복문을 돌려 1부터 a까지의 합을 구하기
#      answer+=i #answer에 i를 다 더한값을 대입
# print(answer)

# n = int(input())
# n_list = list(map(int, input().split())) #리스트의 n개의 갯수만큼 입력받기
# v = int(input())

# print(n_list.count(v))


# n, a = map(int, input().split()) #리스트에 받을 갯수와 비교할 숫자 대입
# n_list = list(map(int, input().split()))

# for i in n_list:
#     if i < a:
#         print(i, end=" ")


# a,b=map(int,input().split())
# a_list=list(map(int,input().split()))

# for i in range(a):
#     if a_list[i]<b:
#         print(a_list[i],end=" ")

# a=int(input())
# a_list=list(map(int,input().split()))
# b=int(input())

# print(a_list.count(b)) 백준10807

# a,b=map(int,input().split())
# a_list=list(map(int,input().split()))
# for i in a_list:
#     if i<b:
#         print(i,end=" ")

# a=int(input())
# a_list=list(map(int,input().split()))
# max=a_list[0]
# min=a_list[0]
# for i in a_list:
#      if i>max:
#           max=i
#      elif i<min:
#           min=i

# print(min,max)

        

# numbers=[ ]
# for i in range(9):
#     i=int(input())
#     numbers.append(i)

# print(max(numbers))
# print(numbers.index(max(numbers))+1)


grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])

lgtwins = {'홍창기':51 , '문성주':8}
print(lgtwins['문성주'])

아이스크림 = ['동건','효현','재민']
print(아이스크림[0:2])