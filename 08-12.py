# numbers = []
# for i in range(4):
#     # 사용자로부터 입력받고 정수로 변환
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# # 모든 숫자를 입력받은 후 출력
# print(numbers)


n,m=map(int,input().split())

basket = [i for i in range(1,n+1)]

for i in range(m):
    i,j=map(int,input().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp
   
print(' '.join(map(str,basket)))

