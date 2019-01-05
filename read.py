data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        #print(len(data))
        if count % 1000 == 0: # %求餘數
            print(len(data))
print('檔案讀取完了，總共有', len(data), '比資料')

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
    print(sum_len)
print('留言的平均長度為', sum_len/len(data))

new = []
for d in data:  #d 字串 data清單
    if len(d) < 100:
        new.append(d)  #長度低於100裝入新的清單
print('一共有', len(new), '筆留言長度小於100')