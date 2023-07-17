num = int(input())
num_sum = 1
i = 1
while num_sum <= num:
    num_sum = num_sum + i
    i = i + 1
else:
    print(i-1)