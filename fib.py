prev_num = 0
num = 1
print(num)
while num + prev_num <= 1000:
    num += prev_num
    print(num)
    prev_num = num - prev_num
    