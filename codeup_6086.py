num = int(input())
sum_ = 0
count = 1
while True :
  sum_ += count
  count += 1
  if sum_>=num :
    break

print(sum_)