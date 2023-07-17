num = int(input())

even_list = list(filter(lambda x: x % 2 == 0, range(1, num+1)))
print(sum(even_list))