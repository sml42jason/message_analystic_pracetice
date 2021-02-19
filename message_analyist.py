data = []
count = 0
with open ('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('Reading finish, total : ', len(data))

sum_len = 0
for a in data:
    sum_len = sum_len + len(a)

print('avg is ', sum_len/len(a), '.')

new = []
for m in data:
    if len(m) < 100:
        new.append(m)
print(len(new), 'message < 100')
