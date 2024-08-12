n = input()  # n은 입력을 받는 문자열
nums = input()  # nums도 입력을 받는 문자열
total = 0
for i in nums:  # nums 문자열의 각 문자에 대해 반복
    total += int(i)  # 각 문자를 정수로 변환하고 total에 더함
print(total)
