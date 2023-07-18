w, h, b = map(int, input().split())

volumn = w * h * b
volumn_mb = volumn / 8 / 1024 / 1024

print(f'{volumn_mb:.2f}', 'MB')