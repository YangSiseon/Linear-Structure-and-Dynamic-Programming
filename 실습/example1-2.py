def main():
    print("Hello, world")
    print("This program computes the average of two exam scores")
    # split method 를 이용해서 ,를 기준으로 분리
    score1, score2 = input("Enter two scores separated by a comma: ").split(",")
    # int()를 이용해서 string 을 integer 로 변형
    average = (int(score1) + int(score2)) / 2.0
    print("The average of the scores is : ", average)

main()

# class HelloWorld:
#     def __init__(self):
#         print("Hello World just one more time")
#     def __del__(self):
#         print("Good bye")
#     def performAverage(self, val1, val2):
#         average = (val1 + val2) / 2.0
#         print("The average of the scores is : ", average)
#
# def main():
#     world = HelloWorld()
#     score1, score2 = input("Enter two scores separated by a comma: ").split(",")
#     world.performAverage(int(score1), int(score2))
#
# main()