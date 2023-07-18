column = int(input(), 16)
mul = 1


while mul < 16:
    column_hex = hex(column)[2:].upper()
    mul_hex = hex(mul)[2:].upper()
    answer = column * mul
    answer_hex = hex(answer)[2:].upper()
    print(column_hex, '*', mul_hex, '=', answer_hex, sep='')
    mul += 1