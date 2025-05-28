# 1

li = [10,501,22,37,100,999,87,351]
ev=[]
od=[]
for i in range(len(li)):
    if li[i]%2==0:
        ev.append(li[i])
    else:
        od.append(li[i])
        
print(ev)
print(od)


# 2

li = [10,501,22,37,100,999,87,351,11]
ne = []
count = 0
for i in li:
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        ne.append(i)
        count = count + 1
print(ne)
print(count)

# 6

lis1 = [1,3,5,7,9]
lis2 = [2,3,9,6,8]
lis3 = [4,6,9,3,1]

duplicates = set(lis1) & set(lis2) & set(lis3)
print(duplicates)


# 4

a = input()
print(int(a[0]) + int(a[-1]))


# 10
nums = [4, 2, -3, 1, 6]
n = len(nums)
found = False
for i in range(n):
    current_sum = 0
    for j in range(i, n):
        current_sum += nums[j]
        if current_sum == 0:
            print(nums[i:j+1])
            found = True
            break
    if found:
        break

# 8
sorted_list1 = [1, 2, 3, 4, 5]
print(sorted_list1[0])


# 3
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
su = 0
for i in numbers:
    seen = set()
    n = i
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(j) ** 2 for j in str(n))
        print(i,n)
    if n == 1:
        su += 1
print(su)



# 9
lis = [10,20,30,9]
num = 59
for i in range(len(lis)):
    if num == sum(lis[i:i+3]):
        print(lis[i:i+3])



# 7

li = [1,3,3,6,5,8,1,4,7]
ne = []
for i in li:
    if li.count(i) == 1:
        ne.append(i)
print(ne)
        




     



