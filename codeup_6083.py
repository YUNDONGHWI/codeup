r, g, b = map(int,input().split())
count = 0

for r_ in range(r):
    for g_ in range(g):
        for b_ in range(b):
            print (f'{r_} {g_} {b_}')
            count += 1
print(count)