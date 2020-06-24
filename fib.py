prev_num = 0
num = 1
limit = input("enter max value: ")
print(num)
while num + prev_num <= limit:
    num += prev_num
    print(num)
    prev_num = num - prev_num
    
