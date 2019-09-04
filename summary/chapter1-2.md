# Hello World in Python

```python
def main():
    print "Hello, world"
    print "This program computes the average of two exam scores"
    
    score1, score2 = input("Enter two scores separated by a comma")
    average = (score1 + score2) / 2.0
    print "The average of the scores is : ", average
    
main()
```

- Procedure-oriented program <--> Object-oriented

  > `main()` is a function
  >
  > Object-oriented --> class 

- Largely in two parts,

  > Definition part
  >
  > Execution part

- `def` : function declaration keyword

- `main` : function name

- `()` : undefined input parameter

- `:` : declaration of block

- python은 indentation을 통해 block을 지정한다.

-----

```python
class HelloWorld:
    def __init__(self):
        print "Hello World just one more time"
    def __del__(self):
        print "Good bye"
    def performAverage(self,val1,val2):
        average = (val1 + val2) / 2.0
        print "The average of the scores is : ", average

def main():
    world = HelloWorld()
    score1, score2 = input("Enter two scores separated by a comma: ")
    world.performAverage(score1,score2)
    
main()
```

- Object-oriented program

  > `HelloWorld` is an object
  >
  > `__init__`, `__del__`, and `performAverage` are methods

- Largely in two parts

  > Definition part
  >
  > Execution part

- `class` : class declaration keyword

- `HelloWorld` : class name

- `self` : 자기자신을 의미, method 선언시 필요, instance명이 들어가게됨

- `:` : declaration of block

- `__init__` : instance가 생성될 때 실행

- `__del__` : instance가 없어질 때 실행

- `world` : instance storage variable

- `HelloWorld` : instance template

