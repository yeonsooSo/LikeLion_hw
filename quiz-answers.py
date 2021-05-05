# # 1


# money = int(input("현재 가진 돈: "))
# if money >= 10000:
#     print("고기를 먹는다")
# elif 5000 <= money < 10000:
#     print("국밥을 먹는다")
# elif money < 5000:
#     print("라면을 먹는다")


# # 2
# fruits = []
# for i in range(5):
#     fruit = input("%d번 과일을 입력하세요 " % i)
#     fruits[i] = fruit

# for i in range(5):
#     print("%d번째 과일은 %s입니다." % (i, fruits[i]))

# # 3
# cookies = {
#     "탱커": "우유맛쿠키",
#     "딜러": "칠리맛쿠키",
#     "힐러": "천사맛쿠키",
#     "서포터": "석류맛쿠키"
# }
# print("바꾸기 전 cookies : ", cookies)

# for cookie in cookies:
#     if cookie == "탱커":
#         cookies[cookie] = "다크초코맛쿠키"
#     elif cookie == "딜러":
#         cookies[cookie] = "라떼맛쿠키"
#     elif cookie == "힐러":
#         cookies[cookie] = "허브맛쿠키"

# print("바꾼 후 cookies : ", cookies)


# # 4

# def add(a, b):
#     print(f"{a} + {b} = {a+b}")


# def sub(a, b):
#     print(f"{a} - {b} = {a-b}")


# def mul(a, b):
#     print(f"{a} * {b} = {a*b}")


# def div(a, b):
#     print(f"{a} / {b} = {a/b}")


# while(True):
#     command = int(input("원하는 숫자를 입력하세요 1. 더하기 2. 빼기 3. 곱하기 4. 나누기 5. 종료"))
#     if(command == 5):
#         print("종료합니다.")
#         break
#     a = int(input("숫자 1을 입력하세요"))
#     b = int(input("숫자 2을 입력하세요"))

#     if command == 1:
#         add(a, b)
#     elif command == 2:
#         sub(a, b)
#     elif command == 3:
#         mul(a, b)
#     elif command == 4:
#         div(a, b)

# 5

class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("안녕 내 이름은", self.name, "이야")

    def walk(self):
        print("나는 걷는 중")


class Worker(Person):
    def __init__(self, name, company):
        Person.__init__(self, name)
        self.company = company
        self.mental = 50

    def hello(self):
        print("안녕 내 이름은 ", self.name, "이고 내가 다니는 회사는 ", self.company,)

    def work(self):
        self.mental = self.mental - 10
        if(self.mental >= 0):
            print("나는 일하는 중, 내 멘탈지수 : ", self.mental)
        elif(self.mental < 0):
            print("더는 일 못해")


p1 = Worker("연수", "꾸글")
p1.work()
p1.work()
p1.work()
p1.work()
p1.work()
p1.work()
