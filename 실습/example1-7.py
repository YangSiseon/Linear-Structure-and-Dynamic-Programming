# numScore = 91

# if numScore > 90:
#     print('A')

# if numScore > 90:
#     print('A')
# else:
#     print('Lower grade')

# if numScore > 90:
#     print('A')
# elif numScore > 80:
#     print('B')
# elif numScore > 70:
#     print('C')
# else:
#     print('D or F')

for itr in range(10):
    print(itr, end=" ")

sum = 0
for itr in range(1, 11):
    sum += itr
print(sum)

for itr in range(1, 100, 10):
    if itr == 51:
        continue
    else:
        print(itr, end=" ")

for itr in range(5):
    print(itr, end=" ")
else:
    print("'")
print("done")

for itr in range(5):
    if itr == 3:
        break
    print(itr, end=" ")
else:
    print("'")
print("done")
