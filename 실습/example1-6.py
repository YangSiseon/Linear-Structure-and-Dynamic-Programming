# strTest = "Hello world! ISE"
# print(strTest)
# print(strTest[1], strTest[2], strTest[3])
# print(strTest[1:3]) # from x to y
# print(strTest[3:])
# print(strTest[:3])
# print(strTest[1:9:2])  #from x to y with z steps
# print(strTest[1:len(strTest):2])
# print(strTest[1::2])
# print(strTest[5::-1])

# lstTest = [1,2,3,4]
# print(lstTest)
# print(lstTest[0], lstTest[1], lstTest[2])
# print(lstTest[-1], lstTest[-2])
# print(lstTest[1:3])
# print(lstTest+lstTest)
# print(lstTest*3)

# lstTest = list(range(1,20,3))
# # in python2 range return a list
# # in python3 range return a range object. The range object does not have an append method.
# print(lstTest)
# print(4 in lstTest, 100 in lstTest, lstTest.append('hey'))
# print(lstTest)
# del(lstTest[0])
# print(lstTest)
# lstTest.reverse()
# print(lstTest)
# lstTest.remove(4)
# print(lstTest)
# lstTest.sort()
# # It generate type-error but i don't know how to solve this...
# print(lstTest)

# tplTest = (1,2,3)
# print(tplTest)
# print(tplTest[0], tplTest[1], tplTest[2])
# print(tplTest[-1],tplTest[-2])
# print(tplTest[1:3])
# print(tplTest+tplTest)
# print(tplTest*3)

# tplTest[0] = 100

dicTest = {1:"one", 2:"two", 3:"three"}
print(dicTest[1])
dicTest[4] = "four"
print(dicTest)
print(dicTest.keys())
print(dicTest.values())
print(dicTest.items())
