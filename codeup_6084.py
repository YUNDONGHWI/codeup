h, b, c, s = map(int, input().split())

volumn = h * b * c * s

volumn_mb = volumn / 8 / 1024 / 1024

print(f'{volumn_mb:.1f}', 'MB')