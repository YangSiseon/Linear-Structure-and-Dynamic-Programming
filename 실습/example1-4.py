# def main():
#     numYearBase10 = 2011
#     numYearBase8 = 0o3733
#     numYearBase16 = 0x7DB

#     print("Year by base 10 : %d, by base 8 : %d, by base 16 : %d" %(numYearBase10, numYearBase8, numYearBase16))

#     numComplex1 = complex(3,4)
#     numComplex2 = 4+3j

#     print("complex value : ", numComplex1)
#     print("Absolute value : ", abs(numComplex2))
#     print("Real value : ", numComplex2.real)
#     print("Image value : ", numComplex2.imag)

#     strDeptName = "Industrial & Systems Engineering"
#     strUnivName = "KAIST"
#     print("Department : ", strDeptName)
#     print("Full name or dept : ", (strDeptName+", "+strUnivName))

# main()

def main():
    numTest1 = 10
    numTest2 = 3.0
    numPlus = numTest1 + numTest2
    numMinus = numTest1 - numTest2
    numMultiply = numTest1 * numTest2
    numDivide = numTest1 / numTest2
    numModulo = numTest1 % numTest2
    print("{0}, {1}, {2}, {3}, {4}".format(numPlus, numMinus, numMultiply, numDivide, numModulo))
    
    numDivideInt = numTest1 / int(numTest2)
    print(numDivide, numDivideInt) # in python3 동일한 값이 출력됨
    # integer output을 얻기 위해서는 / 대신에 // 를 사용한다.

    numTest2, numTest1 = numTest1, numTest2 # swapping statement
    print(numTest1,numTest2)

    print(numTest1 == numTest2)
    print(numTest1 != numTest2)
    print(type(numTest1))

    numTest1 = str(numTest1)
    print(type(numTest1), numTest1)

    strformula = "2011 / 7"
    print(eval(strformula))

main()