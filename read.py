data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        #print(len(data))
        if count % 1000 == 0: # %求餘數
print(len(data))