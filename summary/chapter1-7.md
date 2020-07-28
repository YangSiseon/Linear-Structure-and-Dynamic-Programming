# Condition and Loop Statement

## if

- __if__ Boolean:

  ​	Statement for __True__

  elif boolean:

  ​	Statement for __True__

  else:

  ​	Statement for __False__

```python
if numScore > 90:
    print('A')
    
numScore = 75
if numScore > 90:
    print('A')
else:
    print('Lower grade')
    
if numScore > 90:
    print('A')
elif numScore > 80:
    print('B')
elif numScore > 70:
    print('C')
else:
    print('D or F')
```

- Python does not have a switch-case statement
  - You will have to live with _ifs_
- Watch you indentations carefully because that is your block statements

---

## for

- A loop statement

- The most common loop statement in programming languages

  - __for__ _variable in sequence:_

    ​	_statement for loop_

    __else__:

    ​	when for-loop is finished without a break

```python
for itr in range(10):
    print(itr)
    
sum = 0
for itr in range(1,11):
    sum += itr
print(sum)

for itr in range(1,100,10):
    if itr == 51:
        continue
    else:
        print(itr)
        
for itr in range(5):
    print(itr)
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
```

- Some useful statement for loops
  - _continue_
  - _break_

