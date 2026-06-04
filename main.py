import array as arr
a=arr.array('i',[1,2,3,1,4,5,1,6,7,1,1])
count_1=0
max_count=0
for i in range(len(a)):
    if a[i]==1:
        count_1+=1
        max_count=max(max_count,count_1)
    else:
        count_1=0
print(count_1)