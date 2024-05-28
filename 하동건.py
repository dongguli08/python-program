from itertools import combinations

a,b=map(int,input("숫자의 갯수와 합 입력:").split())
c=list(map(int,input("숫자%d개 입력:" %a).split()))
biggest_sum=0


for i in combinations(c,3):
        list_sum=sum(i)
        if biggest_sum<list_sum<=b:
         biggest_sum=list_sum
print(biggest_sum)


